from PIL import Image, ImageTk
import tkinter as tk
from io import BytesIO
import requests
from bs4 import BeautifulSoup

class SearchHandler:
    def __init__(self, data_handler, flyer_manipulator, update_ui_callback):
        self.data_handler = data_handler
        self.flyer_manipulator = flyer_manipulator
        self.update_ui_callback = update_ui_callback
        self.original_images = {}  # Dictionary to store original images

    def google_img_search(self, query):
        """
        Perform a Google image search and return a list of image objects.
        """
        search_url = f"https://www.google.com/search?tbm=isch&q={query}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }
        response = requests.get(search_url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        img_tags = soup.find_all("img")

        img_objects = []
        for img_tag in img_tags:
            img_url = img_tag.get("src")
            if img_url and img_url.startswith("http"):
                try:
                    # Attempt to find the original source of the image
                    img_response = requests.get(img_url)
                    img = Image.open(BytesIO(img_response.content))
                    img_objects.append(img)
                    if len(img_objects) == 10:  # Change the limit to 10
                        break
                except Exception as e:
                    print(f"Failed to download image from {img_url}: {e}")

        return img_objects

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

        def submit_query():
            query = query_entry.get()
            if query:
                img_objects = self.google_img_search(query)
                self.display_search_results(img_objects, image_key)
            search_window.destroy()

        submit_button = tk.Button(search_window, text="Submit", font=("Helvetica", 14), command=submit_query)
        submit_button.pack(pady=10)

        # Calculate the required window size based on the content
        search_window.update_idletasks()
        window_width = search_window.winfo_reqwidth() + 20
        window_height = search_window.winfo_reqheight() + 20
        search_window.geometry(f"{window_width}x{window_height}")