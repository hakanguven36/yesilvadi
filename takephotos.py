import random
from _datetime import datetime
import time

artansayi = 0
def RandomName():
    global artansayi
    a = datetime.now()
    time.sleep(0.5)
    artansayi += 1
    return str(a.date()) + str(a.strftime("-%H%M%S-") + str(artansayi) + ".jpg")


for i in range(10):
    print(RandomName())

