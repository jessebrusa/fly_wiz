import tkinter as tk
from tkinter import ttk
from image_manipulation.create_image import create_blank_image

from gui.create import CreateImage


class FlyWizGui(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Fly Wiz")
        self.state('zoomed')

        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        # Initialize only the CreateImage frame
        page_name = CreateImage.__name__
        frame = CreateImage(parent=container, controller=self)
        self.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("CreateImage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()


def main():
    # Create the blank image
    create_blank_image()

    # Initialize and run the Fly Wiz app
    app = FlyWizGui()
    app.mainloop()


if __name__ == "__main__":
    main()