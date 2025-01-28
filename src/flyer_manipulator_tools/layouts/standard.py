from .base_layout import BaseLayout
from PIL import ImageFont

class Standard(BaseLayout):
    def __init__(self, flyer_image, data_handler):
        super().__init__(flyer_image, data_handler)
        self.title_text = self.get_data_handler_title_text()
        self.apply_layout()

    def get_data_handler_title_text(self):
        """
        Get the title text from the data handler.
        """
        return self.data_handler.get_data().get("title", "")

    def place_title(self, x=100, y=100, font=None, font_size=40, color="black"):
        """
        Place the title text on the flyer at a specific location for the standard layout.

        Parameters
        ----------
        x : int
            The x-coordinate of the title text.
        y : int
            The y-coordinate of the title text.
        font : str or None
            The path to the font file to be used. If None, the default font is used.
        font_size : int
            The size of the font.
        color : str
            The color of the text.
        """
        if font:
            font = ImageFont.truetype(font, font_size)
        else:
            font = ImageFont.load_default()
        self.draw.text((x, y), self.title_text, font=font, fill=color)  

    def apply_layout(self):
        """
        Apply the standard layout to the flyer.
        """
        # Place the title text at the desired location
        self.place_title(x=100, y=100, font=None, font_size=40, color="black")

        return self.flyer_image