import requests
from bs4 import BeautifulSoup
from PIL import Image
from io import BytesIO

def google_img_search(query):
    search_url = f"https://www.google.com/search?tbm=isch&q={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(search_url, headers=headers)
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
                if len(img_objects) == 5:
                    break
            except Exception as e:
                print(f"Failed to download image from {img_url}: {e}")

    return img_objects

if __name__ == "__main__":
    query = input("Enter search query: ")
    images = google_img_search(query)
    print(images)
    for i, img in enumerate(images):
        img.show()