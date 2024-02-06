#pip install easyocr
#pip install opencv-python
#pip install pyautogui
#pip install pil
#pip install difflib

import difflib
from time import time as t
import cv2
import easyocr
import numpy as np
import pyautogui as pg
from PIL import ImageGrab

reader = easyocr.Reader(['en'], bool = True)

#print the closest match
def center(points):
    
    #calculate the sum of x and y coordinates
    sum_x = sum(point[0] for point in points)
    sum_y = sum(point[1] for point in points)
    center_x = sum_x/len(points)
    center_y = sum_y/len(points)    
    return int(center_x), int(center_y)

#print the result
def ocr_v1_cl(st, double_click=False):
    
    #taking the ss and reading the data
    screen = np.array(ImageGrab.grab())
    image_np = cv2.cvtColor(screen, cv2.COLOR_RGB2BGR)
    
    c = t()
    result = reader.readtext(image_np)
    print("read in ", t()-c, "seconds.".encode('utf-8', errors='ignore').decode('utf-8'))
    arr_of_words = []
    
    #appending the data
    for i in result:
        arr_of_words.append(i[1].lower())
    
    #finding the closest match    
    closest_match = difflib.get_close_matches(st, arr_of_words, n=1)
    
    if closest_match:
        print(f"The best match for '{st}' is '{closest_match[0]}'.".encode('utf-8', errors='ignore').decode('utf-8'))
        for i in result:
            if i[1].lower() == closest_match[0].lower():
                
                if double_click:
                    pg.click(center(i[0]))
                    pg.sleep(0.35)
                    pg.click(center(i[0]))
                else:
                    pg.click(center(i[0]))
                break
        return "clicked" + st + " button sir."
    else:
        return f"no button found named. {st}"

