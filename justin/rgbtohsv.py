import colorsys as col

def set_pixel_hsv(x, y, h, s, v):
    r, g, b = [int(c*255) for c in col.hsv_to_rgb(h,s,v)]
    print(x,y,r,g,b)

def colordots(ldots):
    if (ldots % 1 == 0):
            sat = 1.0
        else:    
            sat = (1.0 * (ldots % 1))
        set_pixel_hsv(.58, sat, 1.0)
    else:


while (t):
    #print(t)
    mins, secs = divmod(t, 60)
    #print(mins,secs)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)
    print(timeformat, end='\r')
    lights = t/dotst
    colordots(lights)
    time.sleep(1)
    t -= 1