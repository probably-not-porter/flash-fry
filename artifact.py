import math
from PIL import Image
from PIL import ImageFilter


foo = Image.open("boar.jpg")


for x in range(4):
    x, y = foo.size
    foo = foo.resize((x//5,y),Image.ANTIALIAS)
    foo = foo.filter(ImageFilter.SHARPEN)
    foo = foo.resize((x,y),Image.ANTIALIAS)

foo.save("test_out.png",quality=95)