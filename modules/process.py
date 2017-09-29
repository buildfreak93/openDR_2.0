## The entire python pipeline to process the image
import cv2
import sys
sys.path.insert(0, '/home/pi/openDR/modules/')
from extract import extract_fundus
import remove_glare
import theia

## TODO:
## ------------
## 1. Image parameters (center x,y, radius) should be arguments
'''2. DONE--<Can integrate all functions into single module '''
## 3. Image file should go as an argument and processed image returned, i.e.
##    this file should also be converted to a module

def grade(filename):
    #filename = str(filename)
    print 'entered grade'
    output = filename
    #img= extract_fundus(filename)
    #img = cv2.imread(filename)
    #print 'exitted extract funsdus'
    #cv2.imwrite(output, remove_glare.remove_glare(img))
    #print 'exitted rempve glare'
    return theia.grade_request(output)
