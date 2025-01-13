from tkinter import ttk

class RightFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent, borderwidth=2, relief="solid")
        self.configure_main_frame_grid()
        self.create_first_section()
        self.create_second_section()

    def configure_main_frame_grid(self):
        self.grid_rowconfigure(0, weight=3)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

    def create_first_section(self):
        first_section = ttk.Frame(self, borderwidth=1, relief="solid")
        first_section.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        first_label = ttk.Label(first_section, text="Right Section 1")
        first_label.pack(pady=10)

    def create_second_section(self):
        second_section = ttk.Frame(self, borderwidth=1, relief="solid")
        second_section.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)
        second_section.grid_rowconfigure(0, weight=1)
        second_section.grid_columnconfigure(0, weight=3)
        second_section.grid_columnconfigure(1, weight=1)
        self.create_left_subsection(second_section)
        self.create_right_subsection(second_section)

    def create_left_subsection(self, parent):
        left_subsection = ttk.Frame(parent, borderwidth=1, relief="solid")
        left_subsection.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        left_label = ttk.Label(left_subsection, text="R2L")
        left_label.pack(pady=10)

    def create_right_subsection(self, parent):
        right_subsection = ttk.Frame(parent, borderwidth=1, relief="solid")
        right_subsection.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
        right_label = ttk.Label(right_subsection, text="R2R")
        right_label.pack(pady=10)