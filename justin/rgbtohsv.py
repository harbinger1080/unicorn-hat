import colorsys as col
import time

t = 60

def set_pixel_hsv(x, y, h, s, v):
    r, g, b = [int(c*255) for c in col.hsv_to_rgb(h,s,v)]
    print(x, y, r, g, b)

def colordots(ldots):
    if (ldots % 1 == 0):
            sat = 1.0
    else:    
        sat = (1.0 * (ldots % 1))
    set_pixel_hsv(0, 0, .58, sat, 1.0)


while (t):
    mins, secs = divmod(t, 60)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat, end='\r')
    lights = t/15
    colordots(lights)
    time.sleep(1)
    t -= 1