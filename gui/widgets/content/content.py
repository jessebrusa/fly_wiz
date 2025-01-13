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

    Methods
    -------
    configure_grid():
        Configures the grid layout for the content section.
    create_left_frame():
        Creates and places the left frame in the content section.
    create_right_frame():
        Creates and places the right frame in the content section.
    """
    def __init__(self, parent):
        """
        Constructs all the necessary attributes for the ContentSection object.

        Parameters
        ----------
        parent : widget
            The parent widget.
        """
        super().__init__(parent, borderwidth=2, relief="solid")
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
        left_frame = LeftFrame(self)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    def create_right_frame(self):
        """
        Creates and places the right frame in the content section.
        """
        right_frame = RightFrame(self)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)