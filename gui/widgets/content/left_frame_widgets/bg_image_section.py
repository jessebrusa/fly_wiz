from tkinter import ttk
from .handlers.color_picker_handler import ColorPickerHandler

LABEL_FONT = ("Helvetica", 16)

class BgImageSection(ttk.Frame):
    def __init__(self, parent, ui_helpers, image_handler, color_wheel_handler, open_search_window):
        """
        Initializes the background image section with the parent widget, UI helpers, image handler, and callbacks.

        Parameters
        ----------
        parent : widget
            The parent widget.
        ui_helpers : UIHelpers
            The UI helpers instance.
        image_handler : ImageHandler
            The image handler instance.
        color_wheel_handler : ColorWheelHandler
            The color wheel handler instance.
        open_search_window : function
            The callback function to open the search window.
        """
        super().__init__(parent, borderwidth=1, relief="solid", width=200)
        self.ui_helpers = ui_helpers
        self.image_handler = image_handler
        self.color_wheel_handler = color_wheel_handler
        self.open_search_window = open_search_window
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

        color_picker_handler = ColorPickerHandler(self.image_handler.data_handler, self.image_handler.main_app.flyer_manipulator)
        color_picker_button = ttk.Button(button_frame_3, text="Color Picker", style="Small.TButton", width=14, command=color_picker_handler.extract_colors)
        color_picker_button.pack(side="left", padx=5)

        color_wheel_button = ttk.Button(button_frame_3, text="Color / Direction", style="Small.TButton", width=14, command=self.open_color_wheel_window)
        color_wheel_button.pack(side="left", padx=5)

        # Check if images are selected
        image1_selected = self.image_handler.data_handler.get_data().get('image1') is not None
        image2_selected = self.image_handler.data_handler.get_data().get('image2') is not None

        # Label for first image
        label_text_1 = "Image 1" + (" ✓:" if image1_selected else " :")
        label = ttk.Label(self, text=label_text_1, font=LABEL_FONT, width=10, anchor="center")
        label.grid(row=1, column=0, padx=5, pady=5, sticky="ns")

        # Frame for the first set of buttons
        button_frame_1 = ttk.Frame(self)
        button_frame_1.grid(row=1, column=1, columnspan=3, padx=5, pady=2, sticky="nsew")

        browse_button_1 = ttk.Button(button_frame_1, text="Browse", style="Small.TButton", width=8, 
                                     command=lambda: self.image_handler.browse_image('image1'))
        browse_button_1.pack(side="left", padx=5)

        search_button_1 = ttk.Button(button_frame_1, text="Search", style="Small.TButton", width=8, 
                                     command=lambda: self.open_search_window('image1'))
        search_button_1.pack(side="left", padx=5)
        
        remove_button_1 = ttk.Button(button_frame_1, text="Remove", style="Small.TButton", width=8, 
                                     command=lambda: self.image_handler.remove_image('image1'))
        remove_button_1.pack(side="left", padx=5)

        # Label for second image
        label_text_2 = "Image 2" + (" ✓:" if image2_selected else " :")
        second_image_label = ttk.Label(self, text=label_text_2, font=LABEL_FONT, width=10, anchor="center")
        second_image_label.grid(row=2, column=0, padx=5, pady=5, sticky="ns")

        # Frame for the second set of buttons
        button_frame_2 = ttk.Frame(self)
        button_frame_2.grid(row=2, column=1, columnspan=3, padx=5, pady=2, sticky="nsew")

        browse_button_2 = ttk.Button(button_frame_2, text="Browse", style="Small.TButton", width=8, 
                                     command=lambda: self.image_handler.browse_image('image2'))
        browse_button_2.pack(side="left", padx=5)

        search_button_2 = ttk.Button(button_frame_2, text="Search", style="Small.TButton", width=8, 
                                     command=lambda: self.open_search_window('image2'))
        search_button_2.pack(side="left", padx=5)
        
        remove_button_2 = ttk.Button(button_frame_2, text="Remove", style="Small.TButton", width=8, 
                                     command=lambda: self.image_handler.remove_image('image2'))
        remove_button_2.pack(side="left", padx=5)

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)

    def open_color_wheel_window(self, gradient=False):
        """
        Open a window with one or two squares for color selection.
        """
        self.color_wheel_handler.open_color_wheel_window(gradient)