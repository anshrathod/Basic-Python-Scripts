from simpleimage import SimpleImage # simpleimage library have to be installed (if not working properly just get the source code from github)
#already calculated value
INTENSITY_THRESHOLD = 1.6

#This code fills the 'red color' in 'filename1' file to the 'parts' in 'filename2' file

#Note:'filename1' file should contain the image with red colored parts 

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
    orginal_stop.show()#shows file1

    back_img = SimpleImage("filename2")
    back_img.show()#shows file2
    new_image = redscreen("filename1", "filename2")
    new_image.show()#shows the output of file1 and file2



if __name__ == '__main__':
    main()

