from simpleimage import SimpleImage # simpleimage library have to be installed (if not working properly just get the source code from github)
INTENSITY_THRESHOLD = 1.6

#converting the filename1 image to red screen image

def redscreen(filename1, filename2):
    Image = SimpleImage(filename1)
    back = SimpleImage(filename2)
    for pixel in Image:
        average = (pixel.red+pixel.green+pixel.blue)//3
        if pixel.red>= average*INTENSITY_THRESHOLD:
            x = pixel.x
            y = pixel.y
            Image.set_pixel(x, y, back.get_pixel(x, y))
    return Image

#driver code
def main():
    orginal_stop = SimpleImage("filename1")
    #orginal_stop.show()

    back_img = SimpleImage("filename2")
    #back_img.show()
    new_image = redscreen("filename1", "filename2")
    new_image.show()


main()
