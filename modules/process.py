## The entire python pipeline to process the image
import cv2
#import sys
#sys.path.insert(0, '/home/pi/openDR/modules/')
#from extract import extract_fundus
import remove_glare
import theia
import numpy as np
## TODO:
## ------------
## 1. Image parameters (center x,y, radius) should be arguments
'''2. DONE--<Can integrate all functions into single module '''
## 3. Image file should go as an argument and processed image returned, i.e.
##    this file should also be converted to a module

def extract_fundus(image):
    mask = np.full((image.shape[0],image.shape[1]),0,dtype=image.dtype)
    cv2.circle(mask,(400,400),50,(255,255,255),-1)
    image = cv2.bitwise_and(image,image,mask=mask)
    return image

def grade(filename):
    img = cv2.imread(filename)
    img = extract_fundus(img)
    cv2.imwrite(filename, remove_glare.remove_glare(img))
    return theia.grade_request(filename)
