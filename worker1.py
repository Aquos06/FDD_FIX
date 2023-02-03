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
#import Yolov7
from yolov7 import detect


class Worker1(QObject):
    
    totalfall = QtCore.pyqtSignal(int,int,int)
    zoom_on = QtCore.pyqtSignal(bool, int)
    fall = QtCore.pyqtSignal(str, int)
    timenow = QtCore.pyqtSignal(str)
    koordinat = QtCore.pyqtSignal(np.ndarray,int)   
    config = QtCore.pyqtSignal(str,int) 
    noCamera = QtCore.pyqtSignal(bool, int)

    def openconfig(self):
        
        self.user = self.config_file['channel1']['user']
        self.ip = self.config_file['channel1']['ip']
        self.password = self.config_file['channel1']['password']
        
        self.cap = f"rtsp://{self.user}:{self.password}@{self.ip}"

        self.config.emit(self.cap,1)
        self.config_file['channel1']['change'] = False
            
        f = open('config2Channels.json', 'w')
        json.dump(self.config_file, f, indent=2)
        f.close()
             
    def prep(self):
        self.config_file = openJson('config2Channels.json')
        self.OCtrack = Trackker()
        self.ready = False
        self.OCtrack.preparation()
        
        self.findfall = Fallutil(1)
        self.detect = True
        self.total_people = []  

        self.yolov7 = detect()

        self.mask_person = cv2.imread('./ROI/Camera1/person.jpg')
        self.mask_fall = cv2.imread('./ROI/Camera1/fall_down.jpg')
        self.mask_PPE = cv2.imread('./ROI/Camera1/PPE.jpg')    
    
    def Jsonprep(self):
        # self.fall_store = openJson('fall_store.json')
        self.function = openJson('function.json')
        self.ROI = openJson('AiSettings.json')
        self.config_file = openJson('config2Channels.json')
        # self.personal = openJson('personal.json')
        self.zoom = openJson('zoom.json')

    
    def checkROI(self):
        try:
            if self.ROI['Camera1']['change'] == True:
                self.mask_person = cv2.imread('./ROI/Camera1/person.jpg')
                self.mask_fall = cv2.imread('./ROI/Camera1/fall_down.jpg')
                self.mask_PPE = cv2.imread('./ROI/Camera1/PPE.jpg')

                self.ROI['Camera1']['change'] = False

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
   
    def run(self):
        self.prep()
        self.img = cv2.imread('NoCamera.png')
        while True:
            self.Jsonprep()
            self.checkROI()
            # self.checkMin()

            while self.berenti:
                time.sleep(0.1)

            self.timenow.emit(self.time_now())

            try:
                if self.config_file['channel1']['change'] == True:
                    self.openconfig()
            except:
                pass

            try:
                if self.config_file['channel1']['active'] == True:
                    self.noCamera.emit(False,1)
            except:
                pass

            try:
                if self.config_file['channel1']['active'] == False:
                    self.noCamera.emit(True,1)
                    self.totalfall.emit(0,0,1)
            except:
                pass
            

            if self.ready== True and self.detect == True and self.config_file['channel1']['active'] == True:
                self.img=cv2.resize(self.img,(640,640))
                coordinate = self.yolov7.predict(self.img)
                self.img = NewDraw(self.img, coordinate)
                # self.img = np.array([self.img])
                self.channel.setPixmap(self.img2pyqt(self.img, self.channel))
                self.ready = False
  



                

         
                        
                        
                    
                

            
