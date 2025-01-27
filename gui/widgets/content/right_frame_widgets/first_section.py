# gui/widgets/content/right_frame_widgets/first_section.py

from tkinter import ttk
from PIL import Image, ImageTk

class FirstSection(ttk.Frame):
    def __init__(self, parent, data_handler):
        """
        Initializes the first section with the parent widget and data handler.

        Parameters
        ----------
        parent : widget
            The parent widget.
        data_handler : DataHandler
            The data handler instance.
        """
        super().__init__(parent, borderwidth=1, relief="solid")
        self.data_handler = data_handler
        self.create_section()

    def create_section(self):
        """
        Creates and places the content in the first section.
        """
        try:
            image = self.data_handler.get_data().get('flyer')
            if image:
                # Set the desired resolution for display with padding
                desired_width = 650  # Adjusted width to fit within the section
                desired_height = 425  # Adjusted height to fit within the section
                scaled_image = image.resize((desired_width, desired_height), Image.LANCZOS)
                
                image_tk = ImageTk.PhotoImage(scaled_image)
                self.image_label = ttk.Label(self, image=image_tk)
                self.image_label.image = image_tk  
                self.image_label.pack(expand=True, padx=10, pady=10)  # Add padding around the image
            else:
                self.image_label = ttk.Label(self, text="No image found")
                self.image_label.pack(expand=True, padx=10, pady=10)  # Add padding around the label
        except Exception as e:
            print(f"An error occurred while creating the first section: {e}")