from PIL import Image
from PIL import ImageFilter


class transform:
    def __init__(self, img):
        self.img = img

    def resize(self):
        img1 = Image.open(self.img)
        img2 = img1.resize((200, 200))
        img2.show()

    def flip(self):
        img1 = Image.open(self.img)
        img2 = img1.transpose(Image.FLIP_LEFT_RIGHT)
        img2.show()

    def spin(self):
        img1 = Image.open(self.img)
        img2 = img1.transpose(Image.ROTATE_270)
        img2.show()


def open():
    img = Image.open("thor.jpg")
    print(img.size)
    print(img.format)
    img.show()


# cropping an image
def crop():
 area = (100,100,300,375)
 img = Image.open("thor.jpg")
 cropped_img = img.crop(area)
 cropped_img.show()


# combining images together
def combine():
 image1 = Image.open("thor.jpg")
 image2= Image.open("venom.jpg")
 area = (100,100,702,439)
 image1.paste(image2 , area)
 image1.show()

# channeling images
def channel():
 image1 = Image.open("thor.jpg")
 r, g, b=image1.split()
 r.show()
 g.show()
 b.show()
 new_img = Image.merge('RGB' , (b, g, r))
# recombining these channels(bands) provdes various filters to the image
 new_img.show()


# overlaying various images
def channel_diff_img():
    image1 = Image.open("thor.jpg")
    image2 = Image.open("venom.jpg")
    r1, g1, b1 = image1.split()
    r2, g2, b2 = image2.split()
    new_img = Image.merge('RGB', (r2, g1, b2))
    new_img.show()



def image_mode_convertor():
    img1 = Image.open("thor.jpg")
    b_w = img1.convert("L")
    b_w.show()


def blur():
    img1 = Image.open("thor.jpg")
    img2 = img1.filter(ImageFilter.BLUR)
    img2.show()

# opposite of blur
def detail():
    img1 = Image.open("thor.jpg")
    img2 = img1.filter(ImageFilter.DETAIL)
    img2.show()


# find edges in the image and highlights the
def edges():
    img1 = Image.open("thor.jpg")
    img2 = img1.filter(ImageFilter.FIND_EDGES)
    img2.show()









