from PyQt5 import QtWidgets
from newsettingmain import Ui_MainWindow
from allutility.httpUtil import get, getIpAddr, put
from utility import toLog
from allutility.factoryreset import FactoryReset

import json
import csv
from datetime import datetime

SERVER_GIVE_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiZmFjZWFpIl0sInNjb3BlIjpbImFwaS1zZXJ2aWNlIl0sImV4cCI6MTkyMTE1MzI1OCwiYXV0aG9yaXRpZXMiOlsiYWl1bmlvbiJdLCJqdGkiOiI3ODI3YTBkYi0zMGQ3LTRhODItYjQyYy0yMTQ0NTMyZWRlNDEiLCJjbGllbnRfaWQiOiJhcGktY2xpZW50In0.mE8WnaGzVuWhS5LfT0ajQcBr_JP2TUOVfhch-5dJ6mA'

class SystemSet(QtWidgets.QMainWindow):
    def __init__(self,mainwindow):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(mainwindow)
        
        self.setup_control()

    def setup_control(self):
        
        self.ui.start.clicked.connect(self.buttonClicked)
        self.ui.back.clicked.connect(self.backup)
        self.ui.sync.clicked.connect(self.checkSync)
        self.ui.pushButtonReset.clicked.connect(self.factoryReset)
        
        self.setSync()
        self.setupData()
        
    def factoryReset(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        msg.setText("Are you sure want to reset the machine?")

        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        retval = msg.exec_()

        if retval == QtWidgets.QMessageBox.Ok:
            FactoryReset()

    def setupData(self):
        try:
            f = open('config2Channels.json', 'r')
            self.data = json.load(f)
            f.close()
        except:
            f = open('./factoryreset/config2Channels.json','r')
            data = json.load(f)
            f.close()
            
            self.data = data
            
            f = open('config2Channels.json', 'w')
            json.dump(self.data,f,indent=2)
            f.close()

        self.ui.toggle_IO_3.setEnabled(False)
        self.ui.toggle_IO_4.setEnabled(False)
        self.ui.ROI_onButton_3.setEnabled(False)
        self.ui.ROI_onButton_4.setEnabled(False)

        self.check_CR()
        self.backup()

    def setSync(self):
        self.Inputlist = [self.ui.place1, self.ui.ip1, self.ui.password1, self.ui.password1_2, self.ui.place2, self.ui.ip2, self.ui.password3, 
        self.ui.password4, self.ui.place3, self.ui.ip3, self.ui.password_new1, self.ui.password1_new2, 
        self.ui.place4, self.ui.ip4, self.ui.password_new3, self.ui.password_new4, self.ui.ROI_onButton,self.ui.toggle_IO,self.ui.ROI_onButton2,self.ui.ROI_onButton_3,
        self.ui.ROI_onButton_4, self.ui.toggle_IO_2, self.ui.toggle_IO_3, self.ui.toggle_IO_4, self.ui.back, self.ui.start]
        self.ui.sync.setChecked(True)
        for i in self.Inputlist:
            i.setEnabled(False)

    def checkSync(self):
        if self.ui.sync.isChecked():
            for i in self.Inputlist:
                i.setEnabled(False)
            toLog("Camera Settings from device disabled")
        else:
            for i in self.Inputlist:
                i.setEnabled(True)
            toLog("Camera Settings from device enabled")
    
    def ChannelOn(self):

        if self.ui.toggle_IO.isChecked():
            self.data['channel1']['active'] = True
        else:
            self.data['channel1']['active'] = False
            

        if self.ui.toggle_IO_2.isChecked():
            self.data['channel2']['active'] = True
        else:
            self.data['channel2']['active'] = False
            

        if self.ui.toggle_IO_3.isChecked():
            self.data['channel3']['active'] = True           
        else:
            self.data['channel3']['active'] = False
            

        if self.ui.toggle_IO_4.isChecked():
            self.data['channel4']['active'] = True
        else:
            self.data['channel4']['active'] = False
        
    def check_CR(self):
        self.checkChannel()
        self.checkradio()
        
    def checkChannel(self):

        if self.data['channel1']['active']:
            self.ui.toggle_IO.setChecked(True)
        else :
            self.ui.toggle_IO.setChecked(False)
            
        if self.data['channel2']['active']:
            self.ui.toggle_IO_2.setChecked(True)
        else:
            self.ui.toggle_IO_2.setChecked(False)
            
        if self.data['channel3']['active']:
            self.ui.toggle_IO_3.setChecked(True)
        else:
            self.ui.toggle_IO_3.setChecked(False)
            
        if self.data['channel4']['active']:
            self.ui.toggle_IO_4.setChecked(True)
        else:
            self.ui.toggle_IO_4.setChecked(False)
        
    def checkradio(self):
        f = open('config2Channels.json', 'r')
        data = json.load(f)
        f.close()
        if data['channel1']["ROI"]:
            self.ui.ROI_onButton.setChecked(True)
        else:
            self.ui.ROI_onButton.setChecked(False)
        if data['channel2']["ROI"]:
            self.ui.ROI_onButton2.setChecked(True)
        else:
            self.ui.ROI_onButton2.setChecked(False)
        if data['channel3']['ROI']:
            self.ui.ROI_onButton_3.setChecked(True)
        else:
            self.ui.ROI_onButton_3.setChecked(False)
        if data['channel4']['ROI']:
            self.ui.ROI_onButton_4.setChecked(True)
        else:
            self.ui.ROI_onButton_4.setChecked(False)

    def checkRoi(self):
        
        if self.ui.ROI_onButton.isChecked():
            self.data['channel1']['ROI'] = True
            self.data['channel1']['change'] = True
        else:
            self.data['channel1']['ROI'] = False
            self.data['channel1']['change'] = True
            
        if self.ui.ROI_onButton2.isChecked():
            self.data['channel2']['ROI'] = True
            self.data['channel2']['change'] = True
        else:
            self.data['channel2']['ROI'] = False
            self.data['channel2']['change'] = True
            
        if self.ui.ROI_onButton_3.isChecked():
            self.data['channel3']['ROI'] = True
            self.data['channel3']['change'] = True
        else:
            self.data['channel3']['ROI'] = False
            self.data['channel3']['change'] = True
            
        if self.ui.ROI_onButton_4.isChecked():
            self.data['channel4']['ROI'] = True
            self.data['channel4']['change'] = True
        else:
            self.data['channel4']['ROI'] = False
            self.data['channel4']['change'] = True
            
    def accept(self):
        fp  = open('config2Channels_default.json','r')
        data = json.load(fp)
        fp.close()    
        fp = open('config2Channels.json', 'w')
        json.dump(data, fp, indent=2)
        fp.close()
        fp  = open('function_default.json','r')
        data = json.load(fp)
        fp.close()    
        fp = open('function.json', 'w')
        json.dump(data, fp, indent=2)
        fp.close()

    def backup(self):

        f = open('config2Channels.json', 'r')
        content = json.load(f)
        f.close()

        self.ui.place1.setText(content['channel1']['place'])
        self.ui.ip1.setText(content['channel1']['ip'])
        self.ui.password1.setText(content['channel1']['user'])
        self.ui.password1_2.setText(content['channel1']['password'])
        self.ui.place1.setText(content['channel1']['place'])

        self.ui.place2.setText(content['channel2']['place'])
        self.ui.ip2.setText(content['channel2']['ip'])
        self.ui.password3.setText(content['channel2']['user'])
        self.ui.password4.setText(content['channel2']['password'])
        self.ui.place2.setText(content['channel2']['place'])
        
        self.ui.place3.setText(content['channel3']['place'])
        self.ui.ip3.setText(content['channel3']['ip'])
        self.ui.password_new1.setText(content['channel3']['user'])
        self.ui.password1_new2.setText(content['channel3']['password'])
        self.ui.place3.setText(content['channel3']['place'])


        self.ui.place4.setText(content['channel4']['place'])
        self.ui.ip4.setText(content['channel4']['ip'])
        self.ui.password_new3.setText(content['channel4']['user'])
        self.ui.password_new4.setText(content['channel4']['password'])
        self.ui.place4.setText(content['channel4']['place'])
        
        self.check_CR()

    def putAPI(self):
        f = open('json/nxconfig.json','r')
        nxconfig = json.load(f)
        f.close()

        f = open('json/timeTable.json','r')
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
                        'ip': self.data['channel1']['ip'], 
                        'title': self.data['channel1']['place'], 
                        'username': self.data['channel1']['user'], 
                        'password': self.data['channel1']['password'], 
                        'active': self.data['channel1']['active'],
                        'ROI': self.data['channel1']['ROI']},
                    {
                        'ip': self.data['channel2']['ip'], 
                        'title': self.data['channel2']['place'], 
                        'username': self.data['channel2']['user'], 
                        'password': self.data['channel2']['password'], 
                        'active': self.data['channel2']['active'],
                        'ROI': self.data['channel2']['active']},
                    {
                        'ip': self.data['channel3']['ip'], 
                        'title': self.data['channel3']['place'], 
                        'username': self.data['channel3']['user'], 
                        'password': self.data['channel3']['password'], 
                        'active': self.data['channel3']['active'],
                        'ROI': self.data['channel3']['active']},
                    {    
                        'ip': self.data['channel2']['ip'], 
                        'title': self.data['channel2']['place'], 
                        'username': self.data['channel2']['user'], 
                        'password': self.data['channel2']['password'], 
                        'active': self.data['channel2']['active'],
                        'ROI': self.data['channel2']['active']}
                    ],
                'Time-Table': timedata
                }
        }

        put('http://192.168.0.107/api/v2/devices/137',json.dumps(putData),None, SERVER_GIVE_TOKEN)
    
    def buttonClicked(self):
        
        self.data["channel1"]["place"] = self.ui.place1.text()
        self.data["channel1"]["ip"] = self.ui.ip1.text()
        self.data["channel1"]["user"] = self.ui.password1.text()
        self.data["channel1"]["password"] = self.ui.password1_2.text()

        self.data["channel2"]["place"] = self.ui.place2.text()
        self.data["channel2"]["ip"] = self.ui.ip2.text() 
        self.data["channel2"]["user"] = self.ui.password3.text()
        self.data["channel2"]["password"] = self.ui.password4.text()

        
        self.data["channel3"]["place"] = self.ui.place3.text()
        self.data["channel3"]["ip"] = self.ui.ip3.text()
        self.data["channel3"]["user"] = self.ui.password_new1.text()
        self.data["channel3"]["password"] = self.ui.password1_new2.text()

        self.data["channel4"]["place"] = self.ui.place4.text()
        self.data["channel4"]["ip"] = self.ui.ip4.text() 
        self.data["channel4"]["user"] = self.ui.password_new3.text()
        self.data["channel4"]["password"] = self.ui.password_new4.text()
        
        self.data['channel1']['change'] = True
        self.data['channel2']['change'] = True
        self.data['channel3']['change'] = True
        self.data['channel4']['change'] = True
        
        self.ChannelOn()
        self.checkRoi()
        
        f = open('config2Channels.json', 'w')
        json.dump(self.data,f,indent=2)
        f.close()
        
        toLog("Camera Settings Updated")
        self.putAPI()

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SystemSet()
    window.showFullScreen()
    sys.exit(app.exec_())
