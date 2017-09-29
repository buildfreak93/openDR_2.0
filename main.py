"""
Description: This is the primary code that controls the flow of the software.
Authors: Shivakshit Patri, Chinmaie Gorla
Last Updated: 29/9/2017
Version: openDR_2.0
Acknowledgements: Koteshwara Rao Chilakala, Sree Charan Manamala.
"""
from import_api import *
from gui_api import Owl_Gui, Owl_Gui_mrnum, owl_screen3 ,screen4_wifi,owl_grade,pwdEntry,confirm_shut
from cam_api import Fundus_Cam
class main():

    def __init__(self):
	self.flow()
        pygame.init()
        pygame.display.init()


    def password(self,obj_wifi,obj_pwd,keyboard):
	while True:
          #  print('password')
	    retVal = 0
	    retVal=obj_pwd.main(keyboard,obj_wifi.clickButton)
          ##### retVal is 1 when the back button is clicked
            if(retVal ==1):
                obj_pwd.screen1.fill((0,0,0))
                break

          ##### retVal is 2 when the Connect button is clicked
            elif(retVal ==2):
                obj_pwd.screen1.fill((0,0,0))
                break
	print(retVal)
	return retVal

    def wifi_screens(self,ogm):
        obj_wifi = screen4_wifi()
        while True:
            #ogm.screen.fill(((0,0,0)),(25,30,30,22))
            #ogm.screen.fill((0,0,0))
            pygame.display.flip()
            #obj_wifi = screen4_wifi()
	    retVal = obj_wifi.upd(obj_wifi.event1,obj_wifi.event2,obj_wifi.event3)
            if(retVal==1):
                obj_wifi.screen.fill((0,0,0))
                break
            elif(retVal==2):
                obj_pwd = pwdEntry()
		keyboard = obj_pwd.keyboard_init()
                obj_pwd.screen1.fill((0,0,0))
		retVal2 = self.password(obj_wifi,obj_pwd,keyboard)
		if retVal2 == 2:
		    break
    def flow(self):
        ############# Touch to proceed Screen ###################
        #og = Owl_Gui()
        # Initiating the screen 1 params.
        #font = pygame.font.Font(None, 30)
        # Updating the screen 1.
        #retVal = og.main_window()
        #ogm = Owl_Gui_mrnum()

        ########## Mr Number entry Screen #####################


        ############# Screen 1 ###################
        og = Owl_Gui()
        # Initiating the screen 1 params.
        font =  pygame.font.Font(None, 30)
        # Updating the screen 1.
        while True:
            retVal = og.main_window()
            # retVal is 1 when the mouse is clicked.
            if (retVal==1):
                ogm = Owl_Gui_mrnum()
                break
        ##########  Screen 2 #####################
        p1 = Process(target=ogm.get_wifi, args=(ogm.event1,ogm.event2,))
        p1.start()

        # Updating the screen.
        keyboard = ogm.keyboard_init()
        while True:
            retVal = ogm.name(ogm.event1,ogm.event2,keyboard)
            # retVal is 1 when the next button is clicked.
            if (retVal == 1):
                os3 = owl_screen3()
                break

         ##### retVal is 2 when the shut down button is clicked.
            elif (retVal == 2):
                obj_shdwn = confirm_shut()
                while True:
                    retVal = obj_shdwn.main_1()

         ##### retVal is 1 when the  confirm shutdown button is clicked
                    if (retVal == 1):
                        os.system("sudo pkill -9 -f main_pupil.py")

         ##### retVal is 2 when the back button is clicked
                    elif (retVal == 2):
                        obj_shdwn.screen1.fill((0,0,0))
                        break


            # retVal is 3 when the wifi button is clicked.
            # This case is not yet complete.
            elif (retVal == 3):
		self.wifi_screens(ogm)


             ############## Password Entry Screen ################
          ##### retVal is 2 when particular network button is selected
                    #elif(retVal==2):
                       # print("entered")
                       # obj_pwd = pwdEntry()
                       # break
                #keyboard = obj_pwd.keyboard_init()
                #while True:
                    #retVal=obj_pwd.main(keyboard,obj_wifi.clickButton)
          ##### retVal is 1 when the back button is clicked
                    #if(retVal ==1):
                        #obj_pwd.screen1.fill((0,0,0))
                        #break

          ##### retVal is 2 when the Connect button is clicked
                    #elif(retVal ==2):
                        #obj_pwd.screen1.fill((0,0,0))
                        #break
            # Some error with the retVal.

        ######### Screen 3  ########################
        self.fc = Fundus_Cam()
        flip_flag = False
        while True:
            retVal,flip_flag = os3.upd(flip_flag)
            # retVal is 1 when flip is clicked.
            if retVal == 1:
                os3.screen1.fill((0,0,0))
                flip_flag = not flip_flag
            # retVal is 2 when back is clicked.
            elif retVal == 2:
                self.fc.stop_preview()
                self.flow()
            # retVal is 3 when capture is clicked.
            elif retVal == 3:
                self.fc.pi_capture()
            elif retVal == 4:
                GradeVal = self.fc.img_grade()
                obj_grade = owl_grade(GradeVal)
                break
        while True:

            self.fc.stop_preview()
            gradeval = obj_grade.name(GradeVal)
            #elif retVal == 5:


        p1.join()
obj = main()
