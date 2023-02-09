from threading import Thread
from PyQt5.QtCore import QObject
from PyQt5 import QtCore, QtGui
import cv2
import numpy as np

class WebcamVideoStream(QObject):
    
    picdone = QtCore.pyqtSignal(np.ndarray)
    ret = QtCore.pyqtSignal(bool,int)
    reconnecting = QtCore.pyqtSignal(bool,int)

    def streamFunc(self,src):
        self.src = src
        self.stream = cv2.VideoCapture(self.src)

    def createSRC(self):
        self.streamFunc(self.src)

    def img2pyqt(self,img,label):
        '''
        convert the opencv format to pyqt format color
        '''
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        temp = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1]*3, QtGui.QImage.Format_RGB888)
        return QtGui.QPixmap.fromImage(temp).scaled(label.width(), label.height())

    def run(self):
        self.createSRC()
        while True:
            if self.change:
                self.streamFunc(self.src)
                self.change = False

            grab, self.frame = self.stream.read()

            try:
               self.ROI.setPixmap(self.img2pyqt(self.frame,self.ROI))
            except:
                pass
            
            if not grab:
                self.ret.emit(False, self.channel)
                while True:
                    self.ret.emit(False,self.channel)
                    self.streamFunc(self.src)
                    ret,self.frame = self.stream.read()
                    if ret:
                        self.ret.emit(True,self.channel)
                        break
            else:
                self.picdone.emit(self.frame)
                # self.picdone.clear()
