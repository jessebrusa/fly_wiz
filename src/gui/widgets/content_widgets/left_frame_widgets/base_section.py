import tkinter as tk
from tkinter import ttk

LABEL_FONT = ("Helvetica", 16)
TEXT_AREA_FONT = ("Helvetica", 15)

class BaseSection(ttk.Frame):
    def __init__(self, parent, label_text, data_handler=None):
        """
        Initializes the base section with the parent widget and label text.

        Parameters
        ----------
        parent : widget
            The parent widget.
        label_text : str
            The label text for the section.
        """
        super().__init__(parent, borderwidth=1, relief="solid", width=200)
        self.label_text = label_text
        self.data_handler = data_handler
        self.pack(fill="both", expand=True, padx=5, pady=5)
        self.grid_propagate(False)
        self.grid_rowconfigure(0, weight=1)
        self.create_section()

    def create_section(self):
        """
        Creates and places the content in the section.
        """
        self.text_area = self.create_label_and_text_area(self, self.label_text)

    def create_label_and_text_area(self, parent, label_text):
        """
        Create a label and text area within the parent frame.
        """
        label = ttk.Label(parent, text=f"{label_text}:", font=LABEL_FONT, width=7, anchor="center")
        label.grid(row=0, column=0, padx=5, pady=5, sticky="ns")
        
        text_area = tk.Text(parent, height=3, width=45, font=TEXT_AREA_FONT, wrap=tk.WORD)
        text_area.grid(row=0, column=1, padx=5, pady=5, sticky="ns")
        
        parent.grid_columnconfigure(1, weight=1)

        return text_area