import random, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import numpy as np


def getCaptchaString():
    r1 = random.randint(5, 10)
    captcha = ""
    for i in range(r1):
        r2 = random.randint(1, 10)
        if r2<6:
            r3 = str(random.randint(0, 9))
        else:
            r3 = chr(random.choice([65, 97])+random.randint(0, 25))
        captcha += r3
    return captcha, r1


def whiteNoise(size, noise=0.5):
    """Generate white noise and merge it with given Image object."""
    w, h = size
    pixel = lambda noise: round(255 * random.uniform(1-noise, 1))
    n_image = Image.new('RGB', size, (0, 0, 0, 0))
    rnd_grid = map(lambda _: tuple([pixel(noise)]) * 3,
                    [0] * w * h)
    n_image.putdata(list(rnd_grid))
    return n_image


def warp(img):
    # Both horizontal and vertical
    # https://subscription.packtpub.com/book/application_development/9781785283932/1/ch01lvl1sec16/image-warping
    cols, rows = img.size
    img = np.array(img).tolist()
    img_output = [(0,0,0)] * rows * cols
    k = 0
    for i in range(rows):
        for j in range(cols):
            offset_x = int(10 * math.sin(2 * 3.14 * i / 150))
            offset_y = int(10 * math.cos(2 * 3.14 * j / 150))
            if i+offset_y < rows and j+offset_x < cols:
                img_output[k] = tuple(img[(i+offset_y)%rows][(j+offset_x)%cols])
            else:
                img_output[k] = tuple(img[i][j])
            k += 1
    n_image = Image.new('RGB', (cols, rows), (0, 0, 0, 0))
    n_image.putdata(img_output)
    return n_image


captcha_string, captcha_len = getCaptchaString()
fnt_size = 40

captcha_image = Image.new('RGB', (captcha_len*(fnt_size//2+10), fnt_size+20), (255, 255, 255))
# add font of your choice
fnt = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", fnt_size)
d = ImageDraw.Draw(captcha_image)
d.text((20, 10), captcha_string, font=fnt, align='center', fill=(0, 0, 0))

captcha_image = warp(captcha_image)
noise = whiteNoise(captcha_image.size, random.uniform(0.4, 0.8))
captcha_image = Image.blend(captcha_image, noise, 0.65)

captcha_image.show()
captcha_image.save('captcha.png', 'PNG')

user_input = input("Enter the code shown: ")
if user_input==captcha_string:
    print("Verification successful!!")
else:
    print("You are a ROBOT!")
