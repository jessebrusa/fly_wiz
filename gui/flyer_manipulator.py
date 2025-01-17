from PIL import Image

class FlyerManipulator:
    """
    A class to create and manipulate a base blank image.

    Attributes
    ----------
    image : Image
        The Pillow image to be manipulated.
    data_handler : DataHandler
        The data handler instance to update data.

    Methods
    -------
    create_base_image():
        Creates a base blank image with dimensions 11 inches by 8.5 inches.
    update_data_handler():
        Updates the data handler with the current image.
    place_images_on_flyer():
        Places images from data_handler on the flyer image.
    update_flyer():
        Updates the flyer by placing images on it.
    """
    def __init__(self, data_handler):
        """
        Initializes the FlyerManipulator and creates the base blank image.

        Parameters
        ----------
        data_handler : DataHandler
            The data handler instance to update data.
        """
        self.image = None
        self.data_handler = data_handler
        try:
            self.create_base_image()
            self.update_data_handler()
        except Exception as e:
            print(f"An error occurred while initializing the FlyerManipulator: {e}")

    def create_base_image(self):
        """
        Creates a base blank image with dimensions 11 inches by 8.5 inches.
        """
        try:
            width, height = 1100, 850  # Dimensions in pixels (assuming 100 pixels per inch)
            self.image = Image.new('RGB', (width, height), color='white')
        except Exception as e:
            print(f"An error occurred while creating the base image: {e}")
            self.image = None

    def update_data_handler(self):
        """
        Updates the data handler with the current image.
        """
        try:
            self.data_handler.update_data('flyer', self.image)
        except Exception as e:
            print(f"An error occurred while updating the data handler: {e}")

    def place_images_on_flyer(self):
        """
        Places images from data_handler on the flyer image.
        """
        try:
            # Recreate the base blank image to clear previous images
            self.create_base_image()

            image1 = self.data_handler.get_data().get('image1')
            image2 = self.data_handler.get_data().get('image2')

            if image1:
                # Resize image1 to fit within 70% of the flyer dimensions
                max_width, max_height = int(1100 * 0.65), int(850 * 0.65)
                image1.thumbnail((max_width, max_height), Image.LANCZOS)

                if image2:
                    # Resize image2 to fit within 70% of the flyer dimensions
                    image2.thumbnail((max_width, max_height), Image.LANCZOS)

                    # Combine images side by side
                    combined_width = image1.width + image2.width
                    combined_height = max(image1.height, image2.height)
                    combined_image = Image.new('RGB', (combined_width, combined_height), color='white')
                    combined_image.paste(image1, (0, (combined_height - image1.height) // 2))
                    combined_image.paste(image2, (image1.width, (combined_height - image2.height) // 2))

                    # Resize combined image if necessary
                    if combined_width > max_width or combined_height > max_height:
                        combined_image.thumbnail((max_width, max_height), Image.LANCZOS)

                    # Place combined image in the center of the flyer
                    x_offset = (1100 - combined_image.width) // 2
                    y_offset = (850 - combined_image.height) // 2
                    self.image.paste(combined_image, (x_offset, y_offset))
                else:
                    # Place image1 in the center of the flyer
                    x_offset = (1100 - image1.width) // 2
                    y_offset = (850 - image1.height) // 2
                    self.image.paste(image1, (x_offset, y_offset))

                # Update the data handler with the modified flyer image
                self.update_data_handler()
        
        except Exception as e:
            print(f"An error occurred while placing images on the flyer: {e}")

    def update_flyer(self):
        """
        Updates the flyer by placing images on it.
        """
        self.place_images_on_flyer()
        self.image.save('flyer.png')