import tkinter as tk
from tkinter import ttk
from image_manipulation.create_image import create_blank_image
from gui.create import CreateImage
import json

class FlyWizGui(tk.Tk):
    def __init__(self, flyer_image, *args, **kwargs):
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
        frame = CreateImage(parent=container, controller=self, flyer_image=flyer_image)
        self.frames[page_name] = frame
        frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("CreateImage")

        # Initialize previous data
        self.previous_data = self.collect_text_data()

        # Start the periodic check
        self.check_for_changes()

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def collect_text_data(self):
        frame = self.frames["CreateImage"]
        return {
            "header": frame.get_header_text(),
            "text_info": frame.get_text_info_text(),
            "styled_info": frame.get_styled_info_text(),
            "footer": frame.get_footer_text(),
            "file_path": frame.get_selected_file_path()  # Include the file path
        }

    def check_for_changes(self):
        current_data = self.collect_text_data()
        if current_data != self.previous_data:
            self.on_text_change(current_data)
            self.previous_data = current_data
        self.after(500, self.check_for_changes)  # Check every 500 milliseconds (0.5 second)

    def on_text_change(self, current_data):
        with open("text_data.json", "w") as file:
            json.dump(current_data, file, indent=4)
        # Perform your desired function here

def main():
    # Create the blank image
    flyer_image = create_blank_image()

    # Initialize and run the Fly Wiz app
    app = FlyWizGui(flyer_image)
    app.mainloop()

if __name__ == "__main__":
    main()