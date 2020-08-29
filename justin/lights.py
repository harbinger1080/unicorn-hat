import colorsys as col
import unicornhat as uh
import time

uh.set_layout(uh.AUTO)
uh.rotation(0)
uh.brightness(0.25)

t = int(input("How many minutes?"))

while (t):
    mins, secs = divmod(t, 60)
    dots = (t*60)//225

    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat, end='\r')

    for x in range(dots//4):
        if (dots % 4 == 0):
            dheight = 4
        else:
            dheight = dots
        for y in range(dheight):
            uh.set_pixel(x,y,3, 130, 255)
            uh.show()
        time.sleep(1)
    t -= 1