from .base_layout import BaseLayout
from PIL import ImageFont

class Standard(BaseLayout):
    def __init__(self, flyer_image, data_handler):
        super().__init__(flyer_image, data_handler)
        self.font_paths = {
            "Bernard Condensed": r"src/flyer_manipulator_tools/layouts/fonts/BernardMTCondensed.ttf",
            "Arial": r"src/flyer_manipulator_tools/layouts/fonts/Arial.ttf",
            "Courier": r"src/flyer_manipulator_tools/layouts/fonts/CourierPrime-Bold.ttf",
            "Helvetica": r"src/flyer_manipulator_tools/layouts/fonts/Helvetica-Bold.ttf",
            "Times New Roman": r"src/flyer_manipulator_tools/layouts/fonts/times new roman bold.ttf",
            "Verdana": r"src/flyer_manipulator_tools/layouts/fonts/VERDANAI.TTF"
        }
        self.apply_layout()

    def get_title_text(self):
        """
        Get the title text from the data handler.
        """
        return self.data_handler.get_data().get("title", {}).get("text", "")

    def get_title_font(self):
        """
        Get the title font from the data handler.
        """
        return self.data_handler.get_data().get("title", {}).get("font", "Bernard Condensed")

    def get_title_font_size(self):
        """
        Get the title font size from the data handler.
        """
        return self.data_handler.get_data().get("title", {}).get("font_size", 40)

    def get_font_path(self, font_name):
        """
        Get the path to the TTF file for the given font name.
        """
        return self.font_paths.get(font_name)

    def place_title(self, x=100, y=100, font_size=None, color="black"):
        """
        Place the title text on the flyer at a specific location for the standard layout.

        Parameters
        ----------
        x : int
            The x-coordinate of the title text.
        y : int
            The y-coordinate of the title text.
        font_size : int or None
            The size of the font. If None, the default size from the data handler is used.
        color : str
            The color of the text.
        """
        title_text = self.get_title_text()
        title_font = self.get_title_font()
        title_font_size = self.get_title_font_size()
        font_path = self.get_font_path(title_font)
        if font_size is None:
            font_size = title_font_size
        try:
            font = ImageFont.truetype(font_path, font_size)
            print(f"Font loaded: {font_path} with size {font_size}")
        except IOError:
            print(f"Failed to load font: {font_path}. Using default font.")
            font = ImageFont.load_default()
        self.draw.text((x, y), title_text, font=font, fill=color)

    def apply_layout(self):
        """
        Apply the standard layout to the flyer.
        """
        self.place_title(x=100, y=100, color="black")

        return self.flyer_image