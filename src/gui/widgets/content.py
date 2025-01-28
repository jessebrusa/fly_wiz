from tkinter import ttk
from .content_widgets.left_frame import LeftFrame
from .content_widgets.right_frame import RightFrame

class ContentSection(ttk.Frame):
    """
    A class to represent the content section of the GUI.
    """
    def __init__(self, parent, data_handler, main_app):
        super().__init__(parent, borderwidth=2, relief="solid")
        self.data_handler = data_handler
        self.main_app = main_app
        self.configure_grid()
        self.create_left_frame()
        self.create_right_frame()

    def configure_grid(self):
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=4)
        self.grid_columnconfigure(1, weight=5)

    def create_left_frame(self):
        self.left_frame = LeftFrame(self, self.data_handler, self.main_app)
        self.left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    def create_right_frame(self):
        self.right_frame = RightFrame(self, self.data_handler, self.main_app)
        self.right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)