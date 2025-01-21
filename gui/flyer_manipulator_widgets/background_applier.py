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
            bg_color = self.data_handler.get_data().get('bg_color', {})
            color1 = bg_color.get('color1', '#FFFFFF')
            color2 = bg_color.get('color2', None)
            gradient_state = bg_color.get('gradient_state', 0)
            direction = bg_color.get('direction', 'Top to Bottom')

            # Ensure colors are in the correct format
            if isinstance(color1, str) and color1.startswith('#'):
                color1 = tuple(int(color1[i:i+2], 16) for i in (1, 3, 5))
            if color2 and isinstance(color2, str) and color2.startswith('#'):
                color2 = tuple(int(color2[i:i+2], 16) for i in (1, 3, 5))

            width, height = image.size
            if gradient_state == 1 and color2:
                image = Image.new('RGBA', (width, height))
                self.apply_gradient_background(image, color1, color2, direction)
                print(f"Applied gradient background: color1={color1}, color2={color2}, direction={direction}")
            else:
                image = Image.new('RGBA', (width, height), color=color1 + (255,))
                print(f"Applied solid background color: {color1}")

            self.data_handler.update_data('flyer', image)
            return image
        except Exception as e:
            print(f"An error occurred while applying the background color: {e}")
            return image

    def apply_gradient_background(self, image, color1, color2, direction):
        """
        Apply a gradient background to the flyer image.
        """
        width, height = image.size
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
        gradient_image = Image.composite(base, top, mask)
        image.paste(gradient_image, (0, 0), gradient_image)