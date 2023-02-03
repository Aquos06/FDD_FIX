from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from .AISettingsMain import Ui_MainWindow
from utility import toLog
from allutility.factoryreset import FactoryReset

import sys
import json

class AiSettings(QtWidgets.QMainWindow):
    def __init__(self,mainwindow):
        super().__init__()
        
        self.ui = Ui_MainWindow()
        self.ui.setupUi(mainwindow)
        
        self.setup()
        
    def setup(self):
        self.ui.fill_1.AI.enterButton.clicked.connect(self.saveFile)
        self.ui.fill_2.AI.enterButton.clicked.connect(self.saveFile)
        self.ui.fill_3.AI.enterButton.clicked.connect(self.saveFile)
        self.ui.fill_4.AI.enterButton.clicked.connect(self.saveFile)
        self.ui.pushButtonReset.clicked.connect(self.factoryReset)
        self.setupData()

    def setupData(self):
        f = open('AiSettings.json', 'r')
        data = json.load(f)
        f.close()

        if data['Camera1']['FallDown'] == True:
            self.ui.fill_1.AI.switchFall.setChecked(True)
        else:
            self.ui.fill_1.AI.switchFall.setChecked(False)

        if data['Camera2']['FallDown'] == True:
            self.ui.fill_2.AI.switchFall.setChecked(True)
        else:
            self.ui.fill_2.AI.switchFall.setChecked(False)

        if data['Camera3']['FallDown'] == True:
            self.ui.fill_3.AI.switchFall.setChecked(True)
        else:
            self.ui.fill_3.AI.switchFall.setChecked(False)

        if data['Camera4']['FallDown'] == True:
            self.ui.fill_4.AI.switchFall.setChecked(True)
        else:
            self.ui.fill_4.AI.switchFall.setChecked(False)
        
    def factoryReset(sef):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        msg.setText("Are you sure want to reset the machine?")
        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        retval = msg.exec_()

        if retval == QtWidgets.QMessageBox.Ok:
            FactoryReset()

    def toCamera(self, index):
        if index == 0:
            return "Camera1"
        elif index == 1:
            return "Camera2"
        elif index == 2:
            return "Camera3"
        else :
            return "Camera4"
        
    def checkOnOFF(self):
        if self.channel == "Camera1":
            if self.ui.fill_1.AI.switchFall.isChecked():
                self.data[self.channel]['FallDown'] = True
            else:
                self.data[self.channel]['FallDown'] = False
                
            if self.ui.fill_1.AI.switchPerson.isChecked():
                self.data[self.channel]['Person'] = True
            else:
                self.data[self.channel]['Person'] = False
                
            if self.ui.fill_1.AI.switchPPE.isChecked():
                self.data[self.channel]['PPE']['active'] = True
            else:
                self.data[self.channel]['PPE']['active'] = False

        elif self.channel == "Camera2":
            if self.ui.fill_2.AI.switchFall.isChecked():
                self.data[self.channel]['FallDown'] = True
            else:
                self.data[self.channel]['FallDown'] = False
                
            if self.ui.fill_2.AI.switchPerson.isChecked():
                self.data[self.channel]['Person'] = True
            else:
                self.data[self.channel]['Person'] = False
                
            if self.ui.fill_2.AI.switchPPE.isChecked():
                self.data[self.channel]['PPE']['active'] = True
            else:
                self.data[self.channel]['PPE']['active'] = False

        elif self.channel == "Camera3":
            if self.ui.fill_3.AI.switchFall.isChecked():
                self.data[self.channel]['FallDown'] = True
            else:
                self.data[self.channel]['FallDown'] = False
                
            if self.ui.fill_3.AI.switchPerson.isChecked():
                self.data[self.channel]['Person'] = True
            else:
                self.data[self.channel]['Person'] = False
                
            if self.ui.fill_3.AI.switchPPE.isChecked():
                self.data[self.channel]['PPE']['active'] = True
            else:
                self.data[self.channel]['PPE']['active'] = False
        else:
            if self.ui.fill_4.AI.switchFall.isChecked():
                self.data[self.channel]['FallDown'] = True
            else:
                self.data[self.channel]['FallDown'] = False
                
            if self.ui.fill_4.AI.switchPerson.isChecked():
                self.data[self.channel]['Person'] = True
            else:
                self.data[self.channel]['Person'] = False
                
            if self.ui.fill_4.AI.switchPPE.isChecked():
                self.data[self.channel]['PPE']['active'] = True
            else:
                self.data[self.channel]['PPE']['active'] = False
        
    def saveFile(self):
        self.channel = self.toCamera(self.ui.tabs.currentIndex())
        
        f = open('AiSettings.json', 'r')
        self.data = json.load(f)
        f.close()
        
        self.checkOnOFF()
        
        try:
            f = open('AiSettings.json', 'w')
            json.dump(self.data,f, indent=2)
            f.close()
            toLog('save AI Settings')
        except:
            print('AI settings failed to Save...')
        
if __name__== '__main__':
    app = QApplication(sys.argv)
    ex = AiSettings()
    ex.show()
    sys.exit(app.exec_())
        
