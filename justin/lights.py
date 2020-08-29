import colorsys as col
import unicornhat as uh
import time
import math

uh.set_layout(uh.AUTO)
uh.rotation(0)
uh.brightness(0.25)

t = (int(input("How many minutes? "))*60)
i=0

def dcounter(totaldots):
    width = (math.ceil(totaldots/4))
    for x in range(width):
        y = (totaldots - x * 4)
        if (y > 4):
            y = 4
        print(x, y)
        time.sleep(10)
        #uh.set_pixel(x,i,3, 130, 255)
        #uh.show()


while (t):
    mins, secs = divmod(t, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat, end='\r')
    dcounter(t)
    time.sleep(1)
    t -= 1