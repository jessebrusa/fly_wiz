from gui.flyer_manipulator_widgets.base_image_creator import BaseImageCreator
from gui.flyer_manipulator_widgets.background_applier import BackgroundApplier
from gui.flyer_manipulator_widgets.layouts.standard import Standard
# Import other layouts as needed

class FlyerManipulator:
    """
    A class to create and manipulate a base blank image.

    Attributes
    ----------
    image : Image
        The Pillow image to be manipulated.
    data_handler : DataHandler
        The data handler instance to update data.
    main_app : FlyWizGui
        The main application instance.
    current_layout : str
        The current layout being used.

    Methods
    -------
    create_base_image():
        Creates a base blank image with dimensions 11 inches by 8.5 inches.
    update_data_handler():
        Updates the data handler with the current image.
    apply_background_color():
        Apply the background color from the data handler to the flyer image.
    place_images_on_flyer():
        Places images from data_handler on the flyer image.
    update_flyer():
        Updates the flyer by placing images on it.
    set_layout(layout_name):
        Sets the current layout and updates the flyer.
    """
    def __init__(self, data_handler, main_app):
        """
        Initializes the FlyerManipulator and creates the base blank image.

        Parameters
        ----------
        data_handler : DataHandler
            The data handler instance to update data.
        main_app : FlyWizGui
            The main application instance.
        """
        self.image = None
        self.data_handler = data_handler
        self.main_app = main_app  
        self.base_image_creator = BaseImageCreator()
        self.background_applier = BackgroundApplier(data_handler)
        self.current_layout = 'standard'  # Default layout
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
        self.image = self.background_applier.apply_background_color(self.image)
        self.update_data_handler()

    def apply_layout(self):
        """
        Applies the current layout to the flyer image.
        """
        if self.current_layout == 'standard':
            layout = Standard(self.image, self.data_handler)
        # Add other layouts as needed
        self.image = layout.apply_layout()
        self.update_data_handler()

    def update_flyer(self):
        """
        Updates the flyer by placing images on it.
        """
        self.apply_background_color()
        self.apply_layout()

    def set_layout(self, layout_name):
        """
        Sets the current layout and updates the flyer.

        Parameters
        ----------
        layout_name : str
            The name of the layout to be applied.
        """
        self.current_layout = layout_name
        self.update_flyer()