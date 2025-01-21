from tkinter import ttk
from tkinter import filedialog
from ..img.image_label import ImageLabel
from PIL import Image, ImageTk
import tkinter as tk
from io import BytesIO
import requests
from bs4 import BeautifulSoup
from tkinter import simpledialog

class SearchHandler:
    def __init__(self, data_handler, flyer_manipulator):
        self.data_handler = data_handler
        self.flyer_manipulator = flyer_manipulator

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
        results_window.geometry("800x600")

        for i, img in enumerate(img_objects):
            img.thumbnail((150, 150))
            img_tk = ImageTk.PhotoImage(img)
            img_label = tk.Label(results_window, image=img_tk)
            img_label.image = img_tk
            img_label.grid(row=i // 5, column=i % 5, padx=5, pady=5)
            img_label.bind("<Button-1>", lambda event, img=img: self.select_image(img, image_key, results_window))

    def select_image(self, img, image_key, results_window):
        """
        Select an image from the search results and update the DataHandler.
        """
        self.data_handler.update_data(image_key, img)
        self.data_handler.save('test_save.json')
        self.flyer_manipulator.update_flyer()
        self.flyer_manipulator.main_app.update_gui()
        results_window.destroy()

    def open_search_window(self, image_key):
        """
        Open a search window to search for images.
        """
        query = simpledialog.askstring("Search", "Enter search query:")
        if query:
            img_objects = self.google_img_search(query)
            self.display_search_results(img_objects, image_key)