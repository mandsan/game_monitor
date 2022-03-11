from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy

def imageGrab():
    image = ImageGrab.grab(bbox =(267, 215, 268, 223))
    num = numpy.array(image)
    # print(num.sum())
    if(num.sum()>950):
        print("魔力爆表囉")
    else:
        print("你可以喝魔力藥水囉")
        pyautogui.click(482,986)

while True:
    imageGrab()
    time.sleep(0.001)  