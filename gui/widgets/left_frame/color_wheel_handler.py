import tkinter as tk
from tkinter import ttk, colorchooser

class ColorWheelHandler:
    def __init__(self, parent, data_handler, main_app):
        self.parent = parent
        self.data_handler = data_handler
        self.main_app = main_app

    def open_color_wheel_window(self, gradient=False):
        """
        Open a window with one or two squares for color selection.
        The first square is white, and the second is transparent by default, both with outlines.
        """
        self.color_wheel_window = tk.Toplevel(self.parent)
        self.color_wheel_window.title("Color Wheel")
        self.color_wheel_window.attributes('-topmost', True)  # Keep the window on top
    
        # Set fixed width and center the window
        window_width = 400
        window_height = 200
        screen_width = self.color_wheel_window.winfo_screenwidth()
        screen_height = self.color_wheel_window.winfo_screenheight()
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)
        self.color_wheel_window.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    
        # Frame for the color squares
        color_frame = ttk.Frame(self.color_wheel_window)
        color_frame.pack(padx=10, pady=10)
    
        # Center the color frame horizontally
        color_frame.grid_columnconfigure(0, weight=1)
        color_frame.grid_columnconfigure(1, weight=1)
        color_frame.grid_columnconfigure(2, weight=1)
        color_frame.grid_columnconfigure(3, weight=1)
    
        # Get the current colors and gradient state from the data handler
        bg_color = self.data_handler.get_data().get('bg_color', {})
        color1 = bg_color.get('color1', '#FFFFFF')
        color2 = bg_color.get('color2', '#FFFFFF')
        direction = bg_color.get('direction', "Top Left to Bottom Right")
        gradient_state = bg_color.get('gradient_state', 0)
    
        # Ensure colors are in the correct format
        if isinstance(color1, tuple):
            color1 = f"#{color1[0]:02x}{color1[1]:02x}{color1[2]:02x}"
        if isinstance(color2, tuple):
            color2 = f"#{color2[0]:02x}{color2[1]:02x}{color2[2]:02x}"
    
        # Create the first color square
        self.color_square_1 = tk.Label(color_frame, bg=color1, width=5, height=2, relief="solid", borderwidth=1)
        self.color_square_1.grid(row=1, column=1, padx=5, pady=5)
        self.color_square_1.bind("<Button-1>", lambda event: self.change_color(self.color_square_1))
    
        # Variable to track the gradient option
        self.gradient_var = tk.IntVar(value=gradient_state)
    
        # Checkbutton for gradient option
        gradient_checkbutton = ttk.Checkbutton(color_frame, text="Gradient", variable=self.gradient_var, command=self.toggle_gradient)
        gradient_checkbutton.grid(row=2, column=1, padx=5, pady=5)
    
        # Dropdown menu for gradient directions (initially hidden)
        self.gradient_direction = tk.StringVar(value="Top Left to Bottom Right")
        self.gradient_direction_menu = ttk.Combobox(color_frame, textvariable=self.gradient_direction, state="readonly", style="TCombobox",
                    font=("Helvetica", 10), width=25)
        self.gradient_direction_menu['values'] = [
            "Top Left to Bottom Right",
            "Top Right to Bottom Left",
            "Bottom Left to Top Right",
            "Bottom Right to Top Left",
            "Top to Bottom",
            "Bottom to Top",
            "Left to Right",
            "Right to Left"
        ]
        self.gradient_direction_menu.option_add('*TCombobox*Listbox.font', ("Helvetica", 10))
        self.gradient_direction_menu.grid(row=2, column=2, padx=5, pady=5)
        self.gradient_direction_menu.grid_remove()
    
        # Create the second color square for gradient (initially hidden)
        self.color_square_2 = tk.Label(color_frame, bg=color2, width=5, height=2, relief="solid", borderwidth=1)
        self.color_square_2.grid(row=1, column=2, padx=5, pady=5)
        self.color_square_2.bind("<Button-1>", lambda event: self.change_color(self.color_square_2))
        self.color_square_2.grid_remove()
    
        # Show or hide the second color square and gradient direction menu based on the gradient option
        if self.gradient_var.get() == 1:
            self.color_square_2.grid()
            self.gradient_direction_menu.grid()
    
        # Submit button
        submit_button = ttk.Button(self.color_wheel_window, text="Submit", command=self.apply_gradient)
        submit_button.pack(pady=10)

    def toggle_gradient(self):
        """
        Toggle the visibility of the second color square and gradient direction menu based on the gradient option.
        """
        if self.gradient_var.get() == 1:
            self.color_square_2.grid()
            self.gradient_direction_menu.grid()
        else:
            self.color_square_2.grid_remove()
            self.gradient_direction_menu.grid_remove()

    def change_color(self, color_square):
        """
        Open a color picker dialog to select a color and change the background color of the square.
        """
        self.color_wheel_window.attributes('-topmost', False)  # Allow the color picker to be on top
        color = colorchooser.askcolor()[1]
        self.color_wheel_window.attributes('-topmost', True)  # Bring the color wheel window back to the top
        if color:
            color_square.config(bg=color)

    def apply_gradient(self):
        """
        Apply the selected gradient to the background.
        """
        # Get the selected colors
        color1 = self.color_square_1.cget("bg")
        color2 = self.color_square_2.cget("bg") if self.gradient_var.get() == 1 else None
        direction = self.gradient_direction.get() if self.gradient_var.get() == 1 else None
    
        # Update the data handler with the selected colors, direction, and gradient state
        self.data_handler.update_data('bg_color', {
            'color1': color1,
            'color2': color2,
            'direction': direction,
            'gradient_state': self.gradient_var.get()
        })
    
        # Print the applied gradient for debugging
        print(f"Applying gradient: color1={color1}, color2={color2}, direction={direction}, gradient_state={self.gradient_var.get()}")
    
        # Retrieve the flyer manipulator instance and update the background color
        flyer_manipulator = self.main_app.flyer_manipulator
        if flyer_manipulator:
            flyer_manipulator.change_made = True  # Set the change flag
            flyer_manipulator.apply_background_color()  # Correct method call
    
        # Close the color wheel window
        self.color_wheel_window.destroy()
        self.data_handler.save('test_save.json')
    
        # Update the flyer
        self.main_app.update_flyer()