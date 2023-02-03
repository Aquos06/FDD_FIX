from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor

class FallDetail(QtWidgets.QWidget):
    def setupUi(self,MainWindow):
        super().__init__()

        self.setFixedSize(QtCore.QSize(1000,600))
        self.setStyleSheet('background: #00172D;')
        self.setWindowTitle('Details')
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.verticalMain = QtWidgets.QVBoxLayout()
        self.verticalMain.setSpacing(0)
        self.verticalMain.addItem(spacerItem)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("HorizontalLayout")
        
        self.FallLabel = QtWidgets.QLabel()
        self.FallLabel.setMinimumSize(QtCore.QSize(700,350))
        self.FallLabel.setMaximumSize(QtCore.QSize(700,350))
        self.FallLabel.setObjectName('FallLabel')
        self.FallLabel.setText('')
        
        self.horizontalLayout.addWidget(self.FallLabel, alignment= QtCore.Qt.AlignHCenter) #1
        self.horizontalLayout.addItem(spacerItem) #0
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)

        self.labelCut = QtWidgets.QLabel()
        self.labelCut.setMinimumSize(QtCore.QSize(200,200))
        self.labelCut.setMaximumSize(QtCore.QSize(200,200))
        self.labelCut.setText('')
        self.verticalLayout.addWidget(self.labelCut)

        self.InformationLabel = QtWidgets.QLabel()
        self.InformationLabel.setStyleSheet("color: white")
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(80)
        self.InformationLabel.setFont(font)
        self.InformationLabel.setMaximumSize(QtCore.QSize(250,150))
        self.InformationLabel.setMinimumSize(QtCore.QSize(250,150))
        self.InformationLabel.setText('')
        self.InformationLabel.setObjectName('InformationLabel')
        self.verticalLayout.addWidget(self.InformationLabel) 
        self.horizontalLayout.addLayout(self.verticalLayout)
        
        self.verticalMain.addLayout(self.horizontalLayout)    

        self.horizontalButton = QtWidgets.QHBoxLayout()
        self.horizontalButton.setSpacing(0)

        self.leftButton = QtWidgets.QPushButton()
        self.leftButton.setStyleSheet("""
            QPushButton{
                background-color: #4277BD;
                color: white;
                border-radius: 10px;
            }
            QPushButton:hover{
                background-color: #499DD0;
                border-radius: 10px;
            }
        """)
        self.leftButton.setText('<')
        self.leftButton.setMinimumSize(QtCore.QSize(30,30))
        self.leftButton.setMaximumSize(QtCore.QSize(30,30))
        self.leftButton.setFont(font)
        self.horizontalButton.addWidget(self.leftButton, alignment= QtCore.Qt.AlignCenter)

        self.buttonBack = QtWidgets.QPushButton()
        self.buttonBack.setFont(font)
        self.buttonBack.setText('')
        self.buttonBack.setMaximumSize(QtCore.QSize(100,50))
        self.buttonBack.setMinimumSize(QtCore.QSize(100,50))
        self.buttonBack.setStyleSheet("""
            QPushButton{
                background-color: #4277BD;
                color: white;
                border-radius: 10px;
            }
            QPushButton:hover{
                background-color: #499DD0;
                border-radius: 10px;
            }
        """)
        self.buttonBack.setObjectName('buttonBack')
        self.horizontalButton.addWidget(self.buttonBack, alignment= QtCore.Qt.AlignCenter)
        
        self.rightButton = QtWidgets.QPushButton()
        self.rightButton.setFont(font)
        self.rightButton.setText('>')
        self.rightButton.setMaximumSize(QtCore.QSize(30,30))
        self.rightButton.setMinimumSize(QtCore.QSize(30,30))
        self.rightButton.setStyleSheet("""
            QPushButton{
                background-color: #4277BD;
                color: white;
                border-radius: 10px;
            }
            QPushButton:hover{
                background-color: #499DD0;
                border-radius: 10px;
            }
        """)
        self.horizontalButton.addWidget(self.rightButton, alignment= QtCore.Qt.AlignCenter)

        self.verticalMain.addItem(spacerItem)
        self.verticalMain.addLayout(self.horizontalButton)
        self.verticalMain.addItem(spacerItem)

        self.verticalMain.setStretch(0,1)
        self.verticalMain.setStretch(1,10)
        self.verticalMain.setStretch(4,1)
        self.verticalMain.setStretch(5,2)
        self.verticalMain.setStretch(6,1)

        self.setLayout(self.verticalMain)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = FallDetail(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())