from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from components.falldownbox import Box

class AnotherWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1143)
        MainWindow.setStyleSheet("background:black;")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-image : url(img/background.png);")
        self.centralwidget.setObjectName("centralwidget")
        
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
        #############################################################################################################
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayoutmain = QtWidgets.QHBoxLayout()
        self.horizontalLayoutmain.setSpacing(0)
        self.horizontalLayoutmain.setObjectName("HorizontalLayoutMain")
        
        self.verticalLayoutmain = QtWidgets.QVBoxLayout()
        self.verticalLayoutmain.setSpacing(0)
        self.verticalLayoutmain.setObjectName("verticalLayoutmain")
        
        # #Channel1 - bar
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:gray;")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_7.addWidget(self.label_6) #Horizontal7 - 1
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_7.addWidget(self.label_2) #Horiontal7 - 2
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setStyleSheet("color:red;")
        self.label.setObjectName("label")
        self.horizontalLayout_7.addWidget(self.label) #Horizontal 7 - 3
        
        self.horizontalLayout_7.addItem(spacerItem)
        
        self.horizontalLayout_7.setStretch(0, 4)
        self.horizontalLayout_7.setStretch(1, 8)
        self.horizontalLayout_7.setStretch(2, 4)
        self.horizontalLayout_7.setStretch(3, 15)
        
        self.verticalLayoutmain.addLayout(self.horizontalLayout_7)
        
        #Channel1- Image
        self.screen = QtWidgets.QLabel(self.centralwidget)
        self.screen.setMaximumSize(QtCore.QSize(1600, 900))
        self.screen.setMinimumSize(QtCore.QSize(800,450))
        self.screen.setStyleSheet("background:white;")
        self.screen.setText("")
        self.screen.setObjectName("lchannel1")
        self.verticalLayoutmain.addWidget(self.screen) #Horizontal19 - 0
        
        self.verticalLayoutmain.addItem(spacerItem)
        
        self.verticalLayoutmain.setStretch(0,1)
        self.verticalLayoutmain.setStretch(1,90)
        self.verticalLayoutmain.setStretch(2,1)

        self.horizontalLayoutmain.addLayout(self.verticalLayoutmain)
        
        self.verticalLayout_right = QtWidgets.QVBoxLayout()
        self.verticalLayout_right.setSpacing(0)
        self.verticalLayout_right.setObjectName("VerticalLayout_right")
        
        self.verticalLayout_right.addItem(spacerItem)

        self.horizontalLayout_time = QtWidgets.QHBoxLayout()
        self.horizontalLayout_time.setSpacing(0)
        self.horizontalLayout_time.setObjectName("HorizontalLayout_time")

        self.time = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.time.setFont(font)
        self.time.setStyleSheet("color:white;")
        self.time.setObjectName("time")
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_time.addWidget(self.time) #Vertical right - 0

        self.horizontalLayout_time.addItem(spacerItem)

        self.login = QtWidgets.QPushButton(self.centralwidget)
        self.login.setMaximumSize(QtCore.QSize(100,50))
        self.login.setMinimumSize(QtCore.QSize(100,50))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(100)
        self.login.setFont(font)
        self.login.setStyleSheet("""
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
        self.login.setDefault(True)
        self.login.setObjectName("login")
        self.login.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout_time.addWidget(self.login)

        self.horizontalLayout_time.addItem(spacerItem)

        self.horizontalLayout_time.setStretch(0,5)
        self.horizontalLayout_time.setStretch(1,3)
        self.horizontalLayout_time.setStretch(2,1)


        self.verticalLayout_right.addLayout(self.horizontalLayout_time)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setSpacing(0)

        self.scrollAreaWidgetContents.setLayout(self.layout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_right.addWidget(self.scrollArea) #vertical right -2

        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setMaximumSize(QtCore.QSize(540, 95))
        self.label_10.setStyleSheet("background:blue")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("img/logoo.png"))
        self.label_10.setScaledContents(False)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_right.addWidget(self.label_10) # Vertical right - 3

        self.verticalLayout_right.setStretch(0,1)
        self.verticalLayout_right.setStretch(1,2)
        self.verticalLayout_right.setStretch(2,50)
        self.verticalLayout_right.setStretch(3,2)

        self.horizontalLayoutmain.addLayout(self.verticalLayout_right)

        
        #############################################################################################################
        #############################################################################################################
        self.horizontalLayoutmain.setStretch(0,89)
        self.horizontalLayoutmain.setStretch(1,1)
        self.horizontalLayoutmain.setStretch(2,10)

        self.verticalLayout_2.addLayout(self.horizontalLayoutmain)
        # self.verticalLayout_2.setStretch(0, 1)
        # self.verticalLayout_2.setStretch(1, 80)
        
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)
        
        self.horizontalLayout_4.setStretch(0, 80)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1920, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_6.setText(_translate("MainWindow", "Camera 1  "))
        self.label_2.setText(_translate("MainWindow", "<font color = red> 跌倒</font> / 總人數 : "))
        self.label.setText(_translate("MainWindow", "0<font color=white> / 0</font>"))

        self.login.setText(_translate("MainWindow", "Back"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AnotherWindow()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec_())
