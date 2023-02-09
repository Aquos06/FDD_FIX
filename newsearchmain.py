from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor
from components.searchBox import searchBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        MainWindow.setStyleSheet("background:black;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-image : url(background.png);")
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        
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
                                                background-color: black;
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
                                                background-color: #00BDFE;
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Group 104.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ppe.setIcon(icon)
        self.ppe.setIconSize(QtCore.QSize(60, 60))
        self.ppe.setObjectName("ppe")
        self.ppe.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
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
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background:black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_5.setContentsMargins(30, 0, 20, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem6) #0
        self.label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setStyleSheet("color:white;")
        self.label.setObjectName("label")
        self.horizontalLayout_6.addWidget(self.label) #1
        
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7) #2
        
        self.startdate = QtWidgets.QDateEdit(self.frame_2)
        self.startdate.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startdate.setFont(font)
        self.startdate.setStyleSheet("background:white;")
        self.startdate.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 4, 1), QtCore.QTime(0, 0, 0)))
        self.startdate.setCalendarPopup(True)
        self.startdate.setObjectName("startdate")
        self.horizontalLayout_6.addWidget(self.startdate) #3
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)#4
        self.starttime = QtWidgets.QTimeEdit(self.frame_2)
        self.starttime.setMinimumSize(QtCore.QSize(0, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.starttime.setFont(font)
        self.starttime.setStyleSheet("background:white;")
        self.starttime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(12, 0, 0)))
        self.starttime.setObjectName("starttime")
        self.horizontalLayout_6.addWidget(self.starttime)#5
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)#6
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color:white;")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3) #7
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem10) #8
        self.enddate = QtWidgets.QDateEdit(self.frame_2)
        self.enddate.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enddate.setFont(font)
        self.enddate.setStyleSheet("background:white;")
        self.enddate.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
        self.enddate.setCalendarPopup(True)
        self.enddate.setObjectName("enddate")
        self.horizontalLayout_6.addWidget(self.enddate) #9
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem11) #10
        self.endtime = QtWidgets.QTimeEdit(self.frame_2)
        self.endtime.setMinimumSize(QtCore.QSize(0, 29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.endtime.setFont(font)
        self.endtime.setStyleSheet("background:white;")
        self.endtime.setDateTime(QtCore.QDateTime(QtCore.QDate(2000, 1, 1), QtCore.QTime(12, 0, 0)))
        self.endtime.setObjectName("endtime")
        self.horizontalLayout_6.addWidget(self.endtime) #11
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem12) #12
        
        self.type = QtWidgets.QComboBox(self.frame_2)
        self.type.setMaximumSize(QtCore.QSize(150,40))
        self.type.setMinimumSize(QtCore.QSize(150,40))
        self.type.setStyleSheet("background:white; font-size: 20px;")
        self.type.setObjectName("type")
        self.type.addItem("")
        self.type.addItem("")
        self.horizontalLayout_6.addWidget(self.type) #13
        
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem15) #14

        self.label_7 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:white;")
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)#15

        self.channel = QtWidgets.QComboBox(self.frame_2)
        self.channel.setStyleSheet("background:white;")
        self.channel.setMaximumSize(QtCore.QSize(150,40))
        self.channel.setMinimumSize(QtCore.QSize(150,40))
        self.channel.setStyleSheet("background:white; font-size: 20px;")
        self.channel.setObjectName("channel")
        self.channel.addItem("")
        self.channel.addItem("")
        self.channel.addItem("")
        self.channel.addItem("")
        self.channel.addItem("")
        self.horizontalLayout_6.addWidget(self.channel)#16
        
        self.label_6 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color:white;")
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_6.addItem(spacerItem) #17
        self.horizontalLayout_6.addWidget(self.label_6) #18
        self.horizontalLayout_6.addItem(spacerItem) #19

        self.total = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.total.setFont(font)
        self.total.setStyleSheet("color:white;")
        self.total.setObjectName("total")
        self.horizontalLayout_6.addWidget(self.total) #20
        self.horizontalLayout_6.addItem(spacerItem) #21

        self.start = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.start.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.start.setFont(font)
        self.start.setStyleSheet("background:#069CFF;")
        self.start.setObjectName("start")
        self.horizontalLayout_6.addWidget(self.start) #15
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem16) #16
        self.cancel = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cancel.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.cancel.setFont(font)
        self.cancel.setStyleSheet("background:#069CFF;\n"
"")
        self.cancel.setObjectName("cancel")
        self.horizontalLayout_6.addWidget(self.cancel) #17
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem17) #18
        self.output = QtWidgets.QPushButton(self.frame_2)
        self.output.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.output.setFont(font)
        self.output.setStyleSheet("background:#069CFF;\n"
"")
        self.output.setObjectName("output")
        self.horizontalLayout_6.addWidget(self.output) #19
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem18) #20
        self.horizontalLayout_6.setStretch(0, 2)
        self.horizontalLayout_6.setStretch(1, 2)
        self.horizontalLayout_6.setStretch(2, 1)
        self.horizontalLayout_6.setStretch(3, 2)
        self.horizontalLayout_6.setStretch(4, 1)
        self.horizontalLayout_6.setStretch(5, 2)
        self.horizontalLayout_6.setStretch(6, 2)
        self.horizontalLayout_6.setStretch(7, 2)
        self.horizontalLayout_6.setStretch(8, 1)
        self.horizontalLayout_6.setStretch(9, 2)
        self.horizontalLayout_6.setStretch(10, 1)
        self.horizontalLayout_6.setStretch(11, 2)
        self.horizontalLayout_6.setStretch(12, 2)
        self.horizontalLayout_6.setStretch(13, 2)
        self.horizontalLayout_6.setStretch(14, 2)
        self.horizontalLayout_6.setStretch(15, 2)
        self.horizontalLayout_6.setStretch(16, 2)
        self.horizontalLayout_6.setStretch(17, 2)
        self.horizontalLayout_6.setStretch(18, 2)
        self.horizontalLayout_6.setStretch(19, 2)
        self.horizontalLayout_6.setStretch(20, 2)
        self.horizontalLayout_6.setStretch(21, 2)

        self.horizontalLayout_6.setStretch(22, 1)
        self.horizontalLayout_6.setStretch(23, 2)
        self.horizontalLayout_6.setStretch(24, 1)
        self.horizontalLayout_6.setStretch(25, 2)
        self.horizontalLayout_6.setStretch(26, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
    
        #############################################################################################################
        #############################################################################################################
        
        # self.scrollArea = QtWidgets.QScrollArea(self.frame_2)

        # self.verticalScrollBar = QtWidgets.QScrollBar(QtCore.Qt.Vertical, self.scrollArea)
        # self.scrollArea.setVerticalScrollBar(self.verticalScrollBar)
        # self.scrollArea.setWidgetResizable(True)
        # self.scrollArea.setObjectName("scrollArea")
        
        # self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.setSpacing(0)

        self.AnsHorizontal1 = QtWidgets.QHBoxLayout()
        self.AnsHorizontal1.setSpacing(0)

        self.box1 = searchBox()
        self.box1.setMinimumHeight(200)
        self.AnsHorizontal1.addWidget(self.box1)
        self.box2 = searchBox()
        self.box2.setMinimumHeight(200)
        self.AnsHorizontal1.addWidget(self.box2)
        self.box3 = searchBox()
        self.box3.setMinimumHeight(200)
        self.AnsHorizontal1.addWidget(self.box3)
        self.box4 = searchBox()
        self.box4.setMinimumHeight(200)
        self.AnsHorizontal1.addWidget(self.box4)

        self.layout.addLayout(self.AnsHorizontal1)
        self.layout.addItem(spacerItem)

        self.AnsHorizontal2 = QtWidgets.QHBoxLayout()
        self.AnsHorizontal2.setSpacing(0)

        self.box5 = searchBox()
        self.box5.setMinimumHeight(200)
        self.AnsHorizontal2.addWidget(self.box5)
        self.box6 = searchBox()
        self.box6.setMinimumHeight(200)
        self.AnsHorizontal2.addWidget(self.box6)
        self.box7 = searchBox()
        self.box7.setMinimumHeight(200)
        self.AnsHorizontal2.addWidget(self.box7)
        self.box8 = searchBox()
        self.box8.setMinimumHeight(200)
        self.AnsHorizontal2.addWidget(self.box8)
        
        self.layout.addLayout(self.AnsHorizontal2)
        self.layout.addItem(spacerItem)

        self.AnsHorizontal3 = QtWidgets.QHBoxLayout()
        self.AnsHorizontal3.setSpacing(0)

        self.box9 = searchBox()
        self.box9.setMinimumHeight(200)
        self.AnsHorizontal3.addWidget(self.box9)
        self.box10 = searchBox()
        self.box10.setMinimumHeight(200)
        self.AnsHorizontal3.addWidget(self.box10)
        self.box11 = searchBox()
        self.box11.setMinimumHeight(200)
        self.AnsHorizontal3.addWidget(self.box11)
        self.box12 = searchBox()
        self.box12.setMinimumHeight(200)
        self.AnsHorizontal3.addWidget(self.box12)
        
        self.layout.addLayout(self.AnsHorizontal3)
        self.layout.addItem(spacerItem)

        self.AnsHorizontal4 = QtWidgets.QHBoxLayout()
        self.AnsHorizontal4.setSpacing(0)

        self.box13 = searchBox()
        self.box13.setMinimumHeight(200)
        self.AnsHorizontal4.addWidget(self.box13)
        self.box14 = searchBox()
        self.box14.setMinimumHeight(200)
        self.AnsHorizontal4.addWidget(self.box14)
        self.box15 = searchBox()
        self.box15.setMinimumHeight(200)
        self.AnsHorizontal4.addWidget(self.box15)
        self.box16 = searchBox()
        self.box16.setMinimumHeight(200)
        self.AnsHorizontal4.addWidget(self.box16)

        self.layout.addLayout(self.AnsHorizontal4)
        self.layout.addItem(spacerItem)

        self.layout.setStretch(0,20)
        self.layout.setStretch(1,1)
        self.layout.setStretch(2,20)
        self.layout.setStretch(3,1)
        self.layout.setStretch(4,20)
        self.layout.setStretch(5,1)
        self.layout.setStretch(6,20)
        self.layout.setStretch(7,1)

        self.verticalLayout.addLayout(self.layout)

        self.PageButton = QtWidgets.QHBoxLayout()
        self.PageButton.setSpacing(0)

        self.leftPage = QtWidgets.QPushButton()
        self.leftPage.setText('<')
        self.leftPage.setFont(font)
        self.leftPage.setStyleSheet(""" 
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
        self.leftPage.setDefault(True)
        self.leftPage.setMaximumSize(QtCore.QSize(40,40))
        self.leftPage.setMinimumSize(QtCore.QSize(40,40))
        self.leftPage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.PageButton.addItem(spacerItem)
        self.PageButton.addWidget(self.leftPage)

        self.labelPage = QtWidgets.QLabel()
        self.labelPage.setFont(font)
        self.labelPage.setText("0/0")
        self.labelPage.setStyleSheet("color:white")
        
        self.PageButton.addItem(spacerItem)
        self.PageButton.addWidget(self.labelPage)
        

        self.rightPage = QtWidgets.QPushButton()
        self.rightPage.setText(">")
        self.rightPage.setFont(font)
        self.rightPage.setStyleSheet(""" 
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
        self.rightPage.setDefault(True)
        self.rightPage.setMaximumSize(QtCore.QSize(40,40))
        self.rightPage.setMinimumSize(QtCore.QSize(40,40))
        self.leftPage.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.PageButton.addItem(spacerItem)
        self.PageButton.addWidget(self.rightPage)
        self.PageButton.addItem(spacerItem)

        self.PageButton.setStretch(0,10)
        self.PageButton.setStretch(1,1)
        self.PageButton.setStretch(2,10)
        self.PageButton.setStretch(3,1)
        self.PageButton.setStretch(4,10)
        self.PageButton.setStretch(5,1)
        self.PageButton.setStretch(6,10)

        self.verticalLayout.addLayout(self.PageButton)

        self.verticalLayout.setStretch(0,20)
        self.verticalLayout.setStretch(1,1)

        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.setStretch(0, 80)
        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0, 20)
        self.horizontalLayout_11.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.verticalLayout_2.setStretch(0, 1)
        self.verticalLayout_2.setStretch(1, 80)
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
        self.pushButton_6.setIcon(QtGui.QIcon("home_white.png"))
        self.pushButton_6.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_8.setIcon(QtGui.QIcon("video.png"))
        self.pushButton_8.setIconSize(QtCore.QSize(70, 70))
        self.pushButton_7.setIcon(QtGui.QIcon("settings_white.png"))
        self.pushButton_7.setIconSize(QtCore.QSize(60, 60))
        self.pushButton_search.setIcon(QtGui.QIcon("search_pls.png"))
        self.pushButton_search.setIconSize(QtCore.QSize(85,85))
        self.label_23.setText(_translate("MainWindow", "查詢"))
        self.label.setText(_translate("MainWindow", "開始時間"))
        self.startdate.setDisplayFormat(_translate("MainWindow", "yyyy / MM / dd"))
        self.starttime.setDisplayFormat(_translate("MainWindow", "HH:mm"))
        self.label_3.setText(_translate("MainWindow", "結束時間"))
        self.enddate.setDisplayFormat(_translate("MainWindow", "yyyy / MM / dd"))
        self.endtime.setDisplayFormat(_translate("MainWindow", "HH:mm"))
        self.start.setText(_translate("MainWindow", "查詢"))
        self.cancel.setText(_translate("MainWindow", "取消"))
        self.output.setText(_translate("MainWindow", "匯出"))
        self.label_7.setText(_translate("MainWindow", "頻道 "))
        
        self.type.setItemText(0, _translate("MainWindow", "All"))
        self.type.setItemText(1, _translate("MainWindow", "fall down"))
    
        self.channel.setItemText(0, _translate("MainWindow", "All"))
        self.channel.setItemText(1, _translate("MainWindow", "Camera 1"))
        self.channel.setItemText(2, _translate("MainWindow", "Camera 2"))
        self.channel.setItemText(3, _translate("MainWindow", "Camera 3"))
        self.channel.setItemText(4, _translate("MainWindow", "Camera 4"))
        
        self.label_6.setText(_translate("MainWindow", "總人數 ： "))
        self.total.setText(_translate("MainWindow", "0"))
        # self.pushButton_35.setText(_translate("MainWindow", "<<"))
        # self.label_4.setText(_translate("MainWindow", "0/0"))
        # self.pushButton_43.setText(_translate("MainWindow", ">>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
