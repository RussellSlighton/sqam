from PIL import Image


def loadImage(path):
    img = Image.open(path).convert('L')
    img.show()

if __name__ == "__main__":
    loadImage('imageLib/movatRaw0.tif')

