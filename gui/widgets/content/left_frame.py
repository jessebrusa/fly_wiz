import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from PIL import Image

LABEL_FONT = ("Helvetica", 18)
TEXT_AREA_FONT = ("Helvetica", 15)
BUTTON_FONT = ("Helvetica", 20)
SMALL_BUTTON_FONT = ("Helvetica", 12) 

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
        for i, label_text in enumerate(label_list[1:]):
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
        label = ttk.Label(section_frame, text=label_text_1, font=LABEL_FONT, width=12, anchor="center")
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
        second_image_label = ttk.Label(section_frame, text=label_text_2, font=LABEL_FONT, width=12, anchor="center")
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
    
        section_frame.grid_columnconfigure(1, weight=1)
        section_frame.grid_columnconfigure(2, weight=1)
        section_frame.grid_columnconfigure(3, weight=1)
        section_frame.grid_rowconfigure(0, weight=1)
        section_frame.grid_rowconfigure(1, weight=1)

    def remove_image(self, image_key):
        """
        Remove the image from the data handler and refresh the GUI.
        """
        # self.data_handler.update_data(image_key, None)
        # print(f"Image removed from data handler with key {image_key}")
        # self.create_label_and_buttons(self.image_section_frame)
        print('remove image')

    def browse_image(self, image_key):
        """
        Open a file dialog to browse for an image file and update the data handler with the image object.
        """
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
            if file_path:
                self.selected_file_path = file_path
                print(f"Selected file: {file_path}")
                
                # Load the image using Pillow
                image = Image.open(file_path)
                
                # Update the data handler with the image object
                self.data_handler.update_data(image_key, image)
                print(f"Image updated in data handler with key {image_key}")
                
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