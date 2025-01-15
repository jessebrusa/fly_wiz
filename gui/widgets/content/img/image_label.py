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
    on_click(event):
        Handles the click event to scale down the image.
    on_release(event):
        Handles the release event to return the image to its original size.
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
        self.original_image, self.scaled_image = self.load_and_scale_image(self.scale_factor)
        self.config(image=self.scaled_image)
        self.bind("<Button-1>", self.on_click)  # Bind left mouse click to the on_click method
        self.bind("<ButtonRelease-1>", self.on_release)  # Bind left mouse release to the on_release method

    def load_and_scale_image(self, scale_factor):
        """
        Loads and scales the image.

        Parameters
        ----------
        scale_factor : float
            The factor by which to scale the image.

        Returns
        -------
        tuple
            The original and scaled images.
        """
        image = Image.open(self.image_path)
        height = int((8.5 / 11) * self.width)  # Calculate height based on the ratio 8.5 by 11
        image = image.resize((self.width, height), Image.LANCZOS)  # Resize the image
        scaled_width = int(self.width * scale_factor)  # Scale width
        scaled_height = int(height * scale_factor)  # Scale height
        scaled_image = image.resize((scaled_width, scaled_height), Image.LANCZOS)
        return ImageTk.PhotoImage(image), ImageTk.PhotoImage(scaled_image)

    def on_click(self, event):
        """
        Handles the click event to scale down the image.

        Parameters
        ----------
        event : Event
            The event object.
        """
        print('clicked')
        self.scale_factor = 0.9  # Set the scale factor to scale down the image slightly
        _, self.scaled_image = self.load_and_scale_image(self.scale_factor)
        self.config(image=self.scaled_image)

    def on_release(self, event):
        """
        Handles the release event to return the image to its original size.

        Parameters
        ----------
        event : Event
            The event object.
        """
        self.scale_factor = 1.0  # Set the scale factor to return the image to its original size
        _, self.scaled_image = self.load_and_scale_image(self.scale_factor)
        self.config(image=self.scaled_image)