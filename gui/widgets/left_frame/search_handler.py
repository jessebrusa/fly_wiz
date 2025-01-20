import tkinter as tk
from tkinter import ttk

class SearchHandler:
    def __init__(self, parent, data_handler):
        self.parent = parent
        self.data_handler = data_handler

    def open_search_window(self, image_key):
        """
        Open a small window with a label, input bar, and search button.
        """
        search_window = tk.Toplevel(self.parent)
        search_window.title("Search")

        label = ttk.Label(search_window, text="Search:", font=("Helvetica", 16))
        label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

        entry = ttk.Entry(search_window, font=("Helvetica", 15))
        entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

        search_button = ttk.Button(search_window, text="Search", style="Small.TButton", command=lambda: self.perform_search(entry.get(), image_key))
        search_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        search_window.grid_columnconfigure(1, weight=1)

        # Bind the Enter key to the search button
        search_window.bind('<Return>', lambda event: self.perform_search(entry.get(), image_key))

    def perform_search(self, query, image_key):
        """
        Perform the search operation.
        """
        print(f"Searching for: {query} for {image_key}")
        # Implement the search functionality here