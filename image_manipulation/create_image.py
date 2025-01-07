from PIL import Image

def create_blank_image():
    width = 3508
    height = 2480
    image = Image.new('RGB', (width, height), color='white')
    image_path = "flyer.jpg"
    image.save(image_path, format="JPEG")
    return image_path