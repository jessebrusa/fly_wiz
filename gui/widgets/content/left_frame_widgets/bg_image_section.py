from tkinter import ttk
from .bg_image_handlers.image_handler import ImageHandler
from .bg_image_handlers.background_handler import BackgroundHandler
from .bg_image_handlers.color_wheel_handler import ColorWheelHandler
from .bg_image_handlers.search_handler import SearchHandler
from .bg_image_handlers.color_picker_handler import ColorPickerHandler

LABEL_FONT = ("Helvetica", 16)

class BgImageSection(ttk.Frame):
    def __init__(self, parent, data_handler, main_app):
        """
        Initializes the background image section with the parent widget, data handler, and main application instance.

        Parameters
        ----------
        parent : widget
            The parent widget.
        data_handler : DataHandler
            The data handler instance.
        main_app : FlyWizGui
            The main application instance.
        """
        super().__init__(parent, borderwidth=1, relief="solid", width=200)
        self.data_handler = data_handler
        self.main_app = main_app
        self.image_handler = ImageHandler(data_handler, main_app, self.update_ui)
        self.background_handler = BackgroundHandler(data_handler, main_app)
        self.color_wheel_handler = ColorWheelHandler(self, data_handler, main_app)
        self.search_handler = SearchHandler(data_handler, main_app.flyer_manipulator, self.update_ui)
        self.pack(fill="both", expand=True, padx=5, pady=5)
        self.grid_propagate(False)
        self.grid_rowconfigure(0, weight=1)
        self.create_section()

    def create_section(self):
        """
        Creates and places the content in the background image section.
        """
        self.create_label_and_buttons()

    def create_label_and_buttons(self):
        """
        Create a label and buttons within the background image section.
        """
        # Clear the parent frame to avoid duplicate widgets
        for widget in self.winfo_children():
            widget.destroy()

        # Label for background color
        label_text_3 = "BG Color:"
        background_label = ttk.Label(self, text=label_text_3, font=LABEL_FONT, width=10, anchor="center")
        background_label.grid(row=0, column=0, padx=5, pady=5, sticky="ns")

        # Frame for the background color buttons
        button_frame_3 = ttk.Frame(self)
        button_frame_3.grid(row=0, column=1, columnspan=2, padx=5, pady=2, sticky="nsew")

        color_picker_handler = ColorPickerHandler(self.data_handler, self.main_app.flyer_manipulator)
        color_picker_button = ttk.Button(button_frame_3, text="Color Picker", style="Small.TButton", width=14, command=color_picker_handler.extract_colors)
        color_picker_button.pack(side="left", padx=5)

        color_wheel_button = ttk.Button(button_frame_3, text="Color / Direction", style="Small.TButton", width=14, command=self.open_color_wheel_window)
        color_wheel_button.pack(side="left", padx=5)

        # Create labels and buttons for images
        self.create_image_section('image1', 1)
        self.create_image_section('image2', 2)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

    def create_image_section(self, image_key, row):
        """
        Create a section for an image with a label and buttons.

        Parameters
        ----------
        image_key : str
            The key for the image in the data handler.
        row : int
            The row in which to place the section.
        """
        image_selected = self.image_handler.is_image_present(image_key)
        label_text = f"Image {row}" + (" ✓:" if image_selected else " :")
        label = ttk.Label(self, text=label_text, font=LABEL_FONT, width=10, anchor="center")
        label.grid(row=row, column=0, padx=5, pady=5, sticky="ns")

        button_frame = ttk.Frame(self)
        button_frame.grid(row=row, column=1, columnspan=3, padx=5, pady=2, sticky="nsew")

        browse_button = ttk.Button(button_frame, text="Browse", style="Small.TButton", width=8, 
                                   command=lambda: self.image_handler.browse_image(image_key))
        browse_button.pack(side="left", padx=5)

        search_button = ttk.Button(button_frame, text="Search", style="Small.TButton", width=8, 
                                   command=lambda: self.search_handler.open_search_window(image_key))
        search_button.pack(side="left", padx=5)
        
        remove_button = ttk.Button(button_frame, text="Remove", style="Small.TButton", width=8, 
                                   command=lambda: self.image_handler.remove_image(image_key))
        remove_button.pack(side="left", padx=5)

    def open_color_wheel_window(self, gradient=False):
        """
        Open a window with one or two squares for color selection.
        """
        self.color_wheel_handler.open_color_wheel_window(gradient)

    def update_ui(self):
        """
        Update the UI by updating the labels and buttons.
        """
        self.update_labels_and_buttons()

    def update_labels_and_buttons(self):
        """
        Update the labels and buttons within the background image section.
        """
        self.create_image_section('image1', 1)
        self.create_image_section('image2', 2)