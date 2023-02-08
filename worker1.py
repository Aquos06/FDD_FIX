from PyQt5.QtCore import QObject
from PyQt5 import QtCore, QtGui

import cv2
import json
from json import JSONDecodeError
import numpy as np
import time
from datetime import datetime


#import trackking
from track import Trackker 
#import video stream
from VideoStreamOriginal import WebcamVideoStream
#import calculate fall
from allutility.falutil import Fallutil
#import coordinate util
from coorutil import specific, drawBbox, openJson, timetoint, NewDraw
#import calculate
from calculate import calculate

class Worker1(QObject):
    
    zoom_on = QtCore.pyqtSignal(bool, int)
    fall = QtCore.pyqtSignal(str, int)
    timenow = QtCore.pyqtSignal(str)
    koordinat = QtCore.pyqtSignal(np.ndarray,int)   
    config = QtCore.pyqtSignal(str,int) 

    def openconfig(self):
        camera1_change = False
        if self.user1 != self.config_file['channel1']['user']:
            camera1_change = True
            self.user1 = self.config_file['channel1']['user']

        if self.ip1 != self.config_file['channel1']['ip']:
            camera1_change = True
            self.ip1 = self.config_file['channel1']['ip']

        if self.password1 != self.config_file['channel1']['password']:
            camera1_change = True
            self.password1 = self.config_file['channel1']['password']
        
        if camera1_change:
            self.cap = f"rtsp://{self.user1}:{self.password1}@{self.ip1}"
            self.config.emit(self.cap,1)
        self.config_file['channel1']['change'] = False

        camera2_change =  False
        if self.user2 != self.config_file['channel2']['user']:
            camera2_change = True
            self.user2 = self.config_file['channel2']['user']
        
        if self.ip2 != self.config_file['channel2']['ip']:
            camera2_change = True
            self.ip2 = self.config_file['channel2']['ip']

        if self.password2 !=  self.config_file['channel2']['password']:
            camera2_change = True
            self.password2 = self.config_file['channel2']['password']

        if camera2_change:
            self.cap = f"rtsp://{self.user2}:{self.password2}@{self.ip2}"
            self.config.emit(self.cap,2)
        self.config_file['channel2']['change'] = False

        camera3_change = False
        if self.user3 != self.config_file['channel3']['user']:
            camera3_change = True
            self.user3 = self.config_file['channel3']['user']
        
        if self.ip3 != self.config_file['channel3']['ip']:
            camera3_change = True
            self.ip3 = self.config_file['channel3']['ip']

        if self.password3 !=  self.config_file['channel3']['password']:
            camera3_change = True
            self.password3 = self.config_file['channel3']['password']

        if camera3_change:
            self.cap = f"rtsp://{self.user3}:{self.password3}@{self.ip3}"
            self.config.emit(self.cap,3)
        self.config_file['channel3']['change'] = False

        camera4_change = False
        if self.user4 != self.config_file['channel4']['user']:
            camera4_change = True
            self.user4 = self.config_file['channel4']['user']
        
        if self.ip4 != self.config_file['channel4']['ip']:
            camera4_change = True
            self.ip4 = self.config_file['channel4']['ip']

        if self.password4 !=  self.config_file['channel4']['password']:
            camera4_change = True
            self.password4 = self.config_file['channel4']['password']

        if camera4_change:
            self.cap = f"rtsp://{self.user4}:{self.password4}@{self.ip4}"
            self.config.emit(self.cap,4)
        self.config_file['channel4']['change'] = False


        f = open('config2Channels.json', 'w')
        json.dump(self.config_file, f, indent=2)
        f.close()
             
    def openCam(self):
        f = open('config2Channels.json','r')
        config = json.load(f)
        f.close()

        self.user1 = config['channel1']['user']
        self.ip1 = config['channel1']['ip']
        self.password1 = config['channel1']['password']  

        self.user2 = config['channel2']['user']
        self.ip2 = config['channel2']['ip']
        self.password2 = config['channel2']['password'] 

        self.user3 = config['channel3']['user']
        self.ip3 = config['channel3']['ip']
        self.password3 = config['channel3']['password']

        self.user4 = config['channel4']['user']
        self.ip4 = config['channel4']['ip']
        self.password4 = config['channel4']['password']        
        
    def prep(self):
        self.config_file = openJson('config2Channels.json')
        self.OCtrack = Trackker()
        self.OCtrack.preparation()
        
        self.findfall = Fallutil()
        self.detect = True
        self.total_people = [[0,0],[0,0],[0,0],[0,0]]  

        self.calculate = calculate()

        self.mask_fall1 = cv2.imread('./ROI/Camera1/fall_down.jpg')
        self.mask_fall2 = cv2.imread('./ROI/Camera2/fall_down.jpg')
        self.mask_fall3 = cv2.imread('./ROI/Camera3/fall_down.jpg')
        self.mask_fall4 = cv2.imread('./ROI/Camera4/fall_down.jpg')

        self.openCam()
    
    def Jsonprep(self):
        self.function = openJson('function.json')
        self.ROI = openJson('AiSettings.json')
        self.config_file = openJson('config2Channels.json')
        self.zoom = openJson('zoom.json')

    def checkROI(self):
        try:
            if self.ROI['Camera1']['change'] == True:
                self.mask_fall1 = cv2.imread('./ROI/Camera1/fall_down.jpg')
                self.ROI['Camera1']['change'] = False

            if self.ROI['Camera2']['change'] == True:
                self.mask_fall2 = cv2.imread('./ROI/Camera2/fall_down.jpg')
                self.ROI['Camera2']['change'] = False
        
            if self.ROI['Camera3']['change'] == True:
                self.mask_fall3 = cv2.imread('./ROI/Camera3/fall_down.jpg')
                self.ROI['Camera3']['change'] = False

            if self.ROI['Camera4']['change'] == True:
                self.mask_fall4 = cv2.imread('./ROI/Camera4/fall_down.jpg')
                self.mask_fall4['Camera4']['change'] = False

            f = open('AiSettings.json', 'w')
            json.dump(self.ROI, f, indent=2)
            f.close()      
        except: 
            return

    def checkMin(self):
        try: 
            if self.config_file['channel1']['ROI'] == True:
                f = open('AiSettings.json', 'r')
                data = json.load(f)
                f.close()

                self.minWidth = data['Camera1']['Min']['width']
                self.minHeight = data['Camera1']['Min']['height']
                self.maxWidth = data['Camera1']['Max']['width']
                self.maxHeight = data['Camera1']['Max']['height']

            else:
                self.minWidth = None
                self.minHeight = None
                self.maxWidth = None
                self.maxHeight = None
        except:
            pass

    def time_now(self):
        Ddate = QtCore.QDateTime.currentDateTime().toString("dd.MM.yyyy").split(".")
        time_now = f"{Ddate[2]}-{Ddate[1]}-{Ddate[0]} {time.strftime('%H:%M:%S')}"
        return time_now

    def checkWH(self, coordinate):
        check = []

        for index, i in enumerate(coordinate):
            x1,y1,x2,y2,_,_ = i
            if self.minWidth and self.maxWidth:
                if x2-x1 < self.minWidth or y2-y1 < self.minHeight:
                    if x2-x1 > self.maxWidth or y2-y1 > self.maxHeight:
                        check.append(index)
            elif self.minWidth:
                if x2-x1 < self.minWidth or y2-y1 < self.minHeight:
                    check.append(index)
            elif self.maxWidth:
                if x2-x1 > self.maxWidth or y2-y2 > self.maxHeight:
                    check.append(index)

        for i in check:
            del coordinate[i]
            
        return coordinate

    def img2pyqt(self,img,label):
        '''
        convert the opencv format to pyqt format color
        '''
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        temp = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1]*3, QtGui.QImage.Format_RGB888)
        return QtGui.QPixmap.fromImage(temp).scaled(label.width(), label.height())
   
    def normalize(self, coordinate, fall):
        '''
            coordinate: x1,y1,x2,y2,conf,class
        '''
        for i,coor in enumerate(coordinate):
            x1,y1,x2,y2,conf,classes = coor
            coordinate[i][0] = x1 / 640 * 3840
            coordinate[i][1] = y1 / 640 * 3840
            coordinate[i][2] = x2 / 640 * 3840
            coordinate[i][3] = y2 / 640 * 3840

        for i,coor in enumerate(fall):
            Id,x1,y1,x2,y2 = coor
            fall[i][1] = x1 / 640 * 3840
            fall[i][2] = y1 / 640 * 3840
            fall[i][3] = x2 / 640 * 3840
            fall[i][4] = y2 / 640 * 3840

        return coordinate, fall

    def separate(self, person, fall):
        person, fall = self.normalize(person, fall)
        person1, person2, person3, person4 = [],[],[],[]
        fall1, fall2, fall3, fall4 = [], [], [], []

        for coor in person:
            if coor[0] < 1920:
                if coor[1] < 1080:
                    if self.config_file['channel1']['ROI'] == True:
                        if self.calculate.find(self.mask_fall1, coor, person = True) == 1:
                            person1.append(coor)
                    else:
                        person1.append(coor)
                else:
                    coor[1] -= 1080
                    coor[3] -= 1080
                    if self.config_file['channel3']['ROI'] == True:
                        if self.calculate.find(self.mask_fall3, coor, person = True) == 1:
                            person3.append(coor)
                    else:
                        person3.append(coor)
            else:
                if coor[1] < 1080:
                    coor[0] -= 1920
                    coor[2] -= 1920
                    if self.config_file['channel2']['ROI'] == True:
                        if self.calculate.find(self.mask_fall2, coor, person = True) == 1:
                            person2.append(coor)
                    else:
                        person2.append(coor)
                else:
                    coor[0] -= 1920
                    coor[1] -= 1080
                    coor[2] -= 1920
                    coor[3] -= 1080
                    if self.config_file['channel4']['ROI'] == True:
                        if self.calculate.find(self.mask_fall4, coor, person = True) == 1:
                            person4.append(coor)
                    else:
                        person4.append(coor)

        for coor in fall:
            if coor[1] < 1920:
                if coor[2] < 1080:
                    if self.config_file['channel1']['ROI'] == True:
                        if self.calculate.find(self.mask_fall1, coor) == 1:
                            fall1.append(coor)
                    else:
                        fall1.append(coor)
                else:
                    coor[2] -= 1080
                    coor[4] -= 1080
                    if self.config_file['channel3']['ROI'] == True:
                        if self.calculate.find(self.mask_fall3, coor) == 1:
                            fall3.append(coor)
                    else:
                        fall3.append(coor)
            else:
                if coor[2] <  1080:
                    coor[1] -= 1920
                    coor[3] -= 1920
                    if self.config_file['channel2']['ROI'] == True:
                        if self.calculate.find(self.mask_fall2, coor) == 1:
                            fall2.append(coor)
                    else:
                        fall2.append(coor)
                else:
                    coor[1] -= 1920
                    coor[2] -= 1080
                    coor[3] -= 1920
                    coor[4] -= 1080
                    if self.config_file['channel4']['ROI'] == True:
                        if self.calculate.find(self.mask_fall4, coor) == 1:
                            fall4.append(coor)
                    else:
                        fall4.append(coor)                    

        return person1, person2, person3, person4, fall1, fall2, fall3, fall4

    def specific(self, coordinate):
        person, fall = [],[]
        for coor in coordinate:
            if coor[-1] == 0:
                person.append(coor)
            else:
                fall.append(coor)

        return np.array(person), np.array(fall)

    def run(self):
        self.prep()
        self.img = np.zeros((2160,3840,3))
        self.noCam = cv2.imread('NoCamera.png')
        while True:
            if self.berenti:
                continue

            else: 
                self.Jsonprep()
                self.checkROI()

                self.timenow.emit(self.time_now())

                try:
                    if self.config_file['channel1']['change'] == True:
                        self.openconfig()
                except:
                    pass

                try :
                    self.camera1Img = self.img1
                    self.camera2Img = self.img2
                    self.camera3Img = self.img3
                    self.camera4Img = self.img4

                    self.img[:1080,:1920,:] = self.camera1Img
                    self.img[:1080,1920:,:] = self.camera2Img
                    self.img[1080:,:1920,:] = self.camera3Img
                    self.img[1080:,1920:,:] = self.camera4Img
                except:
                    pass
                coordinate = self.yolov7.predict(self.img)
                person, fall = self.specific(coordinate)
                fall,_ = self.OCtrack.tracking(fall,self.img)
                coordinate1, coordinate2, coordinate3, coordinate4 ,fall1, fall2, fall3, fall4 = self.separate(person, fall)

                if len(fall) > 0:
                    filename1 = self.findfall.final_fall(fall1, self.camera1Img, 1, self.function['function']['light_delay'])
                    filename2 = self.findfall.final_fall(fall2, self.camera2Img, 2, self.function['function']['light_delay'])
                    filename3 = self.findfall.final_fall(fall3, self.camera3Img, 3, self.function['function']['light_delay'])
                    filename4 = self.findfall.final_fall(fall4, self.camera4Img, 4, self.function['function']['light_delay'])

                    for file in filename1:
                        self.fall.emit(file,1)

                    for file in filename2:
                        self.fall.emit(file,2)
                    
                    for file in filename3:
                        self.fall.emit(file,3)

                    for file in filename4:
                        self.fall.emit(file,4)

                try:
                    if self.config_file['channel1']['active'] == True:
                        self.camera1Img = NewDraw(self.camera1Img, coordinate1, fall1)
                        
                        if self.config_file['channel1']['ROI'] == True: #ROI
                            self.camera1Img = cv2.addWeighted(self.camera1Img, 1, self.mask_fall1, 0.3, 0)

                        if self.zoom['Channel1'] == True:
                            self.screen.setPixmap(self.img2pyqt(self.camera1Img, self.screen))
                        else:
                            self.channel1.setPixmap(self.img2pyqt(self.camera1Img, self.channel1))

                        self.total_people[0][0] = len(fall1)
                        self.total_people[0][1] = len(fall1) + len(coordinate1)
                    else:
                        self.channel1.setPixmap(self.img2pyqt(self.noCam, self.channel1))
                except:
                    pass
                
                try:
                    if self.config_file['channel2']['active'] == True:
                        self.camera2Img = NewDraw(self.camera2Img, coordinate2, fall2)

                        if self.config_file['channel2']['ROI'] == True: #ROI
                            self.camera2Img = cv2.addWeighted(self.camera2Img, 1, self.mask_fall2, 0.3, 0)

                        if self.zoom['Channel2'] == True:
                            self.screen.setPixmap(self.img2pyqt(self.camera2Img, self.screen))
                        else:
                            self.channel2.setPixmap(self.img2pyqt(self.camera2Img, self.channel2))
                        
                        self.total_people[1][0] = len(fall2)
                        self.total_people[1][1] = len(coordinate2) + len(fall2)
                    else:
                        self.channel2.setPixmap(self.img2pyqt(self.noCam, self.channel2))
                except:
                    pass

                try:
                    if self.config_file['channel3']['active'] == True:
                        self.camera3Img = NewDraw(self.camera3Img, coordinate3, fall3)

                        if self.config_file['channel3']['ROI'] == True: #ROI
                            self.camera3Img = cv2.addWeighted(self.camera1Img, 1, self.mask_fall3, 0.3, 0)

                        if self.zoom['Channel3'] == True:
                            self.screen.setPixmap(self.img2pyqt(self.camera3Img, self.screen))
                        else:
                            self.channel3.setPixmap(self.img2pyqt(self.camera3Img, self.channel3))
                        
                        self.total_people[2][0] = len(fall3)
                        self.total_people[2][1] = len(coordinate3) + len(fall3)
                    else:
                        self.channel3.setPixmap(self.img2pyqt(self.noCam, self.channel3))
                except:
                    pass
                
                try:
                    if self.config_file['channel4']['active'] == True:
                        self.camera4Img = NewDraw(self.camera4Img, coordinate4, fall4)

                        if self.config_file['channel4']['ROI'] == True: #ROI
                            self.camera4Img = cv2.addWeighted(self.camera4Img, 1, self.mask_fall4, 0.3, 0)

                        if self.zoom['Channel4'] == True:
                            self.screen.setPixmap(self.img2pyqt(self.camera4Img, self.screen))
                        else:
                            self.channel4.setPixmap(self.img2pyqt(self.camera4Img, self.channel4))
                        
                        self.total_people[3][0] = len(fall4)
                        self.total_people[3][1] = len(coordinate4) + len(fall4)
                    else:
                        self.channel4.setPixmap(self.img2pyqt(self.noCam, self.channel4))
                except:
                    pass