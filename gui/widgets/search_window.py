import tkinter as tk
from tkinter import ttk
from .google_images import google_img_search
from .img_json import image_to_base64
from PIL import ImageTk
import json

def open_search_window():
    # Create a new Tkinter window
    search_window = tk.Toplevel()
    search_window.title("Search Image")
    search_window.geometry("600x150")

    # Center the window on the screen
    window_width = 600
    window_height = 150
    screen_width = search_window.winfo_screenwidth()
    screen_height = search_window.winfo_screenheight()
    position_top = int(screen_height / 2 - window_height / 2)
    position_right = int(screen_width / 2 - window_width / 2)
    search_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

    # Create a frame for the search section
    search_frame = ttk.Frame(search_window, padding="10")
    search_frame.pack(expand=True, fill="both")

    # Define a larger font
    large_font = ("Helvetica", 16)

    # Add a label for the search input
    search_label = ttk.Label(search_frame, text="Search for image:", font=large_font)
    search_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

    # Add an input box for the search query
    search_entry = ttk.Entry(search_frame, width=30, font=large_font)
    search_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

    # Bind the Enter key to the search button
    search_entry.bind("<Return>", lambda event: search_image(search_frame, search_label, search_entry, search_button))

    # Add a search button below the label and input box
    search_button = ttk.Button(search_frame, text="Search", command=lambda: search_image(search_frame, search_label, search_entry, search_button), style="TButton")
    search_button.grid(row=1, column=0, columnspan=2, pady=10)

    # Apply the larger font to the button
    style = ttk.Style()
    style.configure("TButton", font=large_font)

    # Add a placeholder for the error label
    search_frame.error_label = None

def search_image(search_frame, search_label, search_entry, search_button):
    # Get the input from the search entry
    query = search_entry.get()

    # Check if there is an input
    if query:
        # Remove the label, input, and search button
        search_label.grid_remove()
        search_entry.grid_remove()
        search_button.grid_remove()

        # Remove the error label if it exists
        if search_frame.error_label:
            search_frame.error_label.grid_remove()
            search_frame.error_label = None

        # Add a new label saying "Searching... {input}"
        searching_label = ttk.Label(search_frame, text=f"Searching... {query}", font=("Helvetica", 16))
        searching_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")

        # Perform the search logic
        google_img_list = google_img_search(query)

        # Remove the "Searching..." label
        searching_label.grid_remove()

        if google_img_list:
            # Remove everything inside the search_frame
            for widget in search_frame.winfo_children():
                widget.destroy()

            # Create a canvas and a horizontal scrollbar
            canvas = tk.Canvas(search_frame)
            scrollbar = ttk.Scrollbar(search_frame, orient="horizontal", command=canvas.xview)
            scrollable_frame = ttk.Frame(canvas)

            scrollable_frame.bind(
                "<Configure>",
                lambda e: canvas.configure(
                    scrollregion=canvas.bbox("all")
                )
            )

            canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
            canvas.configure(xscrollcommand=scrollbar.set)

            canvas.pack(side="top", fill="both", expand=True)
            scrollbar.pack(side="bottom", fill="x")

            # Add buttons with images to the scrollable frame
            for i, img in enumerate(google_img_list):
                img.thumbnail((100, 100))  # Resize the image to fit the button
                img_tk = ImageTk.PhotoImage(img)
                button = ttk.Button(scrollable_frame, image=img_tk, command=lambda img=img: save_image_to_json(img))
                button.image = img_tk  # Keep a reference to avoid garbage collection
                button.grid(row=0, column=i, padx=5, pady=5)

            # Ensure the scrollbar is always visible by setting a large scrollregion
            canvas.configure(scrollregion=(0, 0, len(google_img_list) * 110, 100))
        else:
            # Display a message if no images are found
            no_images_label = ttk.Label(search_frame, text="No images found.", font=("Helvetica", 16))
            no_images_label.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="w")
    else:
        # Add a new label below the search button saying "*Please provide a search term"
        if not search_frame.error_label:
            search_frame.error_label = ttk.Label(search_frame, text="*Please provide a search term", font=("Helvetica", 16), foreground="red")
            search_frame.error_label.grid(row=2, column=0, columnspan=2, padx=5, pady=5, sticky="w")

def save_image_to_json(img):
    # Convert the image to base64
    img_base64 = image_to_base64(img)

    # Load existing data from text_data.json
    try:
        with open("text_data.json", "r") as json_file:
            data = json.load(json_file)
    except FileNotFoundError:
        data = {}

    # Append the new image data
    if "images" not in data:
        data["images"] = []
    data["images"].append(img_base64)

    # Save the updated data back to text_data.json
    with open("text_data.json", "w") as json_file:
        json.dump(data, json_file)

    print("Image saved to text_data.json")