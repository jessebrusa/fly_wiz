from tkinter import ttk
from .layout_section_tools.image_label import ImageLabel

class LayoutSection(ttk.Frame):
    def __init__(self, parent, main_app):
        """
        Initializes the layout section with the parent widget and main application instance.

        Parameters
        ----------
        parent : widget
            The parent widget.
        main_app : FlyWizGui
            The main application instance.
        """
        super().__init__(parent, borderwidth=1, relief="solid")
        self.main_app = main_app
        self.create_section()

    def create_section(self):
        """
        Creates and places the content in the layout section.
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
                
                image_label = ImageLabel(self, image_path, 110, 1, lambda name=layout_name: self.change_layout(name))
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

    def change_layout(self, layout_name):
        """
        Change the layout of the flyer.
        """
        self.main_app.flyer_manipulator.set_layout(layout_name)
        self.main_app.update_gui()