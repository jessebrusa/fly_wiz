from PIL import Image

class BaseImageCreator:
    def create_base_image(self, width=1100, height=850, color=(255, 255, 255, 255)):
        """
        Creates a base blank image with specified dimensions and color.
        """
        try:
            return Image.new('RGBA', (width, height), color=color)
        except Exception as e:
            print(f"An error occurred while creating the base image: {e}")
            return None