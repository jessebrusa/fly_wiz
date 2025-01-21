from tkinter import ttk
from gui.widgets.content.left_frame import LeftFrame
from gui.widgets.content.right_frame import RightFrame

class ContentSection(ttk.Frame):
    """
    A class to represent the content section of the GUI.

    Attributes
    ----------
    parent : widget
        The parent widget.
    data_handler : DataHandler
        The data handler instance.
    main_app : FlyWizGui
        The main application instance.

    Methods
    -------
    configure_grid():
        Configures the grid layout for the content section.
    create_left_frame():
        Creates and places the left frame in the content section.
    create_right_frame():
        Creates and places the right frame in the content section.
    """
    def __init__(self, parent, data_handler, main_app):
        """
        Constructs all the necessary attributes for the ContentSection object.

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
        try:
            self.configure_grid()
            self.create_left_frame()
            self.create_right_frame()
        except Exception as e:
            print(f"An error occurred while initializing the content section: {e}")

    def configure_grid(self):
        """
        Configures the grid layout for the content section.
        """
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=4)  
        self.grid_columnconfigure(1, weight=5)  

    def create_left_frame(self):
        """
        Creates and places the left frame in the content section.
        """
        self.left_frame = LeftFrame(self, self.data_handler, self.main_app)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    def create_right_frame(self):
        """
        Creates and places the right frame in the content section.
        """
        self.right_frame = RightFrame(self, self.data_handler, self.main_app)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        """
        Creates and places the right frame in the content section.
        """
        self.right_frame = RightFrame(self, self.data_handler, self.main_app)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        """
        Creates and places the right frame in the content section.
        """
        self.right_frame = RightFrame(self, self.data_handler, self.main_app)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)