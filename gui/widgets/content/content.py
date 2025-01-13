from tkinter import ttk
from gui.widgets.content.left_frame import LeftFrame
from gui.widgets.content.right_frame import RightFrame

class ContentSection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, borderwidth=2, relief="solid")
        self.configure_grid()
        self.create_left_frame()
        self.create_right_frame()

    def configure_grid(self):
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=4)  
        self.grid_columnconfigure(1, weight=5)  

    def create_left_frame(self):
        left_frame = LeftFrame(self)
        left_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

    def create_right_frame(self):
        right_frame = RightFrame(self)
        right_frame.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)