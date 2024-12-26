from tkinter import ttk

def create_title_line(parent, line_number, row):
    label_text = f"Title Line {line_number}:"
    label = ttk.Label(parent, text=label_text, font=("Helvetica", 20))
    label.grid(row=row, column=0, padx=20, pady=2, sticky="e")

    entry = ttk.Entry(parent, font=("Helvetica", 20))
    entry.grid(row=row, column=1, padx=20, pady=2, sticky="w")

    setattr(parent, f"title_line{line_number}_label", label)
    setattr(parent, f"title_line{line_number}_entry", entry)

def remove_title_line(parent, line_number):
    label = getattr(parent, f"title_line{line_number}_label", None)
    entry = getattr(parent, f"title_line{line_number}_entry", None)
    if label and entry:
        label.destroy()
        entry.destroy()
        delattr(parent, f"title_line{line_number}_label")
        delattr(parent, f"title_line{line_number}_entry")

