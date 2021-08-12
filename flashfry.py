import argparse
import sys
from PIL import Image
from PIL import ImageFilter


def fry(target):
    
    x, y = target.size
    target = target.resize((x//5,y),Image.ANTIALIAS)
    target = target.filter(ImageFilter.SHARPEN)
    target = target.resize((x,y),Image.ANTIALIAS)

    return target 


def main():
    if (len(sys.argv) == 3):
        img = sys.argv[1]
        itr = int(sys.argv[2])

        if img != None and itr != None:
            target = Image.open(img)
            for x in range(itr):
                print("---> Frying...")
                target = fry(target)
            target.save("fried_" + img,quality=95)
    else:
        print("---> Something went wrong with the way you entered that...")


main()