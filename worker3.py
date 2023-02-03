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
from coorutil import specific, drawBbox, openJson, timetoint



class Worker3(QObject):

    totalfall = QtCore.pyqtSignal(int,int,int)
    zoom_on = QtCore.pyqtSignal(bool, int)
    fall = QtCore.pyqtSignal(str, int)
    timenow = QtCore.pyqtSignal(str)
    koordinat = QtCore.pyqtSignal(np.ndarray,int)   
    config = QtCore.pyqtSignal(str,int) 
    noCamera = QtCore.pyqtSignal(bool, int)

    def openconfig(self):
        
        self.user = self.config_file['channel3']['user']
        self.ip = self.config_file['channel3']['ip']
        self.password = self.config_file['channel3']['password']
        
        self.cap = f"rtsp://{self.user}:{self.password}@{self.ip}/cam/realmonitor?channel=1&subtype=1"
        

        self.config.emit(self.cap,3)
        self.config_file['channel2']['change'] = False
            
        f = open('config2Channels.json', 'w')
        json.dump(self.config_file, f, indent=2)
        f.close()
        
        
    def prep(self):
        self.config_file = openJson('config2Channels.json')
        #self.openconfig()
        self.OCtrack = Trackker()
        self.ready = False
        self.OCtrack.preparation()
        
        self.findfall = Fallutil(3)
        self.detect = True
        self.total_people = []
            
    def ROI_prep(self,image,mask_output,output):
        cv2.imwrite(output, image)
        channel2_mask = np.zeros(image.shape, dtype=np.uint8)
        cv2.imwrite(mask_output,channel2_mask)
        return channel2_mask        
    
    def Jsonprep(self):
        self.fall_store = openJson('fall_store.json')
        self.function = openJson('function.json')
        self.ROI = openJson('AiSettings.json')
        self.config_file = openJson('config2Channels.json')
        self.personal = openJson('personal.json')
        self.zoom = openJson('zoom.json')
    
    def checkROI(self):
        f = open('AiSettings.json', 'r')
        data = json.load(f)
        f.close()
        
        if data['Camera3']['change'] == True:
            self.mask_person = cv2.imread('./ROI/Camera3/person.jpg')
            self.mask_fall = cv2.imread('./ROI/Camera3/fall_down.jpg')
            self.mask_PPE = cv2.imread('./ROI/Camera3/PPE.jpg')

            data['Camera3']['change'] = False
            
            f = open('AiSettings.json', 'w')
            json.dump(data, f, indent=2)
            f.close()      

    def checkMin(self):
        if self.config_file['channel3']['ROI'] == True:
            try:
                f = open('AiSettings.json', 'r')
                data = json.load(f)
                f.close()
            except:
                print('Failed to open AiSettings.json')
                print('Uusing factory reset')
            else:
                print('Open AiSettings sucess..')

            self.minWidth = data['Camera3']['Min']['width']
            self.minHeight = data['Camera3']['Min']['height']
            self.maxWidth = data['Camera3']['Max']['width']
            self.maxHeight = data['Camera3']['Max']['height']

        else:
            self.minWidth = None
            self.minHeight = None
            self.maxWidth = None
            self.maxHeight = None

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

    def run(self):
        self.prep()
        self.img = cv2.imread('NoCamera.png')
        while True:
            self.Jsonprep()
            self.checkROI()
            self.chekcMin()

            while self.berenti:
                time.sleep(0.1)

            if self.config_file['channel3']['change'] == True:
                self.openconfig()
            
            if self.ROI['Camera3']['Person'] == True:
                self.img = cv2.addWeighted(self.img,1,self.mask_person, 0.3,0)
            
            if self.ROI['Camera3']['FallDown'] == True:
                self.img = cv2.addWeighted(self.img,1, self.mask_fall,0.3,0)
            
            if self.ROI['Camera3']['PPE']['active'] == True:
                self.img = cv2.addWeighted(self.img, 1, self.mask_PPE, 0.3,0)


            if self.config_file['channel3']['active'] == False:
                self.noCamera.emit(True,3)
                self.totalfall.emit(0,0,3)

            elif self.ready== True and self.detect == True and self.config_file['channel2']['active'] == True:
                self.noCamera.emit(False,3)
                start = time.time()
                #print(type(self.img))	
                if self.ROI['Channel3']['active'] == True:
                    self.checkROI()
                    self.img = cv2.addWeighted(self.img, 1, self.mask_img, 0.3,0)

                coordinate,fall_coor = self.predictor.predict_image_2([self.img])
                person_coor = specific(coordinate, 0)
                person_coor = self.checkWH(person_coor)
                #self.koordinat.emit(person_coor)
                # track id set
                coor_track, deleted_id = self.OCtrack.tracking(person_coor, self.img)
                # 時間序列與偵測框斜率判斷
                for i in coor_track:
                    if i[0] not in list(self.predictor.timing_fall):
                        self.predictor.timing_fall[i[0]] = list()
                        for s in range(self.predictor.fps):
                            self.predictor.timing_fall[i[0]].append(0)
                    if [True] == self.predictor.attr_res["output"][coor_track.index(i)]:
                        self.predictor.timing_fall[i[0]][self.predictor.frame_id % self.predictor.fps] = 1
                    else:
                        self.predictor.timing_fall[i[0]][self.predictor.frame_id % self.predictor.fps] = 0
                    if sum(self.predictor.timing_fall[i[0]]) / self.predictor.fps < 0.7 or (coor_track[coor_track.index(i)][4]-coor_track[coor_track.index(i)][2])/(coor_track[coor_track.index(i)][3]-coor_track[coor_track.index(i)][1])>2:
                        self.predictor.attr_res['output'][coor_track.index(i)] = [False]
                        self.predictor.pipeline_res.update(self.predictor.attr_res, 'attr')
                    else:
                        self.predictor.attr_res['output'][coor_track.index(i)] = [True]
                        self.predictor.pipeline_res.update(self.predictor.attr_res, 'attr')

                _, fall_coor = self.predictor.visualize_image(self.predictor.pipeline_res)
                fall_coor = np.array(fall_coor)
                self.koordinat.emit(fall_coor,3)
                self.predictor.frame_id += 1

                filename, total_fall = self.findfall.final_fall(fall_coor,coor_track,self.img,3,self.ROI['Camera3']['active'],self.function['function']['light_delay']) #give self function
                self.img, total_peeps, self.total_people = drawBbox(self.img, coor_track, self.total_people,fall_coor)

                for file in filename:
                    self.fall.emit(file,3)
                try:
                    if self.zoom['Channel3'] == True:
                        self.zoom_on.emit(True,3)
                except:
                    pass

                #self.picdone.emit(self.img,1)
                self.totalfall.emit(total_fall,total_peeps,3)
                if time.time() - start > 0.0:
                    print("Paddle: ", ((time.time()-start)))
                self.ready = False
                


                

         
                        
                        
                    
                

            
