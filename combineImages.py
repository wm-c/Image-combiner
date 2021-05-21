from PIL import Image
import os


files = list(filter(lambda x: (".jpg" in x or ".jpeg" in x or ".png" in x), os.listdir()))


size = Image.open(files[0]).size

empty_img = Image.new("I", (size[0], size[1] * len(files)))
empty_img.paste(Image.open(files[0]))


count = 0
for img in files:
    im = Image.open(img).resize(size)
    
    empty_img.paste(im, (0, size[1] * count))
    count += 1



empty_img.convert('RGB').save("Combined.png")


