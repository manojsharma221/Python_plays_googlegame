import numpy as np
import cv2
from mss import mss
from PIL import Image
import pyautogui

mon = {'top': 389, 'left': 175, 'width': 98, 'height': 40}#area of interest on the screen

k=1
while 1:
    img=mss().grab(mon) #capturing the screen shot
    img=np.array(img)   #conveting the image to numpy arrays
    
    cv2.imshow('test', img) #just displaying the image
    p_cac =img[28,:,0]     #storing the blue colour's value of all pixels from 28th pixel 
    p_bird =img[1,:,0]     # storing the blue colour's value of all pixels from 1st pixel
    
    #print (px)
    #print (py)
    p_cac_sum=np.sum(p_cac)  #sum of all the bule values at 28th position
    p_bird_sum=np.sum(p_bird)
    print (p_cac_sum)
    
#white=247 and grey =83	(in my case)
    if p_cac_sum<24108:
     pyautogui.press('up')
    
    if p_bird_sum<24108:
     pyautogui.keyDown('down')
     print (p_bird)
     print (p_bird_sum)
     k=1	 
    
    if p_bird_sum==24108 and k==1:
	       pyautogui.keyUp('down')
	       k=0
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
