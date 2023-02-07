from .TimeTable import TimeTable
import json 
from PyQt5 import QtWidgets
from utility import toLog
from httpUtil import put

SERVER_GIVE_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiZmFjZWFpIl0sInNjb3BlIjpbImFwaS1zZXJ2aWNlIl0sImV4cCI6MTkyMTE1MzI1OCwiYXV0aG9yaXRpZXMiOlsiYWl1bmlvbiJdLCJqdGkiOiI3ODI3YTBkYi0zMGQ3LTRhODItYjQyYy0yMTQ0NTMyZWRlNDEiLCJjbGllbnRfaWQiOiJhcGktY2xpZW50In0.mE8WnaGzVuWhS5LfT0ajQcBr_JP2TUOVfhch-5dJ6mA'

class TimeSelect(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.ui = TimeTable()
        self.ui.setupUi()
        
        
        self.button1 = [self.ui.camera1_0, self.ui.camera1_1, self.ui.camera1_2, self.ui.camera1_3, self.ui.camera1_4, self.ui.camera1_5,
                        self.ui.camera1_6, self.ui.camera1_7, self.ui.camera1_8, self.ui.camera1_9, self.ui.camera1_10, self.ui.camera1_11,
                        self.ui.camera1_12, self.ui.camera1_13, self.ui.camera1_14, self.ui.camera1_15, self.ui.camera1_16, self.ui.camera1_17,
                        self.ui.camera1_18, self.ui.camera1_19, self.ui.camera1_20, self.ui.camera1_21, self.ui.camera1_22, self.ui.camera1_23,
                        self.ui.camera1_24]

        self.button2 = [self.ui.camera2_0, self.ui.camera2_1, self.ui.camera2_2, self.ui.camera2_3, self.ui.camera2_4, self.ui.camera2_5,
                        self.ui.camera2_6, self.ui.camera2_7, self.ui.camera2_8, self.ui.camera2_9, self.ui.camera2_10, self.ui.camera2_11,
                        self.ui.camera2_12, self.ui.camera2_13, self.ui.camera2_14, self.ui.camera2_15, self.ui.camera2_16, self.ui.camera2_17,
                        self.ui.camera2_18, self.ui.camera2_19, self.ui.camera2_20, self.ui.camera2_21, self.ui.camera2_22, self.ui.camera2_23,
                        self.ui.camera2_24]
        
        self.button3 = [self.ui.camera3_0, self.ui.camera3_1, self.ui.camera3_2, self.ui.camera3_3, self.ui.camera3_4, self.ui.camera3_5,
                        self.ui.camera3_6, self.ui.camera3_7, self.ui.camera3_8, self.ui.camera3_9, self.ui.camera3_10, self.ui.camera3_11,
                        self.ui.camera3_12, self.ui.camera3_13, self.ui.camera3_14, self.ui.camera3_15, self.ui.camera3_16, self.ui.camera3_17,
                        self.ui.camera3_18, self.ui.camera3_19, self.ui.camera3_20, self.ui.camera3_21, self.ui.camera3_22, self.ui.camera3_23,
                        self.ui.camera3_24]
        
        self.button4 = [self.ui.camera4_0, self.ui.camera4_1, self.ui.camera4_2, self.ui.camera4_3, self.ui.camera4_4, self.ui.camera4_5,
                        self.ui.camera4_6, self.ui.camera4_7, self.ui.camera4_8, self.ui.camera4_9, self.ui.camera4_10, self.ui.camera4_11,
                        self.ui.camera4_12, self.ui.camera4_13, self.ui.camera4_14, self.ui.camera4_15, self.ui.camera4_16, self.ui.camera4_17,
                        self.ui.camera4_18, self.ui.camera4_19, self.ui.camera4_20, self.ui.camera4_21, self.ui.camera4_22, self.ui.camera4_23,
                        self.ui.camera4_24]
        
        self.flag_1 = False
        self.flag_2 = False
        self.flag_3 = False
        self.flag_4 = False

        for index,i in enumerate(self.button3):
            i.clicked.connect(self.disable3)
        
        for index,i in enumerate(self.button1):
            i.clicked.connect(self.disable1)

        for index,i in enumerate(self.button2):
            i.clicked.connect(self.disable2)

        for index,i in enumerate(self.button4):
            i.clicked.connect(self.disable4)

        self.ui.buttonOK.clicked.connect(self.save)
        self.ui.cancelButton.clicked.connect(self.closewindow)
        self.ui.camera1_all.clicked.connect(self.allcheck1)
        self.ui.camera2_all.clicked.connect(self.allcheck2)
        self.ui.camera3_all.clicked.connect(self.allcheck3)
        self.ui.camera4_all.clicked.connect(self.allcheck4)


    def disable1(self):
        self.ui.camera1_all.setChecked(False)

    def disable2(self):
        self.ui.camera2_all.setChecked(False)

    def disable3(self):
        self.ui.camera3_all.setChecked(False)

    def disable4(self):
        self.ui.camera4_all.setChecked(False)
        
    def setupUI(self,day):
        
        self.day = day
        f = open('json/timeTable.json' , 'r')
        data = json.load(f)
        f.close()
        
        if data[self.day]['Camera1']['all'] == True:
            self.flag_1 = True
            self.ui.camera1_all.setChecked(True)
            for i in self.button1:
                i.setChecked(True)
                
        else:
            for index, i in enumerate(data[self.day]['Camera1']['hour']):
                if i == 1:
                    self.button1[index].setChecked(True)
                else:
                    self.button1[index].setChecked(False)
                    
                    
        if data[self.day]['Camera2']['all'] == True:
            self.flag_2 = True
            self.ui.camera2_all.setChecked(True)
            for i in self.button2:
                i.setChecked(True)
        
        else:
            for index, i in enumerate(data[self.day]['Camera2']['hour']):
                if i == 1:
                    self.button2[index].setChecked(True)
                else:
                    self.button2[index].setChecked(False)
        
        if data[self.day]['Camera3']['all'] == True:
            self.flag_3 = True
            self.ui.camera3_all.setChecked(True)
            for i in self.button3:
                i.setChecked(True)
       
        else:
            for index, i in enumerate(data[self.day]['Camera3']['hour']):
                if i == 1:
                    self.button3[index].setChecked(True)
                else:
                    self.button3[index].isChecked(False)

        if data[self.day]['Camera4']['all'] == True:
            self.flag_4 = True
            self.ui.camera4_all.setChecked(True)
            for i in self.button4:
                i.setChecked(True)

        else:
            for index, i in enumerate(data[self.day]['Camera4']['hour']):
                if i == 1:
                    self.button4[index].setChecked(True)
                else:
                    self.button4[index].setChecked(False)
                    
    def allcheck1(self):
        if not self.flag_1:
            for i in self.button1:
                i.setChecked(True)
            self.flag_1 = True
        
        else:
            for i in self.button1:
                i.setChecked(False)
            self.flag_1=False
        
    def allcheck2(self):
        if not self.flag_2:
            for i in self.button2:
                i.setChecked(True)
            self.flag_2 = True
        
        else:
            for i in self.button2:
                i.setChecked(False)
            self.flag_2=False    
    
    def allcheck3(self):
        if not self.flag_3:
            for i in self.button3:
                i.setChecked(True)
            self.flag_3 = True
        
        else:
            for i in self.button3:
                i.setChecked(False)
            self.flag_3=False
            
    def allcheck4(self):
        if not self.flag_4:
            for i in self.button4:
                i.setChecked(True)
            self.flag_4 = True
        
        else:
            for i in self.button4:
                i.setChecked(False)
            self.flag_4=False

    def putAPI(self):
        f = open('json/nxconfig.json','r')
        nxconfig = json.load(f)
        f.close()

        f = open('config2Channels.json','r')
        CamConfig = json.load(f)
        f.close()

        f = open('json/timeTable.json', 'r')
        timedata = json.load(f)
        f.close()

        putData = {
            'id': 137, 
            'last_seen': None, 
            'source_url': nxconfig['ipaddress'], 
            'enabled': True, 
            'rtc_enabled': True, 
            'name': '99', 
            'device_type': 'aibox', 
            'category': {'id': 17, 'name': '二樓辦公室', 'enabled': True}, 
            'identity': '', 
            'username': 'admin', 
            'password': 'ai123456',  
            'settings': {
                'camera': [
                    {
                        'ip': CamConfig['channel1']['ip'], 
                        'title': CamConfig['channel1']['place'], 
                        'username': CamConfig['channel1']['user'], 
                        'password': CamConfig['channel1']['password'], 
                        'active': CamConfig['channel1']['active'],
                        'ROI': CamConfig['channel1']['ROI']},
                    {
                        'ip': CamConfig['channel2']['ip'], 
                        'title': CamConfig['channel2']['place'], 
                        'username': CamConfig['channel2']['user'], 
                        'password': CamConfig['channel2']['password'], 
                        'active': CamConfig['channel2']['active'],
                        'ROI': CamConfig['channel2']['active']},
                    {
                        'ip': CamConfig['channel3']['ip'], 
                        'title': CamConfig['channel3']['place'], 
                        'username': CamConfig['channel3']['user'], 
                        'password': CamConfig['channel3']['password'], 
                        'active': CamConfig['channel3']['active'],
                        'ROI': CamConfig['channel3']['active']},
                    {    
                        'ip': CamConfig['channel2']['ip'], 
                        'title': CamConfig['channel2']['place'], 
                        'username': CamConfig['channel2']['user'], 
                        'password': CamConfig['channel2']['password'], 
                        'active': CamConfig['channel2']['active'],
                        'ROI': CamConfig['channel2']['active']}
                    ],
                'Time-Table': timedata
        }
    }

        put('http://192.168.0.107/api/v2/devices/137',json.dumps(putData),None, SERVER_GIVE_TOKEN)

    def save(self):
        f = open('json/timeTable.json', 'r')
        data = json.load(f)
        f.close()

        if self.ui.forALL.isChecked():
            for i in data:
                if self.ui.camera1_all.isChecked():
                    data[i]['Camera1']['all'] = True
                else:
                    data[i]['Camera1']['all'] = False
                    
                    for index,button in enumerate(self.button1):
                        if button.isChecked():
                            data[i]['Camera1']['hour'][index] = 1
                        else:
                            data[i]['Camera1']['hour'][index] = 0
                            
                if self.ui.camera2_all.isChecked():
                    data[i]['Camera2']['all'] = True
                else:
                    data[i]['Camera2']['all'] = False
                    
                    for index,button in enumerate(self.button2):
                        if button.isChecked():
                            data[i]['Camera2']['hour'][index] = 1
                        else:
                            data[i]['Camera2']['hour'][index] = 0
                    
                if self.ui.camera3_all.isChecked():
                    data[i]['Camera3']['all'] = True
                else:
                    data[i]['Camera3']['all'] = False
                    
                    for index,button in enumerate(self.button3):
                        if button.isChecked():
                            data[i]['Camera3']['hour'][index] = 1
                        else:
                            data[i]['Camera3']['hour'][index] = 0
                    
                if self.ui.camera4_all.isChecked():
                    data[i]['Camera4']['all'] = True
                else:
                    data[i]['Camera4']['all'] = False
                    
                    for index,button in enumerate(self.button4):
                        if button.isChecked():
                            data[i]['Camera4']['hour'][index] = 1
                        else:
                            data[i]['Camera4']['hour'][index] = 0
        else: 
            if self.ui.camera1_all.isChecked():
                data[self.day]['Camera1']['all'] = True
            else:
                data[self.day]['Camera1']['all'] = False
                
                for index,i in enumerate(self.button1):
                    if i.isChecked():
                        data[self.day]['Camera1']['hour'][index] = 1
                    else:
                        data[self.day]['Camera1']['hour'][index] = 0
                        
            if self.ui.camera2_all.isChecked():
                data[self.day]['Camera2']['all'] = True
            else:
                data[self.day]['Camera2']['all'] = False
                
                for index,i in enumerate(self.button2):
                    if i.isChecked():
                        data[self.day]['Camera2']['hour'][index] = 1
                    else:
                        data[self.day]['Camera2']['hour'][index] = 0
                
            if self.ui.camera3_all.isChecked():
                data[self.day]['Camera3']['all'] = True
            else:
                data[self.day]['Camera3']['all'] = False
                
                for index,i in enumerate(self.button3):
                    if i.isChecked():
                        data[self.day]['Camera3']['hour'][index] = 1
                    else:
                        data[self.day]['Camera3']['hour'][index] = 0
                
            if self.ui.camera4_all.isChecked():
                data[self.day]['Camera4']['all'] = True
            else:
                data[self.day]['Camera4']['all'] = False
                
                for index,i in enumerate(self.button4):
                    if i.isChecked():
                        data[self.day]['Camera4']['hour'][index] = 1
                    else:
                        data[self.day]['Camera4']['hour'][index] = 0
        
        f = open('json/timeTable.json', 'w')
        json.dump(data,f,indent=2)
        f.close()
        toLog('Detection Schedule is updated')
        self.putAPI()
        self.closewindow()
    
    def closewindow(self):
        self.ui.close()
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TimeSelect()
    ui.ui.show()
    sys.exit(app.exec_())        