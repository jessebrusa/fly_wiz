# gui/widgets/content/left_frame_widgets/bg_image_handlers/search_handler.py

from PIL import Image, ImageTk
import tkinter as tk
from io import BytesIO
import requests
from bs4 import BeautifulSoup
from tkinter import simpledialog
import cv2
import numpy as np

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
                    if len(img_objects) == 5:
                        break
                except Exception as e:
                    print(f"Failed to download image from {img_url}: {e}")

        return img_objects

    def display_search_results(self, img_objects, image_key):
        """
        Display the search results in a new window.
        """
        results_window = tk.Toplevel()
        results_window.title("Search Results")
        results_window.geometry("800x200")

        for i, img in enumerate(img_objects):
            self.original_images[i] = img  # Store the original image
            thumbnail_img = img.copy()
            thumbnail_img.thumbnail((150, 150), Image.LANCZOS)  # Use LANCZOS for high-quality resizing
            img_tk = ImageTk.PhotoImage(thumbnail_img)
            img_label = tk.Label(results_window, image=img_tk)
            img_label.image = img_tk
            img_label.grid(row=i // 5, column=i % 5, padx=5, pady=5)
            img_label.bind("<Button-1>", lambda event, img_index=i: self.select_image(img_index, image_key, results_window))

    def select_image(self, img_index, image_key, results_window):
        """
        Select an image from the search results and update the DataHandler.
        """
        img = self.original_images[img_index]  # Get the original image

        # Convert PIL image to OpenCV format
        img_cv = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)

        # Upscale the image using INTER_CUBIC interpolation
        upscale_factor = 2  # Define the upscale factor
        width = int(img_cv.shape[1] * upscale_factor)
        height = int(img_cv.shape[0] * upscale_factor)
        dim = (width, height)
        img_upscaled = cv2.resize(img_cv, dim, interpolation=cv2.INTER_CUBIC)

        # Convert back to PIL format
        img_upscaled_pil = Image.fromarray(cv2.cvtColor(img_upscaled, cv2.COLOR_BGR2RGB))

        self.data_handler.update_data(image_key, img_upscaled_pil)
        self.data_handler.save('test_save.json')
        self.flyer_manipulator.update_flyer()
        self.update_ui_callback()  # Call the callback to update the UI
        results_window.destroy()

    def open_search_window(self, image_key):
        """
        Open a search window to search for images.
        """
        query = simpledialog.askstring("Search", "Enter search query:")
        if query:
            img_objects = self.google_img_search(query)
            self.display_search_results(img_objects, image_key)