import tkinter as tk

def get_footer_text(widget):
    # Retrieve the text from the footer text area
    footer_text = widget.footer_text_area.get("1.0", tk.END).strip()
    return footer_text

def get_selected_file_path(instance):
    # Retrieve the selected file path
    return instance.selected_file_path