from PIL import Image

class ImagePlacer:
    def __init__(self, data_handler):
        self.data_handler = data_handler

    def place_images_on_flyer(self, flyer_image):
        """
        Places images from data_handler on the flyer image.
        """
        if flyer_image is None:
            print("No flyer image provided to place images on.")
            return None

        try:
            image1 = self.data_handler.get_data().get('image1')
            image2 = self.data_handler.get_data().get('image2')

            max_width_scale_factor = .85
            max_height_scale_factor = .5
            max_width, max_height = int(1100 * max_width_scale_factor), int(850 * max_height_scale_factor)  

            def scale_image(image, max_width, max_height):
                """
                Scale the image to fit within the maximum allowed dimensions.
                """
                width_ratio = max_width / image.width
                height_ratio = max_height / image.height
                scale_factor = min(width_ratio, height_ratio)
                new_width = int(image.width * scale_factor)
                new_height = int(image.height * scale_factor)
                return image.resize((new_width, new_height), Image.LANCZOS)

            if image1 and image2:
                # Ensure images have an alpha channel
                if image1.mode != 'RGBA':
                    image1 = image1.convert('RGBA')
                if image2.mode != 'RGBA':
                    image2 = image2.convert('RGBA')

                # Scale images to fit within the maximum allowed dimensions
                image1 = scale_image(image1, max_width, max_height)
                image2 = scale_image(image2, max_width, max_height)

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
                combined_image = scale_image(combined_image, max_width, max_height)

                # Store the combined image in the data handler
                self.data_handler.update_data('combined_image', combined_image)

                # Place the combined image in the center of the flyer
                x_offset = (1100 - combined_image.width) // 2
                y_offset = (850 - combined_image.height) // 2
                flyer_image.paste(combined_image, (x_offset, y_offset), combined_image)

            elif image1:
                # Resize image1 to fit within the maximum allowed dimensions
                image1 = scale_image(image1, max_width, max_height)

                # Ensure image1 has an alpha channel
                if image1.mode != 'RGBA':
                    image1 = image1.convert('RGBA')

                # Place image1 in the center of the flyer
                x_offset = (1100 - image1.width) // 2
                y_offset = (850 - image1.height) // 2
                flyer_image.paste(image1, (x_offset, y_offset), image1)

            elif image2:
                # Resize image2 to fit within the maximum allowed dimensions
                image2 = scale_image(image2, max_width, max_height)

                # Ensure image2 has an alpha channel
                if image2.mode != 'RGBA':
                    image2 = image2.convert('RGBA')

                # Place image2 in the center of the flyer
                x_offset = (1100 - image2.width) // 2
                y_offset = (850 - image2.height) // 2
                flyer_image.paste(image2, (x_offset, y_offset), image2)

            return flyer_image
        except Exception as e:
            print(f"An error occurred while placing images on the flyer: {e}")
            return flyer_image