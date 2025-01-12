from tkinter import ttk

def create_right_frame(parent):
    frame = ttk.Frame(parent, borderwidth=2, relief="solid")

    # Configure grid layout
    frame.grid_rowconfigure(0, weight=3)  # First section takes 3/4 of the space
    frame.grid_rowconfigure(1, weight=1)  # Second section takes 1/4 of the space
    frame.grid_columnconfigure(0, weight=1)  # Ensure the column expands to fill the width

    # Create first section (3/4 of the space)
    first_section = ttk.Frame(frame, borderwidth=1, relief="solid")
    first_section.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    first_label = ttk.Label(first_section, text="Right Section 1")
    first_label.pack(pady=10)

    # Create second section (1/4 of the space)
    second_section = ttk.Frame(frame, borderwidth=1, relief="solid")
    second_section.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

    # Configure grid layout for second section
    second_section.grid_rowconfigure(0, weight=1)  # Ensure the row expands to fill the height
    second_section.grid_columnconfigure(0, weight=3)  # Left section takes 3/4 of the space
    second_section.grid_columnconfigure(1, weight=1)  # Right section takes 1/4 of the space

    # Create left section (3/4 of the space)
    left_subsection = ttk.Frame(second_section, borderwidth=1, relief="solid")
    left_subsection.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
    left_label = ttk.Label(left_subsection, text="R2L")
    left_label.pack(pady=10)

    # Create right section (1/4 of the space)
    right_subsection = ttk.Frame(second_section, borderwidth=1, relief="solid")
    right_subsection.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
    right_label = ttk.Label(right_subsection, text="R2R", font=("Helvetica", 15))
    right_label.pack(pady=10)

    return frame