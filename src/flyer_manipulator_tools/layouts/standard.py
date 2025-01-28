from .base_layout import BaseLayout
from PIL import ImageFont, ImageDraw

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

    def center_text_horizontally(self, text, font):
        """
        Calculate the x-coordinate to center the text horizontally on the flyer.

        Parameters
        ----------
        text : str
            The text to be centered.
        font : ImageFont
            The font used to render the text.

        Returns
        -------
        int
            The x-coordinate to center the text horizontally.
        """
        draw = ImageDraw.Draw(self.flyer_image)
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        image_width = self.flyer_image.width
        x = (image_width - text_width) // 2
        return x

    def center_text_vertically_top_25(self, text, font):
        """
        Calculate the y-coordinate to center the text vertically within the top 25% of the flyer.

        Parameters
        ----------
        text : str
            The text to be centered.
        font : ImageFont
            The font used to render the text.

        Returns
        -------
        int
            The y-coordinate to center the text vertically within the top 25% of the flyer.
        """
        draw = ImageDraw.Draw(self.flyer_image)
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_height = text_bbox[3] - text_bbox[1]
        image_height = self.flyer_image.height
        top_25_height = image_height // 4
        y = (top_25_height - text_height) // 2
        return y

    def place_title(self, font_size=None, color="black"):
        """
        Place the title text on the flyer at a specific location for the standard layout.

        Parameters
        ----------
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
        
        # Calculate the x-coordinate to center the text horizontally
        x = self.center_text_horizontally(title_text, font)
        
        # Calculate the y-coordinate to center the text vertically within the top 25%
        y = self.center_text_vertically_top_25(title_text, font)
        
        # Draw the text on the flyer
        draw = ImageDraw.Draw(self.flyer_image)
        draw.text((x, y), title_text, font=font, fill=color)

    def apply_layout(self):
        """
        Apply the standard layout to the flyer.
        """
        self.place_title(color="black")

        return self.flyer_image