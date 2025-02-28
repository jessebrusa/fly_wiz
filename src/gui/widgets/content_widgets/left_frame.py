import tkinter as tk
from tkinter import ttk
from .left_frame_widgets.title_section import TitleSection
from .left_frame_widgets.styled_info_section import StyledInfoSection
from .left_frame_widgets.text_info_section import TextInfoSection
from .left_frame_widgets.footer_section import FooterSection
from .left_frame_widgets.bg_image_section import BgImageSection

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
        self.title_section = TitleSection(self, self.data_handler, self.main_app)
        self.title_text_area = self.title_section.text_area

        self.bg_image_section = BgImageSection(self, self.data_handler, self.main_app)

        self.styled_info_section = StyledInfoSection(self)
        self.styled_info_text_area = self.styled_info_section.text_area

        self.text_info_section = TextInfoSection(self)
        self.text_info_text_area = self.text_info_section.text_area

        self.footer_section = FooterSection(self)
        self.footer_text_area = self.footer_section.text_area