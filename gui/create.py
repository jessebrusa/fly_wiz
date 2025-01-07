from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from gui.widgets.image import center_image_vertically
from gui.widgets.helpers import get_footer_text, get_selected_file_path
from gui.widgets.frame_creators import (
    create_title_frame,
    create_left_frame,
    create_right_frame
)

class CreateImage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.selected_file_path = None  # Add this line to store the file path

        create_title_frame(self)
        create_left_frame(self)
        create_right_frame(self)

        # Load and display the image on the right side using center_image_vertically function
        image_path = "./flyer.jpg"
        center_image_vertically(self.right_frame, image_path, title_row=0, bottom_row=6, column=0, max_width=960, max_height=540)

        # Configure grid columns to adjust layout in frames
        self.left_frame.grid_columnconfigure(0, weight=1)
        self.left_frame.grid_rowconfigure(0, weight=1)
        self.left_frame.grid_rowconfigure(1, weight=1)
        self.left_frame.grid_rowconfigure(2, weight=1)
        self.left_frame.grid_rowconfigure(3, weight=1)
        self.left_frame.grid_rowconfigure(4, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        self.frames = {"left_frame": self.left_frame, "right_frame": self.right_frame}

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.selected_file_path = file_path  

    def get_header_text(self):
        # Retrieve the text from the text area
        header_text = self.header_text_area.get("1.0", tk.END).strip()
        return header_text

    def get_text_info_text(self):
        # Retrieve the text from the text info text area
        text_info_text = self.text_info_text_area.get("1.0", tk.END).strip()
        return text_info_text

    def get_styled_info_text(self):
        # Retrieve the text from the styled info text area
        styled_info_text = self.styled_info_text_area.get("1.0", tk.END).strip()
        return styled_info_text

    def get_footer_text(self):
        return get_footer_text(self)

    def get_selected_file_path(self):
        return get_selected_file_path(self)

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = CreateImage(root, None, None)
    app.pack(fill="both", expand=True)
    root.mainloop()