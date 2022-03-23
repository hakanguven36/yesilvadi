import os
from tkinter import *
import numpy as np
import cv2 as cv

from os import listdir
from os.path import isfile, join


from PIL import Image, ImageTk


# yıl ay gun saat dakika saniye sanise ile bir id verelim dosyalara
def GetFiles(foldername):
     return [f for f in listdir(foldername) if isfile(join(foldername, f))]


foldername = os.path.realpath("Resimler")
print(foldername)
#filenameList = GetFiles(foldername)
#for file in filenameList:
 #   print(file)







