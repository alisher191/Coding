import pytesseract
from PIL import Image

img = Image.open("img.png")

file_name = img.filename
file_name = file_name.split(".")[0]
text = pytesseract.image_to_string(img)
print(text)

with open(f"{file_name}_text.txt", "w") as text_img:
    text_img.write(text)

