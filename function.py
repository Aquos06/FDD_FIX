from PyQt5 import QtWidgets, QtGui, QtCore
from functionmain2 import Ui_MainWindow
from dialogsure import Ui_Dialog
from Timetable.TableTime import TimeSelect

from allutility.utility import toLog
from allutility.factoryreset import FactoryReset

import json
class SettingFunction(QtWidgets.QMainWindow):
    def __init__(self,mainwindow):
        super().__init__() # in python3, super(Class, self).xxx = super().xxx
        self.ui = Ui_MainWindow()
        self.ui.setupUi(mainwindow)
        self.Dialogsure = QtWidgets.QDialog()
        self.sub_window = Ui_Dialog() 
        self.sub_window.setupUi(self.Dialogsure)
        self.timeTable = TimeSelect()
        
        self.setup_control()

    def setup_control(self):
        self.ui.start.clicked.connect(self.buttonClicked)
        self.ui.back.clicked.connect(self.backup_function)
        
        self.ui.setTimeMonday.clicked.connect(lambda: self.selectTimeTable("週一"))
        self.ui.setTimeTuesday.clicked.connect(lambda: self.selectTimeTable("週二"))
        self.ui.setTimeWednesday.clicked.connect(lambda: self.selectTimeTable("週三"))
        self.ui.setTimeThursday.clicked.connect(lambda: self.selectTimeTable("週四"))
        self.ui.setTimeFriday.clicked.connect(lambda: self.selectTimeTable("週五"))
        self.ui.setTimeSaturday.clicked.connect(lambda: self.selectTimeTable("週六"))
        self.ui.setTimeSunday.clicked.connect(lambda: self.selectTimeTable("週日"))
        self.ui.pushButtonReset.clicked.connect(self.factoryReset)


        self.backup_function()

    def factoryReset(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        msg.setText("Are you sure want to reset the machine?")
        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        retval = msg.exec_()

        if retval == QtWidgets.QMessageBox.Ok:
            FactoryReset()

    def selectTimeTable(self, day):
        
        self.timeTable.day = day
        self.timeTable.ui.TitleLabel.setText(day)
        self.timeTable.setupUI(day)
        self.timeTable.ui.show()

    def backup_function(self):
        f = open('json/function.json', 'r')
        content = json.load(f)
        f.close()
        
        self.ui.delay.setValue(int(content["function"]["light_delay"]))
        counterrestart = content["function"]["counter_reset"][:5].split(':')
        self.ui.counterrestart.setTime(QtCore.QTime(int(counterrestart[0]), int(counterrestart[1]), 0))
        
        if content['function']['GPIO']['Camera1'] == True:
            self.ui.switchGPIO1.setChecked(True)
        else:
            self.ui.switchGPIO1.setChecked(False)

        if content['function']['GPIO']['Camera2'] == True:
            self.ui.switchGPIO2.setChecked(True)
        else:
            self.ui.switchGPIO2.setChecked(False)

        if content['function']['GPIO']['Camera3'] == True:
            self.ui.switchGPIO3.setChecked(True)
        else:
            self.ui.switchGPIO3.setChecked(False)

        if content['function']['GPIO']['Camera4'] == True:
            self.ui.switchGPIO4.setChecked(True)
        else:
            self.ui.switchGPIO4.setChecked(False)

    def buttonClicked(self):

        fp  = open('json/function.json','r')
        statusfp  = open('json/set.json','r')
        data = json.load(fp)
        setStatus = json.load(statusfp)
        fp.close()
        statusfp.close()

        data["function"]["light_delay"] = int(self.ui.delay.text())
        data["function"]["counter_reset"] = self.ui.counterrestart.text()+":00"
        
        if self.ui.switchGPIO1.isChecked():
            data['function']['Camera1'] = True
        else:
            data['function']['Camera1'] = False

        if self.ui.switchGPIO2.isChecked():
            data['function']['Camera2'] = True
        else:
            data['function']['Camera2'] = False

        if self.ui.switchGPIO3.isChecked():
            data['function']['Camera3'] = True
        else:
            data['function']['Camera3'] = False

        if self.ui.switchGPIO4.isChecked():
            data['function']['Camera4'] = True
        else:
            data['function']['Camera4'] = False

        setStatus["setStatus"] = True

        fp = open('json/function.json', 'w')
        statusfp = open('json/set.json', 'w')
        json.dump(data, fp, indent=2)
        json.dump(setStatus, statusfp, indent=2)
        fp.close()
        statusfp.close()
        toLog("GPIO settings is updated")
        self.sub_window.label.setText("確定成功")
        self.Dialogsure.show()
        
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = SettingFunction()
    window.showFullScreen()
    sys.exit(app.exec_())
