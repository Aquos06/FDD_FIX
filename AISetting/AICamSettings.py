from PyQt5 import QtCore, QtGui, QtWidgets
from mySwitch import MySwitch


class AiCamSettings(QtWidgets.QWidget):
    def setupUi(self):
        super(QtWidgets.QWidget)
        
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(100)
        
        font_frame = QtGui.QFont()
        font_frame.setFamily('Ubuntu Mono')
        font_frame.setPointSize(13)
        font_frame.setBold(False)
        font_frame.setWeight(50)
        
        ###################################
        
        
        self.verticalLayoutMain = QtWidgets.QVBoxLayout()
        self.verticalLayoutMain.setSpacing(0)
        self.verticalLayoutMain.setObjectName("VerticalLayoutMain")
        
        self.HorizontalLayoutPerson = QtWidgets.QHBoxLayout()
        self.HorizontalLayoutPerson.setSpacing(0)
        self.HorizontalLayoutPerson.setObjectName('HorizontalLayoutPerson')
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.HorizontalLayoutPerson.addItem(spacerItem) #person 0
        
        self.labelPerson = QtWidgets.QLabel()
        self.labelPerson.setFont(font)
        self.labelPerson.setText("")
        self.labelPerson.setObjectName('labelPerson')
        self.labelPerson.setStyleSheet("color:White")
        self.HorizontalLayoutPerson.addWidget(self.labelPerson) #person 1

        self.HorizontalLayoutPerson.addItem(spacerItem) #person 2
        
        self.switchPerson = MySwitch()
        self.switchPerson.setChecked(False)
        self.switchPerson.setEnabled(False)
        self.switchPerson.setObjectName("switchPerson")
        self.HorizontalLayoutPerson.addWidget(self.switchPerson) #person 3
        
        self.HorizontalLayoutPerson.addItem(spacerItem) #person 4
        
        self.HorizontalLayoutPerson.setStretch(0,1)
        self.HorizontalLayoutPerson.setStretch(1,5)
        self.HorizontalLayoutPerson.setStretch(2,1)
        self.HorizontalLayoutPerson.setStretch(3,3)
        self.HorizontalLayoutPerson.setStretch(4,38)
        
        self.verticalLayoutMain.addItem(spacerItem) #Main 0
        self.verticalLayoutMain.addLayout(self.HorizontalLayoutPerson) #Main 1
        self.verticalLayoutMain.addItem(spacerItem)#Main 2
        
        self.HorizontalLayoutFallDown = QtWidgets.QHBoxLayout()
        self.HorizontalLayoutFallDown.setSpacing(0)
        self.HorizontalLayoutFallDown.setObjectName("HorizontalLayoutFallDown")
        self.HorizontalLayoutFallDown.addItem(spacerItem)
        
        self.labelFall = QtWidgets.QLabel()
        self.labelFall.setFont(font)
        self.labelFall.setText("")
        self.labelFall.setObjectName("labelFall")
        self.labelFall.setStyleSheet("color: white")
        
        self.HorizontalLayoutFallDown.addWidget(self.labelFall)
        self.HorizontalLayoutFallDown.addItem(spacerItem)
        
        self.switchFall = MySwitch()
        self.switchFall.setChecked(True)
        self.switchFall.setObjectName("switchFall")
        
        self.HorizontalLayoutFallDown.addWidget(self.switchFall)
        self.HorizontalLayoutFallDown.addItem(spacerItem)
        
        self.HorizontalLayoutFallDown.setStretch(0,1)
        self.HorizontalLayoutFallDown.setStretch(1,5)
        self.HorizontalLayoutFallDown.setStretch(2,1)
        self.HorizontalLayoutFallDown.setStretch(3,3)
        self.HorizontalLayoutFallDown.setStretch(4,38)
        
        self.verticalLayoutMain.addLayout(self.HorizontalLayoutFallDown) #Main 3
        self.verticalLayoutMain.addItem(spacerItem) #Main 4
        
        self.HorizontalLayoutPPE = QtWidgets.QHBoxLayout()
        
        self.labelPPE = QtWidgets.QLabel()
        self.labelPPE.setText("")
        self.labelPPE.setFont(font)
        self.labelPPE.setStyleSheet("color:white")
        self.labelPPE.setObjectName("labelPPE")

        self.HorizontalLayoutPPE.addItem(spacerItem)
        self.HorizontalLayoutPPE.addWidget(self.labelPPE)
        self.HorizontalLayoutPPE.addItem(spacerItem)
        
        self.switchPPE = MySwitch()
        self.switchPPE.setChecked(False)
        self.switchPPE.setEnabled(False)
        self.switchPPE.setObjectName("SwitchPPE")
        
        self.HorizontalLayoutPPE.addWidget(self.switchPPE)
        self.HorizontalLayoutPPE.addItem(spacerItem)
        
        self.HorizontalLayoutPPE.setStretch(0,1)
        self.HorizontalLayoutPPE.setStretch(1,5)
        self.HorizontalLayoutPPE.setStretch(2,1)
        self.HorizontalLayoutPPE.setStretch(3,3)
        self.HorizontalLayoutPPE.setStretch(4,38)
        
        self.verticalLayoutMain.addLayout(self.HorizontalLayoutPPE) #5
        self.verticalLayoutMain.addItem(spacerItem) #6
        
        self.HorizontalFrame = QtWidgets.QHBoxLayout()
        self.HorizontalFrame.setSpacing(0)
        self.HorizontalFrame.setObjectName('HorizontalFrame')
        
        self.HorizontalLayoutPPEMenu = QtWidgets.QHBoxLayout()
        self.HorizontalLayoutPPEMenu.setSpacing(0)
        self.HorizontalLayoutPPEMenu.setObjectName("HorizontalLayoutPPEMenu")
        self.HorizontalLayoutPPEMenu.addItem(spacerItem)
        
        self.verticalLayoutMainPPEMenu = QtWidgets.QFrame()
        self.verticalLayoutMainPPEMenu.Shape(QtWidgets.QFrame.Box)
        self.verticalLayoutMainPPEMenu.setFrameStyle(QtWidgets.QFrame.Panel | QtWidgets.QFrame.Sunken)
        self.verticalLayoutMainPPEMenu.setObjectName("VerticalLayoutMainPPEMenu")
        self.verticalLayoutMainPPEMenu.setStyleSheet("""
                                                     #VerticalLayoutMainPPEMenu{
                                                             border:3px solid blue;
                                                             padding:10;
                                                     }
                                                     """)
        
        self.VerticalLayoutFrame = QtWidgets.QVBoxLayout(self.verticalLayoutMainPPEMenu)
        self.VerticalLayoutFrame.setSpacing(0)
        self.VerticalLayoutFrame.setObjectName("VerticalLayoutFrame")
        
        self.HorizontalLayoutHelmet = QtWidgets.QHBoxLayout()
        self.HorizontalLayoutHelmet.setSpacing(0)
        self.HorizontalLayoutHelmet.setObjectName('HorizontalLayoutHelmet')

        self.helmet = QtWidgets.QCheckBox(self.verticalLayoutMainPPEMenu)
        self.helmet.setStyleSheet("color:white")
        self.helmet.setFont(font_frame)
        self.helmet.setText("")
        self.helmet.setObjectName("helmet")
        
        self.HorizontalLayoutHelmet.addItem(spacerItem) #Frame 0
        self.HorizontalLayoutHelmet.addWidget(self.helmet)#Frame 1
        
        self.HelmetBlue = QtWidgets.QCheckBox(self.verticalLayoutMainPPEMenu)
        self.HelmetBlue.setStyleSheet("color:white")
        self.HelmetBlue.setText('')
        self.HelmetBlue.setFont(font_frame)
        self.HelmetBlue.setObjectName('HelmetBlue')    
        
        self.HorizontalLayoutHelmet.addItem(spacerItem)
        self.HorizontalLayoutHelmet.addWidget(self.HelmetBlue)
        
        self.HelmetRed = QtWidgets.QCheckBox(self.verticalLayoutMainPPEMenu)
        self.HelmetRed.setStyleSheet("color:white")
        self.HelmetRed.setText('')
        self.HelmetRed.setFont(font_frame)
        self.HelmetRed.setObjectName('HelmetRed')
        
        self.HorizontalLayoutHelmet.addItem(spacerItem)
        self.HorizontalLayoutHelmet.addWidget(self.HelmetRed)
        
        self.HelmetYellow = QtWidgets.QCheckBox(self.verticalLayoutMainPPEMenu)
        self.HelmetYellow.setStyleSheet("color:white")
        self.HelmetYellow.setText('')
        self.HelmetYellow.setFont(font_frame)
        self.HelmetYellow.setObjectName('HelmetYellow')
        
        self.HorizontalLayoutHelmet.addItem(spacerItem)
        self.HorizontalLayoutHelmet.addWidget(self.HelmetYellow)  
        
        self.VerticalLayoutFrame.addLayout(self.HorizontalLayoutHelmet)
        self.VerticalLayoutFrame.addItem(spacerItem)
        
        self.HorizontalLayoutMask = QtWidgets.QHBoxLayout()
        self.HorizontalLayoutMask.setSpacing(0)
        self.HorizontalLayoutMask.setObjectName('HorizontalLayoutMask')
        
        self.maskPPe = QtWidgets.QCheckBox(self.verticalLayoutMainPPEMenu)
        self.maskPPe.setStyleSheet("color:white")
        self.maskPPe.setFont(font_frame)
        self.maskPPe.setText("")
        self.maskPPe.setObjectName("maskPPe")
        
        self.HorizontalLayoutMask.addItem(spacerItem)
        self.HorizontalLayoutMask.addWidget(self.maskPPe)
        self.HorizontalLayoutMask.addItem(spacerItem)

        self.HorizontalLayoutMask.setStretch(0,8)
        self.HorizontalLayoutMask.setStretch(1,5)
        self.HorizontalLayoutMask.setStretch(2,35)
        
        self.VerticalLayoutFrame.addLayout(self.HorizontalLayoutMask)
        self.VerticalLayoutFrame.addItem(spacerItem)
        
        self.HorizontalLayoutVest = QtWidgets.QHBoxLayout()
        self.HorizontalLayoutVest.setSpacing(0)
        self.HorizontalLayoutVest.setObjectName('HorizontalLayoutVest')
        
        self.vest = QtWidgets.QCheckBox(self.verticalLayoutMainPPEMenu)
        self.vest.setStyleSheet("color:white")
        self.vest.setFont(font_frame)
        self.vest.setText("")
        self.vest.setObjectName('vest')
        
        self.HorizontalLayoutVest.addItem(spacerItem) 
        self.HorizontalLayoutVest.addWidget(self.vest) 
        
        self.vestRed = QtWidgets.QCheckBox(self.verticalLayoutMainPPEMenu)
        self.vestRed.setFont(font_frame)
        self.vestRed.setStyleSheet('color:white')
        self.vestRed.setText('')
        self.vestRed.setObjectName('vestRed')
        
        self.HorizontalLayoutVest.addItem(spacerItem)
        self.HorizontalLayoutVest.addWidget(self.vestRed)
        
        self.vestBlue = QtWidgets.QCheckBox(self.verticalLayoutMainPPEMenu)
        self.vestBlue.setFont(font_frame)
        self.vestBlue.setStyleSheet('color:white')
        self.vestBlue.setText('')
        self.vestBlue.setObjectName('vestBlue')
        
        self.HorizontalLayoutVest.addItem(spacerItem)
        self.HorizontalLayoutVest.addWidget(self.vestBlue)
        
        self.vestYellow = QtWidgets.QCheckBox(self.verticalLayoutMainPPEMenu)
        self.vestYellow.setFont(font_frame)
        self.vestYellow.setStyleSheet('color:white')
        self.vestYellow.setText('')
        self.vestYellow.setObjectName('vestYellow')
        
        self.HorizontalLayoutVest.addItem(spacerItem)
        self.HorizontalLayoutVest.addWidget(self.vestYellow)        
        
        self.VerticalLayoutFrame.addItem(spacerItem)
        self.VerticalLayoutFrame.addLayout(self.HorizontalLayoutVest)
        
        self.VerticalLayoutFrame.setStretch(0,2)
        self.VerticalLayoutFrame.setStretch(1,2)
        self.VerticalLayoutFrame.setStretch(2,2)
        
        self.HorizontalFrame.addItem(spacerItem)
        self.HorizontalFrame.addWidget(self.verticalLayoutMainPPEMenu)
        self.HorizontalFrame.addItem(spacerItem)
        
        self.HorizontalFrame.setStretch(0,2)
        self.HorizontalFrame.setStretch(1,20)
        self.HorizontalFrame.setStretch(2,7)
        
        self.verticalLayoutMain.addLayout(self.HorizontalFrame) #7
        self.verticalLayoutMain.addItem(spacerItem) #8
        
        self.enterLayout = QtWidgets.QHBoxLayout()
        self.enterLayout.setSpacing(0)
        self.enterLayout.setObjectName("enterLayout")
        
        self.enterButton = QtWidgets.QPushButton()
        self.enterButton.setText('')
        self.enterButton.setStyleSheet(
            "QPushButton{\n"
"background:#323232;color:white;border: 2px  solid #757475;"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color:lightgray;\n"
"    color:black;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"    background-color:gray;\n"
"    color:white"
"}\n"
""
        )
        self.enterButton.setFont(font)
        self.enterButton.setObjectName('enterButton')
        
        self.enterLayout.addItem(spacerItem)
        self.enterLayout.addWidget(self.enterButton)
        self.enterLayout.addItem(spacerItem)
        
        self.enterLayout.setStretch(0,34)
        self.enterLayout.setStretch(1,3)
        self.enterLayout.setStretch(2,5)
        
        self.verticalLayoutMain.addLayout(self.enterLayout)
        self.verticalLayoutMain.addItem(spacerItem)
        
        self.verticalLayoutMain.setStretch(0,1)
        self.verticalLayoutMain.setStretch(1,2)
        self.verticalLayoutMain.setStretch(2,1)
        self.verticalLayoutMain.setStretch(3,2)
        self.verticalLayoutMain.setStretch(4,1)
        self.verticalLayoutMain.setStretch(5,2)
        self.verticalLayoutMain.setStretch(6,1)
        self.verticalLayoutMain.setStretch(7,5)
        self.verticalLayoutMain.setStretch(8,20)
        self.verticalLayoutMain.setStretch(9,3)
        self.verticalLayoutMain.setStretch(10,7)

        self.setLayout(self.verticalLayoutMain)
        
        
        
        self.retranslateUi()
        
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.labelPerson.setText(_translate("MainWindow", "1. Person"))
        self.labelFall.setText(_translate("MainWindow",  "2. FallDown"))
        self.labelPPE.setText(_translate('MainWindow', '3. PPE'))
        
        self.vest.setText(_translate("MainWindow", "Vest : "))
        self.maskPPe.setText(_translate("MainWindow", "Mask : "))
        self.helmet.setText(_translate("MainWindow", "Helmet : "))
        
        self.vestRed.setText(_translate('MainWindow', 'Red'))
        self.vestYellow.setText(_translate('MainWindow', 'Yellow'))
        self.vestBlue.setText(_translate('MainWindow', 'Blue'))
        
        self.HelmetRed.setText(_translate('MainWindow', 'Red'))
        self.HelmetYellow.setText(_translate('MainWindow', 'Yellow'))
        self.HelmetBlue.setText(_translate('MainWindow', 'Blue'))
        self.enterButton.setText(_translate('MainWindow', 'OK'))
        