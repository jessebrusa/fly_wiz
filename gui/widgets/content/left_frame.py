from tkinter import ttk
from gui.widgets.left_frame.image_handler import ImageHandler
from gui.widgets.left_frame.background_handler import BackgroundHandler
from gui.widgets.left_frame.color_wheel_handler import ColorWheelHandler
from gui.widgets.left_frame.search_handler import SearchHandler
from gui.widgets.left_frame.ui_helpers import create_label_and_text_area, create_label_and_buttons

LABEL_FONT = ("Helvetica", 16)
TEXT_AREA_FONT = ("Helvetica", 15)
BUTTON_FONT = ("Helvetica", 20)
SMALL_BUTTON_FONT = ("Helvetica", 12)
DROPDOWN_FONT = ("Helvetica", 10)  

class LeftFrame(ttk.Frame):
    def __init__(self, parent, data_handler, main_app):
        """
        Initialize the LeftFrame with parent widget, data handler, and main application instance.
        """
        super().__init__(parent, borderwidth=2, relief="solid")
        self.data_handler = data_handler
        self.main_app = main_app  # Set the main_app attribute
        self.image_handler = ImageHandler(data_handler, main_app, self.update_ui)
        self.background_handler = BackgroundHandler(data_handler, main_app)
        self.color_wheel_handler = ColorWheelHandler(self, data_handler, main_app)
        self.search_handler = SearchHandler(self, data_handler)
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
            
            text_area = create_label_and_text_area(section_frame, label_text)
            if label_text == 'Title':
                self.title_text_area = text_area
            elif label_text == 'Styled\nInfo':
                self.styled_info_text_area = text_area
            elif label_text == 'Text\nInfo':
                self.text_info_text_area = text_area
            elif label_text == 'Footer':
                self.footer_text_area = text_area
        
        # Create the section for the image buttons
        self.image_section_frame = ttk.Frame(self, borderwidth=1, relief="solid", width=200)
        self.image_section_frame.pack(fill="both", expand=True, padx=5, pady=5)
        self.image_section_frame.grid_propagate(False)  
        self.image_section_frame.grid_rowconfigure(0, weight=1)
        create_label_and_buttons(self.image_section_frame, self.image_handler, self.open_color_wheel_window, self.search_handler.open_search_window)
        
        # Create the remaining sections for the label and text areas
        for _, label_text in enumerate(label_list[1:]):
            section_frame = ttk.Frame(self, borderwidth=1, relief="solid", width=200)
            section_frame.pack(fill="both", expand=True, padx=5, pady=5)
            section_frame.grid_propagate(False)  
            section_frame.grid_rowconfigure(0, weight=1)  
            
            text_area = create_label_and_text_area(section_frame, label_text)
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
        """
        self.color_wheel_handler.open_color_wheel_window(gradient)

    def update_ui(self):
        """
        Update the UI by recreating the label and buttons.
        """
        create_label_and_buttons(self.image_section_frame, self.image_handler, self.open_color_wheel_window, self.search_handler.open_search_window)