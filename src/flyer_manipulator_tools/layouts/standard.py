from .base_layout import BaseLayout
from PIL import ImageFont

class Standard(BaseLayout):
    def __init__(self, flyer_image, data_handler):
        super().__init__(flyer_image, data_handler)
        self.default_font_path = "src/flyer_manipulator_tools/layouts/fonts/BernardMTCondensed.ttf"
        self.title_text = self.get_data_handler_title_text()
        self.apply_layout()

    def get_data_handler_title_text(self):
        """
        Get the title text from the data handler.
        """
        return self.data_handler.get_data().get("title", "")

    def place_title(self, x=100, y=100, font_path=None, font_size=40, color="black"):
        """
        Place the title text on the flyer at a specific location for the standard layout.

        Parameters
        ----------
        x : int
            The x-coordinate of the title text.
        y : int
            The y-coordinate of the title text.
        font_path : str or None
            The path to the font file to be used. If None, the default BernardMTCondensed font is used.
        font_size : int
            The size of the font.
        color : str
            The color of the text.
        """
        if font_path is None:
            font_path = self.default_font_path
        font = ImageFont.truetype(font_path, font_size)
        self.draw.text((x, y), self.title_text, font=font, fill=color)

    def apply_layout(self):
        """
        Apply the standard layout to the flyer.
        """
        self.place_title(x=100, y=100, font_size=40, color="black")
        return self.flyer_image