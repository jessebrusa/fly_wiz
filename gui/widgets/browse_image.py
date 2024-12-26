from tkinter import filedialog

def browse_image():
        file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if file_path:
            print(file_path)
            return file_path
        else:
            return None