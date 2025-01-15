import tkinter as tk
from PIL import Image, ImageTk

class ImageLabel(tk.Label):
    """
    A class to represent a label with an image that can be scaled.

    Attributes
    ----------
    parent : widget
        The parent widget.
    image_path : str
        The path to the image file.
    width : int
        The desired width of the image.
    scale_factor : float
        The factor by which to scale the image.

    Methods
    -------
    load_and_scale_image():
        Loads and scales the image.
    on_image_press(event):
        Handles the image press event to scale down the image and print a message.
    on_image_release(event):
        Handles the image release event to restore the image size.
    """
    def __init__(self, parent, image_path, width, scale_factor):
        """
        Initializes the ImageLabel with the parent widget, image path, width, and scale factor.

        Parameters
        ----------
        parent : widget
            The parent widget.
        image_path : str
            The path to the image file.
        width : int
            The desired width of the image.
        scale_factor : float
            The factor by which to scale the image.
        """
        super().__init__(parent, borderwidth=0, highlightthickness=0)
        self.image_path = image_path
        self.width = width
        self.scale_factor = scale_factor
        self.original_image, self.scaled_image = self.load_and_scale_image()
        self.config(image=self.original_image)
        self.bind("<ButtonPress-1>", self.on_image_press)
        self.bind("<ButtonRelease-1>", self.on_image_release)

    def load_and_scale_image(self):
        """
        Loads and scales the image.

        Returns
        -------
        tuple
            The original and scaled images.
        """
        image = Image.open(self.image_path)
        height = int((8.5 / 11) * self.width)  # Calculate height based on the ratio 8.5 by 11
        image = image.resize((self.width, height), Image.LANCZOS)  # Resize the image
        scaled_down_width = int(self.width * 0.9)  # Scale down by 10%
        scaled_down_height = int(height * 0.9)  # Scale down by 10%
        scaled_image = image.resize((scaled_down_width, scaled_down_height), Image.LANCZOS)
        return ImageTk.PhotoImage(image), ImageTk.PhotoImage(scaled_image)

    def on_image_press(self, event):
        """
        Handle the image press event to scale down the image and print a message.
        """
        print("Image clicked!")
        self.config(image=self.scaled_image)

    def on_image_release(self, event):
        """
        Handle the image release event to restore the image size.
        """
        self.config(image=self.original_image)
        """
        Handle the image release event to restore the image size.
        """
        self.config(image=self.original_image)