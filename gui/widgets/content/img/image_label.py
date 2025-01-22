from tkinter import ttk
from PIL import Image, ImageTk

class ImageLabel(ttk.Label):
    def __init__(self, parent, image_path, width, scale_factor, on_click):
        """
        Initializes the ImageLabel with the parent widget, image path, width, scale factor, and click handler.

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
        on_click : function
            The function to call when the image is clicked.
        """
        super().__init__(parent, borderwidth=0)
        self.image_path = image_path
        self.width = width
        self.scale_factor = scale_factor
        self.on_click = on_click
        self.original_image, self.scaled_image = self.load_and_scale_image(self.scale_factor)
        self.config(image=self.scaled_image)
        self.bind("<ButtonPress-1>", self.on_press)  # Bind left mouse press to the on_press method
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

    def on_press(self, event):
        """
        Handles the press event to scale down the image.

        Parameters
        ----------
        event : Event
            The event object.
        """
        _, self.scaled_image = self.load_and_scale_image(0.9)  # Scale down the image slightly
        self.config(image=self.scaled_image)

    def on_release(self, event):
        """
        Handles the release event to return the image to its original size and trigger the click handler.

        Parameters
        ----------
        event : Event
            The event object.
        """
        _, self.scaled_image = self.load_and_scale_image(1.0)  # Return the image to its original size
        self.config(image=self.scaled_image)
        self.on_click(event)  # Trigger the click handler