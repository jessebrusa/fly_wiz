from tkinter import ttk

HEADER_FONT_SIZE = 40

class HeaderSection(ttk.Frame):
    """
    A class to represent the header section of the GUI.

    Attributes
    ----------
    parent : widget
        The parent widget.

    Methods
    -------
    __init__(parent):
        Initializes the header section with the parent widget.
    create_header():
        Creates and places the header label in the header section.
    """
    def __init__(self, parent):
        """
        Initializes the header section with the parent widget.

        Parameters
        ----------
        parent : widget
            The parent widget.
        """
        super().__init__(parent, borderwidth=2, relief="solid")
        try:
            self.create_header()
        except Exception as e:
            print(f"An error occurred while initializing the header section: {e}")

    def create_header(self):
        """
        Creates and places the header label in the header section.
        """
        title_name = 'Fly Wiz'
        label = ttk.Label(self, text=title_name, font=("Helvetica", HEADER_FONT_SIZE))
        label.pack(pady=10)