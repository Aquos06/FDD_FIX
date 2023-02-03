from PyQt5 import QtWidgets,QtCore
from .logUI import LogUI
from allutility.factoryreset import FactoryReset

import os
import csv
import shutil
from datetime import datetime

class Log(QtWidgets.QMainWindow):
    def __init__(self,mainwindow):
        super().__init__()
        self.ui = LogUI()
        self.ui.setupUi(mainwindow)
        self.logResult = []
        
        self.setupControl()
        self.pageNow = 0

    def setupControl(self):
        self.ui.okButton.clicked.connect(self.UpdateLog)
        self.ui.RefreshButton.clicked.connect(self.refresh)
        self.ui.deleteButton.clicked.connect(self.sure)
        self.ui.exportButton.clicked.connect(self.export)
        self.ui.leftButton.clicked.connect(self.toLeft)
        self.ui.rightButton.clicked.connect(self.toRight)
        self.ui.enterJump.clicked.connect(self.jumpTo)
        self.ui.pushButtonReset.clicked.connect(self.factoryReset)

        self.ui.enddate.setMaximumDate(QtCore.QDate.currentDate())

    def factoryReset(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        msg.setText("Are you sure want to reset the machine?")

        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        retval = msg.exec_()

        if retval == QtWidgets.QMessageBox.Ok:
            FactoryReset()

    def jumpTo(self):
        self.pageNow = (int(self.ui.jumpTo.text())-1) * 20
        self.ui.tableLog.verticalScrollBar().setValue(self.pageNow)
        self.ui.pageLabel.setText(f'{int(self.pageNow/20)+1} / {self.pageLen}')

    def toLeft(self):
        if self.pageNow - 20 >= 0:
            self.pageNow -= 20
            self.ui.tableLog.verticalScrollBar().setValue(self.pageNow)
            self.ui.pageLabel.setText(f'{int(self.pageNow/20)+1} / {self.pageLen}')

    def toRight(self):
        if self.pageNow + 20 < len(self.logResult):
            self.pageNow  += 20
            self.ui.tableLog.verticalScrollBar().setValue(self.pageNow)
            self.ui.pageLabel.setText(f'{int(self.pageNow/20)+1} / {self.pageLen}')

    def export(self):
        header = ["data","User Name","Activity"]
        with open('settings/templog.csv', 'w', newline = '') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            for i in self.logResult:
                writer.writerow(i)    

        logPath = '/home/nvidia/Desktop/fall_v.5_pp_API/settings/templog.csv'
        folder = QtWidgets.QFileDialog.getExistingDirectory(self, 'Select Folder')

        shutil.copyfile(logPath,os.path.join(folder,'log.csv'))

    def time(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        
        msg.setText("Start time is bigger than End time")
        msg.setWindowTitle("Warning")
        
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)        
 
        retval = msg.exec_()

    def nores(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)

        msg.setText('No Result')
        msg.setWindowTitle('Warning')

        msg.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

        retval = msg.exec_()

    def deleteAll(self):
        with open('settings/log.csv' , 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['Date','User Name', 'Activity'])
        self.clearTable()
        self.ui.pageLabel.setText(f'{0} / {0}')

    def clearTable(self):
        self.ui.tableLog.clearContents()
        self.ui.tableLog.setRowCount(0)

    def sure(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
    
        msg.setText("are you sure you want to delete Log?")
        msg.setWindowTitle("Warning")
        msg.setStandardButtons(QtWidgets.QMessageBox.Ok| QtWidgets.QMessageBox.Cancel)


        retval = msg.exec_()
        if retval == QtWidgets.QMessageBox.Ok:
            self.deleteAll()
        else: 
            print(msg)

    def refresh(self):
        self.clearTable()
        self.showTable()

    def showTable(self):
        with open('settings/log.csv','r') as file:
                reader = csv.reader(file)
                next(reader)
                for row in reader:
                    searchTime = datetime.strptime(row[0], '%Y-%m-%d %H:%M')
                    if (self.startTime<searchTime) and (searchTime<self.endTime):
                        self.logResult.append(row)
        if len(self.logResult) == 0:
            self.nores()

        for ind,i in enumerate(reversed(self.logResult)):
            a = self.ui.tableLog.rowCount()
            self.ui.tableLog.setRowCount(a + 1)
            self.ui.tableLog.setItem(a, 0 ,QtWidgets.QTableWidgetItem(str(ind+1)))
            self.ui.tableLog.setItem(a, 1 ,QtWidgets.QTableWidgetItem(i[0]))
            self.ui.tableLog.setItem(a, 2 ,QtWidgets.QTableWidgetItem(i[1]))
            self.ui.tableLog.setItem(a, 3 ,QtWidgets.QTableWidgetItem(i[-1]))
            self.ui.tableLog.setRowHeight(a,30)

    def UpdateLog(self):
        self.logResult = []
        self.clearTable()

        self.startTime = datetime.strptime(self.ui.startdate.text() + ' ' + self.ui.setstartTimeEdit.text(), "%Y / %m / %d %H:%M")
        self.endTime = datetime.strptime(self.ui.enddate.text() + ' ' + self.ui.setendTimeEdit.text(), "%Y / %m / %d %H:%M")

        if self.endTime < self.startTime:
            self.time()
        self.showTable()
        self.pageLen = int(len(self.logResult) / 20) +1        
        self.ui.pageLabel.setText(f'{1} / {self.pageLen}')

if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = Log()
    window.showFullScreen()
    sys.exit(app.exec_())
