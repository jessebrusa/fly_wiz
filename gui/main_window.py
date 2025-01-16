import tkinter as tk
from tkinter import ttk
from gui.widgets.header import HeaderSection
from gui.widgets.content.content import ContentSection
from gui.data_handler import DataHandler
from gui.flyer_manipulator import FlyerManipulator
import logging

class FlyWizGui(tk.Tk):
    def __init__(self):
        """
        Constructs all the necessary attributes for the FlyWizGui object.
        """
        super().__init__()
        self.title("Fly Wiz")
        self.state('zoomed')

        default_font = ("Helvetica", 24)
        self.option_add("*Font", default_font)

        self.data_handler = DataHandler()
        self.flyer_manipulator = FlyerManipulator(self.data_handler)

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        try:
            self.header_section = HeaderSection(container)
            self.header_section.pack(fill="x", padx=10, pady=5)
            self.content_section = ContentSection(container, self.data_handler)
            self.content_section.pack(fill="both", expand=True, padx=10, pady=5)
        except Exception as e:
            logging.error(f"An error occurred while initializing the GUI: {e}")

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

        # Schedule this method to be called again after 250 milliseconds (0.25 seconds)
        self.after(250, self.check_text)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = FlyWizGui()
    app.mainloop()