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
        """
        Combine and place images on the flyer.
        """
        image1 = self.data_handler.get_data().get('image1')
        image2 = self.data_handler.get_data().get('image2')

        print(f"place_images: image1={image1}, image2={image2}")

        if image1 and image2:
            combined_image = self.combine_images(image1, image2)
            self.data_handler.update_data('combined_image', combined_image)
            return combined_image

        elif image1:
            return self.scale_image(image1)

        elif image2:
            return self.scale_image(image2)

        return None

    def scale_image(self, image, max_width=935, max_height=425):
        """
        Scale the image to fit within the maximum allowed dimensions.
        """
        width_ratio = max_width / image.width
        height_ratio = max_height / image.height
        scale_factor = min(width_ratio, height_ratio)
        new_width = int(image.width * scale_factor)
        new_height = int(image.height * scale_factor)
        return image.resize((new_width, new_height), Image.LANCZOS)

    def combine_images(self, image1, image2):
        """
        Combine two images side by side and return the combined image.
        """
        max_width, max_height = 935, 425

        # Ensure images have an alpha channel
        if image1.mode != 'RGBA':
            image1 = image1.convert('RGBA')
        if image2.mode != 'RGBA':
            image2 = image2.convert('RGBA')

        # Scale images to fit within the maximum allowed dimensions
        image1 = self.scale_image(image1, max_width, max_height)
        image2 = self.scale_image(image2, max_width, max_height)

        # Determine the combined width and height
        combined_width = image1.width + image2.width
        combined_height = max(image1.height, image2.height)

        # Scale the shorter image to match the height of the taller image
        if image1.height < image2.height:
            image1 = image1.resize((int(image1.width * (image2.height / image1.height)), image2.height), Image.LANCZOS)
        elif image2.height < image1.height:
            image2 = image2.resize((int(image2.width * (image1.height / image2.height)), image1.height), Image.LANCZOS)

        # Create a new image to combine both images side by side
        combined_image = Image.new('RGBA', (combined_width, combined_height), (255, 255, 255, 0))

        # Calculate vertical offset for centering shorter image
        image1_y_offset = (combined_height - image1.height) // 2
        image2_y_offset = (combined_height - image2.height) // 2

        # Paste both images onto the combined image
        combined_image.paste(image1, (0, image1_y_offset), image1)
        combined_image.paste(image2, (image1.width, image2_y_offset), image2)

        # Scale the combined image to fit within the maximum allowed dimensions
        combined_image = self.scale_image(combined_image, max_width, max_height)

        return combined_image

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