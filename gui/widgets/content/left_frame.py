from tkinter import ttk

def create_left_frame(parent):
    frame = ttk.Frame(parent, borderwidth=2, relief="solid")

    # Create 5 sections inside the left frame
    for i in range(1, 6):
        section_frame = ttk.Frame(frame, borderwidth=1, relief="solid")
        section_frame.pack(fill="both", expand=True, padx=5, pady=5)
        label = ttk.Label(section_frame, text=f"Left Section {i}")
        label.pack(pady=10)

    return frame