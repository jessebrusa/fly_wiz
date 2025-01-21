from PIL import Image

class BackgroundApplier:
    def __init__(self, data_handler):
        self.data_handler = data_handler

    def apply_background_color(self, image, color1, color2=None, gradient_state=0):
        """
        Apply the background color to the flyer image.
        """
        try:
            width, height = image.size
            if gradient_state == 1 and color2:
                image = Image.new('RGBA', (width, height))
                # Apply gradient background
                self.apply_gradient_background(image, color1, color2)
            else:
                image = Image.new('RGBA', (width, height), color=color1 + (255,))

            print(f"Applied background color: {color1}")
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
        print(f"Applied gradient background: color1={color1}, color2={color2}")
        return image