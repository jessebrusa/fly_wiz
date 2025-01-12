from tkinter import ttk

def create_header_section(parent):
    title_name = 'Fly Wiz'
    frame = ttk.Frame(parent, borderwidth=2, relief="solid")
    label = ttk.Label(frame, text=title_name, font=("Helvetica", 40))
    label.pack(pady=10)
    return frame