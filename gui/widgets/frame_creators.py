from .search_window import open_search_window
from tkinter import ttk
import tkinter as tk


def create_title_frame(instance):
    # Create frame for the title
    title_frame = ttk.Frame(instance, borderwidth=2, relief="solid")
    title_frame.grid(row=0, column=0, columnspan=2, sticky="ew")

    # Add title label to the title frame
    title_label = ttk.Label(title_frame, text="Fly Wiz", font=("Helvetica", 60), borderwidth=2, relief="solid", anchor="center")
    title_label.grid(row=0, column=1, pady=10, sticky="ew")

    # Add empty columns on either side of the title label
    title_frame.grid_columnconfigure(0, weight=1)
    title_frame.grid_columnconfigure(1, weight=1)
    title_frame.grid_columnconfigure(2, weight=1)

def create_left_frame(instance):
    # Create frames for left and right sides
    instance.left_frame = ttk.Frame(instance, borderwidth=2, relief="solid")
    instance.left_frame.grid(row=1, column=0, sticky="nsew")

    create_header_section(instance)
    create_choose_image_section(instance)
    create_text_info_section(instance)
    create_styled_info_section(instance)
    create_footer_section(instance)

def create_right_frame(instance):
    instance.right_frame = ttk.Frame(instance, borderwidth=2, relief="solid")
    instance.right_frame.grid(row=1, column=1, sticky="nsew")

def create_header_section(instance):
    # Create a frame for the header within the left frame
    header_frame = ttk.Frame(instance.left_frame, borderwidth=2, relief="solid")
    header_frame.grid(row=0, column=0, sticky="nsew")

    # Add a label for the header
    header_label = ttk.Label(header_frame, text="Header:", font=("Helvetica", 20), width=15)
    header_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

    # Create a frame to the right of the label
    header_text_area_frame = ttk.Frame(header_frame)
    header_text_area_frame.grid(row=0, column=1, padx=(0, 20), pady=(10, 20), sticky="nsew")

    # Add the text area inside the new frame and center it
    instance.header_text_area = tk.Text(header_text_area_frame, font=("Helvetica", 20), height=3, width=30)  # Increased height
    instance.header_text_area.pack(expand=True, fill="both", padx=10, pady=10)

def create_choose_image_section(instance):
    # Create a frame for the "Choose Image" section within the left frame
    choose_image_frame = ttk.Frame(instance.left_frame, borderwidth=2, relief="solid")
    choose_image_frame.grid(row=1, column=0, sticky="nsew")

    # Add "Choose Image" label and buttons to the choose image frame
    instance.choose_image_label = ttk.Label(choose_image_frame, text="Choose Image:", font=("Helvetica", 20), width=15)
    instance.choose_image_label.grid(row=0, column=0, pady=10, sticky="w")

    instance.browse_button = ttk.Button(choose_image_frame, text="Browse", command=instance.browse_image)  # Update command
    instance.browse_button.grid(row=0, column=1, padx=5, pady=10, sticky="w")

    instance.search_button = ttk.Button(choose_image_frame, text="Search", command=open_search_window)
    instance.search_button.grid(row=0, column=2, padx=5, pady=10, sticky="w")

def create_text_info_section(instance):
    # Create a frame for the text info section within the left frame
    text_info_frame = ttk.Frame(instance.left_frame, borderwidth=2, relief="solid")
    text_info_frame.grid(row=2, column=0, sticky="nsew")

    # Add a label for the text info section
    text_info_label = ttk.Label(text_info_frame, text="Text Info:", font=("Helvetica", 20), width=15)
    text_info_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

    # Create a frame to the right of the label
    text_info_text_area_frame = ttk.Frame(text_info_frame)
    text_info_text_area_frame.grid(row=0, column=1, padx=(0, 20), pady=(10, 20), sticky="nsew")

    # Add the text area inside the new frame and center it
    instance.text_info_text_area = tk.Text(text_info_text_area_frame, font=("Helvetica", 20), height=3, width=30)  # Increased height
    instance.text_info_text_area.pack(expand=True, fill="both", padx=10, pady=10)

def create_styled_info_section(instance):
    # Create a frame for the styled info section within the left frame
    styled_info_frame = ttk.Frame(instance.left_frame, borderwidth=2, relief="solid")
    styled_info_frame.grid(row=3, column=0, sticky="nsew")

    # Add a label for the styled info section
    styled_info_label = ttk.Label(styled_info_frame, text="Styled Info:", font=("Helvetica", 20), width=15)
    styled_info_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

    # Create a frame to the right of the label
    styled_info_text_area_frame = ttk.Frame(styled_info_frame)
    styled_info_text_area_frame.grid(row=0, column=1, padx=(0, 20), pady=(10, 20), sticky="nsew")

    # Add the text area inside the new frame and center it
    instance.styled_info_text_area = tk.Text(styled_info_text_area_frame, font=("Helvetica", 20), height=3, width=30)  # Increased height
    instance.styled_info_text_area.pack(expand=True, fill="both", padx=10, pady=10)

def create_footer_section(instance):
    # Create a frame for the footer section within the left frame
    footer_frame = ttk.Frame(instance.left_frame, borderwidth=2, relief="solid")
    footer_frame.grid(row=4, column=0, sticky="nsew")

    # Add a label for the footer section
    footer_label = ttk.Label(footer_frame, text="Footer:", font=("Helvetica", 20), width=15)
    footer_label.grid(row=0, column=0, padx=20, pady=10, sticky="w")

    # Create a frame to the right of the label
    footer_text_area_frame = ttk.Frame(footer_frame)
    footer_text_area_frame.grid(row=0, column=1, padx=(0, 20), pady=(10, 20), sticky="nsew")

    # Add the text area inside the new frame and center it
    instance.footer_text_area = tk.Text(footer_text_area_frame, font=("Helvetica", 20), height=3, width=30)  # Increased height
    instance.footer_text_area.pack(expand=True, fill="both", padx=10, pady=10)