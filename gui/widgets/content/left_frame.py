import tkinter as tk
from tkinter import ttk, colorchooser
from tkinter import filedialog
from PIL import Image

LABEL_FONT = ("Helvetica", 16)
TEXT_AREA_FONT = ("Helvetica", 15)
BUTTON_FONT = ("Helvetica", 20)
SMALL_BUTTON_FONT = ("Helvetica", 12)
DROPDOWN_FONT = ("Helvetica", 10)  # Smaller font for dropdown menu

class LeftFrame(ttk.Frame):
    def __init__(self, parent, data_handler):
        """
        Initialize the LeftFrame with parent widget and data handler.
        """
        super().__init__(parent, borderwidth=2, relief="solid")
        self.data_handler = data_handler
        self.create_styles()
        self.create_sections()

    def create_styles(self):
        """
        Create and configure styles for the frame.
        """
        self.style = ttk.Style()
        self.style.configure("TButton", font=BUTTON_FONT, padding=(5, 2))  # Adjust padding to reduce button height
        self.style.configure("Small.TButton", font=SMALL_BUTTON_FONT, padding=(5, 2))  # Smaller font for buttons
        self.style.configure("TCombobox", font=DROPDOWN_FONT)  # Smaller font for dropdown menu

    def create_sections(self):
        """
        Create sections within the LeftFrame.
        """
        label_list = ['Title', 'Styled\nInfo', 'Text\nInfo', 'Footer']
        
        # Create the first section for the label and text areas
        for _, label_text in enumerate(label_list[:1]):
            section_frame = ttk.Frame(self, borderwidth=1, relief="solid", width=200)
            section_frame.pack(fill="both", expand=True, padx=5, pady=5)
            section_frame.grid_propagate(False)  
            section_frame.grid_rowconfigure(0, weight=1)  
            
            self.create_label_and_text_area(section_frame, label_text)
        
        # Create the section for the image buttons
        self.image_section_frame = ttk.Frame(self, borderwidth=1, relief="solid", width=200)
        self.image_section_frame.pack(fill="both", expand=True, padx=5, pady=5)
        self.image_section_frame.grid_propagate(False)  
        self.image_section_frame.grid_rowconfigure(0, weight=1)
        self.create_label_and_buttons(self.image_section_frame)
        
        # Create the remaining sections for the label and text areas
        for _, label_text in enumerate(label_list[1:]):
            section_frame = ttk.Frame(self, borderwidth=1, relief="solid", width=200)
            section_frame.pack(fill="both", expand=True, padx=5, pady=5)
            section_frame.grid_propagate(False)  
            section_frame.grid_rowconfigure(0, weight=1)  
            
            self.create_label_and_text_area(section_frame, label_text)

    def create_label_and_text_area(self, section_frame, label_text):
        """
        Create a label and text area within the section frame.
        """
        label = ttk.Label(section_frame, text=f"{label_text}:", font=LABEL_FONT, width=7, anchor="center")
        label.grid(row=0, column=0, padx=5, pady=5, sticky="ns")
        
        text_area = tk.Text(section_frame, height=3, width=45, font=TEXT_AREA_FONT, wrap=tk.WORD)
        text_area.grid(row=0, column=1, padx=5, pady=5, sticky="ns")
        
        section_frame.grid_columnconfigure(1, weight=1)

        if label_text == 'Title':
            self.title_text_area = text_area
        elif label_text == 'Styled\nInfo':
            self.styled_info_text_area = text_area
        elif label_text == 'Text\nInfo':
            self.text_info_text_area = text_area
        elif label_text == 'Footer':
            self.footer_text_area = text_area

    def open_color_wheel_window(self, gradient=False):
        """
        Open a window with one or two squares for color selection.
        The first square is white, and the second is transparent by default, both with outlines.
        """
        self.color_wheel_window = tk.Toplevel(self)
        self.color_wheel_window.title("Color Wheel")
        self.color_wheel_window.attributes('-topmost', True)  # Keep the window on top
    
        # Set fixed width and center the window
        window_width = 400
        window_height = 200
        screen_width = self.color_wheel_window.winfo_screenwidth()
        screen_height = self.color_wheel_window.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.color_wheel_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    
        # Frame for the color squares
        color_frame = ttk.Frame(self.color_wheel_window)
        color_frame.pack(padx=10, pady=10)
    
        # Center the color frame horizontally
        color_frame.grid_columnconfigure(0, weight=1)
        color_frame.grid_columnconfigure(1, weight=1)
        color_frame.grid_columnconfigure(2, weight=1)
        color_frame.grid_columnconfigure(3, weight=1)
    
        # Get the current colors and gradient state from the data handler
        bg_color = self.data_handler.get_data().get('bg_color', {})
        color1 = bg_color.get('color1', '#FFFFFF')
        color2 = bg_color.get('color2', '#FFFFFF')
        direction = bg_color.get('direction', "Top Left to Bottom Right")
        gradient_state = bg_color.get('gradient_state', 0)
    
        # Ensure colors are in the correct format
        if isinstance(color1, tuple):
            color1 = f"#{color1[0]:02x}{color1[1]:02x}{color1[2]:02x}"
        if isinstance(color2, tuple):
            color2 = f"#{color2[0]:02x}{color2[1]:02x}{color2[2]:02x}"
    
        # Create the first color square
        self.color_square_1 = tk.Label(color_frame, bg=color1, width=5, height=2, relief="solid", borderwidth=1)
        self.color_square_1.grid(row=1, column=1, padx=5, pady=5)
        self.color_square_1.bind("<Button-1>", lambda event: self.change_color(self.color_square_1))
    
        # Variable to track the gradient option
        self.gradient_var = tk.IntVar(value=gradient_state)
    
        # Checkbutton for gradient option
        gradient_checkbutton = ttk.Checkbutton(color_frame, text="Gradient", variable=self.gradient_var, command=self.toggle_gradient)
        gradient_checkbutton.grid(row=2, column=1, padx=5, pady=5)
    
        # Dropdown menu for gradient directions (initially hidden)
        self.gradient_direction = tk.StringVar(value=direction)
        self.gradient_direction_menu = ttk.Combobox(color_frame, textvariable=self.gradient_direction, state="readonly", style="TCombobox",
                                font=DROPDOWN_FONT, width=25)
        self.gradient_direction_menu['values'] = [
            "Top Left to Bottom Right",
            "Top Right to Bottom Left",
            "Bottom Left to Top Right",
            "Bottom Right to Top Left",
            "Top to Bottom",
            "Bottom to Top",
            "Left to Right",
            "Right to Left"
        ]
        self.gradient_direction_menu.option_add('*TCombobox*Listbox.font', DROPDOWN_FONT)
        self.gradient_direction_menu.grid(row=2, column=2, padx=5, pady=5)
        self.gradient_direction_menu.grid_remove()
    
        # Create the second color square for gradient (initially hidden)
        self.color_square_2 = tk.Label(color_frame, bg=color2, width=5, height=2, relief="solid", borderwidth=1)
        self.color_square_2.grid(row=1, column=2, padx=5, pady=5)
        self.color_square_2.bind("<Button-1>", lambda event: self.change_color(self.color_square_2))
        self.color_square_2.grid_remove()
    
        # Show or hide the second color square and gradient direction menu based on the gradient option
        if self.gradient_var.get() == 1:
            self.color_square_2.grid()
            self.gradient_direction_menu.grid()
    
        # Submit button
        submit_button = ttk.Button(self.color_wheel_window, text="Submit", command=self.apply_gradient)
        submit_button.pack(pady=10)
    def toggle_gradient(self):
        """
        Toggle the visibility of the second color square and gradient direction menu based on the gradient option.
        """
        if self.gradient_var.get() == 1:
            self.color_square_2.grid()
            self.gradient_direction_menu.grid()
        else:
            self.color_square_2.grid_remove()
            self.gradient_direction_menu.grid_remove()

    def change_color(self, color_square):
        """
        Open a color picker dialog to select a color and change the background color of the square.
        """
        self.color_wheel_window.attributes('-topmost', False)  # Allow the color picker to be on top
        color = colorchooser.askcolor()[1]
        self.color_wheel_window.attributes('-topmost', True)  # Bring the color wheel window back to the top
        if color:
            color_square.config(bg=color)

    def apply_gradient(self):
        """
        Apply the selected gradient to the background.
        """
        # Get the selected colors
        color1 = self.color_square_1.cget("bg")
        color2 = self.color_square_2.cget("bg") if self.gradient_var.get() == 1 else None
        direction = self.gradient_direction.get() if self.gradient_var.get() == 1 else None
    
        # Update the data handler with the selected colors, direction, and gradient state
        self.data_handler.update_data('bg_color', {
            'color1': color1,
            'color2': color2,
            'direction': direction,
            'gradient_state': self.gradient_var.get()
        })
    
        # Print the applied gradient for debugging
        print(f"Applying gradient: color1={color1}, color2={color2}, direction={direction}, gradient_state={self.gradient_var.get()}")
    
        # Close the color wheel window
        self.color_wheel_window.destroy()

    def create_label_and_buttons(self, section_frame):
        """
        Create a label and buttons within the section frame.
        """
        # Clear the section frame to avoid duplicate widgets
        for widget in section_frame.winfo_children():
            widget.destroy()
    
        # Check if images are selected
        image1_selected = self.data_handler.get_data().get('image1') is not None
        image2_selected = self.data_handler.get_data().get('image2') is not None
    
        # Label for first image
        label_text_1 = "Image 1" + (" ✓:" if image1_selected else " :")
        label = ttk.Label(section_frame, text=label_text_1, font=LABEL_FONT, width=10, anchor="center")
        label.grid(row=0, column=0, padx=5, pady=5, sticky="ns")
    
        # Frame for the first set of buttons
        button_frame_1 = ttk.Frame(section_frame)
        button_frame_1.grid(row=0, column=1, columnspan=3, padx=5, pady=2, sticky="nsew")
    
        browse_button_1 = ttk.Button(button_frame_1, text="Browse", style="Small.TButton", width=8, 
                                     command=lambda: self.browse_image('image1'))
        browse_button_1.pack(side="left", padx=5)
    
        search_button_1 = ttk.Button(button_frame_1, text="Search", style="Small.TButton", width=8, 
                                     command=lambda: self.open_search_window('image1'))
        search_button_1.pack(side="left", padx=5)
        
        remove_button_1 = ttk.Button(button_frame_1, text="Remove", style="Small.TButton", width=8, 
                                     command=lambda: self.remove_image('image1'))
        remove_button_1.pack(side="left", padx=5)
    
        # Label for second image
        label_text_2 = "Image 2" + (" ✓:" if image2_selected else " :")
        second_image_label = ttk.Label(section_frame, text=label_text_2, font=LABEL_FONT, width=10, anchor="center")
        second_image_label.grid(row=1, column=0, padx=5, pady=5, sticky="ns")
    
        # Frame for the second set of buttons
        button_frame_2 = ttk.Frame(section_frame)
        button_frame_2.grid(row=1, column=1, columnspan=3, padx=5, pady=2, sticky="nsew")
    
        browse_button_2 = ttk.Button(button_frame_2, text="Browse", style="Small.TButton", width=8, 
                                     command=lambda: self.browse_image('image2'))
        browse_button_2.pack(side="left", padx=5)
    
        search_button_2 = ttk.Button(button_frame_2, text="Search", style="Small.TButton", width=8, 
                                     command=lambda: self.open_search_window('image2'))
        search_button_2.pack(side="left", padx=5)
        
        remove_button_2 = ttk.Button(button_frame_2, text="Remove", style="Small.TButton", width=8, 
                                     command=lambda: self.remove_image('image2'))
        remove_button_2.pack(side="left", padx=5)
    
        # Label for background color
        label_text_3 = "Background:"
        background_label = ttk.Label(section_frame, text=label_text_3, font=LABEL_FONT, width=10, anchor="center")
        background_label.grid(row=2, column=0, padx=5, pady=5, sticky="ns")
    
        # Frame for the background color buttons
        button_frame_3 = ttk.Frame(section_frame)
        button_frame_3.grid(row=2, column=1, columnspan=3, padx=5, pady=2, sticky="nsew")
    
        color_wheel_button = ttk.Button(button_frame_3, text="Color Wheel", style="Small.TButton", width=12, command=self.open_color_wheel_window)
        color_wheel_button.pack(side="left", padx=5)
    
        gradient_button = ttk.Button(button_frame_3, text="Gradient", style="Small.TButton", width=12, command=lambda: self.open_color_wheel_window(gradient=True))
        gradient_button.pack(side="left", padx=5)
    
        section_frame.grid_columnconfigure(1, weight=1)
        section_frame.grid_columnconfigure(2, weight=1)
        section_frame.grid_columnconfigure(3, weight=1)
        section_frame.grid_rowconfigure(0, weight=1)
        section_frame.grid_rowconfigure(1, weight=1)
        section_frame.grid_rowconfigure(2, weight=1)

    def remove_image(self, image_key):
        """
        Remove the image from the data handler and refresh the GUI.
        """
        self.data_handler.update_data(image_key, None)
        self.create_label_and_buttons(self.image_section_frame)
        self.data_handler.save('test_save.json')

    def browse_image(self, image_key):
        """
        Open a file dialog to browse for an image file and update the data handler with the image object.
        """
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
            if file_path:
                self.selected_file_path = file_path
                
                image = Image.open(file_path)
                
                # Update the data handler with the image object
                self.data_handler.update_data(image_key, image)
                
                # Refresh the GUI to reflect the selected image
                self.create_label_and_buttons(self.image_section_frame)
        except Exception as e:
            print(f"An error occurred while browsing for an image: {e}")

    def open_search_window(self, image_key):
        """
        Open a small window with a label, input bar, and search button.
        """
        search_window = tk.Toplevel(self)
        search_window.title("Search")

        label = ttk.Label(search_window, text="Search:", font=LABEL_FONT)
        label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        entry = ttk.Entry(search_window, font=TEXT_AREA_FONT)
        entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        search_button = ttk.Button(search_window, text="Search", style="Small.TButton", command=lambda: self.perform_search(entry.get(), image_key))
        search_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        search_window.grid_columnconfigure(1, weight=1)

        # Bind the Enter key to the search button
        search_window.bind('<Return>', lambda event: self.perform_search(entry.get(), image_key))

    def perform_search(self, query, image_key):
        """
        Perform the search operation.
        """
        print(f"Searching for: {query} for {image_key}")
        # Implement the search functionality here