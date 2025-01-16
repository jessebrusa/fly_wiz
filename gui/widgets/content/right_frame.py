from tkinter import ttk
from .img.image_label import ImageLabel
from PIL import Image, ImageTk

class RightFrame(ttk.Frame):
    """
    A class to represent the right frame of the GUI.

    Attributes
    ----------
    parent : widget
        The parent widget.
    data_handler : DataHandler
        The data handler instance.

    Methods
    -------
    __init__(parent, data_handler):
        Initializes the right frame with the parent widget and data handler.
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
    def __init__(self, parent, data_handler):
        """
        Initializes the right frame with the parent widget and data handler.

        Parameters
        ----------
        parent : widget
            The parent widget.
        data_handler : DataHandler
            The data handler instance.
        """
        super().__init__(parent, borderwidth=2, relief="solid")
        self.data_handler = data_handler
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
        self.grid_rowconfigure(0, weight=8)  # Increase weight for the top section
        self.grid_rowconfigure(1, weight=1, minsize=100)  # Decrease weight and set minimum size for the bottom section
        self.grid_columnconfigure(0, weight=1)

    def create_first_section(self):
        """
        Creates and places the first section in the right frame.
        """
        first_section = ttk.Frame(self, borderwidth=1, relief="solid")
        first_section.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)
        
        # Get the image from the data handler
        image = self.data_handler.get_data().get('flyer')
        if image:
            # Scale the image down to 0.7 of its original size
            width, height = image.size
            scale_factor = 0.45
            new_size = (int(width * scale_factor), int(height * scale_factor))
            scaled_image = image.resize(new_size, Image.LANCZOS)
            
            image_tk = ImageTk.PhotoImage(scaled_image)
            image_label = ttk.Label(first_section, image=image_tk)
            image_label.image = image_tk  # Keep a reference to avoid garbage collection
            image_label.pack(expand=True)  # Center the image vertically
        else:
            print("No image found in data handler")

    def create_second_section(self):
        """
        Creates and places the second section in the right frame.
        """
        second_section = ttk.Frame(self, borderwidth=1, relief="solid")
        second_section.grid(row=1, column=0, sticky="nsew", padx=5, pady=2)
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
        button_frame.pack(expand=True, fill="both")

        # Create an inner frame to hold the buttons and center them vertically
        inner_frame = ttk.Frame(button_frame)
        inner_frame.pack(expand=True)

        # Create Save and Load buttons with increased height and more space between them
        save_button = ttk.Button(inner_frame, text="Save", width=10)
        save_button.pack(pady=5, ipady=12)  # Add padding between buttons

        load_button = ttk.Button(inner_frame, text="Load", width=10)
        load_button.pack(pady=5, ipady=12)  # Add padding between buttons

        # Create Export button
        export_button = ttk.Button(inner_frame, text="Export", width=10)
        export_button.pack(pady=5, ipady=12)  # Add padding between buttons