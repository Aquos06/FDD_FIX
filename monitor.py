import sys
import cv2
import threading
import ctypes
import os
import shutil
import random
import numpy as np
import pycuda.autoinit
import pycuda.driver as cuda
import tensorrt as trty
import time
import json
import logging
import logging.handlers
import RPi.GPIO as GPIO
import base64,io
import torch

from os import stat
from glob import glob
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QImage , QPixmap
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt,QTimer
from newmonitor import Ui_MainWindowp
from yolov5_trt import YoLov5TRT
from logging.handlers import TimedRotatingFileHandler
from playsound import playsound
from datetime import datetime, timezone, timedelta
from shutil import move
from PIL import Image
from io import BytesIO
from torchvision import transforms

'''
hyper parameters
'''
CONF_THRESH = 0.5
IOU_THRESHOLD = 0.4
threadSound = 0
threadGPIO1   = 0
status = 0


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



def open_cam_rtsp(uri, width, height, latency,buffer_size):                         #connect 192.168.0.53 camera
    gst_str = ('rtspsrc tcp-timeout=2000000 location={} latency={} ! '
               'application/x-rtp, media=video ! queue ! decodebin ! '
               'nvvidconv ! '
               'video/x-raw, width=(int){}, height=(int){}, '
               'format=(string)BGRx ! '
               'videoconvert ! appsink max-buffers={} drop=true').format(uri, latency, width, height,buffer_size)
    return cv2.VideoCapture(gst_str, cv2.CAP_GSTREAMER)
    #return cv2.VideoCapture(uri)

def plot_one_box(x, im, color=(0,0,255), channel1=None, line_thickness=3):  
    '''
    plot the box
    '''
    tl = line_thickness or round(0.002 * (im.shape[0] + im.shape[1]) / 2) + 1  # line/font thickness
    c1, c2 = (int(x[0]), int(x[1])), (int(x[2]), int(x[3]))
    cv2.rectangle(im, c1, c2, color, thickness=tl, lineType=cv2.LINE_AA)
    if channel1:
        tf = max(tl - 1, 1)  # font thickness
        t_size = cv2.getTextSize(channel1, 0, fontScale=tl / 3, thickness=tf)[0]
        c2 = c1[0] + t_size[0], c1[1] - t_size[1] - 3
        cv2.rectangle(im, c1, c2, color, -1, cv2.LINE_AA)  # filled
        cv2.putText(im, channel1, (c1[0], c1[1] - 2), 0, tl / 3, [225, 255, 255], thickness=tf, lineType=cv2.LINE_AA)

def tensorrt_init(path):
    '''
    load the tensorRT model. First, we need to convert the model into lib and engine files.
    '''                                              
    ctypes.CDLL(os.path.join(path, 'libmyplugins.so'))
    return YoLov5TRT(os.path.join(path, 'best.engine'))



class detect_tensorrt():
    '''
    tensorrt function
    '''
    def __init__ (self,yolov5_wrapper):
        self.yolov5_wrapper = yolov5_wrapper
    def detect(self,img):
        batch_image_raw,bbox, use_time = self.yolov5_wrapper.infer([img])
        return batch_image_raw,bbox, use_time
    def destroy(self):
        self.yolov5_wrapper.destroy()

class OneScreen(QMainWindow,Ui_MainWindowp):                                    #open window
    def __init__(self): # mode: [0,all] , [1,mask] , [2,temperature]
        QMainWindow.__init__(self)
        Ui_MainWindowp.__init__(self) 
        timer = QTimer(self) 
        self.setupUi(self)
        # self.setup_control()
        self.run_config()
        self.setFunction()

        # set up roi
        global set_roi1
        self.set_roi1 = [[650,0],[1100,0],[650,720],[1100,720]]
        with open('ROIConfig2Channels_one.json') as f:
            json_from_file = json.load(f)
            self.set_roi1 = json_from_file['set_roi1']
            
        set_roi1 = [*self.set_roi1[0], *self.set_roi1[-1]] # [#, #, #, #]
        if (set_roi1[0] > set_roi1[2]): set_roi1[0], set_roi1[2] = set_roi1[2], set_roi1[0]
        if (set_roi1[1] > set_roi1[3]): set_roi1[1], set_roi1[3] = set_roi1[3], set_roi1[1]

        # mouse event
        self.current_index = 0
        self.hit_flag1 = False
        self.point_size = 8 if self.roi1 ==0 else 6
        self.mode1 = -1

        self.page_status1 = 0
        self.page1 = 0

        self.transforms = transforms.Compose([transforms.Resize((224,224)), transforms.ToTensor()])

    # def setup_control(self):
    #     self.clicked_counter = 0
    #     self.roistatus       = 0
    #     self.alarmstatus     = 0
    #     #self.roi.clicked.connect(self.roiClicked)
    #     self.alarm.clicked.connect(self.alarmClicked)
    #     self.pushButtonl.clicked.connect(self.Pushl1Clicked)
    #     self.pushButtonl_2.clicked.connect(self.Pushr1Clicked)

    # def roiClicked(self):
    #     self.clicked_counter += 1
    #     # print(f"you clicked {self.clicked_counter} times.")
    #     if self.roistatus == 0:
    #         self.roi1  = 0
    #         self.roistatus = 1
    #     else:
    #         self.roi1  = 1	
    #         self.roistatus = 0 
    # def alarmClicked(self):
    #     self.clicked_counter += 1
    #     # print(f"you clicked {self.clicked_counter} times.")
    #     if self.alarmstatus == 0:
    #         self.sounds  = 0
    #         self.alarmstatus = 1
    #     else:
    #         self.sounds  = 1
    #         self.alarmstatus = 0 

    # def Pushl1Clicked(self):
    #     global f1
    #     if self.page_status1 == 0:
    #         f1 = sorted(glob("./imgcapture/png/*channel1*.png"))
    #         self.page_status1 = 1  
    #     if self.page1 < len(f1):self.page1 += 3
    #     self.history(self.page1, f1, self.ulabel1, self.ulabel2, self.ulabel3, self.utime1, self.utime2, self.utime3, self.uicon1, self.uicon2, self.uicon3)

    # def Pushr1Clicked(self):
    #     global f1
    #     if self.page_status1 == 1:
    #         if self.page1 - 3 > 0:
    #             self.page1 -=3
    #             self.history(self.page1, f1, self.ulabel1, self.ulabel2, self.ulabel3, self.utime1, self.utime2, self.utime3, self.uicon1, self.uicon2, self.uicon3)
    #         else: 
    #             self.page_status1 = 0
    #             self.page1 = 0
    #             self.ulabel1.clear()
    #             self.ulabel2.clear()
    #             self.ulabel3.clear()
    #             self.utime1.clear()
    #             self.utime2.clear()
    #             self.utime3.clear()
    #             self.uicon1.clear()
    #             self.uicon2.clear()
    #             self.uicon3.clear()
            
    def run_config(self):
        path = "config2Channels.json"
        if os.path.isfile(path):
            self.cfg = self.read(path)
            self.channelSelect = self.cfg['channelSelect']
            self.ip1 = self.cfg['channel1']['ip']
            self.user1 = self.cfg['channel1']['user']
            self.password1 = self.cfg['channel1']['password']
            self.ip2 = self.cfg['channel2']['ip']
            self.user2 = self.cfg['channel2']['user']
            self.password2 = self.cfg['channel2']['password']
            self.storage = "test"
            self.width = self.cfg['utils']['width']
            self.height = self.cfg['utils']['height']
            self.storageMethod = self.cfg['utils']['storageMethod']
            self.usbPath = self.cfg['backup']['user_path']
            
            self.num_cap = 3 # number of capture images in the bottom of the monitor
            self.stopCapture = False
            self.ROItwoPoint = True

            self.model = torch.load('./ttest/falldown_stand_0614_300.pt')

            self.roi1 = False
                       
            # create initial directories
            # if not os.path.exists(self.usbPath): 
            #     os.makedirs(os.path.join(self.usbPath, 'png'))
            #     os.makedirs(os.path.join(self.usbPath, 'json'))
            if not os.path.exists(self.storage): 
                os.makedirs(os.path.join(self.storage, 'png'))
                os.makedirs(os.path.join(self.storage, 'json'))

        else:
            sys.exit()
    
    def setFunction(self):
        jsonData = self.read('function.json')
        self.lightDelay = jsonData['function']["light_delay"]
        self.counterReset = jsonData['function']["counter_reset"]
        self.GPIO = jsonData['function']["GPIO"]
        self.roi1 = jsonData['function']['roi1']
        self.roi2 = jsonData['function']['roi2']
        self.sounds = jsonData['function']['sound']

        self.selectRedHelmet = jsonData['Detection']['helmetColor']['Red']
        self.selectBlueHelmet = jsonData['Detection']['helmetColor']['Blue']
        self.selectYellowHelmet = jsonData['Detection']['helmetColor']['Yellow']
        self.selectWhiteHelmet = jsonData['Detection']['helmetColor']['White']

        self.helmetDetection = jsonData['Detection']['helmet']
        self.vestDetection = jsonData['Detection']['vest']
        currentDate = datetime.today().strftime('%A')
        self.startTime1 = jsonData['worktime'][currentDate]['starttime1']
        self.endTime1 = jsonData['worktime'][currentDate]['endtime1']
        self.startTime2 = jsonData['worktime'][currentDate]['starttime2']
        self.endTime2 = jsonData['worktime'][currentDate]['endtime2']

    def read(self,path):
        with open(path) as JSONfile:
            data = json.load(JSONfile)
            return data

    def test_submit(self, model, img):
        model.eval()    
        # img = Image.open(img_path).convert('RGB')
        img = self.transforms(img)
        img = img.to(torch.device('cuda'))
        img = img.unsqueeze(0)
        with torch.no_grad(): 
            output=model(img)
        pred = output.data.max(dim = 1, keepdim = True)[1]
        
        return pred

    def sound(self):
        '''
        sound function to alert user with a sound
        '''
        global threadSound
        global helmetStatus
        global vestStatus
        global helmetColor
        if self.sounds:
            if threadSound == 1:          
                if self.selectDetection(helmetStatus, vestStatus, helmetColor):
                    playsound('voice/pass.mp3')
                else: 
                    playsound('voice/no_pass.mp3')
                threadSound = 2 # double check
        
    def GPIOgate1(self):  
        '''
        function to alert the light and gate
        '''
        global threadGPIO1
        global helmetStatus
        global vestStatus
        global helmetColor
        
        if threadGPIO1 == 1:
            
            if not self.selectDetection(helmetStatus, vestStatus, helmetColor):
                GPIO.setmode(GPIO.BOARD)
                GPIO.setup(18, GPIO.OUT, initial = GPIO.HIGH)
                if self.light1:
                    GPIO.output(18, GPIO.LOW)
                    time.sleep(self.lightDelay)
                    GPIO.output(18, GPIO.HIGH)
            else:
                PIO.setmode(GPIO.BOARD)
                GPIO.setup(16, GPIO.OUT, initial = GPIO.HIGH)
                if self.light1:
                    GPIO.output(16, GPIO.LOW)
                    time.sleep(self.lightDelay)
                    GPIO.output(16, GPIO.HIGH)
            threadGPIO1 = 2
    
    def checkColor(self, helmetImage):
        '''
        HSV color detection
        '''
        hsv_frame = cv2.cvtColor(helmetImage, cv2.COLOR_BGR2HSV)
        pixel_center = hsv_frame[int(helmetImage.shape[0]/2), int(helmetImage.shape[1]/2)]
        hue_value = pixel_center[0]
        sat_value = pixel_center[1]
        light_value = pixel_center[2]
        
        color = 'Unknown'
        if sat_value < 55 and light_value > 200 and light_value <255 :
            color = 'White'
        else:
            if hue_value < 5: color = 'Red'
            elif hue_value < 22: color = 'Yellow'
            elif hue_value < 33: color = 'Yellow'
            elif hue_value < 78: color = 'Green'
            elif hue_value < 131: color = 'Blue'
            elif hue_value < 170: color = 'Blue'
            else: color = 'Red'
        return color

    def helmetColor(self, img, helmetPosition):
        if helmetPosition != [0,0,0,0]:
            hel_img = img[int(helmetPosition[1])+5:int(helmetPosition[3])-5,int(helmetPosition[0])+5:int(helmetPosition[2])-5]
            helmetColor = self.checkColor(hel_img)
        else:
            helmetColor = 'None'
        return helmetColor

    def iou(self, boxA, boxB, state):
        '''
        intersection of union between two boxes
        '''
        interArea = max(0, min(boxA[2], boxB[2]) - max(boxA[0], boxB[0]) + 1) * max(0, min(boxA[3], boxB[3]) - max(boxA[1], boxB[1]) + 1)
        boxBArea = (boxB[2] - boxB[0]) * (boxB[3] - boxB[1])
        if state is False:
            if (interArea / boxBArea) > 0.8 and boxB[1] > boxA[1]: return True
            else: return False
        else:
            return (interArea / boxBArea) # iou score
    
    def draw_roi(self, frame , roi, roi_name):
        (x1,y1), (x2,y2) = roi[0], roi[-1]
        plot_one_box((x1, y1, x2, y2), frame, (255, 165, 0), roi_name, line_thickness = 2)
        for i in roi: # i = [#, #]
            cv2.circle(frame, tuple(i), 3, (255, 165, 0), -1) # draw 4 point

    def selectHelmetColor(self, helmetColor):
        if helmetColor is 'Red' and self.selectRedHelmet or helmetColor is 'Blue' and self.selectBlueHelmet or helmetColor is 'Yellow' and self.selectYellowHelmet or helmetColor is 'White' and self.selectWhiteHelmet:
            return False
        else:
            return True
    
    def selectDetection(self, helmetStatus, vestStatus, helmetColor):
        helmetColorStatus = False
        if self.helmetDetection and helmetStatus and self.selectHelmetColor(helmetColor):
            helmetColorStatus = True
        
        if (helmetStatus and vestStatus) or helmetColorStatus:
            return True
        else:
            return False

    def saveClass(self, box, label, perlist, helmet, vest):    
        '''
        saveClass
        '''
        if label[box[0]] == 'person': perlist.append(box[1])
        elif label[box[0]] == 'helmet': helmet.append(box[1])
        elif label[box[0]] == 'vest': vest.append(box[1])
        return perlist, helmet, vest
    
    def personStatus(self, person, listHelmet, listVest): 
        '''
        checking the person attributes, do they wear the PPE components correctly?
        input: bounding box of person and attributes
        output: status and helmet position
        '''
        if self.helmetDetection:
            helmetStatus = False
            helmetPos = [0, 0, 0, 0] 
            for helmet in listHelmet:
                if self.iou(person, helmet, True) > 0.5 and (helmet[3] < ((person[3] + person[1])/3)):  # helmet should always in top location
                    helmetPos = helmet
                    helmetStatus = True
                    break
        else:
            helmetStatus = True
            helmetPos = [0, 0, 0, 0]
                
        if self.vestDetection:   
            vestStatus = False 
            for vest in listVest:
                if self.iou(person, vest, True) > 0.8:
                    vestStatus = True
                    break
        else:
            vestStatus = True
            
        return helmetStatus, vestStatus, helmetPos

    def img2pyqt(self,img,label):
        '''
        convert the opencv format to pyqt format color
        '''
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        temp = QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1]*3, QImage.Format_RGB888)
        return QPixmap.fromImage(temp).scaled(label.width(), label.height())

    def changeColor(self, status):
        '''
        change color of the metadata status, pass will be green, otherwise is red
        '''
        color = "green" if status else "red"
        return color
    
    def storage2usb(self):
        '''
        backup the output captured person into the usb file. Please change the usb path in Config2Channels.json
        
        . imgCapture        ./media/nvidia/backup/
        |__ png/            |__ png/
        |__ json/           |__ json/
        e.g: 
        imgCapture/json --> /media/nvidia/backup/json
        imgCapture/png  --> /media/nvidia/backup/png
        '''
        for dirs in os.listdir(self.storage):
            move(os.path.join(file_path, dirs), os.path.join(self.usbPath, dirs))
    
    def snapshot(self, snop, helmet, vest, times, helmetColor):
        '''
        show the pass or no pass in the right of the monitor 
        '''
        passColor = self.changeColor(self.selectDetection(helmet, vest, helmetColor))
        
        br = ''
        if self.helmetDetection:
            helmetMetadata = 'YES' if helmet else 'NO'
            color= 'white' if helmetColor is 'None' else helmetColor
            helmetText = f'<br /><br />color: <font color={color}> {helmetColor} </font>' + f'<br />Helmet: <font color={self.changeColor(helmet)}> {helmetMetadata} </font>'
        else:
            helmetMetadata = 'None'
            helmetText = ''
            br += f'<br /><br /><br />'
        if self.vestDetection:
            vestMetadata = 'YES' if vest else 'NO'
            vestText = f'<br />Vest: <font color={self.changeColor(vest)}> {vestMetadata} </font>'
        else:
            vestMetadata = 'None'
            vestText = ''
            br += f'<br />'
        passMetadata = 'PASS' if self.selectDetection(helmet, vest, helmetColor) else 'NO PASS'

        snop.setText(times.toString("hh:mm:ss") + helmetText + vestText + br + 
        f'<br /><br /><font color={passColor}> {passMetadata} </font>')
        
        # if self.selectDetection(helmet, vest, helmetColor):
        #     src = self.img2pyqt(cv2.imread("img/pass.png"), icon)
        # else :
        #     src = self.img2pyqt(cv2.imread("img/no_pass.png"), icon)
        # icon.clear()
        # icon.setPixmap(src)

    def saveCapJSON(self, passCounter, noPassCounter, imgCounter, helmetStatus, vestStatus, helmetColor, times, crop, counterLabel, status):
        '''
        save the capture along with the json files from one/two channels
        '''
        channel = 'channel1'
        channelBase = 'A1'
        date = times.toString("dd.MM.yyyy").split('.')
        date = date[2] + date[1] + date[0]
        time = times.toString("hh:mm:ss").replace(':','')

        if self.selectDetection(helmetStatus, vestStatus, helmetColor):
            passCounter += 1
            temp = '_pass_'
            tmp = passCounter
            imgCounter += 1
        else:
            noPassCounter += 1
            temp = '_noPass_'
            tmp = noPassCounter
            imgCounter += 1
        counterLabel.clear()
        counterLabel.setText(str(noPassCounter) + "/"+ str(passCounter + noPassCounter))
        baseName = channelBase + date[2:] + time + temp + str(tmp)
        if not self.stopCapture:
            PNGpath = os.path.join(self.storage, 'png', date + '_' + time + '_' + channel + temp + str(tmp) + '.png')
            JSONpath = os.path.join(self.storage, 'json', date + '_' + time + '_' + channel + temp + str(tmp) + '.json') 
            cv2.imwrite(PNGpath, crop)  # save the pass person image
            self.writeJSON(JSONpath, helmetStatus, vestStatus, times, helmetColor, channel)
            self.base64encode(PNGpath, JSONpath, baseName) 
        
        return passCounter, noPassCounter, imgCounter
    
    def counterText(self, passcon1, passcon2, nopasscon1, nopasscon2):
        self.label.clear()
        self.label.setText(str(nopasscon1) + "/"+ str(passcon1 + nopasscon1))
        self.label_7.clear()
        self.label_7.setText(str(nopasscon2) + "/"+ str(passcon2 + nopasscon2))
    
    def tobase64(self, img):
	    return base64.b64encode(img).decode('ascii')

    def imgResize(self, img, scale=1):
	    height, width = img.size
	    return img.resize((int(height*scale), int(width*scale)), Image.BILINEAR)

    def base64encode(self, PNGpath, JSONpath, baseName):
        API_ENDPOINT = 'http://192.168.0.107/api/captures/aibox'
        img = cv2.imread(PNGpath)
        resized = cv2.resize(img, (350, 510), interpolation = cv2.INTER_NEAREST)
        resized = resized[0:270,:]
        pil_img = Image.fromarray(cv2.cvtColor(resized, cv2.COLOR_BGR2RGB))
        rs_im = self.imgResize(pil_img, 0.6)
        imgByteArr = io.BytesIO()
        rs_im.save(imgByteArr, format='PNG')
        encode = self.tobase64(imgByteArr.getvalue())
        # print(len(encode))
        fp = self.read(JSONpath)
        status = 1 if fp["status"] else 0
        metadata = fp["metadata"]
        headers={
            'Content-type':'application/json',
        }
        data = {'device_id':53,
                'channel_id':int(fp["channel"][-1:]),
                'captured_at':fp["time"],
                'metadata_id': baseName,
                'api_metadata':fp["metadata"],
                'status': status,
                'file_path':encode}
        try:
            r = requests.post(
                API_ENDPOINT,
                json=data,
                headers=headers
            )
        except:
            return
        # print("the pastebin url is %s" % r.text)

    def writeJSON(self, file_name, helmetStatus, vestStatus, times, helmetColor, channel):
        '''
        write the output of detection into  json file
        '''
        jsonData = {}
        metaData = {}
        jsonData['channel'] = channel
        jsonData['time'] = times.toMSecsSinceEpoch()
        jsonData['status'] = True if self.selectDetection(helmetStatus, vestStatus, helmetColor) else False
        if self.helmetDetection:
            metaData['color'] = helmetColor if helmetColor is not 'None' else ""
            metaData['helmet'] = True if helmetStatus else False 
        else:
            metaData['color'] = 'None'
            metaData['helmet'] = 'None'
        if self.vestDetection:
            metaData['vest'] = True if vestStatus else False
        else:
            metaData['vest'] = 'None'

        jsonData['metadata'] = metaData
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(jsonData, f, ensure_ascii = False, indent = 4, sort_keys = False) # make sure that SW team is the same 

    def processDetect(self, frame, color, label, box):
        '''
        show bounding box information
        '''
        pos = box[1]
        if label[box[0]] == 'helmet' and self.helmetDetection:
            helmetImage = frame[int(pos[1])+5:int(pos[3])-5,int(pos[0])+5:int(pos[2])-5] # crop only helmet
            plot_one_box(pos, frame, color[box[0]], self.checkColor(helmetImage) + ' helmet')
        elif label[box[0]] == 'vest' and self.vestDetection:
            plot_one_box(pos, frame, color[box[0]], label[box[0]])
        elif label[box[0]] == 'person':
            persomImage = frame[int(pos[1])+5:int(pos[3])-5,int(pos[0])+5:int(pos[2])-5]
            PILimage = Image.fromarray(cv2.cvtColor(persomImage, cv2.COLOR_BGR2RGB))
            personStatus = self.test_submit(self.model, PILimage)
            if personStatus == 1: plot_one_box(pos, frame, color[box[0]], label[box[0]])
            else: plot_one_box(pos, frame, (0, 0, 255), 'falldown')

    def saveBox(self, bbox, label, perlist, helmet, vest, roi):
        '''
        save all the existing bounding box based on the attributes
        '''
        if len(bbox) > 0:
            for _, box in enumerate(bbox): # plotbox
                if self.roi1: 
                    if self.iou(roi, box[1], False):
                        perlist, helmet, vest = self.saveClass(box, label, perlist, helmet, vest)
                else:
                    perlist, helmet, vest = self.saveClass(box, label, perlist, helmet, vest)

        return perlist, helmet, vest

    def drawBbox(self, img, bbox, color, label, roi):
        '''
        drawing bounding boxes
        '''
        if len(bbox) != 0:
            for _, box in enumerate(bbox): # plotbox
                if self.roi1:
                    if self.iou(roi, box[1], False):
                        self.processDetect(img, color, label, box)
                else:
                    self.processDetect(img, color, label, box)

    def mousePressEvent(self, event):
        '''
        any events about the mouse
        '''
        if event.button() == Qt.LeftButton:
            logger.info('left button clicked')
            [x,y] = self.boxSizeTranfer(event.pos(), True)
            for index, i in enumerate(self.set_roi1):
                if abs(x - i[0]) < self.point_size and abs(y - i[1]) < self.point_size:
                    self.current_index = index
                    self.hit_flag1 = True
                    self.mode1 = 0         
            
        # if event.button() == Qt.RightButton: print('right button clicked')

    def mouseReleaseEvent(self,event): 
        '''   
        any mouse release events
        '''
        global set_roi1
        dic = {}
        if self.mode1>-1 :
            dic['set_roi1'] = self.set_roi1
            with open('ROIConfig2Channels_one.json', 'w', encoding='utf-8') as f:
                json.dump(dic, f, ensure_ascii = False, indent = 4, sort_keys = True)
            self.hit_flag1 = False
            set_roi1 = [*self.set_roi1[0] , *self.set_roi1[-1]]
            if (set_roi1[0] > set_roi1[2]):
                set_roi1[0] , set_roi1[2] = set_roi1[2] , set_roi1[0]
            if (set_roi1[1] > set_roi1[3]):
                set_roi1[1] , set_roi1[3] = set_roi1[3] , set_roi1[1]
    
    def boxSizeTranfer(self, pos, status):
        '''
        ROI activation based on the position of the channel
        '''
        # print(pos.x(), pos.y())
        [x, y] = [0, 0]
        if 61 < pos.x()<1527 and 145<pos.y()<797:
            x = int((pos.x() - 61)/1466*1920)
            y = int((pos.y() - 145)/652*1080)
            # print("x y", x, y)
        return [x ,y]

    def mouseMoveEvent(self, event):
        '''
        set ROI
        '''
        if self.hit_flag1: # channel1
            self.pos = event.pos()
            [x,y] = self.boxSizeTranfer(event.pos(), True)
            if self.mode1 == 0:
                self.set_roi1[self.current_index] = [x,y]
                if self.current_index == 0:
                    self.set_roi1[1][1] = y
                    self.set_roi1[2][0] = x
                elif self.current_index == 1:
                    self.set_roi1[0][1] = y
                    self.set_roi1[3][0] = x
                elif self.current_index == 2:
                    self.set_roi1[3][1] = y
                    self.set_roi1[0][0] = x
                elif self.current_index == 3:
                    self.set_roi1[2][1] = y
                    self.set_roi1[1][0] = x                    
            self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_S:
            global show_roi
            show_roi = not show_roi

    def history(self, page, img , ulabel1, ulabel2, ulabel3, utime1, utime2, utime3, uicon1, uicon2, uicon3):
        '''
        able to see the previous detected objects

        [1] [2] [3]
         | current = index

        '''
        index = page
        while index > (page-self.num_cap):
            if index % self.num_cap == 0:
                ulabel1.setPixmap(self.historyImg(img, ulabel1, uicon1, utime1, index))
            elif index % self.num_cap == 2:
                ulabel2.setPixmap(self.historyImg(img, ulabel2, uicon2, utime2, index))
            elif index % self.num_cap == 1:
                ulabel3.setPixmap(self.historyImg(img, ulabel3, uicon3, utime3, index))
            index -= 1

    def historyImg(self, imgs, ulabel, uicon, utime, index):
        '''
        show the list of current and previous detection
        '''
        img = imgs[-index]
        JSON = img.replace('png', 'json')
        self.historyJSON( uicon, utime, JSON)
        img = cv2.imread(img)
        return self.img2pyqt(img, ulabel)
    
    def historyJSON(self, uicon, utime, JSON): # channel1_20220422_113515_pass_0.json
        # with open(JSON) as f:
        #     metadata = json.load(f)
        metadata = self.read(JSON)
        status = metadata['status']
        helmetColor =  metadata['metadata']['color']
        helmet = metadata['metadata']['helmet']
        vest = metadata['metadata']['vest']

        br = ''
        passColor = "green" if  metadata['status'] else "red"
        if self.helmetDetection:
            color = 'white' if helmetColor is 'None' else helmetColor    
            helmetColor = helmetColor if helmetColor != "" else "None"
            helmetMetadata = 'YES' if helmet else 'NO'
            helmetText = f'<br /><br />color: <font color={color}> {helmetColor} </font>' + f'<br />Helmet: <font color={self.changeColor(helmet)}> {helmetMetadata} </font>'
        else:
            helmetMetadata = 'None'
            helmetText = ''
            br += f'<br /><br /><br />'
        if self.vestDetection:
            vestMetadata = 'YES' if vest else 'NO'
            vestText = f'<br />Vest: <font color={self.changeColor(vest)}> {vestMetadata} </font>'
        else:
            vestMetadata = 'None'
            vestText = ''
            br += f'<br />'
        passMetadata = 'PASS' if  status else 'NO PASS'

        time = JSON.split('_')[1]
        time =time[0:2] + ":" + time [2:4] + ':' + time[4:6]

        utime.setText(time + helmetText + vestText + br + 
        f'<br /><br /><font color={passColor}> {passMetadata} </font>')

        tmp = cv2.imread("img/pass.png") if status else cv2.imread("img/no_pass.png")
        uicon.clear()
        uicon.setPixmap(self.img2pyqt(tmp, uicon))

    
    
    def checkCounter(self):
        counterData = self.read('counter_test.json')
        passcon1 = counterData['passCounter1']
        nopasscon1 = counterData['noPassCounter1']
        passcon2 = counterData['passCounter2']
        nopasscon2 = counterData['noPassCounter2']
        imgcounter = counterData['imageCounter']
        return passcon1, passcon2, nopasscon1, nopasscon2, imgcounter

    def writeCounter(self,passcon1, passcon2, nopasscon1, nopasscon2, imgcounter):
        dic = {}
        dic['passCounter1'] = passcon1
        dic['noPassCounter1'] = nopasscon1
        dic['passCounter2'] = passcon2
        dic['noPassCounter2'] = nopasscon2
        dic['imageCounter'] = imgcounter
        with open('counter_test.json', 'w', encoding='utf-8') as f:
            json.dump(dic, f, ensure_ascii = False, indent = 4, sort_keys = False)
    
    def runTime(self):
        currentTime = datetime.strptime(QDateTime.currentDateTime().toString("hh:mm"), "%H:%M")
        startTime1 = datetime.strptime(self.startTime1, "%H:%M")
        endTime1 = datetime.strptime(self.endTime1, "%H:%M")
        startTime2 = datetime.strptime(self.startTime2, "%H:%M")
        endTime2 = datetime.strptime(self.endTime2, "%H:%M")
        if ((currentTime > startTime1) and (currentTime < endTime1)) or ((currentTime > startTime2) and (currentTime < endTime2)):
            return True
        else:
            return False

    def ratio(self, bg, img):
        '''
        write the documentation of each funtion:
        for example:
            def ratio is to .........
            input: ....
            output: ..... 
        '''  
        try: 
            buffer = 20
            if img.shape[0] > bg.shape[0] and img.shape[1] > bg.shape[1]:
                ratio = bg.shape[0]/img.shape[0] if img.shape[0] > img.shape[1] else bg.shape[1]/img.shape[1]
                dim = (int(ratio * img.shape[1]), int(ratio * img.shape[0])-buffer)
                img = cv2.resize(img, (dim))
            elif img.shape[0] > bg.shape[0]:
                ratio = bg.shape[0]/img.shape[0]
                dim = (int(ratio * img.shape[1]), int(ratio * img.shape[0])-buffer)
                img = cv2.resize(img, (dim))
            elif img.shape[1] > bg.shape[1]:
                ratio = bg.shape[1]/img.shape[1]
                dim = (int(ratio * img.shape[1]), int(ratio * img.shape[0])-buffer)
                img = cv2.resize(img, (dim))
            x_offset = (int((bg.shape[1] - img.shape[1])/2))
            y_offset = (int((bg.shape[0] - img.shape[0])/2))
            
            bg[y_offset:y_offset+img.shape[0], x_offset:x_offset+img.shape[1]] = img
            return bg
        except:
            logger.warning("ratio error continue")
              
    def run(self): 
        global threadSound
        global threadGPIO1
        global helmetStatus
        global vestStatus
        global helmetColor
        counter1, counter2, fpscount, fps2counter = 0, 0, 0, 0
        tracking1, tracking2 = 0, 0
        removeNumber = 0
        stopCounter = 0

        label = ["person", "vest", "helmet"] 

        color = [ (100, 0, 50), (0, 255, 0), (0, 255, 0)]

        # passcon1, passcon2, nopasscon1, nopasscon2, imgcounter = self.checkCounter()
        # self.counterText(passcon1, passcon2, nopasscon1, nopasscon2)

        detect_api = detect_tensorrt(yolov5_wrapper = tensorrt_init('../../result/'))

        cap = open_cam_rtsp(f"rtsp://{self.user2}:{self.password2}@{self.ip2}", self.width, self.height, 0, 10)

        tsound = threading.Thread(target = self.sound)
        tgpio1  = threading.Thread(target = self.GPIOgate1)
        
        logger.info(f'Camara1 {cap.isOpened()}')
        logger.info("Ready to detect")

        while(True):
            start = time.time()

            # Ddate = QDateTime.currentDateTime().toString("dd.MM.yyyy").split('.')
            # self.time.setText(Ddate[2] + '.' + Ddate[1] + '.' + Ddate[0])

            # if stopCounter == 1000:
            #     if self.page_status1 == 1:
            #         self.page1 = 0
            #         self.page_status1 = 0
            #         self.ulabel1.clear()
            #         self.ulabel2.clear()
            #         self.ulabel3.clear()
            #         self.utime1.clear()
            #         self.utime2.clear()
            #         self.utime3.clear()
            #         self.uicon1.clear()
            #         self.uicon2.clear()
            #         self.uicon3.clear()
            #     stopCounter = 0
            # stopCounter += 1

            # if QDateTime.currentDateTime().toString("hh:mm") == self.counterReset:
            #     passcon1, passcon2, nopasscon1, nopasscon2 = 0, 0, 0, 0
            #     self.writeCounter(passcon1, passcon2, nopasscon1, nopasscon2, imgcounter)
            #     self.counterText(passcon1, passcon2, nopasscon1, nopasscon2)
            #     self.setFunction()
            #     shutil.rmtree('test/base64')
            #     if not os.path.exists('test/base64'):
            #         os.makedirs('test/base64')
            '''
            if imgcounter >= 15:
                self.stopCapture = True
                if not self.storageMethod: 
                    removeData = sorted(glob("./test/png/*.png"))
                    for i, fileName in enumerate(removeData):
                        jsonName = fileName.replace('png', 'json')
                        os.remove(fileName)
                        os.remove(jsonName)
                        if i == 7:
                            removeNumber = i
                            break
                    imgcounter = 15 - removeNumber
                    self.writeCounter(passcon1, passcon2, nopasscon1, nopasscon2, imgcounter)
                    self.stopCapture = False
            else:
                self.stopCapture = False    
            '''

            fps2counter += 1
            if fps2counter == 180:
                data = self.read('set.json')
                if data['setStatus']:                    
                    self.setFunction()
                    with open('set.json', 'w') as f:
                        dic = {}
                        dic['setStatus'] = False
                        json.dump(dic, f, ensure_ascii = False, indent = 4, sort_keys = False)
                fps2counter = 0

            ret, img = cap.read()

            if not ret:
                img = cv2.imread('bg.jpg')
            else:
                if self.roi1 == True: 
                    self.draw_roi(img, self.set_roi1, 'ROI_1')
                _, bbox, _ = detect_api.detect(img) # person, and other attribures bboxes

                personList   = []
                helmetList   = []
                vestList     = []

                # if self.runTime():
                if True:
                    personList, helmetList, vestList = self.saveBox(bbox, label, personList, helmetList, vestList, set_roi1)
                    
                    for _, person in enumerate(personList):   
                        helmetStatus, vestStatus, helmetPosition = self.personStatus(person, helmetList, vestList)
                        helmetColor = self.helmetColor(img, helmetPosition)

                        cropimg = img[int(person[1])+1:int(person[3])-1,int(person[0])+1:int(person[2])-1]
                        bg = cv2.imread("img/bg_148x248.jpg")
                        bg = self.ratio(bg,cropimg)
                        try:
                            pixmap_src1=self.img2pyqt(bg,self.snap1)
                        except:
                            continue

                        if fpscount == 10:
                            counter1 += 1  
                            print(counter1)
                            if counter1 == 1:
                                datetime1 = QDateTime.currentDateTime()
                                if self.page_status1 == 0:
                                    self.snapshot(self.data1, helmetStatus, vestStatus, datetime1, helmetColor)
                                    self.snap1.setPixmap(pixmap_src1)
                                pic1 = pixmap_src1
                                text1 = helmetStatus, vestStatus, datetime1, helmetColor
                            elif counter1 == 2:   
                                datetime2 = QDateTime.currentDateTime() 
                                if self.page_status1 == 0:
                                    self.snapshot(self.data1, helmetStatus, vestStatus, datetime2, helmetColor) 
                                    self.snapshot(self.data2, text1[0], text1[1], text1[2], text1[3])
                                    self.snap1.setPixmap(pixmap_src1)
                                    self.snap2.setPixmap(pic1)
                                pic2 = pixmap_src1
                                text2 = helmetStatus, vestStatus, datetime2, helmetColor
                            elif counter1 == 3:                  
                                datetime3 = QDateTime.currentDateTime()
                                if self.page_status1 == 0:
                                    self.snapshot(self.data1, helmetStatus, vestStatus, datetime3, helmetColor) 
                                    self.snapshot(self.data2, text2[0], text2[1], text2[2], text2[3])
                                    self.snapshot(self.data3, text1[0], text1[1], text1[2], text1[3])                   
                                    self.snap1.setPixmap(pixmap_src1)
                                    self.snap2.setPixmap(pic2)
                                    self.snap3.setPixmap(pic1)
                                pic3 = pixmap_src1
                                text3 = helmetStatus, vestStatus, datetime3, helmetColor
                            elif counter1 == 4:                  
                                datetime4 = QDateTime.currentDateTime()
                                if self.page_status1 == 0:
                                    self.snapshot(self.data1, helmetStatus, vestStatus, datetime4, helmetColor)
                                    self.snapshot(self.data2, text3[0], text3[1], text3[2], text3[3]) 
                                    self.snapshot(self.data3, text2[0], text2[1], text2[2], text2[3])
                                    self.snapshot(self.data4, text1[0], text1[1], text1[2], text1[3])                   
                                    self.snap1.setPixmap(pixmap_src1)
                                    self.snap2.setPixmap(pic3)
                                    self.snap3.setPixmap(pic2)
                                    self.snap4.setPixmap(pic1)
                                pic4 = pixmap_src1
                                text4 = helmetStatus, vestStatus, datetime4, helmetColor
                            elif counter1 == 5:                  
                                datetime5 = QDateTime.currentDateTime()
                                if self.page_status1 == 0:
                                    self.snapshot(self.data1, helmetStatus, vestStatus, datetime5, helmetColor)
                                    self.snapshot(self.data2, text4[0], text4[1], text4[2], text4[3]) 
                                    self.snapshot(self.data3, text3[0], text3[1], text3[2], text3[3]) 
                                    self.snapshot(self.data4, text2[0], text2[1], text2[2], text2[3])
                                    self.snapshot(self.data5, text1[0], text1[1], text1[2], text1[3])                   
                                    self.snap1.setPixmap(pixmap_src1)
                                    self.snap2.setPixmap(pic4)
                                    self.snap3.setPixmap(pic3)
                                    self.snap4.setPixmap(pic2)
                                    self.snap5.setPixmap(pic1)
                                pic5 = pixmap_src1
                                text5 = helmetStatus, vestStatus, datetime5, helmetColor
                            elif counter1 == 6:                  
                                datetime6 = QDateTime.currentDateTime()
                                if self.page_status1 == 0:
                                    self.snapshot(self.data1, helmetStatus, vestStatus, datetime6, helmetColor)
                                    self.snapshot(self.data2, text5[0], text5[1], text5[2], text5[3]) 
                                    self.snapshot(self.data3, text4[0], text4[1], text4[2], text4[3]) 
                                    self.snapshot(self.data4, text3[0], text3[1], text3[2], text3[3]) 
                                    self.snapshot(self.data5, text2[0], text2[1], text2[2], text2[3])
                                    self.snapshot(self.data6, text1[0], text1[1], text1[2], text1[3])                   
                                    self.snap1.setPixmap(pixmap_src1)
                                    self.snap2.setPixmap(pic5)
                                    self.snap3.setPixmap(pic4)
                                    self.snap4.setPixmap(pic3)
                                    self.snap5.setPixmap(pic2)
                                    self.snap6.setPixmap(pic1)
                                pic6 = pixmap_src1
                                text6 = helmetStatus, vestStatus, datetime6, helmetColor
                            elif counter1 == 7:                  
                                datetime7 = QDateTime.currentDateTime()
                                if self.page_status1 == 0:
                                    self.snapshot(self.data1, helmetStatus, vestStatus, datetime7, helmetColor)
                                    self.snapshot(self.data2, text6[0], text6[1], text6[2], text6[3]) 
                                    self.snapshot(self.data3, text5[0], text5[1], text5[2], text5[3]) 
                                    self.snapshot(self.data4, text4[0], text4[1], text4[2], text4[3]) 
                                    self.snapshot(self.data5, text3[0], text3[1], text3[2], text3[3]) 
                                    self.snapshot(self.data6, text2[0], text2[1], text2[2], text2[3])
                                    self.snapshot(self.data7, text1[0], text1[1], text1[2], text1[3])                   
                                    self.snap1.setPixmap(pixmap_src1)
                                    self.snap2.setPixmap(pic6)
                                    self.snap3.setPixmap(pic5)
                                    self.snap4.setPixmap(pic4)
                                    self.snap5.setPixmap(pic3)
                                    self.snap6.setPixmap(pic2)
                                    self.snap7.setPixmap(pic1)
                                pic7 = pixmap_src1
                                text7 = helmetStatus, vestStatus, datetime7, helmetColor
                            elif counter1 == 8:                  
                                datetime8 = QDateTime.currentDateTime()
                                if self.page_status1 == 0:
                                    self.snapshot(self.data1, helmetStatus, vestStatus, datetime8, helmetColor)
                                    self.snapshot(self.data2, text7[0], text7[1], text7[2], text7[3])
                                    self.snapshot(self.data3, text6[0], text6[1], text6[2], text6[3]) 
                                    self.snapshot(self.data4, text5[0], text5[1], text5[2], text5[3]) 
                                    self.snapshot(self.data5, text4[0], text4[1], text4[2], text4[3]) 
                                    self.snapshot(self.data6, text3[0], text3[1], text3[2], text3[3]) 
                                    self.snapshot(self.data7, text2[0], text2[1], text2[2], text2[3])
                                    self.snapshot(self.data8, text1[0], text1[1], text1[2], text1[3])                   
                                    self.snap1.setPixmap(pixmap_src1)
                                    self.snap2.setPixmap(pic7)
                                    self.snap3.setPixmap(pic6)
                                    self.snap4.setPixmap(pic5)
                                    self.snap5.setPixmap(pic4)
                                    self.snap6.setPixmap(pic3)
                                    self.snap7.setPixmap(pic2)
                                    self.snap8.setPixmap(pic1)
                                pic8 = pixmap_src1
                                text8 = helmetStatus, vestStatus, datetime8, helmetColor
                            elif counter1 == 9:                  
                                datetime9 = QDateTime.currentDateTime()
                                if self.page_status1 == 0:
                                    self.snapshot(self.data1, helmetStatus, vestStatus, datetime9, helmetColor)
                                    self.snapshot(self.data2, text8[0], text8[1], text8[2], text8[3])
                                    self.snapshot(self.data3, text7[0], text7[1], text7[2], text7[3])
                                    self.snapshot(self.data4, text6[0], text6[1], text6[2], text6[3]) 
                                    self.snapshot(self.data5, text5[0], text5[1], text5[2], text5[3]) 
                                    self.snapshot(self.data6, text4[0], text4[1], text4[2], text4[3]) 
                                    self.snapshot(self.data7, text3[0], text3[1], text3[2], text3[3]) 
                                    self.snapshot(self.data8, text2[0], text2[1], text2[2], text2[3])
                                    self.snapshot(self.data9, text1[0], text1[1], text1[2], text1[3])                   
                                    self.snap1.setPixmap(pixmap_src1)
                                    self.snap2.setPixmap(pic8)
                                    self.snap3.setPixmap(pic7)
                                    self.snap4.setPixmap(pic6)
                                    self.snap5.setPixmap(pic5)
                                    self.snap6.setPixmap(pic4)
                                    self.snap7.setPixmap(pic3)
                                    self.snap8.setPixmap(pic2)
                                    self.snap9.setPixmap(pic1)
                                pic9 = pixmap_src1
                                text9 = helmetStatus, vestStatus, datetime9, helmetColor
                            elif counter1 == 10:                  
                                datetime10 = QDateTime.currentDateTime()
                                if self.page_status1 == 0:
                                    self.snapshot(self.data1, helmetStatus, vestStatus, datetime10, helmetColor)
                                    self.snapshot(self.data2, text9[0], text9[1], text9[2], text9[3])
                                    self.snapshot(self.data3, text8[0], text8[1], text8[2], text8[3])
                                    self.snapshot(self.data4, text7[0], text7[1], text7[2], text7[3])
                                    self.snapshot(self.data5, text6[0], text6[1], text6[2], text6[3]) 
                                    self.snapshot(self.data6, text5[0], text5[1], text5[2], text5[3]) 
                                    self.snapshot(self.data7, text4[0], text4[1], text4[2], text4[3]) 
                                    self.snapshot(self.data8, text3[0], text3[1], text3[2], text3[3]) 
                                    self.snapshot(self.data9, text2[0], text2[1], text2[2], text2[3])
                                    self.snapshot(self.data10, text1[0], text1[1], text1[2], text1[3])                   
                                    self.snap1.setPixmap(pixmap_src1)
                                    self.snap2.setPixmap(pic9)
                                    self.snap3.setPixmap(pic8)
                                    self.snap4.setPixmap(pic7)
                                    self.snap5.setPixmap(pic6)
                                    self.snap6.setPixmap(pic5)
                                    self.snap7.setPixmap(pic4)
                                    self.snap8.setPixmap(pic3)
                                    self.snap9.setPixmap(pic2)
                                    self.snap10.setPixmap(pic1)
                                pic10 = pixmap_src1
                                text10 = helmetStatus, vestStatus, datetime10, helmetColor
                            elif counter1 == 11:                  
                                datetime11 = QDateTime.currentDateTime()
                                if self.page_status1 == 0:
                                    self.snapshot(self.data1, helmetStatus, vestStatus, datetime11, helmetColor)
                                    self.snapshot(self.data2, text10[0], text10[1], text10[2], text10[3])
                                    self.snapshot(self.data3, text9[0], text9[1], text9[2], text9[3])
                                    self.snapshot(self.data4, text8[0], text8[1], text8[2], text8[3])
                                    self.snapshot(self.data5, text7[0], text7[1], text7[2], text7[3])
                                    self.snapshot(self.data6, text6[0], text6[1], text6[2], text6[3]) 
                                    self.snapshot(self.data7, text5[0], text5[1], text5[2], text5[3]) 
                                    self.snapshot(self.data8, text4[0], text4[1], text4[2], text4[3]) 
                                    self.snapshot(self.data9, text3[0], text3[1], text3[2], text3[3]) 
                                    self.snapshot(self.data10, text2[0], text2[1], text2[2], text2[3])
                                    self.snapshot(self.data11, text1[0], text1[1], text1[2], text1[3])                   
                                    self.snap1.setPixmap(pixmap_src1)
                                    self.snap2.setPixmap(pic10)
                                    self.snap3.setPixmap(pic9)
                                    self.snap4.setPixmap(pic8)
                                    self.snap5.setPixmap(pic7)
                                    self.snap6.setPixmap(pic6)
                                    self.snap7.setPixmap(pic5)
                                    self.snap8.setPixmap(pic4)
                                    self.snap9.setPixmap(pic3)
                                    self.snap10.setPixmap(pic2)
                                    self.snap11.setPixmap(pic1)
                                pic11 = pixmap_src1
                                text11 = helmetStatus, vestStatus, datetime11, helmetColor
                            elif counter1 == 12:                  
                                datetime12 = QDateTime.currentDateTime()
                                if self.page_status1 == 0:
                                    self.snapshot(self.data1, helmetStatus, vestStatus, datetime12, helmetColor)
                                    self.snapshot(self.data2, text11[0], text11[1], text11[2], text11[3])
                                    self.snapshot(self.data3, text10[0], text10[1], text10[2], text10[3])
                                    self.snapshot(self.data4, text9[0], text9[1], text9[2], text9[3])
                                    self.snapshot(self.data5, text8[0], text8[1], text8[2], text8[3])
                                    self.snapshot(self.data6, text7[0], text7[1], text7[2], text7[3])
                                    self.snapshot(self.data7, text6[0], text6[1], text6[2], text6[3]) 
                                    self.snapshot(self.data8, text5[0], text5[1], text5[2], text5[3]) 
                                    self.snapshot(self.data9, text4[0], text4[1], text4[2], text4[3]) 
                                    self.snapshot(self.data10, text3[0], text3[1], text3[2], text3[3]) 
                                    self.snapshot(self.data11, text2[0], text2[1], text2[2], text2[3])
                                    self.snapshot(self.data12, text1[0], text1[1], text1[2], text1[3])                   
                                    self.snap1.setPixmap(pixmap_src1)
                                    self.snap2.setPixmap(pic11)
                                    self.snap3.setPixmap(pic10)
                                    self.snap4.setPixmap(pic9)
                                    self.snap5.setPixmap(pic8)
                                    self.snap6.setPixmap(pic7)
                                    self.snap7.setPixmap(pic6)
                                    self.snap8.setPixmap(pic5)
                                    self.snap9.setPixmap(pic4)
                                    self.snap10.setPixmap(pic3)
                                    self.snap11.setPixmap(pic2)
                                    self.snap12.setPixmap(pic1)
                                pic1 = pic2
                                pic2 = pic3
                                pic3 = pic4
                                pic4 = pic5
                                pic5 = pic6
                                pic6 = pic7
                                pic7 = pic8
                                pic8 = pic9
                                pic9 = pic10
                                pic10 = pic11
                                pic11 = pixmap_src1
                                text1 = text2
                                text2 = text3
                                text3 = text4
                                text4 = text5
                                text5 = text6
                                text6 = text7
                                text7 = text8
                                text8 = text9
                                text9 = text10
                                text10 = text11
                                text11 = helmetStatus, vestStatus, datetime12, helmetColor
                    self.drawBbox(img, bbox, color, label, set_roi1)          
            self.screen.setPixmap(self.img2pyqt(img,self.screen))
            if fpscount == 10:                                                    
                fpscount = 0
            fpscount += 1
            if cv2.waitKey(1) and 0xff==ord('q') :
                break
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = OneScreen()
    ui.showFullScreen()
    event = threading.Event()
    ui.run()
    GPIO.cleanup()
    sys.exit()       
