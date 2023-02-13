import sys
import cv2
import os
import shutil
import numpy as np
import pycuda.autoinit
import pycuda.driver as cuda
import json
import logging
import logging.handlers
import threading
# import RPi.GPIO as GPIO
import base64
from datetime import date,datetime

import time, json
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow,QWidget


from newtwochannel2 import Ui_MainWindowp
# from playsound import playsound
from components.falldownbox import Box
from clickablefall import InfoDetails
from allutility.utility import text, timetoint, setupLogin, toLog
from allutility.coorutil import openJson

from worker1 import Worker1
from allutility.httpUtil import get, post, getIpAddr
from VideoStream import WebcamVideoStream
from yolov7 import detect


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
        # self.cpBlanktoROI()

        self.InfoDetails = InfoDetails()
        self.yolov7 = detect()
        
        self.totalFall = 0

        self.layoutbig = 0
        self.screen = 0

        self.img = cv2.imread('NoCamera.png')
        self.ReconImg = cv2.imread('recon.png')
        setupLogin()
        
        self.box = [self.box1, self.box2, self.box3, self.box4, self.box5,
                    self.box6, self.box7, self.box8, self.box9, self.box10]

        self.tenFall = []

        self.setSynctoTime()
        
        self.startThread()

    def setSynctoTime(self):
        data = openJson('json/config2Channels.json', 'r')
        data['async']['last'] = time.strftime("%H:%M:%S")

        f = open('json/config2Channels.json', 'w')
        json.dump(data,f,indent=2)
        f.close()

    def cpBlanktoROI(self):
        onePath = '/home/nvidia/yolov7/ROI/Camera1/blank.jpg'
        Path1 = '/home/nvidia/yolov7/ROI/Camera1'
        shutil.copyfile(onePath, os.path.join(Path1, 'fall_down.jpg'))
        shutil.copyfile(onePath, os.path.join(Path1, 'person.jpg'))
        shutil.copyfile(onePath, os.path.join(Path1, 'PPE.jpg'))

        Path2 = '/home/nvidia/Desktop/fall_v.5_pp_API/ROI/Camera2'
        shutil.copyfile(onePath, os.path.join(Path2, 'fall_down.jpg'))
        shutil.copyfile(onePath, os.path.join(Path2, 'person.jpg'))
        shutil.copyfile(onePath, os.path.join(Path2, ' PPE.jpg'))

        Path3 = '/home/nvidia/Desktop/fall_v.5_pp_API/ROI/Camera3'
        shutil.copyfile(onePath, os.path.join(Path3, 'fall_down.jpg'))
        shutil.copyfile(onePath, os.path.join(Path3, 'person.jpg'))
        shutil.copyfile(onePath, os.path.join(Path3, ' PPE.jpg'))

        Path4 = '/home/nvidia/Desktop/fall_v.5_pp_API/ROI/Camera4'
        shutil.copyfile(onePath, os.path.join(Path4, 'fall_down.jpg'))
        shutil.copyfile(onePath, os.path.join(Path4, 'person.jpg'))
        shutil.copyfile(onePath, os.path.join(Path4, ' PPE.jpg'))

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

    def startThread(self):
        
        self.makeThread1()

        self.makeDecoder1()
        self.makeDecoder2()
        self.makeDecoder3()
        self.makeDecoder4()

    def resumeThread(self):
        self.worker1.berenti = False
        pass

    def stopThread(self):
        self.worker1.berenti = True
        pass

    def details(self,filename):
        channel = filename[25]
        
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
        
        
        image_ss = filename
        image = filename
        date = data[filename]['date']
        time = data[filename]['time']
        channel = data[filename]['channel']
        type  = data[filename]['event']
        
        self.InfoDetails.showFullScreen()
        self.InfoDetails.input(image_ss,image,date,time,channel,type)
        self.InfoDetails.ui.back.clicked.connect(self.back2)
    
    # def sound(self): 
    #     playsound('voice/no_pass.mp3')

    # def GPIO(self):  
        
    #     GPIO.setmode(GPIO.BOARD)
    #     GPIO.setup(16, GPIO.OUT, initial = GPIO.HIGH)
    #     if self.light1:
    #         GPIO.output(16, GPIO.LOW)
    #     if self.gate1:
    #         GPIO.output(16, GPIO.LOW)
    #     time.sleep(self.lightDelay)
    #     if self.light1:
    #         GPIO.output(16, GPIO.HIGH)
    #     if self.gate1:
    #         GPIO.output(16, GPIO.HIGH)

    def GPIOon(self):
        tgpio = threading.Thread(target = self.GPIO)
        tgpio.start()
        tgpio.join()

    def Soundon(self):
        sound = threading.Thread(target = self.sound)
        sound.start()
        sound.join()

    def showFall(self,filename,channel):
        
        global SERVER_GIVE_TOKEN
        
        self.tenFall.append(filename)
        if len(self.tenFall) > 10:
            self.tenFall.pop()
        
        cut_add = './falldown/cut'
        ss_add = './falldown/screenshot'
        
        f = open('json/function.json', 'r')
        GPIOData = json.load(f)
        f.close()

        for index, filename in enumerate(self.tenFall):
            self.box[index].setMinimumSize(QtCore.QSize(150,200))
            self.box[index].label.setIcon(QtGui.QIcon(os.path.join(cut_add, (f"{filename}.jpg"))))
            self.box[index].label.setIconSize(QtCore.QSize(150,150))
            self.box[index].information.setText(text("Falldown", filename[9:17], filename[25]))
            self.box[index].label.clicked.connect(lambda _, text = filename : self.details(text))
        
        # if GPIOData['function'][self.camera] == True:
        #     self.Soundon()

        self.totalFall += 1
        self.labelNum.setText(f'<font color=red>{self.totalFall}</font> ')
        
        postData = self.toData(filename,cut_add, ss_add, data[filename]['event'])
        if post('http://192.168.0.107/api/v2/captures/fallDown', json.dumps(postData), None, SERVER_GIVE_TOKEN) != 200:
            f = open('json/InternetProb.json','r')
            inet = json.load(f)
            f.close()

            failData = {
                filename:postData
            }

            inet.update(failData)
            
            f = open('json/InternetProb.json','w')
            json.dump(inet,f,indent=2)
            f.close()

            toLog('Failed to upload Event to Server')

    def toData(self, filename, pathToCut, pathToSS,typeEvent,cid = 0):
        cid = int(filename.split("_")[2][-1])-1
        
        capture_at = round(time.time() * 1000.0)

        f = open('json/config2Channels.json','r')
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
        if channel == 1:
            self.worker1.Zoom1 = True
        elif channel == 2:
            self.worker1.Zoom2 = True
        elif channel == 3:
            self.worker1.Zoom3 = True
        elif channel == 4:
            self.worker1.Zoom4 = True
                
    def back(self):
        self.worker1.Zoom1 = False
        self.worker1.Zoom2 = False
        self.worker1.Zoom3 = False
        self.worker1.Zoom4 = False
        
    def back2(self):
        self.InfoDetails.close()
    
    def img2pyqt(self,img,label):
        '''
        convert the opencv format to pyqt format color
        '''
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        temp = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1]*3, QtGui.QImage.Format_RGB888)
        return QtGui.QPixmap.fromImage(temp).scaled(label.width(), label.height())

    def writeFall(self, channel):
        camera = ['Camera 1', 'Camera 2', 'Camera 3', 'Camera 4']
        
        self.label_6.setText(f'{camera[channel]} : <font color = red>跌倒</font>/總人數：')
        self.label.setText(f'{self.worker1.total_people[channel][0]}<font color=white> / {self.worker1.total_people[channel][1]}</font>')
        
    def imgToBase64(self,image):
        with open(image, "rb") as image2string:
            converted_string = base64.b64encode(image2string.read())
            
        return converted_string
         
    def stringToTime(self,data):
        starttime = datetime.strptime(data['starttime1'],'%H:%M') 
        endtime = datetime.strptime(data['endtime1'], '%H:%M')
        
        return starttime, endtime    
         
    def checkDetect(self, time):

        data = openJson('json/timeTable.json','r')

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

    def getAPI(self,timeNow,tanggal):
        toLog("Sync Settings with Server")
                
        SERVER_GIVE_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiZmFjZWFpIl0sInNjb3BlIjpbImFwaS1zZXJ2aWNlIl0sImV4cCI6MTkyMTE1MzI1OCwiYXV0aG9yaXRpZXMiOlsiYWl1bmlvbiJdLCJqdGkiOiI3ODI3YTBkYi0zMGQ3LTRhODItYjQyYy0yMTQ0NTMyZWRlNDEiLCJjbGllbnRfaWQiOiJhcGktY2xpZW50In0.mE8WnaGzVuWhS5LfT0ajQcBr_JP2TUOVfhch-5dJ6mA'
        dataAPI = get('http://192.168.0.107/devices', 'deviceType=aibox&sourceUrl='+getIpAddr('192.168.0.10'), SERVER_GIVE_TOKEN)
        
        if len(dataAPI) == 0:
            toLog('Fail to Sync with server')
            return
        
        data = openJson('json/config2Channels.json','r')

        data['deviceID'] = dataAPI['result'][0]['id']

        camera1API = dataAPI['result'][0]['settings']['camera'][0]

        data['channel1']['ip'] = camera1API['ip']
        data['channel1']['place'] = camera1API['title']
        data['channel1']['user'] = camera1API['username']
        data['channel1']['password'] = camera1API['password']
        data['channel1']['active'] = camera1API['active']
        data['channel1']['ROI'] = camera1API['ROI']
        data['channel1']['change'] = True

        camera2API = dataAPI['result'][0]['settings']['camera'][1]

        data['channel2']['ip'] = camera2API['ip']
        data['channel2']['place'] = camera2API['title']
        data['channel2']['user'] = camera2API['username']
        data['channel2']['active'] = camera2API['active']
        data['channel2']['password'] = camera2API['password']
        data['channel2']['ROI'] = camera2API['ROI']
        data['channel2']['change'] = True

        camera3API = dataAPI['result'][0]['settings']['camera'][2]
        
        data['channel3']['ip'] = camera3API['ip']
        data['channel3']['place'] = camera3API['title']
        data['channel3']['user'] = camera3API['username']
        data['channel3']['active'] = camera3API['active']
        data['channel3']['password'] = camera3API['password']
        data['channel3']['ROI'] = camera3API['ROI']
        data['channel3']['change'] = True

        camera4API = dataAPI['result'][0]['settings']['camera'][3]

        data['channel4']['ip'] = camera4API['ip']
        data['channel4']['place'] = camera4API['title']
        data['channel4']['user'] = camera4API['username']
        data['channel4']['active'] = camera4API['active']
        data['channel4']['password'] = camera4API['password']
        data['channel4']['ROI'] = camera4API['ROI']
        data['channel4']['change'] = True

        data['async']['last'] = timeNow 
        data['async']['date'] = tanggal

        timeJSon = dataAPI['result'][0]['settings']['Time-Table']

        f = open('json/config2Channels.json', 'w')
        json.dump(data,f,indent=2)
        f.close()

        self.lastSync.setText(timeNow)

        f = open('json/timeTable.json', 'w')
        json.dump(timeJSon, f,indent=2)
        f.close()

    def asyncAPI(self,timeNow):
        try:
            data = openJson('json/config2Channels.json')
        except:
            return
        tanggal = timeNow[:10]
        timeNow = timeNow[-8:]
        if data['async']['enable'] == True:
            nowTime = timetoint(int(timeNow[:2]),int(timeNow[3:5]), int(timeNow[-2:]))
            lastSync = timetoint(int(data['async']['last'][:2]), int(data['async']['last'][3:5]), int(data['async']['last'][-2:]))
            cycleSync = timetoint(0,int(data['async']['time']),0)
            
            if nowTime - lastSync > cycleSync or nowTime - lastSync < 0:
                self.getAPI(timeNow,tanggal)
    
    def toImg(self, image):
        self.worker1.img1 = image
        self.worker1.recon1 = False
            
    def toImg2(self,image):
        self.worker1.img2 = image
        self.worker1.recon2 = False
            
    def toImg3(self,image):
        self.worker1.img3 = image
        self.worker1.recon3 = False

    def toImg4(self,image):
        self.worker1.img4 = image
        self.worker1.recon4 = False
  
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
                if channel == 1:
                    self.worker1.img1 = self.ReconImg
                    self.worker1.recon1 = True
                elif channel == 2:
                    self.worker1.img2 = self.ReconImg
                    self.worker1.recon2 = True
                elif channel == 3:
                    self.worker1.img3 = self.ReconImg
                    self.worker1.recon3 = True
                else:
                    self.worker1.img4 = self.ReconImg
                    self.worker1.recon4 = True

    def makeDecoder1(self): 
        self.threadImg = QtCore.QThread()
        self.worker = WebcamVideoStream()
        self.worker.channel = 1
        self.worker.change = False
        self.worker.moveToThread(self.threadImg)
        
        data = openJson('json/config2Channels.json')

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
 
        data = openJson('json/config2Channels.json')

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
        self.videoStream3.change = False
        self.videoStream3.moveToThread(self.threadImg3)
 
        data = openJson('json/config2Channels.json')

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
        self.videoStream4.change = False
        self.videoStream4.moveToThread(self.threadImg4)
    
        data = openJson('json/config2Channels.json')

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

    def makeThread1(self):
        
        self.thread1 = QtCore.QThread()
        self.worker1 = Worker1()
        self.worker1.moveToThread(self.thread1)
        
        self.thread1.started.connect(self.worker1.run)
        self.worker1.channel1 = self.lchannel1
        self.worker1.channel2 = self.lchannel2
        self.worker1.channel3 = self.lchannel3
        self.worker1.channel4 = self.lchannel4
        
        self.worker1.Zoom1 = False
        self.worker1.Zoom2 = False
        self.worker1.Zoom3 = False
        self.worker1.Zoom4 = False
        
        self.worker1.yolov7 = self.yolov7
        self.worker1.berenti = False
        self.worker1.timenow.connect(self.writetime)
        self.worker1.config.connect(self.changeIP)
        self.worker1.fall.connect(self.showFall)
        
        self.thread1.start()

    def writetime(self, time_now):
        data = openJson('json/function.json')
        self.time.setText(time_now)

        if time_now[-8:-3] == data['function']['counter_reset']:
            self.reset()
        
        # self.asyncAPI(time_now)
        # self.rePost(self)
        # self.checkDetect(time_now)
        
    def rePost(self):
        inet = openJson('json/InternetProb.json','r')

        if len(inet) == 0:
            return
        
        for i in inet:
            if post('http://192.168.0.107/api/v2/captures/fallDown', json.dumps(inet[i]), None, SERVER_GIVE_TOKEN) != 200:
                return
            
        inet = {}
        f = open('json/InternetProb.json','w')
        json.dump(inet,f,indent=2)
        f.close()
           
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = TwoScreen()
    ui.showFullScreen()
    sys.exit(app.exec_())       
