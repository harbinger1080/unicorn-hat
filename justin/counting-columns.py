height = 4
width = 8
i = 10

while i > 0:
    for x in range(width):
        for y in range(height):
            light = "OFF"
            if (i > 0):
                light = "ON"
                i -= 1
            else:
                light = "OFF"
            print(x,y,light)