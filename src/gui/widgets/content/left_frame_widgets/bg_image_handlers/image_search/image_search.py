from PIL import Image
from io import BytesIO
import requests
from bs4 import BeautifulSoup

IMAGE_QUANTITY = 10

class ImageSearch:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
        }

    def google_img_search(self, query):
        """
        Perform a Google image search and return a list of image objects.
        """
        search_url = f"https://www.google.com/search?tbm=isch&q={query}"
        response = requests.get(search_url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")
        img_tags = soup.find_all("img")

        img_objects = []
        for img_tag in img_tags:
            img_url = img_tag.get("src")
            if img_url and img_url.startswith("http"):
                try:
                    img_response = requests.get(img_url)
                    img = Image.open(BytesIO(img_response.content))
                    img_objects.append(img)
                    if len(img_objects) == IMAGE_QUANTITY:  
                        break
                except Exception as e:
                    print(f"Failed to download image from {img_url}: {e}")

        return img_objects