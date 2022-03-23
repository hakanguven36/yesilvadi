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

def swapOriginal():
    global showingOriginal
    showingOriginal = showingOriginal is False
    ResmiGoster()

def ResimleriHazirla():
    global printison
    printison = True
    ResmiGoster()



def MakeScaler(inframe, minimum, maximum, commandante, value, labeltext):
    ininframe = Frame(inframe, borderwidth=3)
    somescaler = Scale(ininframe, from_=minimum, to=maximum, orient=HORIZONTAL, command=commandante, length=240)
    somescaler.set(value)
    somescaler.pack(side="left")
    someLabel = Label(ininframe, text=labeltext)
    someLabel.pack(side="left")

    ininframe.pack(anchor="w")


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
    printBtn = Button(controlframe, text="Resimleri Hazirla", command=ResimleriHazirla)
    printBtn.pack()


def ResmiGoster():
    imageClone = cv2.cvtColor(orjImage, cv2.COLOR_BGR2RGB)[0:resyuk, 0:resgen]
    hsv = cv2.cvtColor(imageClone, cv2.COLOR_RGB2HSV)
    lower_green = np.array([huemin, satmin, vuemin])
    upper_green = np.array([huemax, satmax, vuemax])
    onlyGreen = cv2.inRange(hsv, lower_green, upper_green)
    blured = cv2.blur(onlyGreen, (5,5))
    _, tresh = cv2.threshold(blured, 20,255, cv2.THRESH_BINARY)
    masked = cv2.bitwise_and(imageClone, imageClone, mask=tresh)

    print(tresh.shape)
    step = 50
    karo = 100
    x1 = y1 = 0
    x2 = y2 = karo
    global printison
    if printison:
        while y2 < resyuk:
            x1 = 0
            x2 = karo
            while x2 < resgen:
                parca = tresh[y1:y2, x1:x2]
                if np.mean(parca) > 90:
                    filename = "parts\\resim" + str(x2) + "_" + str(y2) + ".jpg"
                    cv2.imwrite(filename, imageClone[y1:y2, x1:x2])
                x1 += step
                x2 += step
            y1 += step
            y2 += step
        printison = False





    # s = 100
    # for h in range(int(700/s)):
    #     for w in range(int(1000/s)):
    #         c = cropped[s*h:s*(h+1), s*w:s*(w+1)]
    #         #print(np.average(c))
    #         if np.average(c) > 40:
    #             part = orjImage[s * h:s * (h + 1), s * w:s * (w + 1)]
    #             cv2.imwrite("parts/utaem04_" + str(h+w) + ".jpg", part)


    im = Image.fromarray(masked)
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
blur = 4
consize = 25
editedImage = None
targetRectSize = 500
printison = False


root = Tk()
mainframe = Frame(root, border=10)
showtimeframe = Frame(mainframe)
WindowYarat()

img = cv2.imread("210612 2012.jpg")
orjImage = cv2.resize(img, dsize=(1000, 700), interpolation=cv2.INTER_CUBIC)

resgen = 1000
resyuk = 700
ResmiGoster()
root.mainloop()