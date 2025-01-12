from tkinter import ttk
from gui.widgets.content.left_frame import create_left_frame
from gui.widgets.content.right_frame import create_right_frame

def create_content_section(parent):
    frame = ttk.Frame(parent, borderwidth=2, relief="solid")

    # Create left and right frames
    left_frame = create_left_frame(frame)
    right_frame = create_right_frame(frame)

    # Pack the left and right frames to fill half of the content section each
    left_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)
    right_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)

    return frame