import cv2
import numpy as np

hueMin = 0
hueMax = 255
satMin = 0
satMax = 255
vueMin = 0
vueMax = 255
blacked = False

ThisResim = None
sonucResim = None

def ResimAl(filename):
    global ThisResim



def Uygula(h1,h2,s1,s2,v1,v2):
    global sonucResim
    hsv = cv2.cvtColor(ThisResim, cv2.COLOR_BGR2HSV)
    lower_red = np.array([h1, s1, v1])
    upper_red = np.array([h2, s2, v2])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    sonucResim = cv2.bitwise_and(ThisResim, ThisResim, mask=mask)
    return sonucResim