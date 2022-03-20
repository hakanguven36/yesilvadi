#gausianBlur çalışmama nedenini arıyorum.
import cv2
import numpy as np
import cv2 as cv

filename = "G:\\Media\\Ukraine\\DSC00038.JPG"

resim = cv.imread(filename)
kernel = (21,21)
gblur = cv.blur(resim, kernel, cv2.BORDER_TRANSPARENT)

cv.imshow("resim", gblur)

cv2.waitKey(0)
cv2.destroyAllWindows()