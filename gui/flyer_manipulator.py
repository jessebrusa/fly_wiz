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
        self.change_made = False  # Flag to track changes
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

    def apply_background_color(self):
        """
        Apply the background color from the data handler to the flyer image.
        """
        try:
            bg_color = self.data_handler.get_data().get('bg_color', {})
            color1 = bg_color.get('color1', '#FFFFFF')
            color2 = bg_color.get('color2', None)
            direction = bg_color.get('direction', None)
            gradient_state = bg_color.get('gradient_state', 0)

            # Ensure color1 is in the correct format
            if isinstance(color1, str) and color1.startswith('#'):
                color1 = tuple(int(color1[i:i+2], 16) for i in (1, 3, 5))

            print(f"Color1: {color1}, Color2: {color2}, Direction: {direction}, Gradient State: {gradient_state}")

            # Create a new base image with the updated background color
            width, height = 1100, 850  # Dimensions in pixels (assuming 100 pixels per inch)
            if gradient_state == 1 and color2:
                # Ensure color2 is in the correct format
                if isinstance(color2, str) and color2.startswith('#'):
                    color2 = tuple(int(color2[i:i+2], 16) for i in (1, 3, 5))
                self.image = Image.new('RGBA', (width, height))
                # Apply gradient background
                self.apply_gradient_background(color1, color2, direction)
            else:
                self.image = Image.new('RGBA', (width, height), color=color1 + (255,))

            print(f"Applied background color: {color1}")
            self.update_data_handler()
        except Exception as e:
            print(f"An error occurred while applying the background color: {e}")

    def apply_gradient_background(self, color1, color2, direction):
        """
        Apply a gradient background to the flyer image.
        """
        width, height = self.image.size
        base = Image.new('RGBA', (width, height), color1 + (255,))
        top = Image.new('RGBA', (width, height), color2 + (255,))
        mask = Image.new('L', (width, height))
        mask_data = []

        if direction == "Top Left to Bottom Right":
            for y in range(height):
                for x in range(width):
                    mask_data.append(int(255 * (x + y) / (width + height)))
        elif direction == "Top Right to Bottom Left":
            for y in range(height):
                for x in range(width):
                    mask_data.append(int(255 * (width - x + y) / (width + height)))
        elif direction == "Bottom Left to Top Right":
            for y in range(height):
                for x in range(width):
                    mask_data.append(int(255 * (x + height - y) / (width + height)))
        elif direction == "Bottom Right to Top Left":
            for y in range(height):
                for x in range(width):
                    mask_data.append(int(255 * (width - x + height - y) / (width + height)))
        elif direction == "Top to Bottom":
            for y in range(height):
                for x in range(width):
                    mask_data.append(int(255 * y / height))
        elif direction == "Bottom to Top":
            for y in range(height):
                for x in range(width):
                    mask_data.append(int(255 * (height - y) / height))
        elif direction == "Left to Right":
            for y in range(height):
                for x in range(width):
                    mask_data.append(int(255 * x / width))
        elif direction == "Right to Left":
            for y in range(height):
                for x in range(width):
                    mask_data.append(int(255 * (width - x) / width))

        mask.putdata(mask_data)
        self.image = Image.composite(base, top, mask)
        print(f"Applied gradient background: color1={color1}, color2={color2}, direction={direction}")

    def place_images_on_flyer(self):
        """
        Places images from data_handler on the flyer image.
        """
        try:
            image1 = self.data_handler.get_data().get('image1')
            image2 = self.data_handler.get_data().get('image2')
    
            height_scale_factor = .55
            width_scale_factor = .7
            max_width, max_height = int(1100 * width_scale_factor), int(850 * height_scale_factor)  
    
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
            self.change_made = True  # Set the change flag
        except Exception as e:
            print(f"An error occurred while placing images on the flyer: {e}")

    def update_flyer(self):
        """
        Updates the flyer by placing images on it.
        """
        if not self.change_made:
            return

        try:
            print("Updating flyer...")
            self.apply_background_color()
            self.place_images_on_flyer()
            self.update_data_handler()  # Ensure the data handler is updated with the modified flyer image
            self.change_made = False  # Reset the change flag
            # Save the flyer image
            self.image.save('flyer.png')
            print("Flyer image saved as 'flyer.png'")
        except Exception as e:
            print(f"An error occurred while updating the flyer: {e}")