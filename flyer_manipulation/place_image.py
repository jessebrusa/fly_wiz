from PIL import Image

def place_image(flyer_image, current_data, max_width=2200, max_height=1500):
    image_path = current_data["file_path"]
    
    # Open the image to be placed
    image_to_place = Image.open(image_path)
    
    # Calculate the scaling factor to maintain aspect ratio
    image_width, image_height = image_to_place.size
    scaling_factor = min(max_width / image_width, max_height / image_height)
    
    # Calculate the new size
    new_size = (int(image_width * scaling_factor), int(image_height * scaling_factor))
    
    # Resize the image
    image_to_place = image_to_place.resize(new_size, Image.LANCZOS)
    
    # Calculate the position to place the image at the center of the flyer_image
    flyer_width, flyer_height = flyer_image.size
    position = ((flyer_width - new_size[0]) // 2, (flyer_height - new_size[1]) // 2)
    
    # Paste the image onto the flyer_image
    flyer_image.paste(image_to_place, position, image_to_place.convert("RGBA"))

    # Save the modified flyer_image
    output_path = "flyer.jpg"
    flyer_image.save(output_path, format="JPEG")
    
    return flyer_image