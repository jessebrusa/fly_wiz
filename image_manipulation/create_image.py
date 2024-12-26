from PIL import Image

def create_blank_image():
    # Create a blank image with the aspect ratio of 11 by 8.5 at high resolution
    width = 3508
    height = 2480
    image = Image.new('RGB', (width, height), color='white')
    image.save('flyer.jpg')
