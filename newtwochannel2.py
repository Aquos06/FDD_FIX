from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from components.falldownbox import Box
import cv2

class Ui_MainWindowp(object):
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
        
        ############################################################################################################
        #Navbar
        self.horizontalLayout_Navbar = QtWidgets.QHBoxLayout()
        self.horizontalLayout_Navbar.setSpacing(0)
        self.horizontalLayout_Navbar.setObjectName("horizontalLayout_Navbar")
        
        self.labelLogo = QtWidgets.QLabel(self.centralwidget)
        self.labelLogo.setMaximumSize(QtCore.QSize(540, 95))
        self.labelLogo.setStyleSheet("background:blue")
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("img/logoo.png"))
        self.labelLogo.setScaledContents(False)
        self.labelLogo.setObjectName("labelLogo")
        self.horizontalLayout_Navbar.addWidget(self.labelLogo) #Navbar 0
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_Navbar.addItem(spacerItem) #Navbar 1
        
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(100)
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setStyleSheet("color: white")
        self.label_6.setFont(font)
        self.label_6.setText("")
        self.label_6.setObjectName("labelTotal")
        self.horizontalLayout_Navbar.addWidget(self.label_6) #Navbar 2
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setStyleSheet("color:white")
        self.label.setText("")
        self.label.setFont(font)
        self.label.setObjectName("labelNum")
        self.horizontalLayout_Navbar.addWidget(self.label) #Navbar 3
        
        self.horizontalLayout_Navbar.addItem(spacerItem) #Navbar 4

        self.time = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.time.setFont(font)
        self.time.setStyleSheet("color:white;")
        self.time.setObjectName("time")
        self.time.setAlignment(QtCore.Qt.AlignCenter)
        self.horizontalLayout_Navbar.addWidget(self.time) #Navbar 5

        self.horizontalLayout_Navbar.addItem(spacerItem) #Navbar 6

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
                border-radius:10px;
            }
        """)
        self.login.setDefault(True)
        self.login.setObjectName("login")
        self.login.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout_Navbar.addWidget(self.login) #Navbar 7

        self.horizontalLayout_Navbar.addItem(spacerItem) #Navbar 8
        
        self.horizontalLayout_Navbar.setStretch(0,10)
        self.horizontalLayout_Navbar.setStretch(1,5)
        self.horizontalLayout_Navbar.setStretch(2,2)
        self.horizontalLayout_Navbar.setStretch(3,2)
        self.horizontalLayout_Navbar.setStretch(4,25)
        self.horizontalLayout_Navbar.setStretch(5,6)
        self.horizontalLayout_Navbar.setStretch(6,1)
        self.horizontalLayout_Navbar.setStretch(7,3)
        self.horizontalLayout_Navbar.setStretch(8,1)        
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_Navbar)
        
        #############################################################################################################

        self.horizontalLayoutmain = QtWidgets.QHBoxLayout()
        self.horizontalLayoutmain.setSpacing(0)
        self.horizontalLayoutmain.setObjectName("HorizontalLayoutMain")
        
        self.verticalLayoutmain = QtWidgets.QVBoxLayout()
        self.verticalLayoutmain.setSpacing(0)
        self.verticalLayoutmain.setObjectName("verticalLayoutmain")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout() #init Horizontal 0
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        #Channel1- Image
        self.lchannel1 = QtWidgets.QLabel(self.centralwidget)
        self.lchannel1.setMaximumSize(QtCore.QSize(1600, 900))
        self.lchannel1.setMinimumSize(QtCore.QSize(400,225))
        self.lchannel1.setStyleSheet("background:white;")
        self.lchannel1.setText("")
        self.lchannel1.setObjectName("lchannel1")
        
        #Channel2 - Image
        self.lchannel2 = QtWidgets.QLabel(self.centralwidget)
        self.lchannel2.setMaximumSize(QtCore.QSize(1600, 900))
        self.lchannel2.setMinimumSize(QtCore.QSize(400,225))
        self.lchannel2.setStyleSheet("background:white;")
        self.lchannel2.setText("")
        self.lchannel2.setObjectName("lchannel2")
        
        self.horizontalLayout.addWidget(self.lchannel1)
        self.horizontalLayout.addWidget(self.lchannel2)
        
        self.horizontalLayout.setStretch(0, 50)
        self.horizontalLayout.setStretch(1, 50)

        self.verticalLayoutmain.addItem(self.horizontalLayout)#Vertical - 1 add FIrst
        #############################################################################################################
        #Second Line Channel
        self.horizontalLayout27 = QtWidgets.QHBoxLayout() #Init Horizontal
        self.horizontalLayout27.setSpacing(0)
        self.horizontalLayout27.setObjectName("horizontalLayout")
        
        #Image 3
        self.lchannel3 = QtWidgets.QLabel(self.centralwidget)
        self.lchannel3.setMaximumSize(QtCore.QSize(1600, 900))
        self.lchannel3.setMinimumSize(QtCore.QSize(400,225))
        self.lchannel3.setStyleSheet("background:black;")
        self.lchannel3.setText("")
        self.lchannel3.setObjectName("lchannel3")

        self.lchannel4 = QtWidgets.QLabel(self.centralwidget)
        self.lchannel4.setMaximumSize(QtCore.QSize(1600, 900))
        self.lchannel4.setMinimumSize(QtCore.QSize(400,225))
        self.lchannel4.setStyleSheet("background:black;")
        self.lchannel4.setText("")
        self.lchannel4.setObjectName("lchannel4")
        
        self.horizontalLayout27.addWidget(self.lchannel3)
        self.horizontalLayout27.addWidget(self.lchannel4)

        self.horizontalLayout27.setStretch(0, 50)
        self.horizontalLayout27.setStretch(1, 50)
        
        
        self.verticalLayoutmain.addLayout(self.horizontalLayout27) #Vertical - 2 add Second
        #############################################################################################################
        #############################################################################################################
        self.horizontalLayoutmain.addLayout(self.verticalLayoutmain)
        
        self.verticalLayoutRight = QtWidgets.QVBoxLayout()
        self.verticalLayoutRight.setSpacing(0)
        self.verticalLayoutRight.setObjectName('verticalLayoutRight')
        
        self.horizontalTotal = QtWidgets.QHBoxLayout()
        self.horizontalTotal.setSpacing(0)

        self.labelTotal = QtWidgets.QLabel(self.centralwidget)
        self.labelTotal.setStyleSheet("color: white")
        self.labelTotal.setFont(font)
        self.labelTotal.setText("")
        self.labelTotal.setObjectName("labelTotal")
        self.horizontalTotal.addWidget(self.labelTotal) #Navbar 2
        
        self.labelNum = QtWidgets.QLabel(self.centralwidget)
        self.labelNum.setStyleSheet("color:white")
        self.labelNum.setText("")
        self.labelNum.setFont(font)
        self.labelNum.setObjectName("labelNum")
        self.horizontalTotal.addWidget(self.labelNum) #Navbar 3


        self.verticalLayoutRight.addLayout(self.horizontalTotal)
        
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setFixedWidth(400)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setSpacing(0)

        self.scrollAreaWidgetContents.setLayout(self.layout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayoutRight.addWidget(self.scrollArea)
        
        self.horizontalLayoutmain.addLayout(self.verticalLayoutRight)
        
        self.horizontalLayoutmain.setStretch(0,65)
        self.horizontalLayoutmain.setStretch(1,1)
        self.horizontalLayoutmain.setStretch(2,25)

        self.verticalLayout_2.addLayout(self.horizontalLayoutmain)
        
        self.verticalLayout_2.setStretch(0,1)
        self.verticalLayout_2.setStretch(1,10)
        
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

    def img2pyqt_2(self,img,label):
        '''
        convert the opencv format to pyqt format color
        '''
        img = cv2.imread(img)
        frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        temp = QtGui.QImage(frame, frame.shape[1], frame.shape[0], frame.shape[1]*3, QtGui.QImage.Format_RGB888)
        return QtGui.QPixmap.fromImage(temp).scaled(400, 225)
        
    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.login.setText(_translate("MainWindow", "Login"))
        
        self.lchannel3.setPixmap(self.img2pyqt_2("recon.png",self.lchannel3))       
        self.lchannel3.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        self.lchannel4.setPixmap(self.img2pyqt_2("recon.png",self.lchannel4))       
        self.lchannel4.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
        
        self.labelTotal.setText(_translate("MainWindow", "<font color = red>跌倒</font>："))
        self.labelNum.setText(_translate("MainWindow", "<font color=red>0</font> "))
        self.time.setText(_translate("MainWindow", "00:00:00"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowp()
    ui.setupUi(MainWindow)
    MainWindow.showFullScreen()
    sys.exit(app.exec_())
