# FILE: gui/image_manipulator.py

from PIL import Image, ImageDraw, ImageFont

class ImageManipulator:
    """
    A class to manipulate a Pillow image with data from the DataHandler.

    Attributes
    ----------
    image : Image
        The Pillow image to be manipulated.

    Methods
    -------
    load_image(image_path):
        Loads an image from the given path.
    add_text(text, position, font_path, font_size, color):
        Adds text to the image at the specified position.
    save_image(output_path):
        Saves the manipulated image to the specified output path.
    """
    def __init__(self):
        """
        Initializes the ImageManipulator with a None image.
        """
        self.image = None

    def load_image(self, image_path):
        """
        Loads an image from the given path.

        Parameters
        ----------
        image_path : str
            The path to the image file.
        """
        self.image = Image.open(image_path)

    def add_text(self, text, position, font_path, font_size, color):
        """
        Adds text to the image at the specified position.

        Parameters
        ----------
        text : str
            The text to be added to the image.
        position : tuple
            The (x, y) position to add the text.
        font_path : str
            The path to the font file.
        font_size : int
            The size of the font.
        color : tuple
            The color of the text.
        """
        draw = ImageDraw.Draw(self.image)
        font = ImageFont.truetype(font_path, font_size)
        draw.text(position, text, font=font, fill=color)

    def save_image(self, output_path):
        """
        Saves the manipulated image to the specified output path.

        Parameters
        ----------
        output_path : str
            The path to save the manipulated image.
        """
        self.image.save(output_path)