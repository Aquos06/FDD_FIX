
from PyQt5 import QtCore, QtGui, QtWidgets
from .AICamPage import AiPage
from pyqt_main import roiwidge

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920,1080)
        MainWindow.setStyleSheet("background:black")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-image: url(background.png)")
        self.centralwidget.setObjectName("centralwidget")
        
        ######################################################################################
        
        self.horizontalLayoutMain = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayoutMain.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayoutMain.setSpacing(0)
        self.horizontalLayoutMain.setObjectName("horizontalLayout_4")
        self.verticalLayoutMain = QtWidgets.QVBoxLayout()
        self.verticalLayoutMain.setSpacing(0)
        self.verticalLayoutMain.setObjectName("verticalLayout_2")
        
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        
        self.label_10 = QtWidgets.QLabel(self.centralwidget) #logo
        self.label_10.setMaximumSize(QtCore.QSize(540, 95))
        self.label_10.setStyleSheet("background:blue")
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("logoo.png"))
        self.label_10.setScaledContents(False)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_5.addWidget(self.label_10) #horizontal 0
        
        self.horizontalLayout_logo = QtWidgets.QHBoxLayout()
        self.horizontalLayout_logo.setSpacing(0)
        self.horizontalLayout_logo.setObjectName("HorizontalLayout_logo")
        
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget) #go back to menu
        self.pushButton_6.setMinimumSize(QtCore.QSize(80,80))
        self.pushButton_6.setMaximumSize(QtCore.QSize(80,80))
        self.pushButton_6.setStyleSheet("""
                                        QPushButton{
                                                background-color: black;
                                                color:white;
                                                border-radius:10px;
                                        }
                                        QPushButton:hover{
                                                background-color: #00BDFE;
                                        }
                                """)
        self.pushButton_6.setDefault(True)
        self.pushButton_6.setFlat(True)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout_logo.addWidget(self.pushButton_6)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_logo.addItem(spacerItem) 
        
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget) 
        self.pushButton_7.setMinimumSize(QtCore.QSize(80,80))
        self.pushButton_7.setMaximumSize(QtCore.QSize(80,80))
        self.pushButton_7.setStyleSheet("""
                                        QPushButton{
                                                background-color: #00BDFE;
                                                color:white;
                                                border-radius:10px;
                                        }
                                        QPushButton:hover{
                                                background-color: #00BDFE;
                                        }
                                """)
        self.pushButton_7.setDefault(True)
        self.pushButton_7.setFlat(True)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout_logo.addWidget(self.pushButton_7) 
        
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_logo.addItem(spacerItem1) 

        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget) #gotosettings
        self.pushButton_8.setMinimumSize(QtCore.QSize(80,80))
        self.pushButton_8.setMaximumSize(QtCore.QSize(80,80))
        self.pushButton_8.setStyleSheet("""
                                        QPushButton{
                                                background-color: black;
                                                color:white;
                                                border-radius:10px;
                                        }
                                        QPushButton:hover{
                                                background-color: #00BDFE;
                                        }
                                """)
        self.pushButton_8.setDefault(True)
        self.pushButton_8.setFlat(True)
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalLayout_logo.addWidget(self.pushButton_8) 
        
        self.horizontalLayout_logo.addItem(spacerItem)
        
        self.pushButton_search = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_search.setMinimumSize(QtCore.QSize(80,80))
        self.pushButton_search.setMaximumSize(QtCore.QSize(80,80))
        self.pushButton_search.setStyleSheet("""
                                        QPushButton{
                                                background-color: black;
                                                color:white;
                                                border-radius:10px;
                                        }
                                        QPushButton:hover{
                                                background-color: #00BDFE;
                                        }
                                """)
        self.pushButton_search.setDefault(True)
        self.pushButton_search.setFlat(True)
        self.pushButton_search.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_search.setObjectName("PushButton_search")
        self.horizontalLayout_logo.addWidget(self.pushButton_search)
        
        self.horizontalLayout_logo.addItem(spacerItem)
        
        self.horizontalLayout_logo.setStretch(0,10)
        self.horizontalLayout_logo.setStretch(1,1)
        self.horizontalLayout_logo.setStretch(2,9)
        self.horizontalLayout_logo.setStretch(3,1)
        self.horizontalLayout_logo.setStretch(4,9)
        self.horizontalLayout_logo.setStretch(5,1)
        self.horizontalLayout_logo.setStretch(6,9)
        self.horizontalLayout_logo.setStretch(8,10)
        
        self.horizontalLayout_5.addLayout(self.horizontalLayout_logo) #horizontal -2
        
        
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3) #horizontal -3
        
        self.label_23 = QtWidgets.QLabel(self.centralwidget) #tanda window
        font = QtGui.QFont()
        font.setFamily("Noto Sans CJK TC")
        font.setPointSize(20)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet("color:#707070;")
        self.label_23.setObjectName("label_23")
        self.horizontalLayout_5.addWidget(self.label_23) #horizontal -4
        
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4) #horizontal - 5
        
        self.ppe = QtWidgets.QPushButton(self.centralwidget)#logo
        self.ppe.setMaximumSize(QtCore.QSize(60, 60))
        self.ppe.setAutoFillBackground(False)
        self.ppe.setStyleSheet("border-radius: 15px;")
        self.ppe.setText("")
        self.ppe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Group 104.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ppe.setIcon(icon)
        self.ppe.setIconSize(QtCore.QSize(60, 60))
        self.ppe.setObjectName("ppe")
        
        self.horizontalLayout_5.addWidget(self.ppe) #horizontal - 6
        
        
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5) #horizontal - 7
        
        self.horizontalLayout_5.setStretch(0, 3)
        self.horizontalLayout_5.setStretch(1, 80)
        self.horizontalLayout_5.setStretch(2, 10)
        self.horizontalLayout_5.setStretch(3, 1)
        self.horizontalLayout_5.setStretch(4, 1)
        self.horizontalLayout_5.setStretch(5, 1)
        self.horizontalLayout_5.setStretch(6, 2)
        
        
        self.verticalLayoutMain.addLayout(self.horizontalLayout_5)
        
        ########################################################################################################################
        #settings kiri
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("background:#121E28;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        
        
        self.pushButton_2 = QtWidgets.QPushButton(self.frame) #settings 1 and 2
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet("color:white;")
        self.pushButton_2.setObjectName("pushButton_2") #gong neng
        self.verticalLayout.addWidget(self.pushButton_2)
        
        self.pushButton_0 = QtWidgets.QPushButton(self.frame) #settings 1 and 2
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_0.setFont(font)
        self.pushButton_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_0.setStyleSheet("color:white;")
        self.pushButton_0.setObjectName("pushButton_0") #gong neng
        self.verticalLayout.addWidget(self.pushButton_0)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet("color:white;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)#belum ke isi
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setStyleSheet("color:white;background-color:#3A3C41")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setStyleSheet('color: white')
        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButtonReset = QtWidgets.QPushButton(self.frame)
        self.pushButtonReset.setText('Factory Reset')
        self.pushButtonReset.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButtonReset.setFont(font)
        self.pushButtonReset.setAutoFillBackground(False)
        self.pushButtonReset.setStyleSheet('color: white')
        self.verticalLayout.addWidget(self.pushButtonReset, alignment = QtCore.Qt.AlignBottom)

        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem6)
        
        self.verticalLayout_4.addLayout(self.verticalLayout)
        
        self.horizontalLayout.addWidget(self.frame)
        
        ###################################################################################################################
        
        self.layoutMain = QtWidgets.QVBoxLayout()
        self.layoutMain.setSpacing(0)
        self.layoutMain.setObjectName('LayoutMain')
        
        self.tabs = QtWidgets.QTabWidget()
        self.tabs.setStyleSheet(""" 
                            QTabWidget::tab-bar {
                                border: 1px solid gray;
                                }
                                
                            QTabBar::tab {
                                background: #4277BD;
                                color: white;
                                padding: 10px;
                                width : 100px;
                                height:30px;
                                border-top-left-radius: 5;
                                border-top-right-radius: 5;
                                font-size: 20px;
                            }

                            QTabBar::tab:selected {
                                background: black;
                                margin-bottom: -1px; 
                            }
                            QTabWidget::pane { 
                                border: none;
                                top:-1px; 
                            }
                                """)
        
        self.tabCamera1 = QtWidgets.QWidget()
        self.tabCamera2 = QtWidgets.QWidget()
        self.tabCamera3 = QtWidgets.QWidget()
        self.tabCamera4 = QtWidgets.QWidget()
        
        self.tabs.addTab(self.tabCamera1, "Camera 1")
        self.tabs.addTab(self.tabCamera2, "Camera 2")
        self.tabs.addTab(self.tabCamera3, "Camera 3")
        self.tabs.addTab(self.tabCamera4, "Camera 4")

        self.tabCamera1.layout = QtWidgets.QVBoxLayout()
        self.fill_1 = AiPage()
        self.fill_1.setupUi()
        self.fill_1.ROI.setChannel(0)
        self.tabCamera1.layout.addWidget(self.fill_1)
        self.tabCamera1.setLayout(self.tabCamera1.layout)
        
        self.tabCamera2.layout = QtWidgets.QVBoxLayout()
        self.fill_2 = AiPage()
        self.fill_2.setupUi()
        self.fill_2.ROI.setChannel(1)
        self.tabCamera2.layout.addWidget(self.fill_2)
        self.tabCamera2.setLayout(self.tabCamera2.layout)
        
        self.tabCamera3.layout = QtWidgets.QVBoxLayout()
        self.fill_3 = AiPage()
        self.fill_3.setupUi()
        self.fill_3.ROI.setChannel(2)
        self.tabCamera3.layout.addWidget(self.fill_3)
        self.tabCamera3.setLayout(self.tabCamera3.layout)
        
        self.tabCamera4.layout = QtWidgets.QVBoxLayout()
        self.fill_4 = AiPage()
        self.fill_4.setupUi()
        self.fill_4.ROI.setChannel(3)
        self.tabCamera4.layout.addWidget(self.fill_4)
        self.tabCamera4.setLayout(self.tabCamera4.layout)
        
        self.layoutMain.addWidget(self.tabs)
        
        self.horizontalLayout.addLayout(self.layoutMain)
        
        self.horizontalLayout.setStretch(0,3)
        self.horizontalLayout.setStretch(1,20)
        
        self.verticalLayoutMain.addLayout(self.horizontalLayout)
        self.verticalLayoutMain.addItem(spacerItem)
        
        self.verticalLayoutMain.setStretch(0,1)
        self.verticalLayoutMain.setStretch(1,80)
        self.verticalLayoutMain.setStretch(2,3)
        
        self.horizontalLayoutMain.addLayout(self.verticalLayoutMain)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,1920,22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusBar)
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        
        self.pushButton_6.setIcon(QtGui.QIcon("home_white.png"))
        self.pushButton_6.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_8.setIcon(QtGui.QIcon("video.png"))
        self.pushButton_8.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_7.setIcon(QtGui.QIcon("settings_white.png"))
        self.pushButton_7.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_search.setIcon(QtGui.QIcon("search_pls.png"))
        self.pushButton_search.setIconSize(QtCore.QSize(85,85))
        
        self.label_23.setText(_translate("MainWindow", "設定"))
        self.pushButton_2.setText(_translate("MainWindow", "Camera Settings"))
        self.pushButton_0.setText(_translate("MainWindow", "Device Settings"))
        self.pushButton_3.setText(_translate("MainWindow", "功能設定"))
        self.pushButton_4.setText(_translate("MainWindow", "AI Settings"))
        self.pushButton_5.setText(_translate("MainWindow", "Log"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

        
        
