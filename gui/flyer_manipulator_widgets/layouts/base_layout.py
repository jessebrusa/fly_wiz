from PIL import Image, ImageDraw, ImageFont

class BaseLayout:
    def __init__(self, flyer_image, data_handler):
        self.flyer_image = flyer_image
        self.data_handler = data_handler
        self.draw = ImageDraw.Draw(flyer_image)
        self.font = ImageFont.load_default()  # You can load a specific font if needed

    def place_title(self):
        title = self.data_handler.get_data().get('title', '')
        self.draw.text((50, 50), title, font=self.font, fill="black")

    def place_footer(self):
        footer = self.data_handler.get_data().get('footer', '')
        self.draw.text((50, self.flyer_image.height - 50), footer, font=self.font, fill="black")

    def place_images(self):
        image1 = self.data_handler.get_data().get('image1')
        image2 = self.data_handler.get_data().get('image2')
        if image1:
            self.flyer_image.paste(image1, (50, 100), image1)
        if image2:
            self.flyer_image.paste(image2, (300, 100), image2)

    def place_styled_info(self):
        styled_info = self.data_handler.get_data().get('styled_info', '')
        self.draw.text((50, 200), styled_info, font=self.font, fill="black")

    def place_text_info(self):
        text_info = self.data_handler.get_data().get('text_info', '')
        self.draw.text((50, 300), text_info, font=self.font, fill="black")

    def apply_layout(self):
        self.place_title()
        self.place_footer()
        self.place_images()
        self.place_styled_info()
        self.place_text_info()
        return self.flyer_image