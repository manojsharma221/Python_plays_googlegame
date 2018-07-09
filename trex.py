import numpy as np
import cv2
from mss import mss
from PIL import Image
import pyautogui

mon = {'top': 384, 'left': 220, 'width': 100, 'height': 40}#area of interest on the screen

sct = mss()
k=1
while 1:
    img=sct.grab(mon)
    img=np.array(img)
    
    cv2.imshow('test', img)
    px =img[28,:,0]
    py =img[1,:,0]
    
    #print (px)
    #print (py)
    pysum=np.sum(py)
    pxsum=np.sum(px)
    print (pxsum)
    #print (pysum)
#white=247 and grey =83	
    if pxsum<24700:
     pyautogui.press('up')
    
    if pysum<24700:
     pyautogui.keyDown('down')
     print (py)
     print (pysum)
     k=1	 
    
    if pysum==24700 and k==1:
	       pyautogui.keyUp('down')
	       k=0
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break