from tkinter import ttk
import tkinter as tk
from PIL import Image, ImageTk
from gui.widgets.title_line import create_title_line, remove_title_line

class CreateImage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Label at the top middle
        title_label = ttk.Label(self, text="Fly Wiz", font=("Helvetica", 60))
        title_label.grid(row=0, column=0, columnspan=3, pady=10, sticky="n")

        # Label and input for "Title Line 1"
        create_title_line(self, 1, 1)

        # Toggle for new line
        self.new_line_var = tk.BooleanVar()
        new_line_toggle = tk.Checkbutton(self, text="New Line", variable=self.new_line_var, font=("Helvetica", 20), command=self.toggle_new_line)
        new_line_toggle.grid(row=2, column=0, columnspan=2, pady=2, sticky="w")

        # Load and display the image on the right side
        image_path = "./dog.jpg"  # Update with the correct path to your image
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        image_label = tk.Label(self, image=self.photo)
        image_label.grid(row=1, column=2, rowspan=5, padx=20, pady=2, sticky="ns")

        # Configure grid columns to adjust layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

    def toggle_new_line(self):
        if self.new_line_var.get():
            self.add_new_line()
        else:
            self.remove_new_line()

    def add_new_line(self):
        if hasattr(self, 'title_line2_label'):
            return  # If the new line already exists, do nothing

        create_title_line(self, 2, 3)

        # Toggle for adding a third line
        self.new_line_var2 = tk.BooleanVar()
        self.new_line_toggle2 = tk.Checkbutton(self, text="Add New Line", variable=self.new_line_var2, font=("Helvetica", 20), command=self.toggle_third_line)
        self.new_line_toggle2.grid(row=4, column=0, columnspan=2, pady=2, sticky="w")

    def remove_new_line(self):
        remove_title_line(self, 2)

        if hasattr(self, 'new_line_toggle2'):
            self.new_line_toggle2.destroy()
            del self.new_line_toggle2

        # Also remove the third line if it exists
        self.remove_third_line()

    def toggle_third_line(self):
        if self.new_line_var2.get():
            self.add_third_line()
        else:
            self.remove_third_line()

    def add_third_line(self):
        if hasattr(self, 'title_line3_label'):
            return  # If the third line already exists, do nothing

        create_title_line(self, 3, 5)

    def remove_third_line(self):
        remove_title_line(self, 3)