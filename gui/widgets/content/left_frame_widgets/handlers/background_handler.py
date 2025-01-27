from tkinter import colorchooser

class BackgroundHandler:
    def __init__(self, data_handler, main_app):
        self.data_handler = data_handler
        self.main_app = main_app

    def change_color(self, color_square):
        """
        Open a color picker dialog to select a color and change the background color of the square.
        """
        color = colorchooser.askcolor()[1]
        if color:
            color_square.config(bg=color)

    def apply_gradient(self, color_square_1, color_square_2, gradient_var, gradient_direction):
        """
        Apply the selected gradient to the background.
        """
        color1 = color_square_1.cget("bg")
        color2 = color_square_2.cget("bg") if gradient_var.get() == 1 else None
        direction = gradient_direction.get() if gradient_var.get() == 1 else None

        self.data_handler.update_data('bg_color', {
            'color1': color1,
            'color2': color2,
            'direction': direction,
            'gradient_state': gradient_var.get()
        })

        flyer_manipulator = self.main_app.flyer_manipulator
        if flyer_manipulator:
            flyer_manipulator.change_made = True
            flyer_manipulator.apply_background_color()

        self.main_app.update_flyer()