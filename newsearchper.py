
from newsearchmain import Ui_MainWindow
from components.searchBox import searchBox
from glob import glob
from datetime import datetime
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QImage , QPixmap
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QDate
from components.Details.Falling import Falling
import cv2
import json
import xlsxwriter
import os
import numpy as np
import shutil
import math

from utility import text, textforstat, toLog
from components.searchBox import searchBox

count  = [0,1]

class SearchPerson(QtWidgets.QMainWindow):
    def __init__(self):
        super(SearchPerson,self).__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.Searchresult = []
        self.det = Falling()
        self.det.ui.setupUi(self)
        self.det.ui.rightButton.clicked.connect(self.rightButton)
        self.det.ui.leftButton.clicked.connect(self.leftButton)
        self.ui.leftPage.clicked.connect(self.Left)
        self.ui.rightPage.clicked.connect(self.Right)
        self.setup_control()  
        self.awal = 1 #first number to display
        self.now = 0#index displayed in big screen  
        self.everShow = False
        self.range = 10

        self.box = [self.ui.box1, self.ui.box2, self.ui.box3, self.ui.box4, self.ui.box5, self.ui.box6, self.ui.box7, self.ui.box8, self.ui.box9 
                ,self.ui.box10, self.ui.box11, self.ui.box12, self.ui.box13, self.ui.box14, self.ui.box15, self.ui.box16]

        self.path = './falldown/screenshot'
        self.pathcut = './falldown/cut'

        self.blank = cv2.imread('./ROI/Camera1/blank.jpg')

        self.jsoninit()

    def Left(self):
        if self.awal - 16 > 0:
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            self.awal -= 16
            self.ui.labelPage.setText(f"{math.ceil(self.awal/16)} / {math.ceil(len(self.Searchresult)/16)}")
            self.setIcon()
            QtWidgets.QApplication.restoreOverrideCursor()

    def Right(self):
        if self.awal + 16 < len(self.Searchresult):
            QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
            self.awal += 16
            self.ui.labelPage.setText(f"{math.ceil(self.awal/16)} / {math.ceil(len(self.Searchresult)/16)}")
            self.setIcon()
            QtWidgets.QApplication.restoreOverrideCursor()

    def back(self):
        self.det.ui.close()
        self.everShow = False

    def showDetail(self,filenames):

        self.now = self.Searchresult.index(filenames)
        self.det.ui.buttonBack.setText('Back')
        self.det.ui.buttonBack.clicked.connect(self.back)
        
        a = cv2.imread(os.path.join('./falldown/screenshot', filenames))
        b = cv2.imread(os.path.join('./falldown/cut', filenames))

        self.det.ui.FallLabel.setPixmap(self.img2pyqt(a, self.det.ui.FallLabel))
        self.det.ui.labelCut.setPixmap(self.img2pyqt(b,self.det.ui.labelCut))
        event,date,time,channel = self.fromfilename(filenames)
        
        self.det.ui.InformationLabel.setText(textforstat(event,date,time,channel))

        if not self.everShow:
            self.det.ui.show()
            self.everShow = True  
        else:
            self.det.ui.close()
            self.det.ui.show()

    def leftButton(self):
        if (self.now + 1) < len(self.Searchresult):
            self.now += 1
            self.changeDetails()

    def rightButton(self):
        if (self.now - 1) >= 0: 
            self.now -= 1
            self.changeDetails()

    def changeDetails(self):
        a = cv2.imread(os.path.join('./falldown/screenshot', self.Searchresult[int(self.now)]))
        b = cv2.imread(os.path.join('./falldown/cut',self.Searchresult[int(self.now)]))

        self.det.ui.FallLabel.setPixmap(self.img2pyqt(a,self.det.ui.FallLabel))
        self.det.ui.labelCut.setPixmap(self.img2pyqt(b, self.det.ui.labelCut))
        event,date,time,channel = self.fromfilename(self.Searchresult[int(self.now)])

        self.det.ui.InformationLabel.setText(textforstat(event,date,time,channel))

    def jsoninit(self):
        try:
            f = open('falldown/all_falldown.json','r')
            self.all_1 = json.load(f)
            f.close()
        except:
            f = open('falldown/all_falldown.json','w')
            data={}
            json.dump(data,f,indent=2)
            
            f = open('falldown/all_falldown.json','r')
            self.all_1 = json.load(f)
            f.close()
        else:
            print('Open Camera1 Json File: Success...')
        
        try: 
            f = open('falldown/all_falldown2.json', 'r')
            self.all_2 = json.load(f)
            f.close()
        except:        
            f = open('falldown/all_falldown2.json','w')
            data={}
            json.dump(data,f,indent=2)
            
            f = open('falldown/all_falldown2.json','r')
            self.all_2 = json.load(f)
            f.close()
        else:
            print('Open Camera2 Json File: Success...')
        
        try:
            f = open('falldown/all_falldown3.json', 'r')
            self.all_3 = json.load(f)
            f.close()
        except:
            f = open('falldown/all_falldown3.json','w')
            data={}
            json.dump(data,f,indent=2)
            
            f = open('falldown/all_falldown3.json','r')
            self.all_3 = json.load(f)
            f.close()
        else:
            print('Open Camera3 Json File: Success...')
        
        try:
            f = open('falldown/all_falldown4.json', 'r')
            self.all_4 = json.load(f)
            f.close()
        except:
            f = open('falldown/all_falldown4.json','w')
            data={}
            json.dump(data,f,indent=2)
            
            f = open('falldown/all_falldown4.json','r')
            self.all_4 = json.load(f)
            f.close()
        else:
            print('Open Camera4 Json File: Success...')

    def setup_control(self):
        '''
        Initial button Count and stack
        '''
        self.ui.start.clicked.connect(self.searchReady)
        self.ui.output.clicked.connect(self.outputXlsx)

        self.ui.startdate.setMaximumDate(QDate.currentDate())

        self.ui.enddate.setDateTime(QtCore.QDateTime(QtCore.QDate.currentDate(), QtCore.QTime(0, 0, 0)))
        self.ui.endtime.setDateTime(QtCore.QDateTime(QtCore.QDate.currentDate(), QtCore.QTime(17, 0, 0)))
        self.ui.enddate.setMaximumDate(QDate.currentDate())

    def do_action(self):

        if math.floor(self.ui.verticalScrollBar.value()/175) > self.awal :
            self.awal+=1
            try:
                self.makeperSeven(self.newresult[-(self.awal+5)])
            except:
                return

    def findChannel(self, filename):
        channel = filename.split("_")[2]
        return int(channel[-1])
  
    def openJson(self, channel):
        if channel == 1:
            f = open('./falldown/all_falldown.json', 'r')
            data = json.load(f)
            f.close()
        elif channel == 2:
            f = open('./falldown/all_falldown2.json', 'r')
            data = json.load(f)
            f.close()
        elif channel == 3:
            f = open('./falldown/all_falldown3.json', 'r')
            data = json.load(f)
            f.close()
        elif channel == 4:
            f = open('./falldown/all_falldown4.json', 'r')
            data = json.load(f)
            f.close()
            
        return data
  
    def outputXlsx(self):
        '''
        Output all Data to Excel 
        Information: id, picture, channel, time, helmet, mask, vest, status
        '''
        # Create an new Excel file and add a worksheet.
        workbook = xlsxwriter.Workbook('output.xlsx')
        worksheet = workbook.add_worksheet()

        worksheet.write('C2', '搜尋統計表')
        worksheet.write('C3', '開始時間')
        worksheet.write('C4', '結束時間')
        worksheet.write('D2', '時間')
        worksheet.write('E2', 'Total')
        worksheet.write('F2', 'Lie Down')
        worksheet.write('G2', 'Squat')
        worksheet.write('H2', 'Sit')
        worksheet.write('I2', 'chk')

        # Widen the first column to make the text clearer.
        worksheet.set_column('B:B', 45)
        worksheet.set_column('C:C', 20)
        worksheet.set_column('D:D', 20)
        worksheet.set_column('E:E', 15)
        worksheet.set_column('F:F', 10)
        worksheet.write('A6', '序號')
        worksheet.write('B6', '圖片')
        worksheet.write('C6', 'Date')
        worksheet.write('D6', 'Time')
        worksheet.write('E6', 'Event')
        worksheet.write('F6', 'Camera')

        startime    = self.ui.startdate.text()  +  ' '  + self.ui.starttime.text()
        endtime     = self.ui.enddate.text()    +  ' '  + self.ui.endtime.text()
        start       = datetime.strptime(startime, "%Y / %m / %d %H:%M") 
        end         = datetime.strptime(endtime,"%Y / %m / %d %H:%M")

        worksheet.write('D3', start.strftime("%Y-%m-%d %H:%M:%S"))
        worksheet.write('D4', end.strftime("%Y-%m-%d %H:%M:%S"))
        
        rows = [0, 0]


        lie_down,chk,sit,squat = 0,0,0,0
        for filename in self.Searchresult:
            data = self.openJson(self.findChannel(filename))
            position = rows[0]*20+7
            Event = data[filename[:-4]]['event']
            Time = data[filename[:-4]]['time']
            Date = data[filename[:-4]]['date']
            Channel = f"Camera {data[filename[:-4]]['channel']}"
            image_path = os.path.join('./falldown/cut',filename)
            worksheet.write('A{}'.format(position), str(rows[0]+1))
            worksheet.insert_image('B{}'.format(position), image_path, {'x_scale': 0.6, 'y_scale': 0.6})
            worksheet.write('C{}'.format(position), Date)
            worksheet.write('D{}'.format(position), Time)
            worksheet.write('E{}'.format(position), Event)
            worksheet.write('F{}'.format(position), Channel)
            
            if Event == "Sit":
                sit +=1
            elif Event == "Lie Down":
                lie_down += 1
            elif Event == "chk":
                chk +=1
            else:
                squat +=1
            
            rows[0]+=1
            
        worksheet.write('E3', str(len(self.Searchresult)))
        worksheet.write('F3', str(lie_down))
        worksheet.write('G3', str(squat))
        worksheet.write('H3', str(sit))
        worksheet.write('I3', str(chk))
        workbook.close()

        excelPath = "/home/nvidia/Desktop/fall_v.5_pp_API/output.xlsx"
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')

        shutil.copyfile(excelPath, os.path.join(folder,excelPath))

    def img2pyqt(self,img,label):
        '''
        Transfer img to pyqt
        '''
        frame = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        temp = QImage(frame,frame.shape[1],frame.shape[0],frame.shape[1]*3,QImage.Format_RGB888)
        pixmap_src = QPixmap.fromImage(temp).scaled(label.width(),label.height())
        return pixmap_src
        
    def noresult(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        
        msg.setText("No Result")
        msg.setWindowTitle("Warning")
        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)        
 
        retval = msg.exec_()
    
    def time(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        
        msg.setText("Start time is bigger than End time")
        msg.setWindowTitle("Warning")
        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)        
 
        retval = msg.exec_()
    
    def fromfilename(sel,filename):
        date = filename.split("_")[0]
        date = date[0:4] + "-" + date[4:6] + "-" + date[6:8]
        
        time = filename.split("_")[1]
        
        channel = filename.split("_")[2]
        channel = channel[-1]   

        event = "falldown"
        
        return event,time,date,channel
    
    def img2pyqt(self,img,label):
        '''
        convert the opencv format to pyqt format color
        '''
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        temp = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1]*3, QtGui.QImage.Format_RGB888)
        return QtGui.QPixmap.fromImage(temp).scaled(label.width(), label.height())

    def setIcon(self):
        for index,i in enumerate(self.box):
            try:
                filename = self.Searchresult[-(self.awal+index)]
                i.label.setIcon(QtGui.QIcon(os.path.join(self.path,filename)))
                i.label.setIconSize(QtCore.QSize(400,200))
                i.label.clicked.connect(lambda _, text= filename : self.showDetail(text))
                cut = cv2.imread(os.path.join(self.pathcut,filename))
                i.labelcut.setPixmap(self.img2pyqt(cut, i.labelcut))
                event,date,time,channel = self.fromfilename(filename)
                i.information.setText(textforstat(event,date,time,channel))
            except:
                i.label.setIcon(QtGui.QIcon("./ROI/Camera1/blank.jpg"))
                i.labelcut.setPixmap(self.img2pyqt(self.blank, i.labelcut))
                i.information.setText("")

    def clearResult(self):
        for i in self.box:
            i.label.setIcon(QtGui.QIcon("./ROI/Camera1/blank.jpg"))
            i.labelcut.setPixmap(self.img2pyqt(self.blank, i.labelcut))
            i.information.setText("")

    def searchReady(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.Searchresult.clear()
        self.mainSearch()
        self.awal = 1
        toLog("Search Fall down results")
        if len(self.Searchresult) == 0 :
            self.noresult()
            self.clearResult()
            self.ui.labelPage.setText(f"0 / 0")
        else:
            self.setIcon()
            self.ui.labelPage.setText(f" 1 / {math.ceil(len(self.Searchresult)/16)}")
        QtWidgets.QApplication.restoreOverrideCursor()

    def mainSearch(self):
        
        import os
        '''
            main function
            compare the file time with start/end time
            and use counter to find each filename in allFilename
            if pass the filter -> set icon, text and search next person
        '''
        
        startTime       = datetime.strptime(self.ui.startdate.text()  +  ' '  + self.ui.starttime.text() , "%Y / %m / %d %H:%M") 
        endTime         = datetime.strptime(self.ui.enddate.text()    +  ' '  + self.ui.endtime.text(),"%Y / %m / %d %H:%M")   
    
        if endTime < startTime:
            self.time()
                        
        if self.ui.channel.currentText() == 'All':
            data = {}
            data.update(self.all_1)
            data.update(self.all_2)
            data.update(self.all_3)
            data.update(self.all_4)
            
        else:
            if self.ui.channel.currentText()[-1] == str(1):
                data = self.all_1
            elif self.ui.channel.currentText()[-1] == str(2):
                data = self.all_2
            elif self.ui.channel.currentText()[-1] == str(3):
                data = self.all_3
            elif self.ui.channel.currentText()[-1] == str(4):
                data = self.all_4
        
        for key in data:
            searchTime = datetime.strptime(data[key]['date'] + ' '+ data[key]['time'][:-3], "%Y-%m-%d %H:%M")
            if (startTime<searchTime) and (searchTime<endTime):
                if self.ui.type.currentText() == str(data[key]['event']):
                    self.Searchresult.append(key+".jpg")
                elif self.ui.type.currentText() == 'All':
                    self.Searchresult.append(key+".jpg")
        self.Searchresult.sort()
        self.ui.total.setText(str(len(self.Searchresult)))
        

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SearchPerson()
    window.showFullScreen()
    sys.exit(app.exec_())
