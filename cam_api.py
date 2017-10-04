'''
Description: This api contains the back-end processes that are triggered when images are clicked.
Authors: Shivakshit Patri, Chinmaie Gorla
Last Updated: 29/9/2017
Version: openDR v2.0
'''

from import_api import *
import sys
sys.path.insert(0, '/home/pi/openDR_2.0/modules/')

# adding modules folder to the start of python search path
import process      # our processing module
from process import grade
import extract
from extract import extract_fundus
import stitch
from stitch import stitch

class Fundus_Cam(object):

    def __init__(self):
        self.base_folder = '/home/pi/OWL/'
        self.time = datetime.datetime.now()
        self.saveDir = self.base_folder + str(self.time.year) +'-'+ str(self.time.month) +'-'+ str(self.time.day) +'/'+ open('/home/pi/openDR_2.0/Icons/mr_num.txt',"r").read() +'/images/'
        print self.saveDir
	if not os.path.isdir(self.saveDir):
            os.makedirs(self.saveDir)
        self.count = len([name for name in os.listdir(self.saveDir) if os.path.isfile(os.path.join(self.saveDir,name))])
        self.camera = PiCamera()
        self.camera.resolution = (640, 480)
        self.camera.framerate = 60
        self.stream = io.BytesIO()
        #self.start_preview()
        #self.camera.start_preview(fullscreen = False,window = (60,60,640,480))

    def stop_preview(self):
        self.camera.stop_preview()

    def start_preview(self):
        self.camera.start_preview(fullscreen = False,window = (60,60,640,480))


    def pi_capture(self):
        capture_flag = True
        for i in range(0,3):
            self.flag = 0
            self.camera.capture(self.stream,format='jpeg',use_video_port=False)
            Thread(target=self.pi_write,args=(self.stream,)).start()
            self.stream.truncate()
            self.stream.seek(0)
        return capture_flag

    def pi_write(self,stream):
        self.count += 1
        image = np.fromstring(stream.getvalue(),dtype=np.uint8)
        cv2.imwrite(self.saveDir + str(self.count) + '.jpg',cv2.imdecode(image,1))


    #def stitch(srcFolder):

    def img_grade(self):
        file_path = self.saveDir + str(self.count) + '.jpg'
        grade_val = str(grade(self.saveDir + str(self.count) + '.jpg'))[:4]
        return grade_val, file_path

