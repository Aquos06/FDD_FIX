from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor

class LogUI(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920,1080)
        MainWindow.setStyleSheet('background:black;')

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setStyleSheet("background-image : url(background.png);")
        self.centralwidget.setObjectName("centralwidget")
        
        #############################################################################################################
        #############################################################################################################
        
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
        
        
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        
        #############################################################################################################
        #############################################################################################################
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
        self.pushButton_0.setStyleSheet("color:white;")
        self.pushButton_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_0.setObjectName("pushButton_0") #gong neng
        self.verticalLayout.addWidget(self.pushButton_0)
        
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setStyleSheet("color:white;")
        self.pushButton_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)#ke AI
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setAutoFillBackground(False)
        self.pushButton_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_4.setStyleSheet("color:white;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setFont(font)
        self.pushButton_5.setAutoFillBackground(False)
        self.pushButton_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_5.setStyleSheet('color:white;background:#3A3C41;\n')
        self.pushButton_5.setObjectName('pushButton_5')
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
        ###################################################################################

        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())

        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet("background:black")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")

        self.verticalLayout_log = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_log.setSpacing(0)
        self.verticalLayout_log.setObjectName('verticalLayout_log')

        self.horizontalDate = QtWidgets.QHBoxLayout()
        self.horizontalDate.setSpacing(0)

        self.startDateLabel = QtWidgets.QLabel()
        self.startDateLabel.setFont(font)
        self.startDateLabel.setStyleSheet('color:white')
        
        self.horizontalDate.addItem(spacerItem)
        self.horizontalDate.addWidget(self.startDateLabel)
        self.horizontalDate.addItem(spacerItem)

        self.startdate = QtWidgets.QDateEdit(self.frame_2)
        self.startdate.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.startdate.setFont(font)
        self.startdate.setStyleSheet("background:white;")
        self.startdate.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 4, 1), QtCore.QTime(0, 0, 0)))
        self.startdate.setCalendarPopup(True)
        self.startdate.setObjectName("startdate")

        self.horizontalDate.addWidget(self.startdate)
        self.horizontalDate.addItem(spacerItem)

        self.horizontalDate.setStretch(0,6)
        self.horizontalDate.setStretch(1,3)
        self.horizontalDate.setStretch(2,1)
        self.horizontalDate.setStretch(3,3)
        self.horizontalDate.setStretch(4,6)
        
        self.verticalLayout_log.addLayout(self.horizontalDate)

        self.horizontalTime = QtWidgets.QHBoxLayout()
        self.horizontalTime.setSpacing(0)

        self.setstartTime = QtWidgets.QLabel(self.frame_2)
        self.setstartTime.setFont(font)
        self.setstartTime.setStyleSheet('color:white')
        self.horizontalTime.addItem(spacerItem)
        self.horizontalTime.addWidget(self.setstartTime)

        self.setstartTimeEdit = QtWidgets.QTimeEdit(self.frame_2)
        self.setstartTimeEdit.setMinimumSize(QtCore.QSize(0,29))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.setstartTimeEdit.setFont(font)
        self.setstartTimeEdit.setStyleSheet('background:white')
        self.setstartTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000,1,1), QtCore.QTime(12,0,0)))
        self.horizontalTime.addItem(spacerItem)
        self.horizontalTime.addWidget(self.setstartTimeEdit)
        self.horizontalTime.addItem(spacerItem)

        self.horizontalTime.setStretch(0,6)
        self.horizontalTime.setStretch(1,3)
        self.horizontalTime.setStretch(2,1)
        self.horizontalTime.setStretch(3,3)
        self.horizontalTime.setStretch(4,6)
        self.verticalLayout_log.addLayout(self.horizontalTime)

        self.horizontalDateEnd = QtWidgets.QHBoxLayout()
        self.horizontalDateEnd.setSpacing(0)

        self.endDateLabel = QtWidgets.QLabel()
        self.endDateLabel.setFont(font)
        self.endDateLabel.setStyleSheet('color:white')
        
        self.horizontalDateEnd.addItem(spacerItem)
        self.horizontalDateEnd.addWidget(self.endDateLabel)
        self.horizontalDateEnd.addItem(spacerItem)

        self.enddate = QtWidgets.QDateEdit(self.frame_2)
        self.enddate.setMaximumSize(QtCore.QSize(16777215, 27))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.enddate.setFont(font)
        self.enddate.setStyleSheet("background:white;")
        self.enddate.setDateTime(QtCore.QDateTime(QtCore.QDate(2023, 4, 1), QtCore.QTime(0, 0, 0)))
        self.enddate.setCalendarPopup(True)
        self.enddate.setObjectName("enddate")

        self.horizontalDateEnd.addWidget(self.enddate)
        self.horizontalDateEnd.addItem(spacerItem)

        self.horizontalDateEnd.setStretch(0,6)
        self.horizontalDateEnd.setStretch(1,3)
        self.horizontalDateEnd.setStretch(2,1)
        self.horizontalDateEnd.setStretch(3,3)
        self.horizontalDateEnd.setStretch(4,6)
        
        self.verticalLayout_log.addLayout(self.horizontalDateEnd)

        self.horizontalEndTime = QtWidgets.QHBoxLayout()
        self.horizontalEndTime.setSpacing(0)
        
        self.setendTime = QtWidgets.QLabel(self.frame_2)
        self.setendTime.setFont(font)
        self.setendTime.setStyleSheet('color:white')
        self.horizontalEndTime.addItem(spacerItem)
        self.horizontalEndTime.addWidget(self.setendTime)

        self.setendTimeEdit = QtWidgets.QTimeEdit(self.frame_2)
        self.setendTimeEdit.setFont(font)
        self.setendTimeEdit.setMinimumSize(QtCore.QSize(0,29))
        self.setendTimeEdit.setStyleSheet('background:white')
        self.setendTimeEdit.setDateTime(QtCore.QDateTime(QtCore.QDate(2000,1,1), QtCore.QTime(12,0,0)))
        self.horizontalEndTime.addItem(spacerItem)
        self.horizontalEndTime.addWidget(self.setendTimeEdit)
        self.horizontalEndTime.addItem(spacerItem)

        self.horizontalEndTime.setStretch(0,6)
        self.horizontalEndTime.setStretch(1,3)
        self.horizontalEndTime.setStretch(2,1)
        self.horizontalEndTime.setStretch(3,3)
        self.horizontalEndTime.setStretch(4,6)

        self.verticalLayout_log.addLayout(self.horizontalEndTime)

        self.horizontalRE = QtWidgets.QHBoxLayout()
        self.horizontalRE.setSpacing(0)

        self.RefreshButton = QtWidgets.QPushButton()
        self.RefreshButton.setText('Refresh')
        self.RefreshButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.RefreshButton.setStyleSheet("""
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
        self.RefreshButton.setMaximumSize(QtCore.QSize(80,30))
        self.RefreshButton.setMinimumSize(QtCore.QSize(80,30))

        self.horizontalRE.addItem(spacerItem)
        self.horizontalRE.addWidget(self.RefreshButton)

        self.okButton = QtWidgets.QPushButton()
        self.okButton.setText('Apply')
        self.okButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.okButton.setStyleSheet("""
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
        self.okButton.setMaximumSize(QtCore.QSize(80,30))
        self.okButton.setMinimumSize(QtCore.QSize(80,30))

        self.horizontalRE.addItem(spacerItem)
        self.horizontalRE.addWidget(self.okButton)
        self.horizontalRE.addItem(spacerItem)

        self.horizontalRE.setStretch(0,25)
        self.horizontalRE.setStretch(1,5)
        self.horizontalRE.setStretch(2,1)
        self.horizontalRE.setStretch(3,5)
        self.horizontalRE.setStretch(4,10)

        self.verticalLayout_log.addItem(spacerItem)
        self.verticalLayout_log.addLayout(self.horizontalRE)
        self.verticalLayout_log.addItem(spacerItem)

        self.tableLog = QtWidgets.QTableWidget()
        self.tableLog.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableLog.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableLog.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)
        self.tableLog.setColumnCount(4) #no, tanggal, akun, ngapain
        self.tableLog.setStyleSheet(
            """
            QHeaderView{
                background: transparent;
            }
            QHeaderView{
                font-size:14 px;
                color:white;
                border:none;
                text-align:left;
                margin-left:0px;
                padding-left:0px;
            }
            QTableWidget{
                color:#7e7e7e;
                font-size: 20px;
            }
            """
        )

        self.header = self.tableLog.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)

        self.tableLog.verticalHeader().setFixedWidth(50)
        self.tableLog.verticalHeader().setVisible(False)

        item = QtWidgets.QTableWidgetItem()
        self.tableLog.setHorizontalHeaderItem(0, item)
        
        item = QtWidgets.QTableWidgetItem()
        self.tableLog.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableLog.setHorizontalHeaderItem(2, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableLog.setHorizontalHeaderItem(3, item)

        self.verticalLayout_log.addWidget(self.tableLog)

        self.horizontalPage = QtWidgets.QHBoxLayout()
        self.horizontalPage.setSpacing(0)
        
        self.leftButton = QtWidgets.QPushButton()
        self.leftButton.setFont(font)
        self.leftButton.setStyleSheet("""
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
        self.leftButton.setText('<')
        self.leftButton.setMinimumSize(QtCore.QSize(30,30))
        self.leftButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.horizontalPage.addWidget(self.leftButton, alignment = QtCore.Qt.AlignCenter)
        
        self.pageLabel = QtWidgets.QLabel()
        self.pageLabel.setFont(font)
        self.pageLabel.setStyleSheet("color:white") 
        self.pageLabel.setText('0 / 0')
        self.horizontalPage.addWidget(self.pageLabel, alignment = QtCore.Qt.AlignCenter)

        self.rightButton = QtWidgets.QPushButton()
        self.rightButton.setFont(font)
        self.rightButton.setStyleSheet("""
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
        self.rightButton.setText('>')
        self.rightButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.rightButton.setMinimumSize(QtCore.QSize(30,30))
        self.rightButton.setMaximumSize(QtCore.QSize(30,30))
        self.horizontalPage.addWidget(self.rightButton, alignment= QtCore.Qt.AlignCenter)

        self.jumpTo = QtWidgets.QLineEdit()
        self.jumpTo.setFont(font)
        self.jumpTo.setStyleSheet('color:white; border: 1px solid white; margin-right:10px')
        self.jumpTo.setMaximumWidth(50)
        self.jumpTo.setMinimumWidth(50)
        self.horizontalPage.addWidget(self.jumpTo)

        self.enterJump = QtWidgets.QPushButton()
        self.enterJump.setFont(font)
        self.enterJump.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.enterJump.setText('go')
        self.enterJump.setStyleSheet("""
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
        self.enterJump.setMaximumSize(QtCore.QSize(30,30))
        self.enterJump.setMinimumSize(QtCore.QSize(30,30))
        self.horizontalPage.addWidget(self.enterJump)

        self.verticalLayout_log.addLayout(self.horizontalPage)

        self.horizontalButton = QtWidgets.QHBoxLayout()
        self.horizontalButton.setSpacing(0)
        self.horizontalButton.addItem(spacerItem)
        
        self.exportButton = QtWidgets.QPushButton()
        self.exportButton.setText('Export')
        self.exportButton.setFont(font)
        self.exportButton.setStyleSheet("""
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
        self.exportButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.exportButton.setMaximumSize(QtCore.QSize(80,30))
        self.exportButton.setMinimumSize(QtCore.QSize(80,30))
        self.horizontalButton.addWidget(self.exportButton)
        self.horizontalButton.addItem(spacerItem)

        self.deleteButton = QtWidgets.QPushButton()
        self.deleteButton.setText('Delete Log')
        self.deleteButton.setFont(font)
        self.deleteButton.setStyleSheet("""
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
        self.deleteButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.deleteButton.setMaximumSize(QtCore.QSize(120,30))
        self.deleteButton.setMinimumSize(QtCore.QSize(120,30))
        self.horizontalButton.addWidget(self.deleteButton) 
        self.horizontalButton.addItem(spacerItem)      

        self.horizontalButton.setStretch(0,25)
        self.horizontalButton.setStretch(1,3)
        self.horizontalButton.setStretch(2,1)
        self.horizontalButton.setStretch(3,3)
        self.horizontalButton.setStretch(4,5)

        self.verticalLayout_log.addItem(spacerItem)
        self.verticalLayout_log.addLayout(self.horizontalButton)

        self.horizontalLayout.addWidget(self.frame_2)
        self.horizontalLayout.setStretch(0,5)
        self.horizontalLayout.setStretch(1,30)

        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.horizontalLayout_4.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,1920,22))
        self.menubar.setObjectName('menubar')
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName('statusbar')
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
        
        self.label_23.setText(_translate("MainWindow", "設定"))
        self.pushButton_2.setText(_translate("MainWindow", "Camera Settings"))
        self.pushButton_0.setText(_translate("MainWindow", "Device Settings"))
        self.pushButton_3.setText(_translate("MainWindow", "功能設定"))
        self.pushButton_4.setText(_translate("MainWindow", "AI Settings"))
        self.pushButton_5.setText(_translate("MainWindow", "Log"))

        self.setstartTime.setText(_translate("MainWindow", "set Start Time: "))
        self.startdate.setDisplayFormat(_translate("MainWindow", "yyyy / MM / dd"))
        self.setstartTimeEdit.setDisplayFormat(_translate("MainWindow", "HH:mm"))
        self.enddate.setDisplayFormat(_translate("MainWindow", "yyyy / MM / dd"))
        self.setendTimeEdit.setDisplayFormat(_translate("MainWindow", "HH:mm"))
        self.setendTime.setText(_translate("MainWindow", 'set End Time: '))
        self.endDateLabel.setText(_translate("MainWindow", "set End Date: "))
        self.startDateLabel.setText(_translate("MaiWindow", 'set Start Date:'))

        item = self.tableLog.horizontalHeaderItem(0)
        item.setText('No.')
        item = self.tableLog.horizontalHeaderItem(1)
        item.setText('Date')
        item = self.tableLog.horizontalHeaderItem(2)
        item.setText('UserName')
        item = self.tableLog.horizontalHeaderItem(3)
        item.setText('Activity')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = LogUI()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())