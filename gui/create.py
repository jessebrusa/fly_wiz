from tkinter import ttk
import tkinter as tk
from tkinter import filedialog
from gui.widgets.image import center_image_vertically


class CreateImage(ttk.Frame):
    def __init__(self, parent, controller, flyer_image):
        super().__init__(parent)
        self.controller = controller
        self.flyer_image = flyer_image
        self.selected_file_path = None  # Add this line to store the file path

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

        # Create a frame for the header within the left frame
        self.header_frame = ttk.Frame(left_frame, borderwidth=2, relief="solid")
        self.header_frame.grid(row=0, column=0, sticky="nsew")

        # Add a label for the header
        header_label = ttk.Label(self.header_frame, text="Header:", font=("Helvetica", 20), width=15)
        header_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # Create a frame to the right of the label
        header_text_area_frame = ttk.Frame(self.header_frame)
        header_text_area_frame.grid(row=0, column=1, padx=(0, 20), pady=(10, 20), sticky="nsew")

        # Add the text area inside the new frame and center it
        self.header_text_area = tk.Text(header_text_area_frame, font=("Helvetica", 20), height=3, width=30)  # Increased height
        self.header_text_area.pack(expand=True, fill="both", padx=10, pady=10)

        # Create a frame for the "Choose Image" section within the left frame
        choose_image_frame = ttk.Frame(left_frame, borderwidth=2, relief="solid")
        choose_image_frame.grid(row=1, column=0, sticky="nsew")

        # Add "Choose Image" label and buttons to the choose image frame
        self.choose_image_label = ttk.Label(choose_image_frame, text="Choose Image:", font=("Helvetica", 20), width=15)
        self.choose_image_label.grid(row=0, column=0, pady=10, sticky="w")

        self.browse_button = ttk.Button(choose_image_frame, text="Browse", command=self.browse_image)  # Update command
        self.browse_button.grid(row=0, column=1, padx=5, pady=10, sticky="w")

        self.search_button = ttk.Button(choose_image_frame, text="Search")
        self.search_button.grid(row=0, column=2, padx=5, pady=10, sticky="w")

        # Create a frame for the text info section within the left frame
        text_info_frame = ttk.Frame(left_frame, borderwidth=2, relief="solid")
        text_info_frame.grid(row=2, column=0, sticky="nsew")

        # Add a label for the text info section
        text_info_label = ttk.Label(text_info_frame, text="Text Info:", font=("Helvetica", 20), width=15)
        text_info_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # Create a frame to the right of the label
        text_info_text_area_frame = ttk.Frame(text_info_frame)
        text_info_text_area_frame.grid(row=0, column=1, padx=(0, 20), pady=(10, 20), sticky="nsew")

        # Add the text area inside the new frame and center it
        self.text_info_text_area = tk.Text(text_info_text_area_frame, font=("Helvetica", 20), height=3, width=30)  # Increased height
        self.text_info_text_area.pack(expand=True, fill="both", padx=10, pady=10)

        # Create a frame for the styled info section within the left frame
        styled_info_frame = ttk.Frame(left_frame, borderwidth=2, relief="solid")
        styled_info_frame.grid(row=3, column=0, sticky="nsew")

        # Add a label for the styled info section
        styled_info_label = ttk.Label(styled_info_frame, text="Styled Info:", font=("Helvetica", 20), width=15)
        styled_info_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # Create a frame to the right of the label
        styled_info_text_area_frame = ttk.Frame(styled_info_frame)
        styled_info_text_area_frame.grid(row=0, column=1, padx=(0, 20), pady=(10, 20), sticky="nsew")

        # Add the text area inside the new frame and center it
        self.styled_info_text_area = tk.Text(styled_info_text_area_frame, font=("Helvetica", 20), height=3, width=30)  # Increased height
        self.styled_info_text_area.pack(expand=True, fill="both", padx=10, pady=10)

        # Create a frame for the footer section within the left frame
        footer_frame = ttk.Frame(left_frame, borderwidth=2, relief="solid")
        footer_frame.grid(row=4, column=0, sticky="nsew")

        # Add a label for the footer section
        footer_label = ttk.Label(footer_frame, text="Footer:", font=("Helvetica", 20), width=15)
        footer_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        # Create a frame to the right of the label
        footer_text_area_frame = ttk.Frame(footer_frame)
        footer_text_area_frame.grid(row=0, column=1, padx=(0, 20), pady=(10, 20), sticky="nsew")

        # Add the text area inside the new frame and center it
        self.footer_text_area = tk.Text(footer_text_area_frame, font=("Helvetica", 20), height=3, width=30)  # Increased height
        self.footer_text_area.pack(expand=True, fill="both", padx=10, pady=10)

        # Load and display the image on the right side using center_image_vertically function
        image_path = "./flyer.jpg"
        center_image_vertically(right_frame, image_path, title_row=0, bottom_row=6, column=0, max_width=960, max_height=540)
        
        # Configure grid columns to adjust layout in frames
        left_frame.grid_columnconfigure(0, weight=1)
        left_frame.grid_rowconfigure(0, weight=1)
        left_frame.grid_rowconfigure(1, weight=1)
        left_frame.grid_rowconfigure(2, weight=1)
        left_frame.grid_rowconfigure(3, weight=1)
        left_frame.grid_rowconfigure(4, weight=1)
        right_frame.grid_columnconfigure(0, weight=1)

        self.frames = {"left_frame": left_frame, "right_frame": right_frame}

    def browse_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            self.selected_file_path = file_path  # Store the selected file path
            print(f"Selected file: {file_path}")

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
        # Retrieve the text from the footer text area
        footer_text = self.footer_text_area.get("1.0", tk.END).strip()
        return footer_text

    def get_selected_file_path(self):
        # Retrieve the selected file path
        return self.selected_file_path

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = CreateImage(root, None)
    app.pack(fill="both", expand=True)
    root.mainloop()