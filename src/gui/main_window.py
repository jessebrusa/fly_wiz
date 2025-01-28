import tkinter as tk
from .widgets.header import HeaderSection
from .widgets.content import ContentSection
import logging

class FlyWizGui(tk.Tk):
    def __init__(self, data_handler, flyer_manipulator):
        super().__init__()
        self.title("Flyer Wizard")
        self.geometry("1200x800")
        self.data_handler = data_handler
        self.flyer_manipulator = flyer_manipulator
        self.header_section = HeaderSection(self)
        self.header_section.pack(side="top", fill="x")
        self.content_section = ContentSection(self, self.data_handler, self)
        self.content_section.pack(side="top", fill="both", expand=True)
        self.check_text()

    def check_text(self):
        """
        Gets the text from the title, styled text, info text, and footer sections every 0.25 seconds.
        """
        try:
            left_frame = self.content_section.left_frame
            title_text = left_frame.title_text_area.get("1.0", tk.END).strip()
            styled_info_text = left_frame.styled_info_text_area.get("1.0", tk.END).strip()
            text_info_text = left_frame.text_info_text_area.get("1.0", tk.END).strip()
            footer_text = left_frame.footer_text_area.get("1.0", tk.END).strip()

            data = {
                "title": title_text,
                "styled_info": styled_info_text,
                "text_info": text_info_text,
                "footer": footer_text
            }

            # Update the data handler with the new data
            for key, value in data.items():
                if self.data_handler.get_data().get(key) != value:
                    self.data_handler.update_data(key, value)
                    logging.info(f"Updated {key} in data handler: {self.data_handler.get_data()}")

        except Exception as e:
            logging.error(f"An error occurred while getting the text: {e}")

        self.after(250, self.check_text)