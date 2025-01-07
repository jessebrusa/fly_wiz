from PIL import Image

def place_image(flyer_image, current_data):
    image_path = current_data["file_path"]
    
    # Open the image to be placed
    image_to_place = Image.open(image_path)
    
    # Calculate the position to place the image at the center of the flyer_image
    flyer_width, flyer_height = flyer_image.size
    image_width, image_height = image_to_place.size
    position = ((flyer_width - image_width) // 2, (flyer_height - image_height) // 2)
    
    # Paste the image onto the flyer_image
    flyer_image.paste(image_to_place, position, image_to_place.convert("RGBA"))

    # Save the modified flyer_image
    output_path = "flyer.jpg"
    flyer_image.save(output_path, format="JPEG")
    
    return flyer_image