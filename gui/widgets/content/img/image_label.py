from tkinter import ttk, Canvas
from PIL import Image, ImageTk

class ImageLabel(ttk.Frame):
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

        # Create a canvas to place the image
        self.canvas = Canvas(self, width=width, height=int((8.5 / 11) * width), highlightthickness=0)
        self.canvas.pack()

        self.original_image, self.scaled_image = self.load_and_scale_image(self.scale_factor)
        self.image_id = self.canvas.create_image(0, 0, anchor="nw", image=self.scaled_image)

        # Bind click events to the image within the canvas
        self.canvas.tag_bind(self.image_id, "<ButtonPress-1>", self.on_press)
        self.canvas.tag_bind(self.image_id, "<ButtonRelease-1>", self.on_release)

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
        print(f"Loading and scaling image with scale factor: {scale_factor}")
        image = Image.open(self.image_path)
        height = int((8.5 / 11) * self.width)  # Calculate height based on the ratio 8.5 by 11
        image = image.resize((self.width, height), Image.LANCZOS)  # Resize the image
        scaled_width = int(self.width * scale_factor)  # Scale width
        scaled_height = int(height * scale_factor)  # Scale height
        scaled_image = image.resize((scaled_width, scaled_height), Image.LANCZOS)
        print(f"Scaled image size: {scaled_width}x{scaled_height}")
        return ImageTk.PhotoImage(image), ImageTk.PhotoImage(scaled_image)

    def on_press(self, event):
        """
        Handles the press event to scale down the image.

        Parameters
        ----------
        event : Event
            The event object.
        """
        print('Image clicked!')
        _, self.scaled_image = self.load_and_scale_image(0.9)  # Scale down the image slightly
        self.update_image_position()
        print('Image scaled down.')

    def on_release(self, event):
        """
        Handles the release event to return the image to its original size and trigger the click handler.

        Parameters
        ----------
        event : Event
            The event object.
        """
        print('Image released!')
        _, self.scaled_image = self.load_and_scale_image(1.0)  # Return the image to its original size
        self.update_image_position()
        print('Image returned to original size.')
        self.on_click(event)  # Trigger the click handler

    def update_image_position(self):
        """
        Updates the position of the image to keep it centered within the canvas.
        """
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        image_width = self.scaled_image.width()
        image_height = self.scaled_image.height()
        x = (canvas_width - image_width) // 2
        y = (canvas_height - image_height) // 2
        self.canvas.coords(self.image_id, x, y)
        self.canvas.itemconfig(self.image_id, image=self.scaled_image)