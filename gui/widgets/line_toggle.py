import tkinter as tk
from gui.widgets.title_line import create_title_line, remove_title_line

def toggle_new_line(self):
    if self.new_line_var.get():
        self.add_new_line()
    else:
        self.remove_new_line()

def add_new_line(self):
    if hasattr(self, 'title_line2_label'):
        return  # If the new line already exists, do nothing

    create_title_line(self.title_lines_frame, 2, 3)
    self.update_title_lines_section()

    # Toggle for adding a third line
    self.new_line_var2 = tk.BooleanVar()
    self.new_line_toggle2 = tk.Checkbutton(self.title_lines_frame, text="Add New Line", variable=self.new_line_var2, font=("Helvetica", 20), command=self.toggle_third_line)
    self.new_line_toggle2.grid(row=4, column=0, columnspan=2, pady=2, sticky="w")

def remove_new_line(self):
    remove_title_line(self.title_lines_frame, 2)
    self.update_title_lines_section()

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

    create_title_line(self.title_lines_frame, 3, 5)
    self.update_title_lines_section()

def remove_third_line(self):
    remove_title_line(self.title_lines_frame, 3)
    self.update_title_lines_section()

def update_title_lines_section(self):
    # Update the row positions of the title lines within the title_lines_frame
    row = 3
    if hasattr(self, 'title_line2_label'):
        row += 1
    if hasattr(self, 'title_line3_label'):
        row += 1

    # Move "New Line" toggle
    self.new_line_toggle.grid(row=2, column=0, columnspan=2, pady=2, sticky="w")
    if hasattr(self, 'new_line_toggle2'):
        self.new_line_toggle2.grid(row=row + 1, column=0, columnspan=2, pady=2, sticky="w")