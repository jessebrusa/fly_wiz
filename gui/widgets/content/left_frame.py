import tkinter as tk
from tkinter import ttk
from gui.widgets.content.left_frame_widgets.handlers.image_handler import ImageHandler
from gui.widgets.content.left_frame_widgets.handlers.background_handler import BackgroundHandler
from gui.widgets.content.left_frame_widgets.handlers.color_wheel_handler import ColorWheelHandler
from gui.widgets.content.left_frame_widgets.handlers.search_handler import SearchHandler
from gui.widgets.content.left_frame_widgets.ui_helpers import UIHelpers
from gui.widgets.content.left_frame_widgets.title_section import TitleSection
from gui.widgets.content.left_frame_widgets.styled_info_section import StyledInfoSection
from gui.widgets.content.left_frame_widgets.text_info_section import TextInfoSection
from gui.widgets.content.left_frame_widgets.footer_section import FooterSection
from gui.widgets.content.left_frame_widgets.bg_image_section import BgImageSection

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
        self.search_handler = SearchHandler(data_handler, main_app.flyer_manipulator, self.update_ui)  # Correct initialization
        self.ui_helpers = UIHelpers()  # Initialize UIHelpers
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
        self.title_section = TitleSection(self, self.ui_helpers)
        self.title_text_area = self.title_section.text_area

        # Create the section for the image buttons
        self.bg_image_section = BgImageSection(self, self.ui_helpers, self.image_handler, self.color_wheel_handler, self.search_handler.open_search_window)

        self.styled_info_section = StyledInfoSection(self, self.ui_helpers)
        self.styled_info_text_area = self.styled_info_section.text_area

        self.text_info_section = TextInfoSection(self, self.ui_helpers)
        self.text_info_text_area = self.text_info_section.text_area

        self.footer_section = FooterSection(self, self.ui_helpers)
        self.footer_text_area = self.footer_section.text_area

    def update_ui(self):
        """
        Update the UI by recreating the label and buttons.
        """
        self.bg_image_section.create_section()
        self.update_text_areas()

    def update_text_areas(self):
        """
        Update the text areas with the current data from the data handler.
        """
        data = self.data_handler.get_data()
        self.title_text_area.delete("1.0", tk.END)
        self.title_text_area.insert(tk.END, data.get("title", ""))
        self.styled_info_text_area.delete("1.0", tk.END)
        self.styled_info_text_area.insert(tk.END, data.get("styled_info", ""))
        self.text_info_text_area.delete("1.0", tk.END)
        self.text_info_text_area.insert(tk.END, data.get("text_info", ""))
        self.footer_text_area.delete("1.0", tk.END)
        self.footer_text_area.insert(tk.END, data.get("footer", ""))