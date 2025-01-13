import tkinter as tk
from tkinter import ttk
from gui.widgets.header import HeaderSection
from gui.widgets.content.content import ContentSection

class FlyWizGui(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Fly Wiz")
        self.state('zoomed')

        default_font = ("Helvetica", 24)
        self.option_add("*Font", default_font)

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        HeaderSection(container).pack(fill="x", padx=10, pady=5)
        ContentSection(container).pack(fill="both", expand=True, padx=10, pady=5)