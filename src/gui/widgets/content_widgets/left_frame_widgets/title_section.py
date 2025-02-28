import tkinter as tk
from .base_section import BaseSection

class TitleSection(BaseSection):
    def __init__(self, parent, data_handler, main_app):
        super().__init__(parent, 'Title', data_handler=data_handler, flyer_manipulator=main_app.flyer_manipulator, show_align_buttons=False)
        self.data_handler = data_handler
        self.main_app = main_app  
        self.title_text = self.get_title_text()
        self.monitor_title_text()

    def get_title_text(self):
        """
        Get the title text from the text widget.
        """
        return self.text_area.get("1.0", tk.END).strip()

    def title_text_changed(self):
        return self.title_text != self.get_title_text()

    def set_title_text(self, title_text):
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, title_text)
        self.title_text = title_text

    def update_data_handler(self):
        """
        Update the title text in the data handler.
        """
        title_data = self.data_handler.get_data().get('title', {})
        title_data['text'] = self.get_title_text()
        self.data_handler.update_data('title', title_data)

    def update_flyer_manipulator(self):
        self.main_app.flyer_manipulator.update_flyer()

    def update_text(self):
        if self.title_text_changed():
            self.set_title_text(self.get_title_text())
            self.update_data_handler()
            self.update_flyer_manipulator()

    def monitor_title_text(self):
        self.update_text()
        self.after(250, self.monitor_title_text)