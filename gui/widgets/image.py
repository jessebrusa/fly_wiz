from tkinter import Label
from PIL import Image, ImageTk
import json
from flyer_manipulation.img_json import base64_to_image

def create_image_label(parent, row, column, max_width=None, max_height=None, rowspan=1, padx=0, pady=0, sticky=""):
    with open('temp.json', 'r') as file:   
        json_data = json.load(file)
    if not json_data:
        return
    flyer = base64_to_image(json_data["flyer"])

    
    # Resize the image if max_width and max_height are provided
    if max_width and max_height:
        original_width, original_height = flyer.size
        aspect_ratio = original_width / original_height

        if original_width > max_width or original_height > max_height:
            if (max_width / aspect_ratio) <= max_height:
                new_width = max_width
                new_height = int(max_width / aspect_ratio)
            else:
                new_height = max_height
                new_width = int(max_height * aspect_ratio)
            flyer = flyer.resize((new_width, new_height), Image.LANCZOS)
    
    photo = ImageTk.PhotoImage(flyer)
    image_label = Label(parent, image=photo)
    image_label.image = photo  # Keep a reference to avoid garbage collection
    image_label.grid(row=row, column=column, rowspan=rowspan, padx=padx, pady=pady, sticky=sticky)
    return image_label

def center_image_vertically(parent, title_row, bottom_row, column, max_width=None, max_height=None):
    # Configure the rows to expand
    parent.grid_rowconfigure(title_row, weight=1)
    parent.grid_rowconfigure(bottom_row, weight=1)
    parent.grid_rowconfigure(title_row + 1, weight=0)  # Image row

    # Create and place the image label
    create_image_label(parent, row=title_row + 1, column=column, max_width=max_width, max_height=max_height, rowspan=1, padx=20, pady=2, sticky="nsew")