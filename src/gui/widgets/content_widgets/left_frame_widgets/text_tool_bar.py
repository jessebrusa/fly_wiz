import tkinter as tk
from tkinter import ttk

class TextToolBar(tk.Frame):
    def __init__(self, parent, data_handler, flyer_manipulator, show_align_buttons=True, show_font_dropdown=True, 
                 show_font_size_dropdown=True, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.data_handler = data_handler  # Store the data_handler instance
        self.flyer_manipulator = flyer_manipulator  # Store the flyer_manipulator instance
        self.show_align_buttons = show_align_buttons
        self.show_font_dropdown = show_font_dropdown
        self.show_font_size_dropdown = show_font_size_dropdown
        self.create_widgets()

    def create_widgets(self):
        col = 0

        if self.show_align_buttons:
            # Create a frame for the alignment buttons
            align_frame = tk.Frame(self)
            align_frame.grid(row=0, column=col, padx=5, pady=5, sticky="ew")
            col += 1

            # Left align button
            self.left_align_button = tk.Button(align_frame, text="<--", command=self.left_align)
            self.left_align_button.pack(side=tk.LEFT, padx=2, pady=0)

            # Center align button
            self.center_align_button = tk.Button(align_frame, text="<->", command=self.center_align)
            self.center_align_button.pack(side=tk.LEFT, padx=2, pady=0)

            # Right align button
            self.right_align_button = tk.Button(align_frame, text="-->", command=self.right_align)
            self.right_align_button.pack(side=tk.LEFT, padx=2, pady=0)

        if self.show_font_dropdown:
            # Create a dropdown for fonts
            self.font_var = tk.StringVar()
            self.font_dropdown = ttk.Combobox(self, textvariable=self.font_var)
            self.font_dropdown['values'] = ("Bernard Condensed", "Arial", "Courier", "Helvetica", "Times New Roman", "Verdana")
            self.font_dropdown.grid(row=0, column=col, padx=5, pady=0, sticky="ew")
            self.font_dropdown.current(0)  # Set default value
            self.font_dropdown.bind("<<ComboboxSelected>>", self.on_font_selected)
            col += 1

        if self.show_font_size_dropdown:
            # Create a dropdown for font sizes
            self.font_size_var = tk.StringVar()
            self.font_size_dropdown = ttk.Combobox(self, textvariable=self.font_size_var)
            self.font_size_dropdown['values'] = tuple(str(size) for size in range(40, 201, 2))
            self.font_size_dropdown.grid(row=0, column=col, padx=5, pady=0, sticky="ew")
            self.font_size_dropdown.current(self.font_size_dropdown['values'].index('70'))  # Set default value (70)
            self.font_size_dropdown.bind("<<ComboboxSelected>>", self.on_font_size_selected)
            col += 1

        # Configure grid to ensure elements are spaced evenly
        for i in range(col):
            self.grid_columnconfigure(i, weight=1)

    def on_font_selected(self, event):
        selected_font = self.font_var.get()
        print(f"Selected font: {selected_font}")
        
        # Update the DataHandler with the selected font
        title_data = self.data_handler.get_data().get('title', {})
        title_data['font'] = selected_font
        self.data_handler.update_data('title', title_data)
        
        # Call the update_flyer method of the flyer_manipulator
        self.flyer_manipulator.update_flyer()

    def on_font_size_selected(self, event):
        selected_font_size = self.font_size_var.get()
        print(f"Selected font size: {selected_font_size}")
        
        # Update the DataHandler with the selected font size
        title_data = self.data_handler.get_data().get('title', {})
        title_data['font_size'] = int(selected_font_size)
        self.data_handler.update_data('title', title_data)
        
        # Call the update_flyer method of the flyer_manipulator
        self.flyer_manipulator.update_flyer()

    def left_align(self):
        print("Left align")

    def center_align(self):
        print("Center align")

    def right_align(self):
        print("Right align")