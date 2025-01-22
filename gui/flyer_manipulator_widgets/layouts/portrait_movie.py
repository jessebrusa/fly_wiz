from .base_layout import BaseLayout

class PortraitMovie(BaseLayout):
    def place_images(self):
        """
        Place images on the flyer.
        """
        combined_image = super().place_images()

        if combined_image:
            # Ensure combined_image is in 'RGBA' mode
            if combined_image.mode != 'RGBA':
                combined_image = combined_image.convert('RGBA')

            # Place the combined image in the center of the flyer
            x_offset = (1100 - combined_image.width) // 2
            y_offset = (850 - combined_image.height) // 2
            alpha_mask = combined_image.split()[3]  # Extract the alpha channel
            self.flyer_image.paste(combined_image, (x_offset, y_offset), alpha_mask)