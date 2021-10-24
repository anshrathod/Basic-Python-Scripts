

from simpleimage import SimpleImage

def darker(image):
    """
    Makes image passed in darker by halving red, green, blue values.
    Note: changes in image persist after function ends.
    """
    # Demonstrate looping over all the pixels of an image,
    # changing each pixel to be half its original intensity.
    for pixel in image:
        pixel.red = pixel.red // 2
        pixel.green = pixel.green // 2
        pixel.blue = pixel.blue // 2
def red_channel(filename):
    image=SimpleImage(filename)
    for pixel in image:
        pixel.green=0
        pixel.blue=0
    return image
def compute_luminousity(red,green,blue):
    return(0.299*red)+(0.587*green)+(0.114*blue)
def grayscale(filename):
    image=SimpleImage(filename)
    for pixel in image:
        luminousity=compute_luminousity(pixel.red,pixel.green,pixel.blue)
        pixel.red=luminousity
        pixel.green=luminousity
        pixel.blue=luminousity
    return image
def main():
    image = SimpleImage('flower.jpg')
    image.show()
    darker(image)
    image.show()
    red_flower=red_channel("flower.jpg")
    red_flower.show()
    gray_scale=grayscale("flower.jpg")
    gray_scale.show()


main()
