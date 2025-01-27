from tkinter import ttk

class BaseSection(ttk.Frame):
    def __init__(self, parent, ui_helpers, label_text):
        """
        Initializes the base section with the parent widget, UI helpers, and label text.

        Parameters
        ----------
        parent : widget
            The parent widget.
        ui_helpers : UIHelpers
            The UI helpers instance.
        label_text : str
            The label text for the section.
        """
        super().__init__(parent, borderwidth=1, relief="solid", width=200)
        self.ui_helpers = ui_helpers
        self.label_text = label_text
        self.pack(fill="both", expand=True, padx=5, pady=5)
        self.grid_propagate(False)
        self.grid_rowconfigure(0, weight=1)
        self.create_section()

    def create_section(self):
        """
        Creates and places the content in the section.
        """
        self.text_area = self.ui_helpers.create_label_and_text_area(self, self.label_text)