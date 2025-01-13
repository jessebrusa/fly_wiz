from tkinter import ttk

HEADER_FONT_SIZE = 40

class HeaderSection(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, borderwidth=2, relief="solid")
        self.create_header()

    def create_header(self):
        title_name = 'Fly Wiz'
        label = ttk.Label(self, text=title_name, font=("Helvetica", HEADER_FONT_SIZE))
        label.pack(pady=10)