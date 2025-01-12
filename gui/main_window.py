import tkinter as tk
from tkinter import ttk
from gui.widgets.header import create_header_section
from gui.widgets.content.content import create_content_section

class FlyWizGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fly Wiz")
        self.state('zoomed')

        # Set the default font for the entire application
        default_font = ("Helvetica", 25)
        self.option_add("*Font", default_font)

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        # Create and place sections with outlines
        create_header_section(container).pack(fill="x", padx=10, pady=5)
        create_content_section(container).pack(fill="both", expand=True, padx=10, pady=5)

        # Additional setup if needed