from PIL import ImageGrab, ImageOps
import pyautogui
import time
import numpy

def imageGrab():
    image = ImageGrab.grab(bbox =(267, 195, 270, 210))
    num = numpy.array(image)
    # print(num.sum())
    if(num.sum()>9000):
        print("HP已滿")
    else:
        print("HP到設定值，觸發點擊")
        pyautogui.click(482,986)

while True:
    imageGrab()
    time.sleep(0.001)  