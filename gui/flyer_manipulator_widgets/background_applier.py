from PIL import Image

class BackgroundApplier:
    def __init__(self, data_handler):
        self.data_handler = data_handler

    def apply_background_color(self, image):
        """
        Apply the background color to the flyer image.
        """
        if image is None:
            print("No image provided to apply background color.")
            return None

        try:
            # Retrieve the colors from the data handler
            extracted_colors = self.data_handler.get_data().get('extracted_colors', {})
            color1 = extracted_colors.get('color1', None)
            color2 = extracted_colors.get('color2', None)

            # If both colors are None, return without applying any background
            if color1 is None and color2 is None:
                print("No background color applied: both color1 and color2 are None")
                return image

            width, height = image.size

            # If both colors are present, apply a gradient background
            if color1 and color2:
                image = Image.new('RGBA', (width, height))
                self.apply_gradient_background(image, color1, color2)
                print(f"Applied gradient background: color1={color1}, color2={color2}")
            else:
                # Apply a solid background with the available color
                solid_color = color1 if color1 else color2
                image = Image.new('RGBA', (width, height), color=solid_color + (255,))
                print(f"Applied solid background color: {solid_color}")

            self.data_handler.update_data('flyer', image)
            return image
        except Exception as e:
            print(f"An error occurred while applying the background color: {e}")
            return image

    def apply_gradient_background(self, image, color1, color2):
        """
        Apply a gradient background to the flyer image.
        """
        width, height = image.size
        base = Image.new('RGBA', (width, height), color1 + (255,))
        top = Image.new('RGBA', (width, height), color2 + (255,))
        mask = Image.new('L', (width, height))
        mask_data = []

        for y in range(height):
            for x in range(width):
                mask_data.append(int(255 * y / height))

        mask.putdata(mask_data)
        gradient_image = Image.composite(base, top, mask)
        image.paste(gradient_image, (0, 0), gradient_image)