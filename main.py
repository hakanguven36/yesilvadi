from tkinter import *
import numpy as np
import cv2
from PIL import Image, ImageTk
import Resimler


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
def blackedToggle():
    global blacked
    blacked = blacked == False
    ResmiGoster()
def blurchange(v):
    global blur
    blur = int(v)
    ResmiGoster()
def consizechange(v):
    global consize
    consize = int(v)*10
    ResmiGoster()

def MakeScaler(inframe, minimum, maximum, commandante, value, labeltext):
    ininframe = Frame(inframe, borderwidth=3, pady=10)
    somescaler = Scale(ininframe, from_=minimum, to=maximum, orient=HORIZONTAL, command=commandante, length=240)

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
    btn_Blacked = Button(controlframe, text="Blacked", command=blackedToggle)
    btn_Blacked.pack()

def ResmiGoster():
    hsv = cv2.cvtColor(orjImage, cv2.COLOR_BGR2HSV)
    lower_red = np.array([huemin, satmin, vuemin])
    upper_red = np.array([huemax, satmax, vuemax])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    masked = cv2.bitwise_and(orjImage, orjImage, mask=mask)
    gray = cv2.cvtColor(masked, cv2.COLOR_BGR2GRAY)

        #blue, green, red = cv2.split(sonucResim)
        #sonucResim = cv2.merge((red, green, blue))


    ret, tresh = cv2.threshold(gray, 50,255, cv2.THRESH_BINARY)
    blured = cv2.blur(tresh, (blur,blur))
    ret, tresh = cv2.threshold(blured, 50, 255, cv2.THRESH_BINARY)

    contours, hierarchy = cv2.findContours(tresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    imageClone = np.array(orjImage)

    contours_poly = [None] * len(contours)
    boundRect = [None] * len(contours)
    for i, c in enumerate(contours):
        contours_poly[i] = cv2.approxPolyDP(c, 3, True)
        boundRect[i] = cv2.boundingRect(contours_poly[i])


    for i in range(len(contours)):
        color = (255,120,50)
        cv2.drawContours(imageClone, contours_poly, i, (255,0,),2)
        conArea = cv2.contourArea(contours[i])
        if conArea > consize:
            rx = int(boundRect[i][0])
            ry = int(boundRect[i][1])
            rgen = int(boundRect[i][2])
            ryuk = int(boundRect[i][3])
            cv2.rectangle(imageClone, (rx, ry), (rx + rgen, ry + ryuk), color, 2)

    for i in range(len(contours)):
        color = (255,120,50)




    #cv2.drawContours(fakeimage, contours, -1, (255, 0, 0), 1)
    #for i in range(len(contours)):
    #    if cv2.contourArea(contours[i]) > 1540:
    #        cv2.drawContours(fakeimage, contours, i, (255, 0, 0), 2)

    im = Image.fromarray(imageClone)
    global editedImage
    editedImage = ImageTk.PhotoImage(image=im)
    for chld in showtimeframe.winfo_children():
        chld.destroy()
    Label(showtimeframe, image=editedImage).pack()

huemin = 29
huemax = 80
satmin = 50
satmax = 255
vuemin = 0
vuemax = 255
blacked = True
blur = 10
consize = 25
editedImage = None
targetRectSize = 500


root = Tk()
mainframe = Frame(root, border=10)
showtimeframe = Frame(mainframe)
WindowYarat()

orjImage = cv2.imread("utaem04.jpg")
height, width, channels = orjImage.shape
ResmiGoster()
root.mainloop()








