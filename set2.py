from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QFileDialog
from newsettingmain2 import Ui_MainWindow
from dialog import Ui_Dialog
from dialogbackup import Ui_Dialogb
from allutility.timeAPI import setTime
from allutility.factoryreset import FactoryReset
from httpUtil import put
from utility import toLog

from contextlib import closing
from socket import socket, AF_INET, SOCK_DGRAM
import struct

import shutil
import os
import json
from time import ctime

from zipfile import ZipFile
SERVER_GIVE_TOKEN = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOlsiZmFjZWFpIl0sInNjb3BlIjpbImFwaS1zZXJ2aWNlIl0sImV4cCI6MTkyMTE1MzI1OCwiYXV0aG9yaXRpZXMiOlsiYWl1bmlvbiJdLCJqdGkiOiI3ODI3YTBkYi0zMGQ3LTRhODItYjQyYy0yMTQ0NTMyZWRlNDEiLCJjbGllbnRfaWQiOiJhcGktY2xpZW50In0.mE8WnaGzVuWhS5LfT0ajQcBr_JP2TUOVfhch-5dJ6mA'

class SystemSet2(QtWidgets.QMainWindow):
    def __init__(self,mainwindow):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(mainwindow)
        self.Dialog = QtWidgets.QDialog()
        self.sub_window = Ui_Dialog() 
        self.sub_window.setupUi(self.Dialog)
        self.Dialogbackup = QtWidgets.QDialog()
        self.backup_window = Ui_Dialogb() 
        self.backup_window.setupUi(self.Dialogbackup)
        self.setup_control()

    def setup_control(self):
        self.ui.start.clicked.connect(self.buttonClicked)
        self.ui.pathButton.clicked.connect(self.browsefile)
        self.ui.pathButton_2.clicked.connect(self.copy)
        self.ui.UpdateButton.clicked.connect(self.update)
        self.ui.TimeButton.clicked.connect(self.setTime)
        self.ui.IPButton.clicked.connect(self.msgIP)
        self.ui.zijiButton.clicked.connect(self.cmdTime)
        self.ui.asyncSwitch.clicked.connect(self.checksync)
        self.ui.spin_time.valueChanged.connect(self.storeTime)
        self.ui.NTPSwitch.clicked.connect(self.NTP)
        self.ui.ManualSwitch.clicked.connect(self.manual)
        self.ui.pushButtonReset.clicked.connect(self.factoryReset)
        self.ui.exportButton.clicked.connect(self.exportConfig)

        self.setupData()

    def exportConfig(self):
        DestFile = QFileDialog.getExistingDirectory(self, "Select Directory")
        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        NewFile = os.path.join(DestFile, "Config")
        os.mkdir(NewFile)

        shutil.copyfile('/home/nvidia/Desktop/fall_v.5_pp_API/config2Channels.json', os.path.join(NewFile,'Config.json'))
        shutil.copyfile('/home/nvidia/Desktop/fall_v.5_pp_API/AiSettings.json', os.path.join(NewFile, 'AiSettings.json'))
        shutil.copyfile('/home/nvidia/Desktop/fall_v.5_pp_API/function.json', os.path.join(NewFile, 'function.json'))
        shutil.copyfile('/home/nvidia/Desktop/fall_v.5_pp_API/json/timeTable.json', os.path.join(NewFile, 'TimeTable.json'))

        QtWidgets.QApplication.restoreOverrideCursor()

        self.exportFinish()

    def exportFinish(self):
        msg = QtWidgets.QMessageBox()

        msg.setText('Export Configuration Finished')
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        retval = msg.exec_()

    def setupData(self):

        f = open('config2Channels.json', 'r')
        data = json.load(f)
        f.close()

        self.ui.spin_time.setValue(data["async"]['time'])
        self.ui.path.setText(data['backup']['user_path'])

        f = open('json/time.json','r')
        data = json.load(f)
        f.close()

        self.ui.TimeInput.setText(data['server'])

        f = open('json/nxconfig.json','r')
        data = json.load(f)
        f.close()
        self.ui.IpInput.setText(data['ipaddress'])

        f = open('config2Channels.json','r')
        data = json.load(f)
        f.close()

        self.ui.syncTime.setText(f"{data['async']['date']} {data['async']['last']}")

        f = open('json/version.json', 'r')
        data = json.load(f)
        f.close()
        
        self.ui.versionLabel.setText(f'Version: {data["version"]}')

    def factoryReset(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        msg.setText("Are you sure want to reset the machine?")

        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        retval = msg.exec_()

        if retval == QtWidgets.QMessageBox.Ok:
            FactoryReset()       

    def NTP(self):
        if self.ui.NTPSwitch.isChecked():
            toLog('Time Synchronization changed to NTP')
            self.ui.ManualSwitch.setChecked(False)
            self.ui.zijiButton.setEnabled(False)
            self.ui.zijiInput.setEnabled(False)
            self.ui.zidateInput.setEnabled(False)
            
            self.ui.TimeInput.setEnabled(True)
            self.ui.TimeButton.setEnabled(True)

        else:
            self.ui.ManualSwitch.setChecked(True)
            self.ui.zijiButton.setEnabled(True)
            self.ui.zijiInput.setEnabled(True)
            self.ui.zidateInput.setEnabled(False)

            self.ui.TimeInput.setEnabled(False)
            self.ui.TimeButton.setEnabled(False)

    def manual(self):
        if self.ui.ManualSwitch.isChecked():
            toLog('Time Synchronization changed to Manual')
            self.ui.NTPSwitch.setChecked(False)
            self.ui.zijiButton.setEnabled(True)
            self.ui.zidateInput.setEnabled(True)
            self.ui.zijiInput.setEnabled(True)

            self.ui.TimeInput.setEnabled(False)
            self.ui.TimeButton.setEnabled(False)
        else:
            self.ui.NTPSwitch.setChecked(True)
            self.ui.zijiButton.setEnabled(False)
            self.ui.zidateInput.setEnabled(False)
            self.ui.zijiInput.setEnabled(False)
            
            self.ui.TimeInput.setEnabled(True)
            self.ui.TimeButton.setEnabled(True)

    def checksync(self):
        f = open('config2Channels.json','r')
        data = json.load(f)
        f.close()
        if self.ui.asyncSwitch.isChecked():
            data["async"]["enable"] = True
        else:
            data["async"]["enable"] = False
        f = open('config2Channels.json','w')
        json.dump(data,f,indent=2)
        f.close()

    def storeTime(self):
        f = open('config2Channels.json', 'r')
        data = json.load(f)
        f.close()

        data["async"]['time'] = self.ui.spin_time.value()

        f = open('config2Channels.json', 'w')
        json.dump(data,f,indent=2)
        f.close()

    def cmdTime(self):
        time = self.ui.zijiInput.text()
        date = self.ui.zidateInput.text()
        dateTime = date + " " + time

        cmd = f'timedatectl  set-time "{dateTime}"'
        os.system(cmd)

        self.msgTime()

    def msgTime(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        msg.setText("Manual Time Change success")
        msg.setWindowTitle("Warning")

        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        retval = msg.exec_()

    def msgIP(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        msg.setText("Are you sure want to change IP address?")
        msg.setWindowTitle("Warning")
        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        retval = msg.exec_()

        if retval == QtWidgets.QMessageBox.Ok:
            self.cmdIP()

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
    

    def cmdIP(self):
        ip = self.ui.IpInput.text()
        cmd = f'sudo ifconfig eth0 {ip} netmask 255.255.255.0'

        f = open('json/nxconfig.json', 'w')
        data = {
            "ipaddress": ip
        }

        json.dump(data,f,indent=2)
        f.close()

        self.putAPI()

        os.system(cmd)


    def testTime(self,server):

        NTP_PACKET_FORMAT = "!12I"
        NTP_DELTA = 2208988800  # 1970-01-01 00:00:00
        NTP_QUERY = b'\x1b' + 47 * b'\0'  

        with closing(socket( AF_INET, SOCK_DGRAM)) as s:
            s.sendto(NTP_QUERY, (server, 123))
            s.settimeout(1)
            msg, address = s.recvfrom(1024)
        unpacked = struct.unpack(NTP_PACKET_FORMAT,
                    msg[0:struct.calcsize(NTP_PACKET_FORMAT)])
        return unpacked[10] + float(unpacked[11]) / 2**32 - NTP_DELTA

    def timeError(self):
        msg= QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        
        msg.setText("Time server is not found")
        msg.setWindowTitle("Warning")
        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        retval = msg.exec_()

    def timeSuccess(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        msg.setText("IP Time Server Changed")
        msg.setWindowTitle("Warning")

        msg.setStandardButtons(QtWidgets.QMessageBox.Ok)

        retval = msg.exec_()

        toLog("IP Machine was changed")

    def realMonth(self,month):
        monthlist = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Des']
        monthint = ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12']
        return monthint[monthlist.index(month)]

    def setTime(self):
        yes = True

        if len(self.ui.TimeInput.text()) == 0:
            self.timeError()
            return

        try:
            self.testTime(self.ui.TimeInput.text())
        except:
            self.timeError()
            yes = False

        if yes:
            f = open('json/time.json', 'r')
            data = json.load(f)
            f.close()

            data['server'] = self.ui.TimeInput.text()
            data['change'] = True

            a = ctime(self.testTime(self.ui.TimeInput.text())).replace("  ", " ")
            date = a.split(' ')[-1] + "-" + self.realMonth(a.split(' ')[1]) + "-" + a.split(' ')[2]
            time = a.split(' ')[3]
            
            dateTime = date + " " + time

            setTime(date,time)
            cmd = f'timedatectl set-time "{dateTime}"'
            os.system(cmd)

            f = open('json/time.json', 'w')
            json.dump(data,f,indent=2)
            f.close()

            self.timeSuccess()

        else:
            f = open('json/time.json', 'r')
            data = json.load(f)
            f.close()

            self.ui.TimeInput.setText(data['server'])

    def update(self):
        zipName,_  = QtWidgets.QFileDialog.getOpenFileName(self)
        shutil.copyfile(zipName,'/home/nvidia/Desktop/fall_v.5_pp_API/update.zip')

        with ZipFile('/home/nvidia/Desktop/fall_v.5_pp_API/update.zip','r') as  zObj:
            zObj.extractall('/home/nvidia/Desktop/fall_v.5_pp_API')

        toLog("Software Updated")

        f = open('./json/version.json', 'r')
        data = json.load(f)
        f.close()

        version = float(data['version'])
        version += 0.1

        self.ui.versionLabel.setText(f'Version: {version}')
        data['version'] = version

        f = open('./json/version.json', 'w')
        json.dump(data,f,indent=2)
        f.close()

    def default(self):
        self.Dialogbackup.show()
        self.Dialogbackup.accepted.connect(self.restore)

    def copy(self):
        self.sub_window.label.setText("")
        self.sub_window.label_3.setText("")
        path ="/home/nvidia/Desktop/fall_v.5_pp_API/falldown" #fill the path 


        QtWidgets.QApplication.setOverrideCursor(QtCore.Qt.WaitCursor)
        dest = os.path.join(self.ui.path.text(),'Falldown')
        shutil.copytree(path, dest)
        QtWidgets.QApplication.restoreOverrideCursor()
        self.Dialog.show()

    def buttonClicked(self):
        
        path  = self.ui.path.text()
        fp  = open('config2Channels.json','r')
        data = json.load(fp)
        fp.close()

        data["backup"]["user_path"] = path
        if(self.ui.cover.currentText() == '停止'): data["utils"]["storageMethod"] = True
        else: data["utils"]["storageMethod"] = False
        
        fp = open('config2Channels.json', 'w')
        json.dump(data, fp, indent=2)
        fp.close()

    def browsefile(self):
        fname = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.path.setText(fname)
        f = open('config2Channels.json','r')
        data = json.load(f)
        f.close()
        data['backup']['user_path'] = fname
        f = open('config2Channels.json', 'w')
        json.dump(data,f,indent=2)
        f.close()



if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SystemSet2()
    window.showFullScreen()
    sys.exit(app.exec_())
