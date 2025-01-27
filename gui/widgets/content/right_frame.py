from tkinter import ttk
from tkinter import filedialog
from .img.image_label import ImageLabel
from .right_frame_widgets.first_section import FirstSection

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
        self.first_section = FirstSection(self, self.data_handler)
        self.first_section.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)
        self.image_label = self.first_section.image_label  # Reference the image_label from FirstSection

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

        # Create a 3x2 grid of ImageLabels with layout names
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
                
                image_label = ImageLabel(left_subsection, image_path, 110, 1, lambda event, name=layout_name: self.change_layout(name))
                image_label.grid(row=row+1, column=col, sticky="nsew", padx=5, pady=5)

        # Configure the grid to ensure labels expand to fill the space
        self.configure_grid(left_subsection, 3, 3)

    def change_layout(self, layout_name):
        """
        Change the layout of the flyer.
        """
        print(f"Setting layout to: {layout_name}")
        self.main_app.flyer_manipulator.set_layout(layout_name)
        self.main_app.update_gui()

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

        # Create a frame to center the buttons vertically and horizontally
        button_frame = ttk.Frame(right_subsection)
        button_frame.grid(row=0, column=0, sticky="nsew")

        # Configure the grid to ensure buttons expand to fill the space
        right_subsection.grid_rowconfigure(0, weight=1)
        right_subsection.grid_columnconfigure(0, weight=1)
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_rowconfigure(1, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        button_width = 8  

        save_button = ttk.Button(button_frame, text="Save", width=button_width, command=self.save_data)
        save_button.grid(row=0, column=0, padx=5, pady=2, sticky="nsew")

        load_button = ttk.Button(button_frame, text="Load", width=button_width, command=self.load_data)
        load_button.grid(row=0, column=1, padx=5, pady=2, sticky="nsew")

        export_button = ttk.Button(button_frame, text="Export", width=button_width)
        export_button.grid(row=1, column=0, padx=5, pady=15, sticky="nsew")

        print_button = ttk.Button(button_frame, text="Print", width=button_width)
        print_button.grid(row=1, column=1, padx=5, pady=15, sticky="nsew")

    def save_data(self):
        """
        Open a file dialog to pick a location and name for the file, then save the data.
        """
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            self.data_handler.save(file_path)
            print(f"Data saved to {file_path}")

    def load_data(self):
        """
        Open a file dialog to select a JSON file, then load the data.
        """
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            self.data_handler.load(file_path)
            print(f"Data loaded from {file_path}")
            self.main_app.update_gui()

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