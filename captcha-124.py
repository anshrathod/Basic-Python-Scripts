from captcha.image import ImageCaptcha
from captcha.audio import AudioCaptcha
import random, time
from PIL import Image
from playsound import playsound


def randomiseString():
    r1 = random.randint(6, 10)
    cap = ""
    for i in range(r1):
        r2 = random.randint(0, 10)
        if r2 <= 5:
            cap += str(random.randint(0, 9))
        else:
            cap += random.choice(
                [chr(x) for x in range(ord("a"), ord("z") + 1)]
                # + [chr(x) for x in range(ord("A"), ord("Z") + 1)]
            )
    return cap


def randomiseNumbers():
    r1 = random.randint(4, 6)
    cap = ""
    for i in range(r1):
        cap += str(random.randint(0, 9))
    return cap


tries, i = 3, 0


# image captcha
image = ImageCaptcha(width=400, height=150)
data = randomiseString()
image.write(
    data, "out.png",
)

im = Image.open("out.png")
im.show()

print("Enter the captcha : ")
while True:
    valid = input()
    if valid == data:
        print("Captcha Validated")
        break
    else:
        i += 1
        if i == tries:
            print("Failed! The captcha was", data)
            break
        print("Wrong input! Try again")


# audio captcha
nums = randomiseNumbers()
audio = AudioCaptcha()
audio.write(nums, "out.wav")
playsound("out.wav")

i = 0
print("Enter the captcha : ")
while True:
    valid = input()
    if valid == nums:
        print("Captcha Validated")
        break
    else:
        i += 1
        if i == tries:
            print("Failed! The captcha was", nums)
            break
        print("Wrong input! Try again")

