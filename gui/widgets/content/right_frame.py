from tkinter import ttk
from .right_frame_widgets.flyer_image_section import FlyerImageSection
from .right_frame_widgets.layout_section import LayoutSection
from .right_frame_widgets.export_section import ExportSection

class RightFrame(ttk.Frame):
    def __init__(self, parent, data_handler, main_app):
        """
        Initializes the right frame with the parent widget, data handler, and main application instance.

        Parameters
        ----------
        parent : widget
            The parent widget.
        data_handler : DataHandler
            The data handler instance.
        main_app : FlyWizGui
            The main application instance.
        """
        super().__init__(parent, borderwidth=2, relief="solid")
        self.data_handler = data_handler
        self.main_app = main_app
        self.config(width=300)  # Set a fixed width for the right frame
        try:
            self.configure_main_frame_grid()
            self.create_flyer_image_section()
            self.create_second_section()
        except Exception as e:
            print(f"An error occurred while initializing the right frame: {e}")

    def configure_main_frame_grid(self):
        """
        Configures the grid layout for the main frame.
        """
        self.grid_rowconfigure(0, weight=8)  # Increase weight for the top section
        self.grid_rowconfigure(1, weight=1, minsize=100)  # Decrease weight and set minimum size for the bottom section
        self.grid_columnconfigure(0, weight=1)

    def create_flyer_image_section(self):
        """
        Creates and places the flyer image section in the right frame.
        """
        self.flyer_image_section = FlyerImageSection(self, self.data_handler)
        self.flyer_image_section.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)
        self.image_label = self.flyer_image_section.image_label  # Reference the image_label from FlyerImageSection

    def create_second_section(self):
        """
        Creates and places the second section in the right frame.
        """
        second_section = ttk.Frame(self, borderwidth=1, relief="solid")
        second_section.grid(row=1, column=0, sticky="nsew", padx=5, pady=2)
        second_section.grid_rowconfigure(0, weight=1)
        second_section.grid_columnconfigure(0, weight=3)
        second_section.grid_columnconfigure(1, weight=1)
        self.create_layout_section(second_section)
        self.create_export_section(second_section)

    def create_layout_section(self, parent):
        """
        Creates and places the layout section in the second section.

        Parameters
        ----------
        parent : widget
            The parent widget.
        """
        self.layout_section = LayoutSection(parent, self.main_app)
        self.layout_section.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    def create_export_section(self, parent):
        """
        Creates and places the export section in the second section.

        Parameters
        ----------
        parent : widget
            The parent widget.
        """
        self.export_section = ExportSection(parent, self.data_handler, self.main_app)
        self.export_section.grid(row=0, column=1, sticky="nsew", padx=5, pady=2)

    def configure_grid(self, parent, rows, cols):
        """
        Configures the grid layout to ensure labels expand to fill the space.

        Parameters
        ----------
        parent : widget
            The parent widget.
        rows : int
            The number of rows in the grid.
        cols : int
            The number of columns in the grid.
        """
        for row in range(rows):
            parent.grid_rowconfigure(row, weight=1)
        for col in range(cols):
            parent.grid_columnconfigure(col, weight=1)