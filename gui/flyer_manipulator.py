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
        self.background_color = (255, 255, 255)  # White
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
            self.image = Image.new('RGBA', (width, height), color=(255, 255, 255, 255))  # White background
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

            max_width, max_height = int(1100 * 0.7), int(850 * 0.7)  

            if image1 and image2:
                # Resize both images to fit within the maximum allowed dimensions
                image1.thumbnail((max_width, max_height), Image.LANCZOS)
                image2.thumbnail((max_width, max_height), Image.LANCZOS)

                # Ensure images have an alpha channel
                if image1.mode != 'RGBA':
                    image1 = image1.convert('RGBA')
                if image2.mode != 'RGBA':
                    image2 = image2.convert('RGBA')

                # Create a new image to combine both images side by side
                combined_width = image1.width + image2.width
                combined_height = max(image1.height, image2.height)

                # Ensure the combined image does not exceed the maximum allowed dimensions
                if combined_width > max_width or combined_height > max_height:
                    scale_factor = min(max_width / combined_width, max_height / combined_height)
                    combined_width = int(combined_width * scale_factor)
                    combined_height = int(combined_height * scale_factor)
                    image1 = image1.resize((int(image1.width * scale_factor), int(image1.height * scale_factor)), Image.LANCZOS)
                    image2 = image2.resize((int(image2.width * scale_factor), int(image2.height * scale_factor)), Image.LANCZOS)

                combined_image = Image.new('RGBA', (combined_width, combined_height), (255, 255, 255, 0))

                # Calculate vertical offset for centering shorter image
                image1_y_offset = (combined_height - image1.height) // 2
                image2_y_offset = (combined_height - image2.height) // 2

                # Paste both images onto the combined image
                combined_image.paste(image1, (0, image1_y_offset), image1)
                combined_image.paste(image2, (image1.width, image2_y_offset), image2)

                # Place the combined image in the center of the flyer
                x_offset = (1100 - combined_image.width) // 2
                y_offset = (850 - combined_image.height) // 2
                self.image.paste(combined_image, (x_offset, y_offset), combined_image)

            elif image1:
                # Resize image1 to fit within the maximum allowed dimensions
                image1.thumbnail((max_width, max_height), Image.LANCZOS)

                # Ensure image1 has an alpha channel
                if image1.mode != 'RGBA':
                    image1 = image1.convert('RGBA')

                # Place image1 in the center of the flyer
                x_offset = (1100 - image1.width) // 2
                y_offset = (850 - image1.height) // 2
                self.image.paste(image1, (x_offset, y_offset), image1)

            elif image2:
                # Resize image2 to fit within the maximum allowed dimensions
                image2.thumbnail((max_width, max_height), Image.LANCZOS)

                # Ensure image2 has an alpha channel
                if image2.mode != 'RGBA':
                    image2 = image2.convert('RGBA')

                # Place image2 in the center of the flyer
                x_offset = (1100 - image2.width) // 2
                y_offset = (850 - image2.height) // 2
                self.image.paste(image2, (x_offset, y_offset), image2)

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