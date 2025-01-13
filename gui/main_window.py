import tkinter as tk
from tkinter import ttk
from gui.widgets.header import HeaderSection
from gui.widgets.content.content import ContentSection

class FlyWizGui(tk.Tk):
    """
    A class to represent the main window of the Fly Wiz application.

    Attributes
    ----------
    None

    Methods
    -------
    __init__():
        Initializes the main window, sets the title, state, and default font, and adds the header and content sections.
    """
    def __init__(self):
        """
        Constructs all the necessary attributes for the FlyWizGui object.
        """
        super().__init__()
        self.title("Fly Wiz")
        self.state('zoomed')

        default_font = ("Helvetica", 24)
        self.option_add("*Font", default_font)

        container = ttk.Frame(self)
        container.pack(fill="both", expand=True)

        HeaderSection(container).pack(fill="x", padx=10, pady=5)
        ContentSection(container).pack(fill="both", expand=True, padx=10, pady=5)