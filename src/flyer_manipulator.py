from src.flyer_manipulator_tools.base_image_creator import BaseImageCreator
from src.flyer_manipulator_tools.background_applier import BackgroundApplier
from src.flyer_manipulator_tools.layouts import standard, flyer, halfsheet, info, landscape_movie, large_picture, portrait_movie

class FlyerManipulator:
    def __init__(self, data_handler, main_app):
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
        self.image = self.base_image_creator.create_base_image()

    def update_data_handler(self):
        try:
            self.data_handler.update_data('flyer', self.image)
        except Exception as e:
            print(f"An error occurred while updating the data handler: {e}")

    def apply_background_color(self):
        self.image = self.background_applier.apply_background_color(self.image)
        self.update_data_handler()

    def set_layout(self, layout_name):
        print(f"Setting layout to: {layout_name}")
        self.current_layout = layout_name
        self.update_flyer()

    def apply_layout(self):
        if self.current_layout == 'standard':
            layout = standard.Standard(self.image, self.data_handler)
        elif self.current_layout == 'flyer':
            layout = flyer.Flyer(self.image, self.data_handler)
        elif self.current_layout == 'halfsheet':
            layout = halfsheet.HalfSheet(self.image, self.data_handler)
        elif self.current_layout == 'info':
            layout = info.Info(self.image, self.data_handler)
        elif self.current_layout == 'landscape_movie':
            layout = landscape_movie.LandscapeMovie(self.image, self.data_handler)
        elif self.current_layout == 'large_picture':
            layout = large_picture.LargePicture(self.image, self.data_handler)
        elif self.current_layout == 'portrait_movie':
            layout = portrait_movie.PortraitMovie(self.image, self.data_handler)
        else:
            raise ValueError(f"Unknown layout: {self.current_layout}")
        self.image = layout.apply_layout()
        self.update_data_handler()

    def update_flyer_image_gui(self):
        self.main_app.content_section.right_frame.flyer_image_section.update_image()

    def update_flyer(self):
        self.apply_background_color()
        self.apply_layout()
        self.update_flyer_image_gui()