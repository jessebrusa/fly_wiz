from tkinter import ttk
from ..img.image_label import ImageLabel

class LeftSubsection(ttk.Frame):
    def __init__(self, parent, change_layout_callback):
        """
        Initializes the left subsection with the parent widget and change layout callback.

        Parameters
        ----------
        parent : widget
            The parent widget.
        change_layout_callback : function
            The callback function to change the layout.
        """
        super().__init__(parent, borderwidth=1, relief="solid")
        self.change_layout_callback = change_layout_callback
        self.create_subsection()

    def create_subsection(self):
        """
        Creates and places the content in the left subsection.
        """
        layout_names = ["standard", "flyer", "halfsheet", "info", "landscape_movie", "large_picture", "portrait_movie"]
        image_paths = [
            "./gui/widgets/content/img/standard.jpg",
            "./gui/widgets/content/img/flyer-halfsheet.jpg",
            "./gui/widgets/content/img/info.jpg",
            "./gui/widgets/content/img/landscape_movie.jpg",
            "./gui/widgets/content/img/portrait_movie.jpg",
            "./gui/widgets/content/img/large_picture.jpg"
        ]
        for row in range(2):
            for col in range(3):
                layout_name = layout_names[row * 3 + col]
                image_path = image_paths[row * 3 + col]
                
                image_label = ImageLabel(self, image_path, 110, 1, lambda event, name=layout_name: self.change_layout_callback(name))
                image_label.grid(row=row+1, column=col, sticky="nsew", padx=5, pady=5)

        # Configure the grid to ensure labels expand to fill the space
        self.configure_grid(3, 3)

    def configure_grid(self, rows, cols):
        """
        Configures the grid layout to ensure labels expand to fill the space.

        Parameters
        ----------
        rows : int
            The number of rows in the grid.
        cols : int
            The number of columns in the grid.
        """
        for row in range(rows):
            self.grid_rowconfigure(row, weight=1)
        for col in range(cols):
            self.grid_columnconfigure(col, weight=1)