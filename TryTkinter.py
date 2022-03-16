from tkinter import *
import numpy as np
import cv2
from PIL import Image, ImageTk

root = Tk()
root.geometry("1200x800")
mainframe = Frame(root, border=10)
mainframe.pack(side="top", anchor="w")

controlframe = Frame(mainframe)
controlframe.pack( side="left",anchor="n")

showtimeframe = Frame(mainframe)
showtimeframe.pack( side="left", anchor="n")

scaller_hueMin = Scale(controlframe, from_=0, to=255,orient=HORIZONTAL)
scaller_hueMin.pack()
scaller_hueMax = Scale(controlframe, from_=0, to=255,orient=HORIZONTAL)
scaller_hueMax.pack()

resim = cv2.imread("utaem04.jpg")




#Rearrange colors
blue,green,red = cv2.split(resim)
img = cv2.merge((red,green,blue))
im = Image.fromarray(img)
imgtk = ImageTk.PhotoImage(image=im)
Label(showtimeframe, image=imgtk).pack()







root.mainloop()