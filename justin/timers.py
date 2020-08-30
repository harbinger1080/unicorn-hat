import time

t = input("Enter some seconds: ")

    mins, secs = divmod(t, 60)
    secs, ms = divmod(secs, 1000)
    timeformat = '{:02d}:{:02d}'.format(mins, secs)