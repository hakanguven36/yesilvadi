from tkinter import *
import numpy as np
import cv2
from PIL import Image, ImageTk

def MakeKulturBitkisi():
    return

def MakeYabanciOt():
    return

def WindowYarat():
    root.geometry("1400x800")
    mainframe.pack(side="top", anchor="w")
    showtimeframe.pack(side="left", anchor="n")
    controlframe.pack(anchor="ne")

    btnKultur = Button(controlframe, text="Kültür Bitkisi", command=MakeKulturBitkisi, width=60 , pady=20)
    btnKultur.pack()

    btnYabanci = Button(controlframe, text="Yabancı Ot", command=MakeYabanciOt, width=60 , pady=20)
    btnYabanci.pack()


def ResmiGoster():
    imageClone = cv2.cvtColor(orjImage, cv2.COLOR_BGR2RGB)[0:resyuk, 0:resgen]

    im = Image.fromarray(imageClone)
    global editedImage
    editedImage = ImageTk.PhotoImage(image=im)
    for chld in showtimeframe.winfo_children():
        chld.destroy()
    Label(showtimeframe, image=editedImage).pack()

root = Tk()
mainframe = Frame(root, border=10)
showtimeframe = Frame(mainframe, border=20)
controlframe = Frame(mainframe, border=20)
WindowYarat()

orjImage = cv2.imread("utaem04.jpg")
resgen = 1000
resyuk = 700
ResmiGoster()


root.mainloop()