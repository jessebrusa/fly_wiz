import tkinter as tk
from .widgets.header import HeaderSection
from .widgets.content import ContentSection
import logging

class FlyWizGui(tk.Tk):
    def __init__(self, data_handler, flyer_manipulator):
        super().__init__()
        self.title("Flyer Wizard")
        self.geometry("1200x800")
        self.data_handler = data_handler
        self.flyer_manipulator = flyer_manipulator
        self.header_section = HeaderSection(self)
        self.header_section.pack(side="top", fill="x")
        self.content_section = ContentSection(self, self.data_handler, self)
        self.content_section.pack(side="top", fill="both", expand=True)
