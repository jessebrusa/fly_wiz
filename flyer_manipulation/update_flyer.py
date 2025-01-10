from flyer_manipulation.background_text_color import background_text_color
from flyer_manipulation.place_image import place_image

def update_flyer(flyer_image, current_data):
    flyer_image, text_colors = background_text_color(flyer_image, current_data)
    flyer_image = place_image(flyer_image, current_data)
