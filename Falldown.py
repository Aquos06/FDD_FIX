from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow,QApplication, QShortcut
from PyQt5.QtGui import QKeySequence   
from PyQt5.QtCore import Qt

from mainprotol import Protol
from password import PassWord
from newsearchper import SearchPerson
from set import SystemSet
from set2 import SystemSet2
from function import SettingFunction
from new_main import TwoScreen
from AISetting.AISettings import AiSettings
from ZoomScreen.biggerscreen import biggerScreen
from settings.log import Log
from allutility.utility import toLog

import sys
import json
import sqlite3


class Screen1(QMainWindow):
    def __init__(self):
        super(Screen1,self).__init__()
        protol = Protol()
        protol.setupUi(self)
        protol.settingButton.clicked.connect(self.gotosettingscreen)
        protol.searchButton.clicked.connect(self.gotosearchscreen)
        protol.ppeButton.clicked.connect(self.gotocctvscreen)
        
        def foo1(*args,**kwargs):
            self.gotosearchscreen()
            
        def foo2(*args,**kwargs):
            Maincctv.resumeThread()
            self.gotocctvscreen()
            
        def foo3(*args,**kwargs):
            self.gotosettingscreen()

        protol.label_2.mouseDoubleClickEvent = foo1
        protol.label.mouseDoubleClickEvent = foo2
        protol.label_6.mouseDoubleClickEvent = foo3
                    
    def gotocctvscreen(self):
        widget.setCurrentWidget(screen2)
    
    def gotosettingscreen(self):
        widget.setCurrentWidget(screen4)
    
    def gotosearchscreen(self):
        widget.setCurrentWidget(screen3)

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.RightButton:
            Maincctv.resumeThread()
            self.gotocctvscreen()

class Screen2(QMainWindow): #CCTV
    def __init__(self):
        super(Screen2,self).__init__()
        
        global Maincctv
        Maincctv= TwoScreen(self)
        f = open("json/personal.json", "r")
        self.data = json.load(f)
        f.close()
        global Settings_4
        Maincctv.worker.ROI = Settings_4.ui.fill_1.ROI.ui.ROILabel
        Maincctv.videoStream.ROI = Settings_4.ui.fill_2.ROI.ui.ROILabel
        Maincctv.videoStream3.ROI = Settings_4.ui.fill_3.ROI.ui.ROILabel
        Maincctv.videoStream4.ROI = Settings_4.ui.fill_4.ROI.ui.ROILabel
        
        Maincctv.login.clicked.connect(self.gotopassword)
        Maincctv.login.setText('Login')
        global Settings_2
        Maincctv.lastSync = Settings_2.ui.syncTime
            
        def foo1(*args, **kwargs):
            f = open('json/config2Channels.json','r')
            data = json.load(f)
            f.close()            
            if data['channel1']['active'] == True:
                global BiggerScreen
                BiggerScreen.ui.label_6.setText('Camera 1')
                Maincctv.zoom_show(1)
                widget.setCurrentWidget(screen9)

        def foo2(*args, **kwargs):
            f = open('json/config2Channels.json','r')
            data = json.load(f)
            f.close()  
            if data['channel2']['active'] == True:
                global BiggerScreen
                BiggerScreen.ui.label_6.setText('Camera 2')
                Maincctv.zoom_show(2)
                widget.setCurrentWidget(screen9)

        def foo3(*args, **kwargs):
            f = open('json/config2Channels.json','r')
            data = json.load(f)
            f.close()  
            if data['channel3']['active'] == True:
                global BiggerScreen
                BiggerScreen.ui.label_6.setText('Camera 3')
                Maincctv.zoom_show(3)
                widget.setCurrentWidget(screen9)

        def foo4(*args, **kwargs):
            f = open('json/config2Channels.json','r')
            data = json.load(f)
            f.close()  
            if data['channel4']['active'] == True:
                global BiggerScreen
                BiggerScreen.ui.label_6.setText('Camera 4')
                Maincctv.zoom_show(4)
                widget.setCurrentWidget(screen9)
            
        def foo5(*args, **kwargs):
            Maincctv.writeFall(0)

        def foo6(*args, **kwargs):
            Maincctv.writeFall(1)

        def foo7(*args, **kwargs):
            Maincctv.writeFall(2)

        def foo8(*args, **kwargs):
            Maincctv.writeFall(3)

        Maincctv.lchannel1.mouseDoubleClickEvent = foo1
        Maincctv.lchannel2.mouseDoubleClickEvent = foo2
        Maincctv.lchannel3.mouseDoubleClickEvent = foo3
        Maincctv.lchannel4.mouseDoubleClickEvent = foo4

        Maincctv.lchannel1.mousePressEvent = foo5
        Maincctv.lchannel2.mousePressEvent = foo6
        Maincctv.lchannel3.mousePressEvent = foo7
        Maincctv.lchannel4.mousePressEvent = foo8
        
    def gotoprotol(self):
        Maincctv.stopThread()
        widget.setCurrentWidget(screen1)
        widget.showFullScreen()

    def gotopassword(self):
        widget.setCurrentWidget(screen6)
        widget.showFullScreen()
    
    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.RightButton:
            Maincctv.label_6.setText('')
            Maincctv.label.setText('')

class Screen3(QMainWindow): #search
    def __init__(self):
        super(Screen3,self).__init__()
        global Search
        Search = SearchPerson(self)
        Search.ui.pushButton_6.clicked.connect(self.gotoprotol)
        Search.ui.pushButton_7.clicked.connect(self.gotosetting)
        Search.ui.pushButton_8.clicked.connect(self.gotocctvscreen)
        Search.ui.ppe.clicked.connect(self.gotoprotol)

    def gotoprotol(self):
        widget.setCurrentWidget(screen1)

    def gotosetting(self):
        widget.setCurrentWidget(screen4)
    
    def gotocctvscreen(self):
        Maincctv.resumeThread()
        widget.setCurrentWidget(screen2)

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.RightButton:
            self.gotoprotol()

class Screen4(QMainWindow): #settings
    def __init__(self):
        super(Screen4,self).__init__()

        global Settings_1
        Settings_1 = SystemSet(self)
        Settings_1.setupData()
        Settings_1.ui.pushButton_6.clicked.connect(self.gotoprotol)
        Settings_1.ui.pushButton_3.clicked.connect(self.gotofunctionset)
        Settings_1.ui.pushButton_search.clicked.connect(self.gotosearch)
        Settings_1.ui.pushButton_8.clicked.connect(self.gotocctvscreen)
        Settings_1.ui.pushButton_0.clicked.connect(self.goto34)
        Settings_1.ui.pushButton_4.clicked.connect(self.gotoAISet)
        Settings_1.ui.ppe.clicked.connect(self.gotoprotol)
        Settings_1.ui.pushButton_5.clicked.connect(self.gotoLog)

    def gotoLog(self):
        widget.setCurrentWidget(screen10)

    def gotoAISet(self):
        widget.setCurrentWidget(screen8)
        
    def gotoprotol(self):      
        widget.setCurrentWidget(screen1)

    def gotosearch(self):
        widget.setCurrentWidget(screen3)

    def gotofunctionset(self):
        widget.setCurrentWidget(screen5)
    
    def gotocctvscreen(self):
        Maincctv.resumeThread()
        widget.setCurrentWidget(screen2)
        
    def goto34(self):
        widget.setCurrentWidget(screen7)

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.RightButton:
            self.gotoprotol()

class Screen5(QMainWindow):
    def __init__(self):
        super(Screen5,self).__init__()
        global Settings_3
        Settings_3 = SettingFunction(self)
        Settings_3.backup_function()
        Settings_3.ui.pushButton_6.clicked.connect(self.gotoprotol)
        Settings_3.ui.pushButton_search.clicked.connect(self.gotosearch)
        Settings_3.ui.pushButton_2.clicked.connect(self.gotosystemset)
        Settings_3.ui.pushButton_8.clicked.connect(self.gotocctvscreen)
        Settings_3.ui.pushButton_0.clicked.connect(self.goto34)
        Settings_3.ui.pushButton_4.clicked.connect(self.gotoAISet)
        Settings_3.ui.pushButton_5.clicked.connect(self.gotoLog)

    def gotoLog(self):
        widget.setCurrentWidget(screen10)
        
    def gotoAISet(self):
        widget.setCurrentWidget(screen8)
        
    def gotoprotol(self):         
        widget.setCurrentWidget(screen1)

    def gotosearch(self):
        widget.setCurrentWidget(screen3)

    def gotosystemset(self):
        widget.setCurrentWidget(screen4)
    
    def gotocctvscreen(self):
        Maincctv.resumeThread()
        widget.setCurrentWidget(screen2)
        
    def goto34(self):
        widget.setCurrentWidget(screen7)

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.RightButton:
            self.gotoprotol()
    
class Screen6(QMainWindow): #password
    def __init__(self):
        super(Screen6,self).__init__()
        self.uipass = PassWord()
        self.uipass.setupUi(self)
        self.uipass.pushButton_5.clicked.connect(self.gotonext)
        self.uipass.pushButton_4.clicked.connect(self.gotoprotol)
        enter = QShortcut(QKeySequence(Qt.Key_Return), self)
        enter.activated.connect(self.gotonext)

    def gotonext(self):
        if self.uipass.lineEdit_3.text() == 'admin' and self.uipass.lineEdit_4.text() == 'admin':

            f = open('json/personal.json', 'r')
            self.data = json.load(f)
            f.close()
            
            self.data['loggedIn'] = True
            
            f = open('json/personal.json', 'w')
            json.dump(self.data,f,indent=2)
            f.close()
            
            self.uipass.passworderror.setText('')
            self.uipass.lineEdit_3.clear()
            self.uipass.lineEdit_4.clear()
            
            widget.setCurrentWidget(screen2)

            Maincctv.login.setText('Home')
            Maincctv.login.clicked.connect(screen2.gotoprotol)

            toLog("Admin Log In")
        else:
            self.uipass.passworderror.setText('password error') 

    def gotoprotol(self):        
        widget.setCurrentWidget(screen1)
        
class Screen7(QMainWindow): 
    def __init__(self):
        super(Screen7,self).__init__()
        global Settings_2
        Settings_2 = SystemSet2(self)
        Settings_2.setupData()
        Settings_2.ui.pushButton_6.clicked.connect(self.gotoprotol)
        Settings_2.ui.pushButton_search.clicked.connect(self.gotosearch)
        Settings_2.ui.pushButton_3.clicked.connect(self.gotofunctionset)
        Settings_2.ui.pushButton_2.clicked.connect(self.gotosystemset)
        Settings_2.ui.pushButton_8.clicked.connect(self.gotocctvscreen)
        Settings_2.ui.pushButton_4.clicked.connect(self.gotoAISet)
        Settings_2.ui.pushButton_5.clicked.connect(self.gotoLog)

    def gotoLog(self):
        widget.setCurrentWidget(screen10)

    def gotoAISet(self):
        widget.setCurrentWidget(screen8)

    def gotoprotol(self):  
        widget.setCurrentWidget(screen1)

    def gotosearch(self):
        widget.setCurrentWidget(screen3)

    def gotofunctionset(self):
        widget.setCurrentWidget(screen5)
    
    def gotocctvscreen(self):
        Maincctv.resumeThread()
        widget.setCurrentWidget(screen2)
        
    def gotosystemset(self):
        widget.setCurrentWidget(screen4)

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.RightButton:
            self.gotoprotol()
        
class Screen8(QMainWindow): #AI settings
    def __init__(self):
        super(Screen8, self).__init__()
        global Settings_4
        Settings_4 = AiSettings(self)
        Settings_4.setupData()
        Settings_4.ui.pushButton_6.clicked.connect(self.gotoprotol)
        Settings_4.ui.pushButton_search.clicked.connect(self.gotosearch)
        Settings_4.ui.pushButton_3.clicked.connect(self.gotofunctionset)
        Settings_4.ui.pushButton_0.clicked.connect(self.goto34)
        Settings_4.ui.pushButton_2.clicked.connect(self.gotosystemset)
        Settings_4.ui.pushButton_8.clicked.connect(self.gotocctvscreen)
        Settings_4.ui.pushButton_5.clicked.connect(self.gotoLog)

    def goto34(self):
        widget.setCurrentWidget(screen7)

    def gotoLog(self):
        widget.setCurrentWidget(screen10)
        
    def gotoprotol(self): 
        widget.setCurrentWidget(screen1)

    def gotosearch(self):
        widget.setCurrentWidget(screen3)

    def gotofunctionset(self):
        widget.setCurrentWidget(screen5)
    
    def gotocctvscreen(self):
        Maincctv.resumeThread()
        widget.setCurrentWidget(screen2)
        
    def gotosystemset(self):
        widget.setCurrentWidget(screen4) 

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.RightButton:
            self.gotoprotol() 
        
class Screen9(QMainWindow):
    def __init__(self):
        super(Screen9,self).__init__()
        global BiggerScreen
        global Maincctv
        BiggerScreen = biggerScreen(self)
        BiggerScreen.ui.layout = Maincctv.layout
        BiggerScreen.ui.login.clicked.connect(self.goBack)
        
        Maincctv.worker1.screen = BiggerScreen.ui.screen
        Maincctv.layoutbig = BiggerScreen.ui.layout
        
    def goBack(self):
        Maincctv.back()
        widget.setCurrentWidget(screen2)

class Screen10(QMainWindow):
    def __init__(self):
        super(Screen10, self).__init__()
        global log
        log = Log(self)
        log.ui.pushButton_6.clicked.connect(self.gotoprotol)
        log.ui.pushButton_search.clicked.connect(self.gotosearch)
        log.ui.pushButton_3.clicked.connect(self.gotofunctionset)
        log.ui.pushButton_2.clicked.connect(self.gotosystemset)
        log.ui.pushButton_0.clicked.connect(self.gotoDevice)
        log.ui.pushButton_8.clicked.connect(self.gotocctvscreen)
        log.ui.pushButton_4.clicked.connect(self.gotoAISet)

    def gotoDevice(self):
        widget.setCurrentWidget(screen7)
        
    def gotoprotol(self): 
        widget.setCurrentWidget(screen1)

    def gotosearch(self):
        widget.setCurrentWidget(screen3)

    def gotofunctionset(self):
        widget.setCurrentWidget(screen5)
    
    def gotocctvscreen(self):
        Maincctv.resumeThread()
        widget.setCurrentWidget(screen2)

    def gotosystemset(self):
        widget.setCurrentWidget(screen4)

    def gotoAISet(self):
        widget.setCurrentWidget(screen8)

    def mousePressEvent(self, event):
        if event.buttons() == QtCore.Qt.RightButton:
            self.gotoprotol()

app=QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()

screen1 = Screen1() #protol
screen7 = Screen7() #Device settings
screen8 = Screen8() #AI Settings
screen2 = Screen2() #maincctv
screen3 = Screen3() #search
screen4 = Screen4() #camera Settings
screen5 = Screen5() #function
screen6 = Screen6() #password
screen9 = Screen9() #Zoom screen
screen10 = Screen10() #log Screen

widget.addWidget(screen1)
widget.addWidget(screen2)
widget.addWidget(screen3)
widget.addWidget(screen4)
widget.addWidget(screen5)
widget.addWidget(screen6)
widget.addWidget(screen7)
widget.addWidget(screen8)
widget.addWidget(screen9)
widget.addWidget(screen10)

widget.setCurrentWidget(screen2)
widget.showFullScreen()

sys.exit(app.exec_())