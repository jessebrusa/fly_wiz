from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from gui.widgets.title_line import create_title_line, remove_title_line
from gui.widgets.image import center_image_vertically
from gui.widgets.line_toggle import toggle_new_line, add_new_line, remove_new_line, toggle_third_line, add_third_line, remove_third_line, update_title_lines_section

class CreateImage(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        # Create frame for the title
        title_frame = ttk.Frame(self, borderwidth=2, relief="solid")
        title_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

        # Add title label to the title frame
        title_label = ttk.Label(title_frame, text="Fly Wiz", font=("Helvetica", 60), borderwidth=2, relief="solid", anchor="center")
        title_label.grid(row=0, column=1, pady=10, sticky="ew")

        # Add empty columns on either side of the title label
        title_frame.grid_columnconfigure(0, weight=1)
        title_frame.grid_columnconfigure(1, weight=1)
        title_frame.grid_columnconfigure(2, weight=1)

        # Create frames for left and right sides
        left_frame = ttk.Frame(self, borderwidth=2, relief="solid")
        right_frame = ttk.Frame(self, borderwidth=2, relief="solid")

        left_frame.grid(row=1, column=0, sticky="nsew")
        right_frame.grid(row=1, column=1, sticky="nsew")

        # Configure grid columns to adjust layout
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Create a frame for the title lines within the left frame
        self.title_lines_frame = ttk.Frame(left_frame, borderwidth=2, relief="solid")
        self.title_lines_frame.grid(row=0, column=0, sticky="nsew")

        # Add widgets to the title lines frame
        create_title_line(self.title_lines_frame, 1, 1)

        self.new_line_var = tk.BooleanVar()

        # Bind the imported functions to the class
        self.toggle_new_line = toggle_new_line.__get__(self)
        self.add_new_line = add_new_line.__get__(self)
        self.remove_new_line = remove_new_line.__get__(self)
        self.toggle_third_line = toggle_third_line.__get__(self)
        self.add_third_line = add_third_line.__get__(self)
        self.remove_third_line = remove_third_line.__get__(self)
        self.update_title_lines_section = update_title_lines_section.__get__(self)

        self.new_line_toggle = tk.Checkbutton(self.title_lines_frame, text="New Line", variable=self.new_line_var, font=("Helvetica", 20), command=self.toggle_new_line)
        self.new_line_toggle.grid(row=2, column=0, columnspan=2, pady=2, sticky="w")

        # Create a frame for the "Choose Image" section within the left frame
        choose_image_frame = ttk.Frame(left_frame, borderwidth=2, relief="solid")
        choose_image_frame.grid(row=1, column=0, sticky="nsew")

        # Add "Choose Image" label and buttons to the choose image frame
        self.choose_image_label = ttk.Label(choose_image_frame, text="Choose Image", font=("Helvetica", 20))
        self.choose_image_label.grid(row=0, column=0, pady=10, sticky="w")

        self.browse_button = ttk.Button(choose_image_frame, text="Browse", command=self.browse_image)
        self.browse_button.grid(row=0, column=1, padx=5, pady=10, sticky="w")

        self.search_button = ttk.Button(choose_image_frame, text="Search")
        self.search_button.grid(row=0, column=2, padx=5, pady=10, sticky="w")

        # Load and display the image on the right side using center_image_vertically function
        image_path = "./flyer.jpg"
        center_image_vertically(right_frame, image_path, title_row=0, bottom_row=6, column=0, max_width=960, max_height=540)
        
        # Configure grid columns to adjust layout in frames
        left_frame.grid_columnconfigure(0, weight=1)
        left_frame.grid_rowconfigure(0, weight=1)
        left_frame.grid_rowconfigure(1, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)

        self.frames = {"left_frame": left_frame, "right_frame": right_frame}

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            # Handle the selected file path
            print(f"Selected file: {file_path}")