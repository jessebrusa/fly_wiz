from tkinter import ttk
from PIL import Image, ImageTk

class FlyerImageSection(ttk.Frame):
    def __init__(self, parent, data_handler):
        """
        Initializes the flyer image section with the parent widget and data handler.

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
        Creates and places the content in the flyer image section.
        """
        try:
            image = self.data_handler.get_data().get('flyer')
            if image:
                desired_width = 650  
                desired_height = 425  
                scaled_image = image.resize((desired_width, desired_height), Image.LANCZOS)
                
                image_tk = ImageTk.PhotoImage(scaled_image)
                self.image_label = ttk.Label(self, image=image_tk)
                self.image_label.image = image_tk  
                self.image_label.pack(expand=True, padx=10, pady=10)  # Add padding around the image
            else:
                self.image_label = ttk.Label(self, text="No image found")
                self.image_label.pack(expand=True, padx=10, pady=10)  # Add padding around the label
        except Exception as e:
            print(f"An error occurred while creating the flyer image section: {e}")

    def update_image(self):
        """
        Update the image in the flyer image section.
        """
        try:
            image = self.data_handler.get_data().get('flyer')
            if image:
                desired_width = 650  
                desired_height = 425  
                scaled_image = image.resize((desired_width, desired_height), Image.LANCZOS)
                
                image_tk = ImageTk.PhotoImage(scaled_image)
                self.image_label.config(image=image_tk)
                self.image_label.image = image_tk  
            else:
                self.image_label.config(text="No image found")
                self.image_label.image = None
        except Exception as e:
            print(f"An error occurred while updating the flyer image: {e}")
        """
        Update the image in the flyer image section.
        """
        try:
            image = self.data_handler.get_data().get('flyer')
            if image:
                desired_width = 650  
                desired_height = 425  
                scaled_image = image.resize((desired_width, desired_height), Image.LANCZOS)
                
                image_tk = ImageTk.PhotoImage(scaled_image)
                self.image_label.config(image=image_tk)
                self.image_label.image = image_tk  
            else:
                self.image_label.config(text="No image found")
                self.image_label.image = None
        except Exception as e:
            print(f"An error occurred while updating the flyer image: {e}")