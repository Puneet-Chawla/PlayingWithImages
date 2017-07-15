from struct import *
from PIL import Image
from PIL import ImageFilter


packed_data = pack('iif' , 1, 2, 2.32)
print(packed_data)

print(unpack('iif', packed_data))

def double (a):
    return a*2

income = [10, 20, 30]
new = list(map(double, income))
print(new)

def blur ():
    image = Image.open("thor.jpg")
    b = image.filter(ImageFilter.BLUR)
    b.show()










