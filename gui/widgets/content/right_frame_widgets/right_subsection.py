from tkinter import ttk
from tkinter import filedialog

class RightSubsection(ttk.Frame):
    def __init__(self, parent, data_handler, main_app):
        """
        Initializes the right subsection with the parent widget, data handler, and main application instance.

        Parameters
        ----------
        parent : widget
            The parent widget.
        data_handler : DataHandler
            The data handler instance.
        main_app : FlyWizGui
            The main application instance.
        """
        super().__init__(parent, borderwidth=1, relief="solid")
        self.data_handler = data_handler
        self.main_app = main_app
        self.create_subsection()

    def create_subsection(self):
        """
        Creates and places the content in the right subsection.
        """
        # Create a frame to center the buttons vertically and horizontally
        button_frame = ttk.Frame(self)
        button_frame.grid(row=0, column=0, sticky="nsew")

        # Configure the grid to ensure buttons expand to fill the space
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        button_frame.grid_rowconfigure(0, weight=1)
        button_frame.grid_rowconfigure(1, weight=1)
        button_frame.grid_columnconfigure(0, weight=1)
        button_frame.grid_columnconfigure(1, weight=1)

        button_width = 8  

        save_button = ttk.Button(button_frame, text="Save", width=button_width, command=self.save_data)
        save_button.grid(row=0, column=0, padx=5, pady=2, sticky="nsew")

        load_button = ttk.Button(button_frame, text="Load", width=button_width, command=self.load_data)
        load_button.grid(row=0, column=1, padx=5, pady=2, sticky="nsew")

        export_button = ttk.Button(button_frame, text="Export", width=button_width)
        export_button.grid(row=1, column=0, padx=5, pady=15, sticky="nsew")

        print_button = ttk.Button(button_frame, text="Print", width=button_width)
        print_button.grid(row=1, column=1, padx=5, pady=15, sticky="nsew")

    def save_data(self):
        """
        Open a file dialog to pick a location and name for the file, then save the data.
        """
        file_path = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if file_path:
            self.data_handler.save(file_path)
            print(f"Data saved to {file_path}")

    def load_data(self):
        """
        Open a file dialog to select a JSON file, then load the data.
        """
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            self.data_handler.load(file_path)
            print(f"Data loaded from {file_path}")
            self.main_app.update_gui()