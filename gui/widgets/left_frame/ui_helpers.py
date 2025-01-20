import tkinter as tk
from tkinter import ttk

LABEL_FONT = ("Helvetica", 16)
TEXT_AREA_FONT = ("Helvetica", 15)

def create_label_and_text_area(parent, label_text):
    """
    Create a label and text area within the parent frame.
    """
    label = ttk.Label(parent, text=f"{label_text}:", font=LABEL_FONT, width=7, anchor="center")
    label.grid(row=0, column=0, padx=5, pady=5, sticky="ns")
    
    text_area = tk.Text(parent, height=3, width=45, font=TEXT_AREA_FONT, wrap=tk.WORD)
    text_area.grid(row=0, column=1, padx=5, pady=5, sticky="ns")
    
    parent.grid_columnconfigure(1, weight=1)

    return text_area

def create_label_and_buttons(parent, image_handler, open_color_wheel_window, open_search_window):
    """
    Create a label and buttons within the parent frame.
    """
    # Clear the parent frame to avoid duplicate widgets
    for widget in parent.winfo_children():
        widget.destroy()

    # Check if images are selected
    image1_selected = image_handler.data_handler.get_data().get('image1') is not None
    image2_selected = image_handler.data_handler.get_data().get('image2') is not None

    # Label for first image
    label_text_1 = "Image 1" + (" ✓:" if image1_selected else " :")
    label = ttk.Label(parent, text=label_text_1, font=LABEL_FONT, width=10, anchor="center")
    label.grid(row=0, column=0, padx=5, pady=5, sticky="ns")

    # Frame for the first set of buttons
    button_frame_1 = ttk.Frame(parent)
    button_frame_1.grid(row=0, column=1, columnspan=3, padx=5, pady=2, sticky="nsew")

    browse_button_1 = ttk.Button(button_frame_1, text="Browse", style="Small.TButton", width=8, 
                                 command=lambda: image_handler.browse_image('image1'))
    browse_button_1.pack(side="left", padx=5)

    search_button_1 = ttk.Button(button_frame_1, text="Search", style="Small.TButton", width=8, 
                                 command=lambda: open_search_window('image1'))
    search_button_1.pack(side="left", padx=5)
    
    remove_button_1 = ttk.Button(button_frame_1, text="Remove", style="Small.TButton", width=8, 
                                 command=lambda: image_handler.remove_image('image1'))
    remove_button_1.pack(side="left", padx=5)

    # Label for second image
    label_text_2 = "Image 2" + (" ✓:" if image2_selected else " :")
    second_image_label = ttk.Label(parent, text=label_text_2, font=LABEL_FONT, width=10, anchor="center")
    second_image_label.grid(row=1, column=0, padx=5, pady=5, sticky="ns")

    # Frame for the second set of buttons
    button_frame_2 = ttk.Frame(parent)
    button_frame_2.grid(row=1, column=1, columnspan=3, padx=5, pady=2, sticky="nsew")

    browse_button_2 = ttk.Button(button_frame_2, text="Browse", style="Small.TButton", width=8, 
                                 command=lambda: image_handler.browse_image('image2'))
    browse_button_2.pack(side="left", padx=5)

    search_button_2 = ttk.Button(button_frame_2, text="Search", style="Small.TButton", width=8, 
                                 command=lambda: open_search_window('image2'))
    search_button_2.pack(side="left", padx=5)
    
    remove_button_2 = ttk.Button(button_frame_2, text="Remove", style="Small.TButton", width=8, 
                                 command=lambda: image_handler.remove_image('image2'))
    remove_button_2.pack(side="left", padx=5)

    # Label for background color
    label_text_3 = "Background:"
    background_label = ttk.Label(parent, text=label_text_3, font=LABEL_FONT, width=10, anchor="center")
    background_label.grid(row=2, column=0, padx=5, pady=5, sticky="ns")

    # Frame for the background color buttons
    button_frame_3 = ttk.Frame(parent)
    button_frame_3.grid(row=2, column=1, columnspan=3, padx=5, pady=2, sticky="nsew")

    color_wheel_button = ttk.Button(button_frame_3, text="Color Wheel", style="Small.TButton", width=12, command=open_color_wheel_window)
    color_wheel_button.pack(side="left", padx=5)

    gradient_button = ttk.Button(button_frame_3, text="Gradient", style="Small.TButton", width=12, command=lambda: open_color_wheel_window(gradient=True))
    gradient_button.pack(side="left", padx=5)

    parent.grid_columnconfigure(1, weight=1)
    parent.grid_columnconfigure(2, weight=1)
    parent.grid_columnconfigure(3, weight=1)
    parent.grid_rowconfigure(0, weight=1)
    parent.grid_rowconfigure(1, weight=1)
    parent.grid_rowconfigure(2, weight=1)