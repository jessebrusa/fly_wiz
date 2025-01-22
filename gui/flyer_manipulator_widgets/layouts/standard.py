from .base_layout import BaseLayout

class Standard(BaseLayout):
    def place_images(self):
        """
        Place images on the flyer.
        """
        combined_image = super().place_images()

        print(f"Standard.place_images: combined_image={combined_image}")

        if combined_image:
            # Ensure combined_image is in 'RGBA' mode
            if combined_image.mode != 'RGBA':
                combined_image = combined_image.convert('RGBA')

            # Place the combined image in the center of the flyer
            x_offset = (1100 - combined_image.width) // 2
            y_offset = (850 - combined_image.height) // 2
            alpha_mask = combined_image.split()[3]  # Extract the alpha channel
            self.flyer_image.paste(combined_image, (x_offset, y_offset), alpha_mask)

    def apply_layout(self):
        self.place_title()
        self.place_footer()
        self.place_images()
        self.place_styled_info()
        self.place_text_info()
        return self.flyer_image