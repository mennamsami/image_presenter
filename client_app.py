import requests
from urllib.parse import urljoin
from PIL import Image

def decode_image(img_str):
    img_bytes = bytes(img_str, encoding="utf-8")
    img = Image.open(io.BytesIO(base64.b64decode(img_bytes)))
    return img

def encode_img(img_path):
    with open(img_path, "rb") as f:
        img_bytes = f.read()
    img_str = base64.b64encode(img_bytes).decode("utf-8")
    return img_str

URL = "http://localhost:5000/"
def fetch_image(id: str):
    end_point = f"/img/{id}"
    response = requests.get(urljoin(URL,end_point))
    data = response.json()
    img = data["image"]
    decode_image(img)

def post_image(path: str):
    img = encode_img(path)
    end_point = "/img"
    data = {
        "id": "samlogo",
        "image": img
    }
    response = requests.post(urljoin(URL,end_point),json=data)
    if response.text == "OK":
        print("Added Successfully!")

if __name__ == "__main__":
    ...
    
