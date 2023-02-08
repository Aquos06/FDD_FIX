
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
        self.setup_control()  
        self.awal = 0 #first number to display
        self.now = 0#index displayed in big screen  
        self.everShow = False
        self.range = 10

        self.jsoninit()

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

        self.ui.verticalScrollBar.valueChanged.connect(lambda: self.do_action())
        self.ui.verticalScrollBar.rangeChanged.connect(lambda: self.ui.verticalScrollBar.setMaximum(self.range))
  
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

    def makeperSeven(self,filenames):
        path = './falldown/screenshot'
        pathcut = './falldown/cut'
        vertical = QtWidgets.QVBoxLayout()
        horizontal = QtWidgets.QHBoxLayout()
        horizontal.setSpacing(0)
        for index,i in enumerate(reversed(filenames)):
            if i != str(0):
                box = searchBox()
                box.label.setIcon(QtGui.QIcon(os.path.join(path,i)))
                box.label.setIconSize(QtCore.QSize(400,200))
                box.setMinimumHeight(200)
                box.label.clicked.connect(lambda _, text = i : self.showDetail(text))
                cut = cv2.imread(os.path.join(pathcut,i))
                box.labelcut.setPixmap(self.img2pyqt(cut,box.labelcut))
                event,date,time,channel = self.fromfilename(i)
                box.information.setText(textforstat(event,date,time,channel))
                horizontal.addWidget(box)
            else:
                box = searchBox()
                horizontal.addWidget(box)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        vertical.addLayout(horizontal)
        vertical.addItem(spacerItem)

        vertical.setStretch(0,20)
        vertical.setStretch(1,1)

        self.ui.layout.addLayout(vertical)

    def listtoSeven(self,lists,first, perRow):
        a = np.zeros(((first*perRow)-len(lists))).astype(int)
        b = np.array([lists])
        c = np.append(a,b)

        return c.tolist()

    def setIcon(self):
        perRow = 4
        if len(self.Searchresult) == 0:
            self.noresult()
        else: 
            first = int(len(self.Searchresult)/perRow)+1
            self.newresult = self.listtoSeven(self.Searchresult,first,perRow)
            self.newresult = np.array([self.newresult])
            self.newresult = self.newresult.reshape(first,perRow) #2 dimension array for search box
            for index,i in enumerate(reversed(self.newresult)):
                if index == 6:
                    break
                self.makeperSeven(i)

    def cleardata(self):
        self.Searchresult.clear()
        for i in range(self.ui.layout.count()):
            layout = self.ui.layout.itemAt(i)
            self.clearLabel(self.ui.layout)
            self.ui.layout.removeItem(layout)

    def clearLabel(self,layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    # widget.setParent(None)
                    # widget.close()
                    widget.deleteLater()
                else:
                    self.clearLabel(item.layout())

    def searchReady(self):
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        self.cleardata()
        self.mainSearch()
        toLog("Search Fall down results")
        self.awal = 0
        if len(self.Searchresult) / 4 > 4:
            self.range = ((len(self.Searchresult) / 4)+1) * 180 
        else:
            self.range = 0
        self.setIcon()
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
