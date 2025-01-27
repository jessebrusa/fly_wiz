import tkinter as tk
from tkinter import ttk

LABEL_FONT = ("Helvetica", 16)
TEXT_AREA_FONT = ("Helvetica", 15)

class UIHelpers:
    def __init__(self):
        pass

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