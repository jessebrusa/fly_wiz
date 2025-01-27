from tkinter import filedialog
from PIL import Image

class ImageHandler:
    def __init__(self, data_handler, main_app, update_ui_callback):
        self.data_handler = data_handler
        self.main_app = main_app
        self.update_ui_callback = update_ui_callback

    def browse_image(self, image_key):
        """
        Open a file dialog to browse for an image file and update the data handler with the image object.
        """
        try:
            file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
            if file_path:
                image = Image.open(file_path)
                self.data_handler.update_data(image_key, image)
                self.main_app.flyer_manipulator.change_made = True
                self.main_app.update_flyer()
                self.update_ui_callback()  # Call the callback to update the UI
        except Exception as e:
            print(f"An error occurred while browsing for an image: {e}")

    def remove_image(self, image_key):
        """
        Remove the image from the data handler and refresh the GUI.
        """
        try:
            self.data_handler.update_data(image_key, None)
            
            # Remove the combined image if either image1 or image2 is removed
            if image_key in ['image1', 'image2']:
                self.data_handler.update_data('combined_image', None)
            
            self.main_app.flyer_manipulator.change_made = True
            self.main_app.update_flyer()
            self.update_ui_callback()  # Call the callback to update the UI

        except Exception as e:
            print(f"An error occurred while removing the image: {e}")

    def is_image_present(self, image_key):
        """
        Check if an image is present in the data handler.
        """
        return self.data_handler.get_data().get(image_key) is not None