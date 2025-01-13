from tkinter import ttk

class LeftFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, borderwidth=2, relief="solid")
        self.create_sections()

    def create_sections(self):
        for i in range(1, 6):
            section_frame = ttk.Frame(self, borderwidth=1, relief="solid")
            section_frame.pack(fill="both", expand=True, padx=5, pady=5)
            label = ttk.Label(section_frame, text=f"Left Section {i}")
            label.pack(pady=10)