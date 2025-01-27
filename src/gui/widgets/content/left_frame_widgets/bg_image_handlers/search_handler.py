from PIL import Image, ImageTk
import tkinter as tk
from .image_search.image_search import ImageSearch

class SearchHandler:
    def __init__(self, data_handler, flyer_manipulator, update_ui_callback):
        self.data_handler = data_handler
        self.flyer_manipulator = flyer_manipulator
        self.update_ui_callback = update_ui_callback
        self.original_images = {}  # Dictionary to store original images
        self.image_search = ImageSearch()  # Initialize the ImageSearch class

    def display_search_results(self, img_objects, image_key):
        """
        Display the search results in a new window.
        """
        # Calculate the required window size
        num_images = len(img_objects)
        num_columns = 5
        num_rows = (num_images + num_columns - 1) // num_columns
        thumbnail_size = 150
        window_width = num_columns * (thumbnail_size + 10) + 20
        window_height = num_rows * (thumbnail_size + 50) + 20

        results_window = tk.Toplevel()
        results_window.title("Search Results")
        results_window.geometry(f"{window_width}x{window_height}")

        for i, img in enumerate(img_objects):
            self.original_images[i] = img  # Store the original image
            thumbnail_img = img.copy()
            thumbnail_img.thumbnail((thumbnail_size, thumbnail_size), Image.LANCZOS)  # Use LANCZOS for high-quality resizing
            img_tk = ImageTk.PhotoImage(thumbnail_img)
            
            # Create a frame for each image and label
            frame = tk.Frame(results_window)
            frame.grid(row=i // num_columns, column=i % num_columns, padx=5, pady=5)
            
            # Add a label with a larger font size above each image
            label = tk.Label(frame, text=f"Image {i+1}", font=("Helvetica", 12))
            label.pack()
            
            img_label = tk.Label(frame, image=img_tk)
            img_label.image = img_tk
            img_label.pack()
            img_label.bind("<Button-1>", lambda event, img_index=i: self.select_image(img_index, image_key, results_window))

    def select_image(self, img_index, image_key, results_window):
        """
        Select an image from the search results and update the DataHandler.
        """
        img = self.original_images[img_index]  # Get the original image

        # Directly update the data handler with the selected image
        self.data_handler.update_data(image_key, img)
        self.data_handler.save('test_save.json')
        self.flyer_manipulator.update_flyer()
        self.update_ui_callback()  # Call the callback to update the UI
        results_window.destroy()

    def open_search_window(self, image_key):
        """
        Open a search window to search for images.
        """
        search_window = tk.Toplevel()
        search_window.title("Search")

        label = tk.Label(search_window, text="Enter search query:", font=("Helvetica", 14))
        label.pack(pady=10)

        query_entry = tk.Entry(search_window, font=("Helvetica", 14), width=30)
        query_entry.pack(pady=10)
        query_entry.focus_set()  # Set focus to the input field

        def submit_query():
            query = query_entry.get()
            if query:
                img_objects = self.image_search.google_img_search(query)
                self.display_search_results(img_objects, image_key)
            search_window.destroy()

        submit_button = tk.Button(search_window, text="Submit", font=("Helvetica", 14), command=submit_query)
        submit_button.pack(pady=10)

        # Bind the Enter key to the submit button
        search_window.bind('<Return>', lambda event: submit_query())

        # Calculate the required window size based on the content
        search_window.update_idletasks()
        window_width = search_window.winfo_reqwidth() + 20
        window_height = search_window.winfo_reqheight() + 20
        search_window.geometry(f"{window_width}x{window_height}")