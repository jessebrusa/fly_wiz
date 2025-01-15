from tkinter import ttk
from .img.image_label import ImageLabel

class RightFrame(ttk.Frame):
    """
    A class to represent the right frame of the GUI.

    Attributes
    ----------
    parent : widget
        The parent widget.

    Methods
    -------
    __init__(parent):
        Initializes the right frame with the parent widget.
    configure_main_frame_grid():
        Configures the grid layout for the main frame.
    create_first_section():
        Creates and places the first section in the right frame.
    create_second_section():
        Creates and places the second section in the right frame.
    create_left_subsection(parent):
        Creates and places the left subsection in the second section.
    create_right_subsection(parent):
        Creates and places the right subsection in the second section.
    """
    def __init__(self, parent):
        """
        Initializes the right frame with the parent widget.

        Parameters
        ----------
        parent : widget
            The parent widget.
        """
        super().__init__(parent, borderwidth=2, relief="solid")
        try:
            self.configure_main_frame_grid()
            self.create_first_section()
            self.create_second_section()
        except Exception as e:
            print(f"An error occurred while initializing the right frame: {e}")

    def configure_main_frame_grid(self):
        """
        Configures the grid layout for the main frame.
        """
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_first_section(self):
        """
        Creates and places the first section in the right frame.
        """
        first_section = ttk.Frame(self, borderwidth=1, relief="solid")
        first_section.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        first_label = ttk.Label(first_section, text="Right Section 1")
        first_label.pack(pady=10)

    def create_second_section(self):
        """
        Creates and places the second section in the right frame.
        """
        second_section = ttk.Frame(self, borderwidth=1, relief="solid")
        second_section.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        second_section.grid_rowconfigure(0, weight=1)
        second_section.grid_columnconfigure(0, weight=3)
        second_section.grid_columnconfigure(1, weight=1)
        self.create_left_subsection(second_section)
        self.create_right_subsection(second_section)

    def create_left_subsection(self, parent):
        """
        Creates and places the left subsection in the second section.

        Parameters
        ----------
        parent : widget
            The parent widget.
        """
        left_subsection = ttk.Frame(parent, borderwidth=1, relief="solid")
        left_subsection.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

        # Create a 3x2 grid of ImageLabels
        image_path = "./gui/widgets/content/img/layout_1.jpg"
        for row in range(2):
            for col in range(3):
                image_label = ImageLabel(left_subsection, image_path, 110, 1.1)
                image_label.grid(row=row+1, column=col, sticky="nsew")

        # Configure the grid to ensure labels expand to fill the space
        self.configure_grid(left_subsection, 3, 3)

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
        parent.grid_rowconfigure(0, weight=1)
        parent.grid_rowconfigure(rows, weight=1)

    def create_right_subsection(self, parent):
        """
        Creates and places the right subsection in the second section.

        Parameters
        ----------
        parent : widget
            The parent widget.
        """
        right_subsection = ttk.Frame(parent, borderwidth=1, relief="solid")
        right_subsection.grid(row=0, column=1, sticky="nsew", padx=5, pady=2)

        # Create a frame to center the buttons vertically
        button_frame = ttk.Frame(right_subsection)
        button_frame.pack(expand=True)

        # Create Save and Load buttons with increased height and more space between them
        save_button = ttk.Button(button_frame, text="Save", width=10)
        save_button.pack(pady=(15, 5), ipady=12)  # Add more padding between buttons and increase internal padding

        load_button = ttk.Button(button_frame, text="Load", width=10)
        load_button.pack(pady=(5, 15), ipady=12)  # Add more padding between buttons and increase internal padding