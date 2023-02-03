import cv2
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QImage , QPixmap
from PyQt5 import QtGui, QtWidgets, QtCore
from clickfall import Details
import sys
import os
import json

class InfoDetails(QtWidgets.QMainWindow):                                    #open window
    def __init__(self): # mode: [0,all] , [1,mask] , [2,temperature]
        super().__init__()
        self.ui = Details()
        self.ui.setupUi(self)
        self.go = False
        self.image = cv2.imread('bg.jpg')
        f = open('personal.json', 'r')
        self.data = json.load(f)
        f.close()
        
    def text(self):
        text =  f'Event: {self.type} ' + \
                f'<br />Time: {self.time}' + \
                f'<br />Channel: {self.channel} '
        
        return text
  
    def run(self):
        
        path_ss = './falldown/screenshot'
        path = './falldown/cut'
        
        self.ui.screen.setPixmap(self.img2pyqt(os.path.join(path_ss,self.image_ss),self.ui.screen))
        self.ui.box.label.setIcon(QtGui.QIcon(os.path.join(path, (self.image))))
        self.ui.box.label.setIconSize(QtCore.QSize(150,150))
        self.ui.box.information.setText(self.text())
        self.ui.label_6.setText(self.image)
        
    def input(self,image_ss,image,date,time,channel,event):
        self.image_ss = f"{image_ss}.jpg"
        self.image = f"{image}.jpg"
        self.date = date
        self.time = time 
        self.channel = channel
        self.type = event
        self.run()
        
    def img2pyqt(self,img,label):
        '''
        convert the opencv format to pyqt format color
        '''
        img = cv2.imread(img)
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        temp = QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1]*3, QImage.Format_RGB888)
        return QPixmap.fromImage(temp).scaled(label.width(), label.height())
    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = InfoDetails()
    window.showFullScreen()
    window.run()
    sys.exit(app.exec_())
    
