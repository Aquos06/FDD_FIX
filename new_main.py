import sys
import cv2
import os
import shutil
import numpy as np
import pycuda.autoinit
import pycuda.driver as cuda
import tensorrt as trty
import json
import logging
import logging.handlers
import threading
import RPi.GPIO as GPIO
import base64
from datetime import date,datetime

from os import stat
from glob import glob
import time, json
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow,QWidget


from newtwochannel2 import Ui_MainWindowp
from playsound import playsound
from ZoomScreen.biggerscreen import biggerScreen
from components.falldownbox import Box
from clickablefall import InfoDetails
from pp_deploy.pipeline import pipeline
from utility import text, timetoint, setupLogin, toLog

from worker1 import Worker1
from worker2  import Worker2
from worker3 import Worker3
from worker4 import Worker4
from yoloEngine import yolov5_engine
from coorutil import drawBbox
from httpUtil import get, post, getIpAddr
from VideoStream import WebcamVideoStream
from allutility.updateTime import UpdateTime


#HYPER PARAMS
SERVER_GIVE_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiZmFjZWFpIl0sInNjb3BlIjpbImFwaS1zZXJ2aWNlIl0sImV4cCI6MTkyMTE1MzI1OCwiYXV0aG9yaXRpZXMiOlsiYWl1bmlvbiJdLCJqdGkiOiI3ODI3YTBkYi0zMGQ3LTRhODItYjQyYy0yMTQ0NTMyZWRlNDEiLCJjbGllbnRfaWQiOiJhcGktY2xpZW50In0.mE8WnaGzVuWhS5LfT0ajQcBr_JP2TUOVfhch-5dJ6mA'

'''
logging file
'''
logging.basicConfig(
    filename='mask_debug.log',
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

#make function to clear the ROI

class TwoScreen(QMainWindow, Ui_MainWindowp):
    def __init__(self,mainwindow):
        QMainWindow.__init__(self)
        Ui_MainWindowp.__init__(self)
        
        self.setupUi(mainwindow)
        self.cpBlanktoROI()

        self.InfoDetails = InfoDetails()
        
        self.zoom_channel = 0
        self.totalFall = [0,0,0,0]
        self.totalPerson = [0,0,0,0]  

        self.PCoor =[[],[],[],[]]
        self.zoom = [False,False,False,False]
        self.flag = [False,False,False,False]

        self.layoutbig = 0
        self.screen = 0

        self.img = cv2.imread('NoCamera.png')
        setupLogin()
        
        self.bg = cv2.imread('bg.jpg')

        # # pp model for 1 import
        # self.predictor1 = pipeline.PipePredictor()
        # # pp model for 2 import
        # self.predictor2 = pipeline.PipePredictor()

        self.setSynctoTime()
        
        self.tempJsonClear()        
        self.startThread()

    def setSynctoTime(self):
        f = open('config2Channels.json','r')
        data = json.load(f)
        f.close()

        data['async']['last'] = time.strftime("%H:%M:%S")

        f = open('config2Channels.json', 'w')
        json.dump(data,f,indent=2)
        f.close()

    def cpBlanktoROI(self):
        onePath = '/home/nvidia/Desktop/fall_v.5_pp_API/ROI/Camera1/blank.jpg'
        Path1 = '/home/nvidia/Desktop/fall_v.5_pp_API/ROI/Camera1'
        shutil.copyfile(onePath, os.path.join(Path1, 'fall_down.jpg'))
        shutil.copyfile(onePath, os.path.join(Path1, 'person.jpg'))
        shutil.copyfile(onePath, os.path.join(Path1, 'PPE.jpg'))

        Path2 = '/home/nvidia/Desktop/fall_v.5_pp_API/ROI/Camera2'
        shutil.copyfile(onePath, os.path.join(Path2, 'fall_down.jpg'))
        shutil.copyfile(onePath, os.path.join(Path2, 'person.jpg'))
        shutil.copyfile(onePath, os.path.join(Path2, ' PPE.jpg'))

    def deleteItemsOfLayout(self,layout):
     if layout is not None:
         while layout.count():
             item = layout.takeAt(0)
             widget = item.widget()
             if widget is not None:
                 widget.deleteLater()
             else:
                self.deleteItemsOfLayout(item.layout())

    def reset(self):
        self.tempJsonClear()
        
        for i in range(self.layout.count()):
            layout = self.layout.itemAt(i)
            self.deleteItemsOfLayout(layout.layout())
            self.layout.removeItem(layout)
            layout.deleteLater()

    def tempJsonClear(self):
        data = {}
        f = open('./temp_falldown/fall_store.json', 'w')
        json.dump(data,f,indent=2)
        f.close()
    
        f = open('./temp_falldown/fall_store2.json', 'w')
        json.dump(data,f,indent=2)
        f.close()
        
        f = open('./temp_falldown/fall_store3.json', 'w')
        json.dump(data,f,indent=2)
        f.close()
        
        f = open('./temp_falldown/fall_store4.json', 'w')
        json.dump(data,f,indent=2)
        f.close()

        data = {
            "Channel1": False,
            "Channel2": False,
            "Channel3": False,
            "Channel4": False
}
        f = open('zoom.json','w')
        json.dump(data,f,indent=2)
        f.close()
    
    def startThread(self):
        
        self.makeThread1()
        self.makeThread2()
        # self.makeThread3()
        # self.makeThread4()

        self.makeDecoder1()
        self.makeDecoder2()
        # self.makeDecoder3()
        # self.makeDecoder4()

    def resumeThread(self):
        self.worker1.berenti = False
        self.worker2.berenti = False
        # self.worker3.berenti = False
        # self.worker4.berenti = False
        
    def stopThread(self):
        
        self.worker1.berenti = True
        self.worker2.berenti = True
        # self.worker3.berenti = True
        # self.worker4.berenti = True

    def details(self,filename):
        channel = filename[23]
        self.stopThread()
        
        if channel == str(1):
            f = open('./falldown/all_falldown.json', 'r')
        elif channel == str(2):
            f = open('./falldown/all_falldown2.json', 'r')
        elif channel == str(3):
            f = open('./falldown/all_falldown3.json', 'r')
        elif channel == str(4):
            f = open('./falldown/all_falldown4.json', 'r')
        
        data = json.load(f)
        f.close()
        
        self.resumeThread()
        
        image_ss = filename
        image = filename
        date = data[filename]['date']
        time = data[filename]['time']
        channel = data[filename]['channel']
        type  = data[filename]['event']
        
        self.InfoDetails.showFullScreen()
        self.InfoDetails.input(image_ss,image,date,time,channel,type)
        self.InfoDetails.ui.back.clicked.connect(self.back2)
    
    def sound(self): 
        playsound('voice/no_pass.mp3')

    def GPIO(self):  
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(16, GPIO.OUT, initial = GPIO.HIGH)
        if self.light1:
            GPIO.output(16, GPIO.LOW)
        if self.gate1:
            GPIO.output(16, GPIO.LOW)
        time.sleep(self.lightDelay)
        if self.light1:
            GPIO.output(16, GPIO.HIGH)
        if self.gate1:
            GPIO.output(16, GPIO.HIGH)

    def GPIOon(self):
        tgpio = threading.Thread(target = self.GPIO)
        tgpio.start()
        tgpio.join()

    def Soundon(self):
        sound = threading.Thread(target = self.sound)
        sound.start()
        sound.join()

    def showFall(self,filename,channel):
        self.stopThread()
        
        global SERVER_GIVE_TOKEN
        
        if channel == 1:
            f = open('./falldown/all_falldown.json', 'r')
            self.camera = 'Camera1'
        elif channel == 2:
            f = open('./falldown/all_falldown2.json', 'r')
            self.camera = 'Camera2'
        elif channel == 3:
            f = open('./falldown/all_falldown3.json', 'r')
            self.camera = 'Camera3'
        elif channel == 4:
            f = open('./falldown/all_falldown4.json', 'r')
            self.camera = 'Camera4'
        
        cut_add = './falldown/cut'
        ss_add = './falldown/screenshot'
        
        data = json.load(f)
        f.close()
        
        self.resumeThread()

        f = open('function.json', 'r')
        GPIOData = json.load(f)
        f.close()

        path = './falldown/cut'
        
        vertical = QtWidgets.QVBoxLayout()
        vertical.setSpacing(0)
        box = Box()
        box.setMinimumSize(QtCore.QSize(150,200))
        vertical.addWidget(box)
        box.label.setIcon(QtGui.QIcon(os.path.join(path, (f"{filename}.jpg"))))
        box.label.setIconSize(QtCore.QSize(150,150))
        box.information.setText(text(data[filename]['event'], data[filename]['time'], data[filename]['channel']))
        box.label.clicked.connect(lambda _, text = filename : self.details(text))
        
        if GPIOData['function'][self.camera] == True:
            self.Soundon()

        vertical.setStretch(0,10)
        
        self.layout.insertLayout(0,vertical)

        f = open('zoom.json','r')
        datazoom = json.load(f)
        f.close()
        
        for i in datazoom:
            if datazoom[i] == True:
                self.layoutbig.insertLayout(0,vertical)
        
        postData = self.toData(filename,cut_add, ss_add, data[filename]['event'])
        post('http://192.168.0.107/api/v2/captures/fallDown', json.dumps(postData), None, SERVER_GIVE_TOKEN)
        
    def toData(self, filename, pathToCut, pathToSS,typeEvent,cid = 0):
        cid = int(filename.split("_")[2][-1])-1
        
        capture_at = round(time.time() * 1000.0)

        f = open('config2Channels.json','r')
        data = json.load(f)
        f.close()
     
        deviceID = data['deviceID']
       
        filename += ".jpg" 
        print(deviceID)        

        photo       = os.path.join(pathToCut,filename)
        background = os.path.join(pathToSS,filename)
        
        photo = self.imgToBase64(photo)
        background = self.imgToBase64(background)
        
        data = {
            'deviceId': deviceID,
            'cid'     : cid,
            'captured_at': capture_at,
            'type': "falldown",
            'photo': photo.decode('utf-8'),
            'background': background.decode('utf-8'),
        }
        
        
        return data
    
    def zoom_show(self,channel):        
        self.stopThread()
        f = open('zoom.json', 'r')
        zoom_json = json.load(f)
        f.close()
        
        if channel == 1:
            self.zoom[0] = True
            zoom_json['Channel1'] = True
        elif channel == 2:
            self.zoom[1] = True
            zoom_json['Channel2'] = True
        elif channel == 3:
            self.zoom[2] = True
            zoom_json['Channel3'] = True
        elif channel == 4:
            self.zoom[3] = True
            zoom_json['Channel4'] = True

        f = open('zoom.json', 'w')
        json.dump(zoom_json, f, indent= 2)
        f.close()
        self.resumeThread()
                
    def back(self):
        self.stopThread()
        f = open('zoom.json', 'r')
        zoom_json = json.load(f)
        f.close()
        
        for index,i in enumerate(zoom_json):
            zoom_json[i] = False
            self.zoom[index] = False

        f = open('zoom.json', 'w')
        json.dump(zoom_json, f, indent=2)
        f.close()
        self.resumeThread()
        
    def back2(self):
        self.InfoDetails.close()
        
    def openJson(self,file):
        
        f = open(file,'r')
        data = json.load(f)
        f.close()
        
        
        return data
    
    def img2pyqt(self,img,label):
        '''
        convert the opencv format to pyqt format color
        '''
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        temp = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1]*3, QtGui.QImage.Format_RGB888)
        return QtGui.QPixmap.fromImage(temp).scaled(label.width(), label.height())
    
    def show(self,img, channel): 
        if channel == 1:
            try:
                if self.worker1.config_file['channel1']['ROI'] == True:
                    if self.worker1.ROI['Camera1']['FallDown'] == True:
                        self.worker1.mask_fall = cv2.resize(self.worker1.mask_fall,(img.shape[1],img.shape[0]), interpolation = cv2.INTER_AREA)
                        img = cv2.addWeighted(img,1, self.worker1.mask_fall,0.3,0)    
            except:
                pass
            if self.zoom[0] == True:
                try:
                    self.screen.setPixmap(self.img2pyqt(img,self.screen))
                except:
                    self.lchannel1.setPixmap(self.img2pyqt(img, self.lchannel1))
            else:
                self.lchannel1.setPixmap(self.img2pyqt(img,self.lchannel1))

        elif channel == 2:
            try:
                if self.worker2.config_file['channel2']['ROI'] == True:
                    if self.worker2.ROI['Camera2']['FallDown'] == True:
                        self.worker2.mask_fall = cv2.resize(self.worker2.mask_fall, (img.shape[1], img.shape[0]), interpolation = cv2.INTER_AREA)
                        img = cv2.addWeighted(img,1, self.worker2.mask_fall, 0.3, 0)
            except:
                pass
            if self.zoom[1] == True:
                try:
                    self.screen.setPixmap(self.img2pyqt(img,self.screen))
                except:
                    self.lchannel2.setPixmap(self.img2pyqt(img, self.lchannel2))
            else:
                self.lchannel2.setPixmap(self.img2pyqt(img,self.lchannel2))

        elif channel == 3:
            if self.zoom[2] == True:
                self.screen.setPixmap(self.img2pyqt(img,self.screen))
            else:
                self.lchannel3.setPixmap(self.img2pyqt(img,self.lchannel3))
        else:
            if self.zoom[3] == True:
                self.screen.setPixmap(self.img2pyqt(img,self.screen))
            else:
                self.lchannel4.setPixmap(self.img2pyqt(img,self.lchannel4))

    def writelabel(self, fall, people,channel):
        
        if channel == 1:
            # self.label.setText(f"{fall}<font color=white> / {people}</font>")
            self.totalFall[0] = fall
            self.totalPerson[0] = people

        elif channel ==2 :
            # self.label_7.setText(f"{fall}<font color=white> / {people}</font>")
            self.totalFall[1] = fall
            self.totalPerson[1] = people

        elif channel == 3:
            # self.label_4.setText(f"{fall}<font color=white> / {people}</font>")
            self.totalFall[2] = fall
            self.totalPerson[2] = people

        else:
            # self.label_13.setText(f"{fall}<font color=white> / {people}</font>")
            self.totalFall[3] = fall
            self.totalPerson[3] = people

        self.labelNum.setText(f"<font color = red>{sum(self.totalFall)}</font> / {sum(self.totalPerson)}")

    def writeFall(self, channel):
        camera = ['Camera 1', 'Camera 2', 'Camera 3', 'Camera 4']
        
        self.label_6.setText(f'{camera[channel]} : <font color = red>跌倒</font>/總人數：')
        self.label.setText(f'{self.totalFall[channel]}<font color=white> / {self.totalPerson[channel]}</font>')
        
    def imgToBase64(self,image):
        with open(image, "rb") as image2string:
            converted_string = base64.b64encode(image2string.read())
            
        return converted_string
         
    def stringToTime(self,data):
        starttime = datetime.strptime(data['starttime1'],'%H:%M') 
        endtime = datetime.strptime(data['endtime1'], '%H:%M')
        
        return starttime, endtime    
         
    def checkDetect(self, time):

        f= open('json/timeTable.json', 'r')
        data = json.load(f)
        f.close()

        hourNow = datetime.now().strftime('%H')
        hourNow = datetime.strptime(hourNow,'%H')
        hourNow = int(str(hourNow.time())[:2])

        todayDay = datetime.today().strftime('%A')
        if data[todayDay]['Camera1']['all'] == True:
            self.worker1.detect = True
        else:
            if data[todayDay]['Camera1']['hour'][hourNow] == 1:
                self.worker1.detect = True
            else:
                self.worker1.detect = False

        if data[todayDay]['Camera2']['all'] == True:
            self.worker2.detect = True
        else:
            if data[todayDay]['Camera2']['hour'][hourNow] == 1:
                self.worker2.detect = True
            else:
                self.worker2.detect = False

    def passtozoom(self,img, channel):
        if channel == 1:
            self.zoom[0] = img
        elif channel == 2:
            self.zoom[1] = img
        elif channel == 3:
            self.zoom[2] = img
        elif channel == 4:
            self.zoom[3] = img

    def getAPI(self,timeNow,tanggal):
        toLog("Sync Settings with Server")
                
        SERVER_GIVE_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiZmFjZWFpIl0sInNjb3BlIjpbImFwaS1zZXJ2aWNlIl0sImV4cCI6MTkyMTE1MzI1OCwiYXV0aG9yaXRpZXMiOlsiYWl1bmlvbiJdLCJqdGkiOiI3ODI3YTBkYi0zMGQ3LTRhODItYjQyYy0yMTQ0NTMyZWRlNDEiLCJjbGllbnRfaWQiOiJhcGktY2xpZW50In0.mE8WnaGzVuWhS5LfT0ajQcBr_JP2TUOVfhch-5dJ6mA'
        dataAPI = get('http://192.168.0.107/devices', 'deviceType=aibox&sourceUrl='+getIpAddr('192.168.0.10'), SERVER_GIVE_TOKEN)
        self.stopThread()
        f = open('config2Channels.json', 'r')
        data = json.load(f)
        f.close()
        self.resumeThread()

        data['deviceID'] = dataAPI['result'][0]['id']

        camera1API = dataAPI['result'][0]['settings']['camera'][0]

        data['channel1']['ip'] = camera1API['ip']
        data['channel1']['place'] = camera1API['title']
        data['channel1']['user'] = camera1API['username']
        data['channel1']['password'] = camera1API['password']
        # data['channel1']['active'] = camera1API['active']
        # data['channel1']['ROI'] = camera1API['ROI']
        # data['channel1']['change'] = True

        camera2API = dataAPI['result'][0]['settings']['camera'][1]

        data['channel2']['ip'] = camera2API['ip']
        data['channel2']['place'] = camera2API['title']
        data['channel2']['user'] = camera2API['username']
        # data['channel2']['active'] = camera2API['active']
        data['channel2']['password'] = camera2API['password']
        # data['channel2']['ROI'] = camera2API['ROI']
        # data['channel2']['change'] = True

        data['async']['last'] = timeNow 
        data['async']['date'] = tanggal

        # ROIcoor = dataAPI['result'][0]['settings']['ROI']
        # timeJSon = dataAPI['result'][0]['settings']['timeTable']

        self.stopThread()
        f = open('config2Channels.json', 'w')
        json.dump(data,f,indent=2)
        f.close()
        self.resumeThread()

        self.lastSync.setText(timeNow)

        # f = open('output/loggin.json','r')
        # json.dump(ROIcoor,f,indent=2)
        # f.close()

        # f = open('json/timeTable.json', 'r')
        # json.dump(timeJSon, f,indent=2)
        # f.close()

    def asyncAPI(self,timeNow):
        self.stopThread()
        try:
            f = open('config2Channels.json', 'r')
            data = json.load(f)
            f.close()
        except:
            return
        self.resumeThread()
        tanggal = timeNow[:10]
        timeNow = timeNow[-8:]
        if data['async']['enable'] == True:
            nowTime = timetoint(int(timeNow[:2]),int(timeNow[3:5]), int(timeNow[-2:]))
            lastSync = timetoint(int(data['async']['last'][:2]), int(data['async']['last'][3:5]), int(data['async']['last'][-2:]))
            cycleSync = timetoint(0,int(data['async']['time']),0)
            
            if nowTime - lastSync > cycleSync or nowTime - lastSync < 0:
                self.getAPI(timeNow,tanggal)
    
    def toImg(self, image):
        if self.worker1.ready == False:  
            self.worker1.img = image
            self.worker1.ready = True
        # self.ROI1.setPixmap(self.img2pyqt(image,self.ROI1))
        # img,_,_ = drawBbox(image,self.PCoor[0], [], [])
        # if not self.flag[0]:
            # self.show(img,1)

    def toImg2(self,image):
        if self.worker2.ready == False:
            self.worker2.img = image
            self.worker2.ready = True
        self.ROI2.setPixmap(self.img2pyqt(image, self.ROI2))
        img,_,_ = drawBbox(image,self.PCoor[1], [],[])
        if not self.flag[1]:
            self.show(img,2)

    def toImg3(self,image):
        if self.worker3.ready == False:
            self.worker3.img = image
            self.worker3.ready = True
        img,_,_ = drawBbox(image,self.PCoor[2], [],[])
        if not self.flag[2]:
            self.show(img,3)

    def toImg4(self,image):
        if self.worker4.ready == False:
            self.worker4.img = image
            self.worker4.ready = True
        img,_,_ = drawBbox(image,self.PCoor[3], [],[])
        if not self.flag[3]:
            self.show(img,4)
  
    def reconnecting(self, hai,channel):
        if not hai:
            if channel == 1:
                camera = 'channel1'
            elif channel == 2:
                camera = 'channel2'
            elif channel == 3:
                camera = 'channel3'
            else:
                camera = 'channel4'
            if self.worker1.config_file[camera]['active'] == True:
                img = cv2.imread('recon.png')
                self.show(img,channel)

    def coorToImg(self, personCoor, channel):
        if channel == 1:
            self.PCoor[0] = personCoor
        elif channel == 2:
            self.PCoor[1] = personCoor
        elif channel == 3:
            self.PCoor[2] = personCoor
        else:
            self.PCoor[3] = personCoor

    def makeDecoder1(self): 
        self.threadImg = QtCore.QThread()
        self.worker = WebcamVideoStream()
        self.worker.channel = 1
        self.worker.change = False
        self.worker.moveToThread(self.threadImg)
        
        f = open('config2Channels.json' , 'r')
        data = json.load(f)
        f.close()

        src = f"rtsp://{data['channel1']['user']}:{data['channel1']['password']}@{data['channel1']['ip']}"

        self.worker.src= src        

        self.threadImg.started.connect(self.worker.run)
        self.worker.picdone.connect(self.toImg)
        self.worker.ret.connect(self.reconnecting)
        self.threadImg.start()    

    def makeDecoder2(self):
        self.threadImg2 = QtCore.QThread()
        self.videoStream = WebcamVideoStream()
        self.videoStream.channel = 2
        self.videoStream.change = False
        self.videoStream.moveToThread(self.threadImg2)
 
        f = open('config2Channels.json', 'r')
        data = json.load(f)
        f.close()

        src = f"rtsp://{data['channel2']['user']}:{data['channel2']['password']}@{data['channel2']['ip']}"

        self.videoStream.src = src

        self.threadImg2.started.connect(self.videoStream.run)
        self.videoStream.picdone.connect(self.toImg2)
        self.videoStream.ret.connect(self.reconnecting)
        self.threadImg2.start()

    def makeDecoder3(self):
        self.threadImg3 = QtCore.QThread()
        self.videoStream3 = WebcamVideoStream()
        self.videoStream3.channel = 3
        self.videoStream3.moveToThread(self.threadImg3)
 
        f = open('config2Channels.json', 'r')
        data = json.load(f)
        f.close()

        src = f"rtsp://{data['channel3']['user']}:{data['channel3']['password']}@{data['channel3']['ip']}"

        self.videoStream3.src = src

        self.threadImg3.started.connect(self.videoStream3.run)
        self.videoStream3.picdone.connect(self.toImg3)
        self.videoStream3.ret.connect(self.reconnecting)
        self.threadImg3.start()

    def makeDecoder4(self):
        self.threadImg4 = QtCore.QThread()
        self.videoStream4 = WebcamVideoStream()
        self.videoStream4.channel = 4
        self.videoStream4.moveToThread(self.threadImg4)
 
        f = open('config2Channels.json', 'r')
        data = json.load(f)
        f.close()

        src = f"rtsp://{data['channel4']['user']}:{data['channel4']['password']}@{data['channel4']['ip']}"

        self.videoStream4.src = src

        self.threadImg4.started.connect(self.videoStream4.run)
        self.videoStream4.picdone.connect(self.toImg4)
        self.videoStream4.ret.connect(self.reconnecting)
        self.threadImg4.start()
 
    def changeIP(self,uri,channel):
        if channel == 1:
            self.worker.src= uri
            self.worker.change = True
        elif channel == 2:
            self.videoStream.src = uri
            self.videoStream.change = True
        elif channel == 3:
            self.videoStream3.streamFunc(uri)
        else:
            self.videoStream4.streamFunc(uri)

    def noCam(self, flag, channel):
        if channel == 1: 
            if flag :
                self.flag[0] = flag
                img = cv2.imread('NoCamera.png')
                self.show(img,1)
            else:
                self.flag[0] = flag
        elif channel == 2:
            if flag :
                self.flag[1] = flag
                img = cv2.imread('NoCamera.png')
                self.show(img,2)
            else:
                self.flag[1] = flag
        elif channel == 3:
            if flag:
                self.flag[2] = flag
                img = cv2.imread('NoCamera.png')
                self.show(img,3)
            else:
                self.flag[2] = flag
        else:
            if flag:
                self.flag[3] = flag
                img = cv2.imread('NoCamera.png')
                self.show(img,4)
            else:
                self.flag[3] = flag

    def makeThread1(self):
        
        self.thread1 = QtCore.QThread()
        self.worker1 = Worker1()
        self.worker1.moveToThread(self.thread1)
        
        # self.worker1.predictor = self.predictor1

        self.thread1.started.connect(self.worker1.run)
        self.worker1.ready = False
        self.worker1.berenti = False
        self.worker1.channel = self.lchannel1
        self.worker1.timenow.connect(self.writetime)
        self.worker1.noCamera.connect(self.noCam)
        self.worker1.totalfall.connect(self.writelabel)
        self.worker1.zoom_on.connect(self.passtozoom)
        self.worker1.config.connect(self.changeIP)
        self.worker1.koordinat.connect(self.coorToImg)
        self.worker1.fall.connect(self.showFall)
        
        self.thread1.start()

    def makeThread2(self):
        
        self.thread2 = QtCore.QThread()
        self.worker2 = Worker2()
        self.worker2.moveToThread(self.thread2)

        # self.worker2.predictor = self.predictor2        

        self.thread2.started.connect(self.worker2.run)
        self.worker2.noCamera.connect(self.noCam)
        self.worker2.ready = False
        self.worker2.berenti = False
        self.worker2.totalfall.connect(self.writelabel)
        self.worker2.config.connect(self.changeIP)
        self.worker2.koordinat.connect(self.coorToImg)
        self.worker2.fall.connect(self.showFall)
        
        self.thread2.start()

    def makeThread3(self):
        
        self.thread3 = QtCore.QThread()
        self.worker3 = Worker3()
        self.worker3.moveToThread(self.thread3)

        self.worker3.predictor = self.predictor3       

        self.thread3.started.connect(self.worker3.run)
        self.worker3.noCamera.connect(self.noCam)
        self.worker3.ready = False
        self.worker3.totalfall.connect(self.writelabel)
        self.worker3.zoom_on.connect(self.passtozoom)
        self.worker3.config.connect(self.changeIP)
        self.worker3.koordinat.connect(self.coorToImg)
        self.worker3.fall.connect(self.showFall)
        
        self.thread3.start()

    def makeThread4(self):
        
        self.thread4 = QtCore.QThread()
        self.worker4 = Worker4()
        self.worker4.moveToThread(self.thread4)
        self.worker4.ready=False
        self.worker4.predictor = self.predictor4     

        self.thread4.started.connect(self.worker2.run)
        self.worker4.noCamera.connect(self.noCam)
        self.worker4.totalfall.connect(self.writelabel)
        self.worker4.zoom_on.connect(self.passtozoom)
        self.worker4.config.connect(self.changeIP)
        self.worker4.koordinat.connect(self.coorToImg)
        self.worker4.fall.connect(self.showFall)
        
        self.thread4.start()
        
    def writetime(self, time_now):
        self.stopThread()
        f = open('function.json','r')
        data = json.load(f)
        f.close()
        self.resumeThread()
        self.time.setText(time_now)

        if time_now[-8:-3] == data['function']['counter_reset']:
            self.reset()
        
        self.asyncAPI(time_now)
        self.checkDetect(time_now)
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = TwoScreen()
    ui.showFullScreen()
    sys.exit(app.exec_())       
