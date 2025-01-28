import tkinter as tk
from .base_section import BaseSection

class TitleSection(BaseSection):
    def __init__(self, parent, data_handler):
        super().__init__(parent, 'Title')
        self.data_handler = data_handler
        self.title_text = self.get_title_text()
        self.monitor_title_text()

    def get_title_text(self):
        return self.text_area.get("1.0", tk.END).strip()

    def title_text_changed(self):
        return self.title_text != self.get_title_text()

    def set_title_text(self, title_text):
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, title_text)
        self.title_text = title_text

    def update_data_handler(self):
        self.data_handler.update_data('title', self.get_title_text())

    def update_text(self):
        if self.title_text_changed():
            print(f"Title text changed: {self.get_title_text()}")
            self.set_title_text(self.get_title_text())
            self.update_data_handler()

    def monitor_title_text(self):
        self.update_text()
        self.after(250, self.monitor_title_text)  