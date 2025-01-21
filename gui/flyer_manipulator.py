from gui.flyer_manipulator_widgets.base_image_creator import BaseImageCreator
from gui.flyer_manipulator_widgets.background_applier import BackgroundApplier
from gui.flyer_manipulator_widgets.image_placer import ImagePlacer

class FlyerManipulator:
    """
    A class to create and manipulate a base blank image.

    Attributes
    ----------
    image : Image
        The Pillow image to be manipulated.
    data_handler : DataHandler
        The data handler instance to update data.

    Methods
    -------
    create_base_image():
        Creates a base blank image with dimensions 11 inches by 8.5 inches.
    update_data_handler():
        Updates the data handler with the current image.
    place_images_on_flyer():
        Places images from data_handler on the flyer image.
    update_flyer():
        Updates the flyer by placing images on it.
    """
    def __init__(self, data_handler):
        """
        Initializes the FlyerManipulator and creates the base blank image.

        Parameters
        ----------
        data_handler : DataHandler
            The data handler instance to update data.
        """
        self.image = None
        self.data_handler = data_handler
        self.background_color = (255, 255, 255)  # White
        self.change_made = False  # Flag to track changes
        self.base_image_creator = BaseImageCreator()
        self.background_applier = BackgroundApplier(data_handler)
        self.image_placer = ImagePlacer(data_handler)
        try:
            self.create_base_image()
            self.update_data_handler()
        except Exception as e:
            print(f"An error occurred while initializing the FlyerManipulator: {e}")

    def create_base_image(self):
        """
        Creates a base blank image with dimensions 11 inches by 8.5 inches.
        """
        self.image = self.base_image_creator.create_base_image()

    def update_data_handler(self):
        """
        Updates the data handler with the current image.
        """
        try:
            self.data_handler.update_data('flyer', self.image)
        except Exception as e:
            print(f"An error occurred while updating the data handler: {e}")

    def apply_background_color(self):
        """
        Apply the background color from the data handler to the flyer image.
        """
        bg_color = self.data_handler.get_data().get('bg_color', {})
        color1 = bg_color.get('color1', '#FFFFFF')
        color2 = bg_color.get('color2', None)
        gradient_state = bg_color.get('gradient_state', 0)

        # Ensure colors are in the correct format
        if isinstance(color1, str) and color1.startswith('#'):
            color1 = tuple(int(color1[i:i+2], 16) for i in (1, 3, 5))
        if color2 and isinstance(color2, str) and color2.startswith('#'):
            color2 = tuple(int(color2[i:i+2], 16) for i in (1, 3, 5))

        self.image = self.background_applier.apply_background_color(self.image, color1, color2, gradient_state)
        self.update_data_handler()

    def place_images_on_flyer(self):
        """
        Places images from data_handler on the flyer image.
        """
        self.image = self.image_placer.place_images_on_flyer(self.image)
        self.update_data_handler()
        self.change_made = True  # Set the change flag

    def update_flyer(self):
        """
        Updates the flyer by placing images on it.
        """
        self.apply_background_color()
        self.place_images_on_flyer()
        """
        Updates the flyer by placing images on it.
        """
        self.apply_background_color()
        self.place_images_on_flyer()
        """
        Updates the flyer by placing images on it.
        """
        self.apply_background_color()
        self.place_images_on_flyer()