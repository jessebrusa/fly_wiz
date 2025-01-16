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
        label_list = ['Title', 'Image', 'Styled\nInfo', 'Text\nInfo', 'Footer']
        for i in range(1, 6):
            section_frame = ttk.Frame(self, borderwidth=1, relief="solid", width=200)
            section_frame.pack(fill="both", expand=True, padx=5, pady=5)
            section_frame.grid_propagate(False)  
            section_frame.grid_rowconfigure(0, weight=1)  
            
            if i != 2:
                self.create_label_and_text_area(section_frame, label_list[i-1])
            else:
                self.create_label_and_buttons(section_frame)

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
        label_text = "Image"  # Define the label text within the method
        label = ttk.Label(section_frame, text="Image 1:", font=LABEL_FONT, width=7, anchor="center")
        label.grid(row=0, column=0, padx=5, pady=5, sticky="ns")

        # Frame for the first set of buttons
        button_frame_1 = ttk.Frame(section_frame)
        button_frame_1.grid(row=0, column=1, columnspan=2, padx=5, pady=2, sticky="nsew")

        browse_button_1 = ttk.Button(button_frame_1, text="Browse", style="Small.TButton", width=8, 
                                   command=self.browse_image)
        browse_button_1.pack(side="left", padx=5)

        search_button_1 = ttk.Button(button_frame_1, text="Search", style="Small.TButton", width=8, 
                                   command=self.open_search_window)
        search_button_1.pack(side="left", padx=5)

        # Label for second image
        second_image_label = ttk.Label(section_frame, text="Image 2:", font=LABEL_FONT, width=12, anchor="center")
        second_image_label.grid(row=1, column=0, padx=5, pady=5, sticky="ns")

        # Frame for the second set of buttons
        button_frame_2 = ttk.Frame(section_frame)
        button_frame_2.grid(row=1, column=1, columnspan=2, padx=5, pady=2, sticky="nsew")

        browse_button_2 = ttk.Button(button_frame_2, text="Browse", style="Small.TButton", width=8, 
                                   command=self.browse_image)
        browse_button_2.pack(side="left", padx=5)

        search_button_2 = ttk.Button(button_frame_2, text="Search", style="Small.TButton", width=8, 
                                   command=self.open_search_window)
        search_button_2.pack(side="left", padx=5)

        section_frame.grid_columnconfigure(1, weight=1)
        section_frame.grid_columnconfigure(2, weight=1)
        section_frame.grid_rowconfigure(0, weight=1)
        section_frame.grid_rowconfigure(1, weight=1)

    def browse_image(self):
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
                self.data_handler.update_data('image', image)
                print("Image updated in data handler")
        except Exception as e:
            print(f"An error occurred while browsing for an image: {e}")

    def open_search_window(self):
        """
        Open a small window with a label, input bar, and search button.
        """
        search_window = tk.Toplevel(self)
        search_window.title("Search")

        label = ttk.Label(search_window, text="Search:", font=LABEL_FONT)
        label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        entry = ttk.Entry(search_window, font=TEXT_AREA_FONT)
        entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        search_button = ttk.Button(search_window, text="Search", style="Small.TButton", command=lambda: self.perform_search(entry.get()))
        search_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        search_window.grid_columnconfigure(1, weight=1)

        # Bind the Enter key to the search button
        search_window.bind('<Return>', lambda event: self.perform_search(entry.get()))

    def perform_search(self, query):
        """
        Perform the search operation.
        """
        print(f"Searching for: {query}")