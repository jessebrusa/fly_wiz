import tkinter as tk
from tkinter import ttk
from .text_tool_bar import TextToolBar

LABEL_FONT = ("Helvetica", 16)
TEXT_AREA_FONT = ("Helvetica", 15)

class BaseSection(ttk.Frame):
    def __init__(self, parent, label_text, data_handler=None, show_align_buttons=True, show_font_dropdown=True, show_font_size_dropdown=True):
        """
        Initializes the base section with the parent widget and label text.

        Parameters
        ----------
        parent : widget
            The parent widget.
        label_text : str
            The label text for the section.
        data_handler : object, optional
            The data handler object.
        show_align_buttons : bool, optional
            Whether to show the alignment buttons in the text tool bar.
        show_font_dropdown : bool, optional
            Whether to show the font dropdown in the text tool bar.
        show_font_size_dropdown : bool, optional
            Whether to show the font size dropdown in the text tool bar.
        """
        super().__init__(parent, borderwidth=1, relief="solid", width=200)
        self.label_text = label_text
        self.data_handler = data_handler
        self.show_align_buttons = show_align_buttons
        self.show_font_dropdown = show_font_dropdown
        self.show_font_size_dropdown = show_font_size_dropdown
        self.pack(fill="both", expand=True, padx=5, pady=5)
        self.grid_propagate(False)
        self.grid_rowconfigure(0, weight=1)
        self.create_section()

    def create_section(self):
        """
        Creates and places the content in the section.
        """
        self.text_area = self.create_label_and_text_area(self, self.label_text)
        self.text_tool_bar = TextToolBar(self, show_align_buttons=self.show_align_buttons, show_font_dropdown=self.show_font_dropdown, show_font_size_dropdown=self.show_font_size_dropdown)
        self.text_tool_bar.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky="ew")

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