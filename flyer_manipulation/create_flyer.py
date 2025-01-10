from PIL import Image
from flyer_manipulation.img_json import image_to_base64
import json


def create_blank_flyer():
    width = 3508
    height = 2480
    image = Image.new('RGB', (width, height), color='white')
    
    with open("temp.json", "r") as file:
        data = json.load(file)
    
    data['flyer'] = image_to_base64(image)
    
    with open("temp.json", "w") as file:
        json.dump(data, file, indent=4)
