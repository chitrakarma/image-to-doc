import pytesseract as tess
from PIL import Image

img = Image.open('images/hello-world.png')
text = tess.image_to_string(img)

print(text)
