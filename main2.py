from tkinter import *
import numpy as np
import cv2
from PIL import Image, ImageTk


def hueminchange(v):
    global huemin
    huemin = int(v)
    ResmiGoster()
def huemaxchange(v):
    global huemax
    huemax = int(v)
    ResmiGoster()
def satminchange(v):
    global satmin
    satmin = int(v)
    ResmiGoster()
def satmaxchange(v):
    global satmax
    satmax = int(v)
    ResmiGoster()
def vueminchange(v):
    global vuemin
    vuemin = int(v)
    ResmiGoster()
def vuemaxchange(v):
    global vuemax
    vuemax = int(v)
    ResmiGoster()
def blurchange(v):
    global blur
    blur = int(v)
    ResmiGoster()
def consizechange(v):
    global consize
    consize = int(v)*10
    ResmiGoster()
def treshchange(v):
    global tresh
    tresh = int(v)
    ResmiGoster()
def Yazdir():
    global yazdırOnay
    yazdırOnay = True
    ResmiGoster()

def MakeScaler(inframe, minimum, maximum, commandante, value, labeltext):
    ininframe = Frame(inframe, borderwidth=3, pady=10)
    somescaler = Scale(ininframe,  from_=minimum, to=maximum, orient=HORIZONTAL, command=commandante, length=240)
    somescaler.set(value)
    somescaler.pack()
    someLabel = Label(ininframe, text=labeltext)
    someLabel.pack()
    ininframe.pack()


def WindowYarat():
    global showtimeframe
    root.geometry("1400x800")
    mainframe.pack(side="top", anchor="w")
    controlframe = Frame(mainframe)
    controlframe.pack(side="left", anchor="n")
    showtimeframe.pack(side="left", anchor="n")
    MakeScaler(controlframe, 0, 255, hueminchange, huemin,"huemin")
    MakeScaler(controlframe, 0, 255, huemaxchange, huemax,"huemax")
    MakeScaler(controlframe, 0, 255, satminchange, satmin,"saturationmin")
    MakeScaler(controlframe, 0, 255, satmaxchange, satmax,"saturationmax")
    MakeScaler(controlframe, 0, 255, vueminchange, vuemin,"valuemin")
    MakeScaler(controlframe, 0, 255, vuemaxchange, vuemax,"valuemax")
    MakeScaler(controlframe, 1, 150, blurchange, blur, "blur")
    MakeScaler(controlframe, 1, 200, consizechange, consize, "contourSizeMin*10")
    MakeScaler(controlframe, 0, 150, treshchange, tresh, "tresh")
    btnyazdir = Button(controlframe, text="yazdır", command=Yazdir)
    btnyazdir.pack()



def ResmiGoster():

    #gerçek programda performans için bu kısım değişecek
    blue, green, red = cv2.split(orjImage)
    merged = cv2.merge((red, green, blue))
    imageClone = np.array(merged[0:resyuk,0:resgen])

    hsv = cv2.cvtColor(imageClone, cv2.COLOR_BGR2HSV)
    lower_green = np.array([huemin, satmin, vuemin])
    upper_green = np.array([huemax, satmax, vuemax])
    mask = cv2.inRange(hsv, lower_green, upper_green)
    masked = cv2.bitwise_and(imageClone, imageClone, mask=mask)
    gray = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)
    blured = cv2.blur(gray, (blur,blur))

    ret, treshed = cv2.threshold(blured, tresh, 255, cv2.THRESH_BINARY)

    imageClone = cv2.bitwise_and(imageClone, imageClone, mask=treshed)

    #cropped1 = cropped[0:50, 0:50]
    #cropped2 = cropped[50:100,0:50]
    #vis = np.concatenate((cropped1, cropped2), axis=0)


    global yazdırOnay

    S = 100
    s = 50
    if yazdırOnay:
        for h in range(int(resyuk/s)):
            for w in range(int(resgen/s)):
                c = tresh[s*h:s*(h+1), s*w:s*(w+1)]
                if np.average(c) > 60:
                    part = orjImage[s * h:s * (h + 1), s * w:s * (w + 1)]
                    cv2.imwrite("parts/utaem04_" + str(h+w) + ".jpg", part)
    yazdırOnay = False

    im = Image.fromarray(imageClone)
    global editedImage
    editedImage = ImageTk.PhotoImage(image=im)
    for chld in showtimeframe.winfo_children():
        chld.destroy()
    Label(showtimeframe, image=editedImage).pack()

huemin = 30
huemax = 80
satmin = 50
satmax = 255
vuemin = 0
vuemax = 255
blur = 15
consize = 25
tresh = 12
yazdırOnay = False

root = Tk()
mainframe = Frame(root, border=10)
showtimeframe = Frame(mainframe)
WindowYarat()

orjImage = cv2.imread("utaem04.jpg")
orjheight, orjwidth, orjchannels = orjImage.shape
resgen = 1000
resyuk=700


ResmiGoster()

if __name__ == '__main__':
    root.mainloop()
