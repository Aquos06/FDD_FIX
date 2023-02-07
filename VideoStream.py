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

    def run(self):
        self.createSRC()
        while True:
            if self.change:
                self.streamFunc(self.src)
                self.change = False

            grab, self.frame = self.stream.read()

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
