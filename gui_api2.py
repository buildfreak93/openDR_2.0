"""
Description: This api contains all the GUI features.
Authors: Shivakshit Patri, Chinmaie Gorla
Last updated: 29/9/2017
Version: openDR v2.0
"""

from import_api import *

class Owl_Gui():

    def __init__(self):

        self.display_width = 800
        self.display_height = 480
        self.imagepath = ('/home/pi/openDR_New/Icons/')
        self.img = pygame.image.load(self.imagepath + 'touch_screen.png')
        self.img_resized = pygame.transform.scale(self.img,(self.display_width,self.display_height))
        self.screen = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.display.set_caption('OWL 1')

    def main_window(self):
        pygame.display.flip()
        retVal = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
        self.screen.blit(self.img_resized,(0,0))
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            retVal = 1
        pygame.display.flip()
	return retVal

class Owl_Gui_mrnum():

    def __init__(self):

        self.event1 = Event()
        self.event2 = Event()
        self.event3 = Event()
        self.fontStyle = "helvetica"
        self.fontSize = 20
        self.display_width = 800
        self.display_height = 480
        self.black = (0,0,0)
        self.imagepath = ('/home/pi/openDR_New/Icons/')
        self.screen = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.display.set_caption('OWL_2')
        self.clock = pygame.time.Clock()
        self.text=""
        self.wifiConnec = pygame.image.load(self.imagepath + 'wifi.png')
        self.wifiDisConnec=pygame.image.load(self.imagepath + 'wifi_disabled.png')
        self.powerBtn=pygame.image.load(self.imagepath + 'powerbutton-01.png')
        self.logo=pygame.image.load(self.imagepath + 'OIO_head.png')
        self.next_Btn=pygame.image.load(self.imagepath + 'Next_Btn.png')
        self.next_Btn_clk=pygame.image.load(self.imagepath + 'Next_hvr_Btn.png')
        self.mrnumber=pygame.image.load(self.imagepath + 'mrnumber.png')
        self.wificlk=pygame.image.load(self.imagepath + 'wifiwhite.png')
        self.powerBtn_resized = pygame.transform.scale(self.powerBtn,(30,30))
        self.screen.fill(self.black)
        self.screen.blit(self.powerBtn_resized,(750,30))
        self.screen.blit(self.logo,(356,30))
        self.screen.blit(self.next_Btn,(751,185))
        self.screen.blit(self.mrnumber,(90,180))
        pygame.draw.line(self.screen,(0,0,0),(0,240),(800,240),8)

        ### to check the status of wifi
        self.parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
        self.parser.add_argument(dest='interface', nargs='?', default='wlan0',help='wlan0 interface (default: wlan0)')
        self.args = self.parser.parse_args()

    def get_wifi(self,event1,event2):
        while True:
            cmd = subprocess.Popen('iwconfig %s' % self.args.interface, shell=True,stdout=subprocess.PIPE)
            for line in cmd.stdout:
                if 'off/any' in line:
                    self.event1.set()
                elif 'Link Quality' in line:
                    self.event2.set()

    def keyboard_init(self):
        layout = VKeyboardLayout(VKeyboardLayout.AZERTY)
        keyboard = VKeyboard(self.screen, self.consumer, layout)
        #keyboard.enable()
        #keyboard.draw()
        return keyboard

    # accepts the input from keyboard
    def consumer(self,text):
        font = pygame.font.SysFont("Roboto", 50)
        block = font.render(text, True,(180,180,180))
        self.screen.blit(block,(300,160))
        self.screen.fill((0,0,0),(300,160,400,70))
        self.screen.blit(block,(300,160))
        pygame.display.update()
        if(len(text) >= 1):
            self.f11=open(self.imagepath + 'mr_num.txt',"wb")
            self.f11.write(text)
            self.f11.close()
        return text

    # accepts the main window
    def name(self,event1,event2,keyboard):
        retVal = 0
        keyboard.enable()
        keyboard.draw()
        pygame.display.flip()
        for event in pygame.event.get():
            keyboard.on_event(event)
            if event.type == QUIT:
                pygame.quit()
                running = False
        localtime = time.asctime(time.localtime(time.time()))
        current_time = time.ctime()
        font = pygame.font.SysFont(self.fontStyle, self.fontSize)
        time_date = font.render(localtime, 0,(146,148,151))
        self.screen.fill(self.black,(750,30,35,35))
        self.screen.blit(self.powerBtn_resized,(750,30))

        self.screen.fill(self.black,(300,30,107,44))
        self.screen.blit(self.logo,(356,30))

        self.screen.fill(self.black,(90,180,178,25))
        self.screen.blit(self.mrnumber,(90,180))

        if(self.event1.is_set()):
            self.screen.fill((0,0,0),(25,30,32,24))
            self.screen.blit(self.wifiDisConnec,(25,30))
            self.event1.clear()
        elif(self.event2.is_set()):
            self.screen.fill((0,0,0),(25,30,32,24))
            self.screen.blit(self.wifiConnec,(25,30))
            self.event2.clear()
        pygame.display.flip()
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

# for power btn
        if (780 > mouse[0] > 750) and (60 > mouse[1] > 30):
            if click[0] == 1:
                retVal = 2
## for wifi button
        if (55 > mouse[0] > 25) and (50 > mouse[1] > 30):
            if click[0] == 1:
                retVal = 3
#for next button
        if (788 > mouse[0] > 750) and (238 > mouse[1] > 125):
            self.screen.fill(self.black,(750,125,38,113))
            self.screen.blit(self.next_Btn_clk,(750,125))
            if click[0] == 1:
                retVal = 1
        else:
            self.screen.fill(self.black,(750,125,38,113))
            self.screen.blit(self.next_Btn,(750,125))

        pygame.display.flip()
        return retVal

####Confirm shutdown screen
class confirm_shut():
    def __init__(self):
        self.imagepath = ('/home/pi/openDR_New/Icons/')
        self.gray = (35,31,32)
        self.back_Btn=pygame.image.load(self.imagepath + 'Back_Btn.png')
        self.back_hvr_Btn=pygame.image.load(self.imagepath + 'Back_hvr_Btn.png')
        self.display_width = 800
        self.display_height = 480
        self.warng_1=pygame.image.load(self.imagepath + 'Power_Btn.png')
        self.warng_hvr_1=pygame.image.load(self.imagepath + 'Power_hvr_Btn.png')
        self.screen1 = pygame.display.set_mode((self.display_width,self.display_height))
        pygame.display.set_caption('OWL')

## to update the gui
    def main_1(self):
        retVal=0
        pygame.init()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        self.screen1.fill(self.gray)
        self.screen1.blit(self.back_Btn,(50,185))
        self.screen1.fill(self.gray,(315,150,206,209))
        self.screen1.blit(self.warng_1,(315,150))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

###to confirm shutdown
        if (521 > mouse[0] > 315) and (359 > mouse[1] > 209):
            self.screen1.fill(self.gray,(315,150,206,209))
            self.screen1.blit(self.warng_hvr_1,(315,150))
            if (click[0]==1):
                retVal = 1
        else:
            self.screen1.fill(self.gray,(315,150,206,209))
            self.screen1.blit(self.warng_1,(315,150))
###to go back
        if (88 > mouse[0] > 50) and (298 > mouse[1] > 185):
            self.screen1.fill(self.gray,(50,185,38,113))
            self.screen1.blit(self.back_hvr_Btn,(50,185))
            if (click[0]==1):
                retVal = 2
        else:
            self.screen1.fill(self.gray,(50,185,38,113))
            self.screen1.blit(self.back_Btn,(50,185))
        pygame.display.flip()
        return retVal

####Screen to capture fundus images
class owl_screen3():
    def __init__(self):
#a dynamic grading key
        self.imagepath = ('/home/pi/openDR_New/Icons/')
        self.i=1 # initial_counter
        ###### upd variable #####################
        self.flag =1
        self.enable = 0
        self.wifi_check=0
        self.no=0
        self.bg_clr = (0,0,0)
        self.enable_flip = 0

        self.event1 = Event()
        self.event2 = Event()
        self.event3 = Event()
        self.event4 = Event()
        self.event5 = Event()
        ############# GUI Vars ############################
        self.fontSize = 20
        self.fontStyle="Helvetica"
        self.display_width = 800
        self.display_height = 480
        #########   Initialization  ###############
        self.screen = pygame.display.set_mode((self.display_width,self.display_height),pygame.RESIZABLE)
        self.screen.fill((0,0,0))
        self.screen1 = pygame.display.set_mode((self.display_width,self.display_height),pygame.RESIZABLE)
        self.screen1.fill((0,0,0))
        pygame.display.set_caption('OWL_3')
        self.clock = pygame.time.Clock()
        font = pygame.font.SysFont(self.fontStyle, 20)

##############
        self.flip_btn=pygame.image.load(self.imagepath + 'flip.png')
        self.capture_btn=pygame.image.load(self.imagepath + 'capture.png')
        self.grade_btn=pygame.image.load(self.imagepath + 'grade.png')
        self.back_btn=pygame.image.load(self.imagepath + 'back.png')
        self.stitch_btn=pygame.image.load(self.imagepath + 'stitch.png')
        self.flip_hvr_btn=pygame.image.load(self.imagepath + 'flip_hvr.png')
        self.capture_hvr_btn=pygame.image.load(self.imagepath + 'capture_hvr.png')
        self.grade_hvr_btn=pygame.image.load(self.imagepath + 'grade_hvr.png')
        self.back_hvr_btn=pygame.image.load(self.imagepath + 'back_hvr.png')
        self.stitch_hvr_btn=pygame.image.load(self.imagepath + 'stitch_hvr.png')
############180 degree roated gui icons

        self.flip_btn_inv=pygame.transform.rotate(self.flip_btn,180)
        self.capture_btn_inv=pygame.transform.rotate(self.capture_btn,180)
        self.grade_btn_inv=pygame.transform.rotate(self.grade_btn,180)
        self.back_btn_inv=pygame.transform.rotate(self.back_btn,180)
        self.stitch_btn_inv=pygame.transform.rotate(self.stitch_btn,180)
        self.flip_hvr_btn_inv=pygame.transform.rotate(self.flip_hvr_btn,180)
        self.capture_hvr_btn_inv=pygame.transform.rotate(self.capture_hvr_btn,180)
        self.grade_hvr_btn_inv=pygame.transform.rotate(self.grade_hvr_btn,180)
        self.back_hvr_btn_inv=pygame.transform.rotate(self.back_hvr_btn,180)
        self.stitch_hvr_btn_inv=pygame.transform.rotate(self.stitch_hvr_btn,180)

        self.wifiConnec = pygame.image.load(self.imagepath + 'wifi.png')
        self.wifiDisConnec=pygame.image.load(self.imagepath + 'wifi_disabled.png')
        self.wifiConnec_rot=pygame.transform.rotate(self.wifiConnec,180)
        self.wifiDisConnec_rot=pygame.transform.rotate(self.wifiDisConnec,180)

        self.parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
        self.parser.add_argument(dest='interface', nargs='?', default='wlan0',help='wlan0 interface (default: wlan0)')
        self.args = self.parser.parse_args()


    def upd(self,flip_flag=False):
        retVal = 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        cmd = subprocess.Popen('iwconfig %s' % self.args.interface, shell=True,stdout=subprocess.PIPE)

        for line in cmd.stdout:
            if 'off/any' in line:
                self.event4.clear()
                self.event5.set()
                if(not flip_flag):
                    self.screen.fill((0,0,0),(750,50,32,24))
                    self.screen.blit(self.wifiDisConnec,(750,50))

                else:
                    self.screen1.fill((0,0,0),(50,420,32,24))
                    self.screen1.blit(self.wifiDisConnec_rot,(50,420))

            elif 'Link Quality' in line:
                self.check_wifi=1
                self.event5.clear()
                self.event4.set()
                if (not flip_flag):
                    self.screen.fill((0,0,0),(750,50,32,24))
                    self.screen.blit(self.wifiConnec,(750,50))
                else:
                    self.screen1.fill((0,0,0),(50,420,32,24))
                    self.screen1.blit(self.wifiConnec_rot,(50,420))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if not flip_flag:
            # Flip button
            if 39 < mouse[0] < 220 and 35 < mouse[1] < 118:
                self.screen.fill(self.bg_clr,(39,35,181,83))
                self.screen.blit(self.flip_hvr_btn,(39,35))
                if click[0] == 1:
                    retVal = 1
            else:
                self.screen.fill(self.bg_clr,(39,35,181,83))
                self.screen.blit(self.flip_btn,(39,35))

            # Back button
            if 39 < mouse[0] < 220 and 367 < mouse[1] < 450:
                self.screen.fill(self.bg_clr,(39,367,181,83))
                self.screen.blit(self.back_hvr_btn,(39,367))
                if click[0] == 1:
                    retVal = 2
            else:
                self.screen.fill(self.bg_clr,(39,367,181,83))
                self.screen.blit(self.back_btn,(39,367))

            # Capture button
            if 39 < mouse[0] < 220 and 118 < mouse[1] < 201:
                self.screen.fill(self.bg_clr,(39,118,181,83))
                self.screen.blit(self.capture_hvr_btn,(39,118))
                if click[0] == 1:
                    retVal = 3
            else:
                self.screen.fill(self.bg_clr,(39,118,181,83))
                self.screen.blit(self.capture_btn,(39,118))

            # Grade button.
            if 39 < mouse[0] < 220 and 201 < mouse[1] < 284:
                self.screen.fill(self.bg_clr,(39,201,181,83))
                self.screen.blit(self.grade_hvr_btn,(39,201))
                if click[0] == 1:
                   # owl_grade()
                    retVal = 4
            else:
                self.screen.fill(self.bg_clr,(39,201,181,83))
                self.screen.blit(self.grade_btn,(39,201))

            # Stitch button.
            if 39 < mouse[0] < 220 and 284 < mouse[1] < 367:
                self.screen.fill(self.bg_clr,(39,284,181,83))
                self.screen.blit(self.stitch_hvr_btn,(39,284))
                if click[0] == 1:
                    retVal = 5
            else:
                self.screen.fill(self.bg_clr,(39,284,181,83))
                self.screen.blit(self.stitch_btn,(39,284))



        else:
            # Flip in flip mode.
            if 584 < mouse[0] < 765 and 358 < mouse[1] < 441:
                self.screen1.fill(self.bg_clr,(584,358,181,83))
                self.screen1.blit(self.flip_hvr_btn_inv,(584,358))
                if click[0] == 1:
                    retVal = 1
            else:
                self.screen1.fill(self.bg_clr,(584,358,181,83))
                self.screen1.blit(self.flip_btn_inv,(584,358))

            # Back in flip mode.
            if 584 < mouse[0] < 765 and 26 < mouse[1] < 109:
                self.screen1.fill(self.bg_clr,(584,26,181,83))
                self.screen1.blit(self.back_hvr_btn_inv,(584,26))
                if click[0] == 1:
                    retVal = 2
            else:
                self.screen1.fill(self.bg_clr,(584,26,181,83))
                self.screen1.blit(self.back_btn_inv,(584,26))

            # Capture in flip mode.
            if 584 < mouse[0] < 765 and 275 < mouse[1] < 358:
                self.screen1.fill(self.bg_clr,(584,275,181,83))
                self.screen1.blit(self.capture_hvr_btn_inv,(584,275))
                if click[0] == 1:
                    retVal = 3
            else:
                self.screen1.fill(self.bg_clr,(584,275,181,83))
                self.screen1.blit(self.capture_btn_inv,(584,275))

            # Grade in flip mode.
            if 584 < mouse[0] < 765 and 192 < mouse[1] < 275:
                self.screen1.fill(self.bg_clr,(584,192,181,83))
                self.screen1.blit(self.grade_hvr_btn_inv,(584,192))
                if click[0] == 1:
                    #owl_grade()
                    retVal = 4
            else:
                self.screen1.fill(self.bg_clr,(584,192,181,83))
                self.screen1.blit(self.grade_btn_inv,(584,192))

            # Stitch in flip mode.
            if 584 < mouse[0] < 765 and 109 < mouse[1] < 192:
                self.screen1.fill(self.bg_clr,(584,109,181,83))
                self.screen1.blit(self.stitch_hvr_btn_inv,(584,109))
                if click[0] == 1:
                    retVal = 5
            else:
                self.screen1.fill(self.bg_clr,(584,109,181,83))
                self.screen1.blit(self.stitch_btn_inv,(584,109))

        pygame.display.flip()
        return retVal,flip_flag

###still not yet complete , wifi trigger on screen3
    def Connect_wifi(self,msg,x,y,w,h,ic,ac,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            if click[0] == 1 and action ==None:
                self.screen.fill(((0,0,0)),(25,30,30,22))
                if(self.event2.is_set()):
                    screen4_wifi()
                else:
                    try:
                        obj_fc.stop_preview()
                        obj_fc.stop()
                        screen4_wifi()
                    except:
                        screen4_wifi()

##### Screen for display of grade
class owl_grade():
    def __init__(self):
        self.imagepath = ('/home/pi/openDR_New/Icons/')
        self.display_width = 800
        self.display_height = 480
        self.black = (0,0,0)
        self.screen = pygame.display.set_mode((self.display_width,self.display_height))
        self.screen.fill(self.black)
        pygame.display.set_caption('OWL')
        clock = pygame.time.Clock()
        self.next_Btn=pygame.image.load(self.imagepath + 'next.png')

    def name(self,GradeVal):
        pygame.init()
        font = pygame.font.SysFont("helvetica",50)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                running = False

        self.screen.blit(self.next_Btn,(750,185))
        grade_text = font.render('Grade :',0,(255,255,255))
        grade_value = font.render(GradeVal,0,(255,255,255))
        self.screen.blit(grade_text,(210,100))
        self.screen.blit(grade_value,(410,100))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if 771 > mouse[0] > 750 and 224 > mouse[1] > 176:
            if click[0] == 1:
          ##### return to mr number screen
                Owl_Gui_mrnum()
        pygame.display.flip()

####Gui for wifi network display and connectivity

class Finder:
    def __init__(self, *args, **kwargs):
        self.server_name = kwargs['server_name']
        self.password = kwargs['password']
        self.interface_name = kwargs['interface']
        self.main_dict = {}

    def run(self):
        #command = """sudo iwlist wlx18d6c71c04b2 scan | grep -ioE 'ssid:"(.*{}.*)'"""
        command = """sudo iwlist wlan0 scan | grep -ioE 'ssid:"(.*{}.*)'"""
        result = os.popen(command.format(self.server_name))
        result = list(result)

        if "Device or resource busy" in result:
                return None
        else:
            ssid_list = [item.lstrip('SSID:').strip('"\n') for item in result]
            print ssid_list
            print("Successfully get ssids {}".format(str(ssid_list)))

        for name in ssid_list:
            try:
                result = self.connection(name)
            except Exception as exp:
                print("Couldn't connect to name : {}. {}".format(name, exp))
            else:
                if result:
                    print("Successfully connected to {}".format(name))

    def connection(self, name):
        try:
            os.system("sudo nmcli d wifi connect '{}' password {} iface {}".format(name,
       self.password,
       self.interface_name))
        except:
            raise
        else:
            return True


class screen4_wifi():
    def __init__(self):
        self.imagepath = ('/home/pi/openDR_New/Icons/')
        self.event1 = Event()
        self.event2 = Event()
        self.event3 = Event()
        self.fontStyle = "helvetica"
        self.fontSize = 20
        self.display_width = 800
        self.display_height = 480
        self.black = (0,0,0)
        self.pos1_x=0
        self.pos2_x=700
        self.pos_y=400
        self.chocolate=(96,96,96)
        self.olive=(180,180,180)
        self.screen = pygame.display.set_mode((self.display_width,self.display_height))
        self.screen.fill(self.black)
        self.screen1 = pygame.display.set_mode((self.display_width,self.display_height))
        self.screen1.fill(self.black)
        pygame.display.set_caption('OWL_wifi')
        self.clock = pygame.time.Clock()
        self.ch = []
        self.text = ['']
        self.lines_4 = []
        self.clickButton = 0
        self.f11 = open('/home/pi/openDR_New/' + 'network.txt','r')
        self.lines_1 = self.f11.readlines()
        self.f11.close()
        self.f11 = open('/home/pi/openDR_New/' + 'network.txt','r')
        self.lines = len(self.f11.readlines())
        for self.i in range(self.lines):
            self.ch.append(self.lines_1[self.i])
        self.f11.close()
        self.back_btn=pygame.image.load(self.imagepath + 'Back_Btn.png')
        self.back_hvr_btn=pygame.image.load(self.imagepath + 'Back_hvr_Btn.png')
        self.x_cord = 100
        self.y_cord = 10
        self.text_x_cord = 20
        self.text_y_cord = 20
        self.count = 0
        self.name1=""
        self.gray=(35,31,32)

###### to create textobjects
    def text_objects(self,text,font):
        textSurface = font.render(text, True,self.black)
        return textSurface,textSurface.get_rect()

######### GUI FOR WIFI network display
    def upd(self,event1,event2,event3):
        pygame.display.flip()
        retVal = 0
        self.name = ""
        self.temp = ""
        self.name1=""
        font = pygame.font.SysFont(self.fontStyle, 15)
        text_1 = font.render("Available wifi networks", 0,(180,180,180))
        self.ctr=0
        self.count = 0
        for evt in pygame.event.get():
            if evt.type == KEYDOWN:
                temp = evt.unicode
                if evt.unicode.isalnum():
                    name += evt.unicode
                elif evt.key == K_BACKSPACE:
                    name = name[:-1]
                elif evt.key == K_RETURN:
                    name1 = name
    		break
            elif evt.type == QUIT:
                return
        text_2 = font.render(self.name, 0,(180,180,180))
        text_3 = font.render("Password:", 0,(180,180,180))
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

######### when escape is clicked
        if 138 > mouse[0] > 100 and 238 > mouse[1] > 125:
            self.screen.fill(self.gray,(100,125,38,113))
            self.screen.blit(self.back_hvr_btn,(100,125))
            if click[0] == 1:
                print("esc is clckld")
                retVal=1
        else:
            self.screen.fill(self.gray,(100,125,38,113))
            self.screen.blit(self.back_btn,(100,125))

        for line in self.lines_1:
            line = line.strip()
            self.words,self.networks,null=line.split('"')
            self.lines_4.append(self.networks.strip())
        if self.count != self.lines:
            for i in range(self.lines):
                retVal = self.button(self.lines_4[i],430,(self.text_y_cord+self.ctr),300,30,self.olive,self.chocolate,i,retVal)
                self.ctr=self.ctr+50
                self.count = self.count + 1

        self.ctr=0
        for i in range(self.lines):
            self.button(self.lines_4[i],430,(self.text_y_cord+self.ctr),300,30,self.olive,self.chocolate, i,retVal)
            self.ctr=self.ctr+50
        pygame.display.flip()
        return retVal

######Creates buttons for wifi networks
    def button(self,msg,x,y,w,h,ic,ac, i,retVal,action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x+w > mouse[0] > x and y+h > mouse[1] > y:
            pygame.draw.rect(self.screen, ac,(x,y,w,h))
            if click[0] == 1 and action ==None:
                self.clickButton = i
                self.event2.set()
                retVal=2
        else:
            pygame.draw.rect(self.screen, ic,(x,y,w,h))

        smallText = pygame.font.SysFont(self.fontStyle,16)
        textSurf, textRect = self.text_objects(msg, smallText)
        textRect.center = ( (x+(w/2)), (y+(h/2)) )
        self.screen.blit(textSurf, textRect)
        return retVal

class pwdEntry():
    def __init__(self):
        self.imagepath = ('/home/pi/openDR_New/Icons/')
        self.clickButton = -1
        self.display_width = 800
        self.display_height = 480
        self.gray=(35,31,32)
        self.screen1 = pygame.display.set_mode((self.display_width,self.display_height))
        self.screen1.fill((35,31,32))
        self.event3 = Event()
        self.f11 = open('/home/pi/openDR_New/' + 'network.txt','r')
        self.lines_1 = self.f11.readlines()
        self.f11.close()
        self.lines_4 = []
        self.back_btn=pygame.image.load(self.imagepath + 'Back_Btn.png')
        self.back_hvr_btn=pygame.image.load(self.imagepath + 'Back_hvr_Btn.png')
        self.next_btn=pygame.image.load(self.imagepath + 'Next_Btn.png')
        self.next_hvr_btn=pygame.image.load(self.imagepath + 'Next_hvr_Btn.png')

#####Initialization of Keyboard
    def keyboard_init(self):
        layout = VKeyboardLayout(VKeyboardLayout.AZERTY)
        keyboard = VKeyboard(self.screen1, self.consumer, layout)
        return keyboard

###### Accepts the input from keyboard
    def consumer(self,text):
        font = pygame.font.SysFont("Helvetica", 30)
        block = font.render(text, True,(180,180,180))
        self.screen1.blit(block,(300,160))
        self.screen1.fill((35,31,32),(300,160,400,70))
        self.screen1.blit(block,(300,160))
        pygame.display.update()
        if(len(text) >= 1):
            self.f11=open('/home/pi/openDR_New' + 'network.txt',"wb")
            self.f11.write(text)
            self.f11.close()
        return text

####To update the GUI onto the screen
    def main(self,keyboard,clickButton):
        retVal = 0
        self.clickButton = clickButton
        font = pygame.font.SysFont("Helvetica", 30)
        content = font.render("Enter the password", True,(180,180,180))
        self.screen1.fill((35,31,32),(50,30,350,50))
        self.screen1.blit(content,(50,30))
        keyboard.enable()
        keyboard.draw()
        for event in pygame.event.get():
            keyboard.on_event(event)
            if event.type == QUIT:
                pygame.quit()
                running = False

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

#####Back Button
        if 88 > mouse[0] > 50 and 238 > mouse[1] > 125:
            self.screen1.fill(self.gray,(50,125,38,113))
            self.screen1.blit(self.back_hvr_btn,(50,125))
            if click[0] == 1:
                retVal=1
        else:
            self.screen1.fill(self.gray,(50,125,38,113))
            self.screen1.blit(self.back_btn,(50,125))

#####Next button
        if (788 > mouse[0] > 750) and (238 > mouse[1] > 125):
            self.screen1.fill(self.gray,(750,125,38,113))
            self.screen1.blit(self.next_hvr_btn,(750,125))
            if click[0] == 1:
                self.event3.set()
                retVal = 2
                self.upd1()
        else:
            self.screen1.fill(self.gray,(750,125,38,113))
            self.screen1.blit(self.next_btn,(750,125))
        pygame.display.flip()
	return retVal

#####To connect to wifi
    def upd1(self):
        for line in self.lines_1:
            line = line.strip()
            self.words,self.networks,self.null=line.split('"')
            self.lines_4.append(self.networks.strip())
        if(self.event3.is_set()):
            self.f11 = open(self.imagepath + 'key.txt','r')
            self.key = self.f11.readline()
            self.f11.close
            F = Finder(server_name=self.lines_4[self.clickButton],
               password=self.key,
                   interface="wlan0")
            F.run()
