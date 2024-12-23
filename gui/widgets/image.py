from tkinter import Label
from PIL import Image, ImageTk

def create_image_label(parent, image_path, row, column, rowspan=1, padx=0, pady=0, sticky=""):
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image)
    image_label = Label(parent, image=photo)
    image_label.image = photo  # Keep a reference to avoid garbage collection
    image_label.grid(row=row, column=column, rowspan=rowspan, padx=padx, pady=pady, sticky=sticky)
    return image_label