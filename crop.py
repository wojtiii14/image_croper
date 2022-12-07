from PIL import Image
import os

dir_list = os.listdir()

for file in dir_list:
    if file.endswith('.jpeg'):
        img = Image.open(file)
        img.thumbnail((5000, 512))

        x1 = (img.width - 512) / 2
        y1 = (img.height - 512) / 2
        x2 = (img.width + 512) / 2
        y2 = (img.height + 512) / 2

        cropped = img.crop((x1,y1,x2,y2))

        cropped.save(file)
