import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

LABEL_FONT = ("Helvetica", 18)
TEXT_AREA_FONT = ("Helvetica", 15)
BUTTON_FONT = ("Helvetica", 20)

class LeftFrame(ttk.Frame):
    def __init__(self, parent):
        """
        Initialize the LeftFrame with parent widget.
        """
        super().__init__(parent, borderwidth=2, relief="solid")
        self.create_styles()
        self.create_sections()

    def create_styles(self):
        """
        Create and configure styles for the frame.
        """
        self.style = ttk.Style()
        self.style.configure("TButton", font=BUTTON_FONT, padding=(5, 2))  # Adjust padding to reduce button height

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
                self.create_label_and_buttons(section_frame, label_list[i-1])

    def create_label_and_text_area(self, section_frame, label_text):
        """
        Create a label and text area within the section frame.
        """
        label = ttk.Label(section_frame, text=f"{label_text}:", font=LABEL_FONT, width=7, anchor="center")
        label.grid(row=0, column=0, padx=5, pady=5, sticky="ns")
        
        text_area = tk.Text(section_frame, height=3, width=45, font=TEXT_AREA_FONT, wrap=tk.WORD)
        text_area.grid(row=0, column=1, padx=5, pady=5, sticky="ns")
        
        section_frame.grid_columnconfigure(1, weight=1)

    def create_label_and_buttons(self, section_frame, label_text):
        """
        Create a label and buttons within the section frame.
        """
        label = ttk.Label(section_frame, text=f"{label_text}:", font=LABEL_FONT, width=7, anchor="center")
        label.grid(row=0, column=0, padx=5, pady=5, sticky="ns")

        browse_button = ttk.Button(section_frame, text="Browse", style="TButton", width=10, 
                                   command=self.browse_image)
        browse_button.grid(row=0, column=1, padx=5, pady=18, sticky="ns")

        search_button = ttk.Button(section_frame, text="Search", style="TButton", width=10)
        search_button.grid(row=0, column=2, padx=5, pady=18, sticky="ns")

        section_frame.grid_columnconfigure(1, weight=1)
        section_frame.grid_columnconfigure(2, weight=1)

    def browse_image(self):
        """
        Open a file dialog to browse for an image file.
        """
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
            if file_path:
                self.selected_file_path = file_path
                print(f"Selected file: {file_path}")
        except Exception as e:
            print(f"An error occurred while browsing for an image: {e}")