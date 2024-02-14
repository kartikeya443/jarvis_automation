import pygetwindow as gw
from time import sleep

while 1:
    try:
        CURRENT_APP = gw.getActiveWindowTitle()
    except gw.PyGetWindowException:
        CURRENT_APP = ""
    sleep(1)
    print(CURRENT_APP.split(" - "))