import tkinter as tk
from tkinter import ttk
from gui.widgets.header import HeaderSection
from gui.widgets.content.content import ContentSection
from gui.data_handler import DataHandler
from gui.flyer_manipulator import FlyerManipulator
import logging
from PIL import Image, ImageTk

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
            self.content_section = ContentSection(container, self.data_handler, self)
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

    def update_gui(self):
        """
        Updates the GUI with the data from the data handler.
        """
        try:
            data = self.data_handler.get_data()
            left_frame = self.content_section.left_frame

            # Update text areas
            left_frame.title_text_area.delete("1.0", tk.END)
            left_frame.title_text_area.insert(tk.END, data.get("title", ""))

            left_frame.styled_info_text_area.delete("1.0", tk.END)
            left_frame.styled_info_text_area.insert(tk.END, data.get("styled_info", ""))

            left_frame.text_info_text_area.delete("1.0", tk.END)
            left_frame.text_info_text_area.insert(tk.END, data.get("text_info", ""))

            left_frame.footer_text_area.delete("1.0", tk.END)
            left_frame.footer_text_area.insert(tk.END, data.get("footer", ""))

            # Update images
            right_frame = self.content_section.right_frame
            flyer_image = data.get("flyer")
            if flyer_image:
                # Set the desired resolution for display
                desired_width = 650
                desired_height = 425
                flyer_image_resized = flyer_image.resize((desired_width, desired_height), Image.LANCZOS)
                flyer_image_tk = ImageTk.PhotoImage(flyer_image_resized)
                right_frame.image_label.config(image=flyer_image_tk)
                right_frame.image_label.image = flyer_image_tk

        except Exception as e:
            logging.error(f"An error occurred while updating the GUI: {e}")

    def update_flyer(self):
        """
        Updates the flyer by placing images on it.
        """
        try:
            self.flyer_manipulator.update_flyer()
            self.update_gui()  # Update the GUI with the new flyer image
        except Exception as e:
            logging.error(f"An error occurred while updating the flyer: {e}")