from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QCursor

class TimeTable(QtWidgets.QWidget):
    def setupUi(self):
        super().__init__()
    
        self.setFixedSize(QtCore.QSize(1550,500))
        self.setStyleSheet('background: #00172D')
        self.setWindowTitle('Time Table')
        
        font = QtGui.QFont()       
        font.setFamily("Ubuntu Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(80)

        fontTitle = QtGui.QFont()       
        fontTitle.setFamily("Ubuntu Mono")
        fontTitle.setPointSize(30)
        fontTitle.setBold(True)
        fontTitle.setWeight(100)
        
        fontButton = QtGui.QFont()
        fontButton.setFamily("Ubuntu Mono")
        font.setPointSize(15)
        font.setBold(False)
        font.setWeight(50)
        
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        
        self.verticalLayoutMain = QtWidgets.QVBoxLayout()
        self.verticalLayoutMain.setSpacing(0)
        self.verticalLayoutMain.setObjectName('VerticalLayoutMain')
        
        self.TitleLabel = QtWidgets.QLabel()
        self.TitleLabel.setText('Monday')
        self.TitleLabel.setFont(fontTitle)
        self.TitleLabel.setObjectName('TitleLabel')
        self.TitleLabel.setStyleSheet('color: white')
        
        self.verticalLayoutMain.addItem(spacerItem) #0
        self.verticalLayoutMain.addWidget(self.TitleLabel, alignment = QtCore.Qt.AlignHCenter) #1
        self.verticalLayoutMain.addItem(spacerItem) #2
        
        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        
        self.verticalLayoutFrame = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayoutFrame.setSpacing(0)
        self.verticalLayoutFrame.setObjectName('verticalLayoutFrame')
        
        self.horizontalName = QtWidgets.QHBoxLayout()
        self.horizontalName.setSpacing(0)
        self.horizontalName.setObjectName('horizontalName')
        
        self.labelTitle = QtWidgets.QLabel()
        self.labelTitle.setMinimumSize(QtCore.QSize(60,20))
        self.labelTitle.setMaximumSize(QtCore.QSize(60,20))
        self.labelTitle.setStyleSheet("color:white")
        self.labelTitle.setText('')
     
        self.label_all = QtWidgets.QLabel()
        self.label_all.setMinimumSize(QtCore.QSize(40,25))
        self.label_all.setMaximumSize(QtCore.QSize(40,25))
        self.label_all.setAlignment(QtCore.Qt.AlignLeft)
        self.label_all.setFont(font)
        self.label_all.setStyleSheet('color: white')
        self.label_all.setText('全開')
        
        self.label_0 = QtWidgets.QLabel()
        self.label_0.setMinimumSize(QtCore.QSize(40,20))
        self.label_0.setMaximumSize(QtCore.QSize(40,20))
        self.label_0.setAlignment(QtCore.Qt.AlignLeft)
        self.label_0.setFont(font)
        self.label_0.setStyleSheet('color: white')
        self.label_0.setText('0')
     
        self.label_1 = QtWidgets.QLabel()
        self.label_1.setMinimumSize(QtCore.QSize(40,20))
        self.label_1.setMaximumSize(QtCore.QSize(40,20))
        self.label_1.setStyleSheet('color: white')
        self.label_1.setFont(font)
        self.label_1.setAlignment(QtCore.Qt.AlignLeft)
        self.label_1.setText('1')
     
        self.label_2 = QtWidgets.QLabel()
        self.label_2.setMinimumSize(QtCore.QSize(40,20))
        self.label_2.setMaximumSize(QtCore.QSize(40,20))
        self.label_2.setAlignment(QtCore.Qt.AlignLeft)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet('color: white')
        self.label_2.setText('2')
     
        self.label_3 = QtWidgets.QLabel()
        self.label_3.setMinimumSize(QtCore.QSize(40,20))
        self.label_3.setMaximumSize(QtCore.QSize(40,20))
        self.label_3.setAlignment(QtCore.Qt.AlignLeft)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet('color: white')
        self.label_3.setText('3')
     
        self.label_4 = QtWidgets.QLabel()
        self.label_4.setMinimumSize(QtCore.QSize(40,20))
        self.label_4.setMaximumSize(QtCore.QSize(40,20))
        self.label_4.setStyleSheet('color:white')
        self.label_4.setFont(font)
        self.label_4.setAlignment(QtCore.Qt.AlignLeft)
        self.label_4.setText('4')
     
        self.label_5 = QtWidgets.QLabel()
        self.label_5.setMinimumSize(QtCore.QSize(40,20))
        self.label_5.setMaximumSize(QtCore.QSize(40,20))
        self.label_5.setAlignment(QtCore.Qt.AlignLeft)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet('color: white')
        self.label_5.setText('5')
     
        self.label_6 = QtWidgets.QLabel()
        self.label_6.setMinimumSize(QtCore.QSize(40,20))
        self.label_6.setMaximumSize(QtCore.QSize(40,20))
        self.label_6.setStyleSheet('color: white')
        self.label_6.setFont(font)
        self.label_6.setAlignment(QtCore.Qt.AlignLeft)
        self.label_6.setText('6')
     
        self.label_7 = QtWidgets.QLabel()
        self.label_7.setMinimumSize(QtCore.QSize(40,20))
        self.label_7.setMaximumSize(QtCore.QSize(40,20))
        self.label_7.setStyleSheet('color: white')
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignLeft)
        self.label_7.setText('7')
     
        self.label_8 = QtWidgets.QLabel()
        self.label_8.setMinimumSize(QtCore.QSize(40,20))
        self.label_8.setMaximumSize(QtCore.QSize(40,20))
        self.label_8.setStyleSheet('color: white')
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignLeft)
        self.label_8.setText('8')
     
        self.label_9 = QtWidgets.QLabel()
        self.label_9.setMinimumSize(QtCore.QSize(40,20))
        self.label_9.setMaximumSize(QtCore.QSize(40,20))
        self.label_9.setStyleSheet('color: white')
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignLeft)
        self.label_9.setText('9')
     
        self.label_10 = QtWidgets.QLabel()
        self.label_10.setMinimumSize(QtCore.QSize(40,20))
        self.label_10.setMaximumSize(QtCore.QSize(40,20))
        self.label_10.setStyleSheet('color: white')
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignLeft)
        self.label_10.setText('10')
     
        self.label_11 = QtWidgets.QLabel()
        self.label_11.setMinimumSize(QtCore.QSize(40,20))
        self.label_11.setMaximumSize(QtCore.QSize(40,20))
        self.label_11.setStyleSheet('color: white')
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignLeft)
        self.label_11.setText('11')
     
        self.label_12 = QtWidgets.QLabel()
        self.label_12.setMinimumSize(QtCore.QSize(40,20))
        self.label_12.setMaximumSize(QtCore.QSize(40,20))
        self.label_12.setStyleSheet('color: white')
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignLeft)
        self.label_12.setText('12')
     
        self.label_13 = QtWidgets.QLabel()
        self.label_13.setMinimumSize(QtCore.QSize(40,20))
        self.label_13.setMaximumSize(QtCore.QSize(40,20))
        self.label_13.setStyleSheet('color: white')
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignLeft)
        self.label_13.setText('13')
     
        self.label_14 = QtWidgets.QLabel()
        self.label_14.setMinimumSize(QtCore.QSize(40,20))
        self.label_14.setMaximumSize(QtCore.QSize(40,20))
        self.label_14.setStyleSheet('color: white')
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignLeft)
        self.label_14.setText('14')
     
        self.label_15 = QtWidgets.QLabel()
        self.label_15.setMinimumSize(QtCore.QSize(40,20))
        self.label_15.setMaximumSize(QtCore.QSize(40,20))
        self.label_15.setStyleSheet('color: white')
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignLeft)
        self.label_15.setText('15')
     
        self.label_16 = QtWidgets.QLabel()
        self.label_16.setMinimumSize(QtCore.QSize(40,20))
        self.label_16.setMaximumSize(QtCore.QSize(40,20))
        self.label_16.setStyleSheet('color: white')
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignLeft)
        self.label_16.setText('16')
     
        self.label_17 = QtWidgets.QLabel()
        self.label_17.setMinimumSize(QtCore.QSize(40,20))
        self.label_17.setMaximumSize(QtCore.QSize(40,20))
        self.label_17.setStyleSheet('color: white')
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignLeft)
        self.label_17.setText('17')
     
        self.label_18 = QtWidgets.QLabel()
        self.label_18.setMinimumSize(QtCore.QSize(40,20))
        self.label_18.setMaximumSize(QtCore.QSize(40,20))
        self.label_18.setStyleSheet('color: white')
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignLeft)
        self.label_18.setText('18')
     
        self.label_19 = QtWidgets.QLabel()
        self.label_19.setMinimumSize(QtCore.QSize(40,20))
        self.label_19.setMaximumSize(QtCore.QSize(40,20))
        self.label_19.setStyleSheet('color: white')
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignLeft)
        self.label_19.setText('19')
     
        self.label_20 = QtWidgets.QLabel()
        self.label_20.setMinimumSize(QtCore.QSize(40,20))
        self.label_20.setMaximumSize(QtCore.QSize(40,20))
        self.label_20.setStyleSheet('color: white')
        self.label_20.setFont(font)
        self.label_20.setAlignment(QtCore.Qt.AlignLeft)
        self.label_20.setText('20')
     
        self.label_21 = QtWidgets.QLabel()
        self.label_21.setMinimumSize(QtCore.QSize(40,20))
        self.label_21.setMaximumSize(QtCore.QSize(40,20))
        self.label_21.setStyleSheet('color: white')
        self.label_21.setFont(font)
        self.label_21.setAlignment(QtCore.Qt.AlignLeft)
        self.label_21.setText('21')
     
        self.label_22 = QtWidgets.QLabel()
        self.label_22.setMinimumSize(QtCore.QSize(40,20))
        self.label_22.setMaximumSize(QtCore.QSize(40,20))
        self.label_22.setStyleSheet('color: white')
        self.label_22.setFont(font)
        self.label_22.setAlignment(QtCore.Qt.AlignLeft)
        self.label_22.setText('22')
     
        self.label_23 = QtWidgets.QLabel()
        self.label_23.setMinimumSize(QtCore.QSize(40,20))
        self.label_23.setMaximumSize(QtCore.QSize(40,20))
        self.label_23.setAlignment(QtCore.Qt.AlignLeft)
        self.label_23.setFont(font)
        self.label_23.setStyleSheet('color: white')
        self.label_23.setText('23')
     
        self.label_24 = QtWidgets.QLabel()
        self.label_24.setMinimumSize(QtCore.QSize(40,20))
        self.label_24.setMaximumSize(QtCore.QSize(40,20))
        self.label_24.setAlignment(QtCore.Qt.AlignLeft)
        self.label_24.setFont(font)
        self.label_24.setStyleSheet('color: white')
        self.label_24.setText('24')
     
        self.horizontalName.addWidget(self.labelTitle)   
        self.horizontalName.addWidget(self.label_all)   
        self.horizontalName.addWidget(self.label_0)        
        self.horizontalName.addWidget(self.label_1)        
        self.horizontalName.addWidget(self.label_2)        
        self.horizontalName.addWidget(self.label_3)        
        self.horizontalName.addWidget(self.label_4)        
        self.horizontalName.addWidget(self.label_5)        
        self.horizontalName.addWidget(self.label_6)        
        self.horizontalName.addWidget(self.label_7)        
        self.horizontalName.addWidget(self.label_8)        
        self.horizontalName.addWidget(self.label_9)        
        self.horizontalName.addWidget(self.label_10)        
        self.horizontalName.addWidget(self.label_11)        
        self.horizontalName.addWidget(self.label_12)        
        self.horizontalName.addWidget(self.label_13)        
        self.horizontalName.addWidget(self.label_14)        
        self.horizontalName.addWidget(self.label_15)        
        self.horizontalName.addWidget(self.label_16)        
        self.horizontalName.addWidget(self.label_17)        
        self.horizontalName.addWidget(self.label_18)        
        self.horizontalName.addWidget(self.label_19)        
        self.horizontalName.addWidget(self.label_20)        
        self.horizontalName.addWidget(self.label_21)        
        self.horizontalName.addWidget(self.label_22)        
        self.horizontalName.addWidget(self.label_23)        
        self.horizontalName.addWidget(self.label_24)
        
        self.verticalLayoutFrame.addLayout(self.horizontalName)
        self.verticalLayoutFrame.addItem(spacerItem)
        
        self.horizontalCamera1 = QtWidgets.QHBoxLayout()
        self.horizontalCamera1.setSpacing(0)       
        self.horizontalCamera1.setObjectName('HorizontalCamera1')
        
        self.camera1 = QtWidgets.QLabel()
        self.camera1.setMinimumSize(QtCore.QSize(60,20))
        self.camera1.setMaximumSize(QtCore.QSize(60,20))
        self.camera1.setAlignment(QtCore.Qt.AlignLeft)
        self.camera1.setStyleSheet("color:white")
        self.camera1.setText('Camera 1')
        
        self.camera1_all = QtWidgets.QPushButton()
        self.camera1_all.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_all.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_all.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_all.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_all.setCheckable(True)
        self.camera1_all.setText('') 
        
        self.camera1_0 = QtWidgets.QPushButton()
        self.camera1_0.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_0.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_0.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_0.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_0.setCheckable(True)
        self.camera1_0.setText('') 
     
        self.camera1_1 = QtWidgets.QPushButton()
        self.camera1_1.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_1.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_1.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_1.setCheckable(True)
        self.camera1_1.setText('') 
     
        self.camera1_2 = QtWidgets.QPushButton()
        self.camera1_2.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_2.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_2.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_2.setCheckable(True)
        self.camera1_2.setText('') 
     
        self.camera1_3 = QtWidgets.QPushButton()
        self.camera1_3.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_3.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_3.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_3.setCheckable(True)
        self.camera1_3.setText('') 
     
        self.camera1_4 = QtWidgets.QPushButton()
        self.camera1_4.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_4.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_4.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_4.setCheckable(True)
        self.camera1_4.setText('') 
     
        self.camera1_5 = QtWidgets.QPushButton()
        self.camera1_5.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_5.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_5.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_5.setCheckable(True)
        self.camera1_5.setText('') 
     
        self.camera1_6 = QtWidgets.QPushButton()
        self.camera1_6.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_6.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_6.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_6.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_6.setCheckable(True)
        self.camera1_6.setText('') 
     
        self.camera1_7 = QtWidgets.QPushButton()
        self.camera1_7.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_7.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_7.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_7.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_7.setCheckable(True)
        self.camera1_7.setText('') 
     
        self.camera1_8 = QtWidgets.QPushButton()
        self.camera1_8.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_8.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_8.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_8.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_8.setCheckable(True)
        self.camera1_8.setText('') 
     
        self.camera1_9 = QtWidgets.QPushButton()
        self.camera1_9.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_9.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_9.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_9.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_9.setCheckable(True)
        self.camera1_9.setText('') 
     
        self.camera1_10 = QtWidgets.QPushButton()
        self.camera1_10.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_10.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_10.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_10.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_10.setCheckable(True)
        self.camera1_10.setText('') 
     
        self.camera1_11 = QtWidgets.QPushButton()
        self.camera1_11.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_11.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_11.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_11.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_11.setCheckable(True)
        self.camera1_11.setText('') 
     
        self.camera1_12 = QtWidgets.QPushButton()
        self.camera1_12.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_12.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_12.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_12.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_12.setCheckable(True)
        self.camera1_12.setText('') 
     
        self.camera1_13 = QtWidgets.QPushButton()
        self.camera1_13.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_13.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_13.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_13.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_13.setCheckable(True)
        self.camera1_13.setText('') 
     
        self.camera1_14 = QtWidgets.QPushButton()
        self.camera1_14.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_14.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_14.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_14.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_14.setCheckable(True)
        self.camera1_14.setText('') 
     
        self.camera1_15 = QtWidgets.QPushButton()
        self.camera1_15.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_15.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_15.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_15.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_15.setCheckable(True)
        self.camera1_15.setText('') 
     
        self.camera1_16 = QtWidgets.QPushButton()
        self.camera1_16.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_16.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_16.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_16.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_16.setCheckable(True)
        self.camera1_16.setText('') 
     
        self.camera1_17 = QtWidgets.QPushButton()
        self.camera1_17.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_17.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_17.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_17.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_17.setCheckable(True)
        self.camera1_17.setText('') 
     
        self.camera1_18 = QtWidgets.QPushButton()
        self.camera1_18.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_18.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_18.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_18.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_18.setCheckable(True)
        self.camera1_18.setText('') 
     
        self.camera1_19 = QtWidgets.QPushButton()
        self.camera1_19.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_19.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_19.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_19.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_19.setCheckable(True)
        self.camera1_19.setText('') 
     
        self.camera1_20 = QtWidgets.QPushButton()
        self.camera1_20.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_20.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_20.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_20.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_20.setCheckable(True)
        self.camera1_20.setText('') 
     
        self.camera1_21 = QtWidgets.QPushButton()
        self.camera1_21.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_21.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_21.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_21.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_21.setCheckable(True)
        self.camera1_21.setText('') 
     
        self.camera1_22 = QtWidgets.QPushButton()
        self.camera1_22.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_22.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_22.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_22.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_22.setCheckable(True)
        self.camera1_22.setText('') 
     
        self.camera1_23 = QtWidgets.QPushButton()
        self.camera1_23.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_23.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_23.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_23.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border: none;
                            }
                            """)
        self.camera1_23.setCheckable(True)
        self.camera1_23.setText('') 
        
        self.camera1_24 = QtWidgets.QPushButton()
        self.camera1_24.setMinimumSize(QtCore.QSize(40,20))
        self.camera1_24.setMaximumSize(QtCore.QSize(40,20))
        self.camera1_24.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera1_24.setStyleSheet("""
                            QPushButton{
                                background-color:white;
                            }
                            QPushButton:checked{
                                background-color: #68BB59;
                                border:none;
                            }
                            """)
        self.camera1_24.setCheckable(True)
        self.camera1_24.setText('') 
        
        self.horizontalCamera1.addWidget(self.camera1)
        self.horizontalCamera1.addWidget(self.camera1_all)
        self.horizontalCamera1.addWidget(self.camera1_0)
        self.horizontalCamera1.addWidget(self.camera1_1)
        self.horizontalCamera1.addWidget(self.camera1_2)
        self.horizontalCamera1.addWidget(self.camera1_3)
        self.horizontalCamera1.addWidget(self.camera1_4)
        self.horizontalCamera1.addWidget(self.camera1_5)
        self.horizontalCamera1.addWidget(self.camera1_6)
        self.horizontalCamera1.addWidget(self.camera1_7)
        self.horizontalCamera1.addWidget(self.camera1_8)
        self.horizontalCamera1.addWidget(self.camera1_9)
        self.horizontalCamera1.addWidget(self.camera1_10)
        self.horizontalCamera1.addWidget(self.camera1_11)
        self.horizontalCamera1.addWidget(self.camera1_12)
        self.horizontalCamera1.addWidget(self.camera1_13)
        self.horizontalCamera1.addWidget(self.camera1_14)
        self.horizontalCamera1.addWidget(self.camera1_15)
        self.horizontalCamera1.addWidget(self.camera1_16)
        self.horizontalCamera1.addWidget(self.camera1_17)
        self.horizontalCamera1.addWidget(self.camera1_18)
        self.horizontalCamera1.addWidget(self.camera1_19)
        self.horizontalCamera1.addWidget(self.camera1_20)
        self.horizontalCamera1.addWidget(self.camera1_21)
        self.horizontalCamera1.addWidget(self.camera1_22)
        self.horizontalCamera1.addWidget(self.camera1_23)
        self.horizontalCamera1.addWidget(self.camera1_24)
    
        self.verticalLayoutFrame.addLayout(self.horizontalCamera1)
        
        self.horizontalCamera2 = QtWidgets.QHBoxLayout()
        self.horizontalCamera2.setSpacing(0)       
        self.horizontalCamera2.setObjectName('HorizontalCamera1')
        
        self.camera2 = QtWidgets.QLabel()
        self.camera2.setMinimumSize(QtCore.QSize(60,20))
        self.camera2.setMaximumSize(QtCore.QSize(60,20))
        self.camera2.setStyleSheet('color:white')
        self.camera2.setAlignment(QtCore.Qt.AlignLeft)
        self.camera2.setText('Camera 2')
        
        self.camera2_all = QtWidgets.QPushButton()
        self.camera2_all.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_all.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_all.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_all.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_all.setCheckable(True)
        self.camera2_all.setText('') 
        
        self.camera2_0 = QtWidgets.QPushButton()
        self.camera2_0.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_0.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_0.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_0.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_0.setCheckable(True)
        self.camera2_0.setText('') 
     
        self.camera2_1 = QtWidgets.QPushButton()
        self.camera2_1.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_1.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_1.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_1.setCheckable(True)
        self.camera2_1.setText('') 
     
        self.camera2_2 = QtWidgets.QPushButton()
        self.camera2_2.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_2.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_2.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_2.setCheckable(True)
        self.camera2_2.setText('') 
     
        self.camera2_3 = QtWidgets.QPushButton()
        self.camera2_3.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_3.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_3.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_3.setCheckable(True)
        self.camera2_3.setText('') 
     
        self.camera2_4 = QtWidgets.QPushButton()
        self.camera2_4.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_4.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_4.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_4.setCheckable(True)
        self.camera2_4.setText('') 
     
        self.camera2_5 = QtWidgets.QPushButton()
        self.camera2_5.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_5.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_5.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_5.setCheckable(True)
        self.camera2_5.setText('') 
     
        self.camera2_6 = QtWidgets.QPushButton()
        self.camera2_6.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_6.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_6.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_6.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_6.setCheckable(True)
        self.camera2_6.setText('') 
     
        self.camera2_7 = QtWidgets.QPushButton()
        self.camera2_7.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_7.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_7.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_7.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_7.setCheckable(True)
        self.camera2_7.setText('') 
     
        self.camera2_8 = QtWidgets.QPushButton()
        self.camera2_8.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_8.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_8.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_8.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_8.setCheckable(True)
        self.camera2_8.setText('') 
     
        self.camera2_9 = QtWidgets.QPushButton()
        self.camera2_9.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_9.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_9.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_9.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_9.setCheckable(True)
        self.camera2_9.setText('') 
     
        self.camera2_10 = QtWidgets.QPushButton()
        self.camera2_10.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_10.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_10.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_10.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_10.setCheckable(True)
        self.camera2_10.setText('') 
     
        self.camera2_11 = QtWidgets.QPushButton()
        self.camera2_11.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_11.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_11.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_11.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_11.setCheckable(True)
        self.camera2_11.setText('') 
     
        self.camera2_12 = QtWidgets.QPushButton()
        self.camera2_12.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_12.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_12.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_12.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_12.setCheckable(True)
        self.camera2_12.setText('') 
     
        self.camera2_13 = QtWidgets.QPushButton()
        self.camera2_13.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_13.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_13.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_13.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_13.setCheckable(True)
        self.camera2_13.setText('') 
     
        self.camera2_14 = QtWidgets.QPushButton()
        self.camera2_14.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_14.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_14.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_14.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_14.setCheckable(True)
        self.camera2_14.setText('') 
     
        self.camera2_15 = QtWidgets.QPushButton()
        self.camera2_15.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_15.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_15.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_15.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_15.setCheckable(True)
        self.camera2_15.setText('') 
     
        self.camera2_16 = QtWidgets.QPushButton()
        self.camera2_16.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_16.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_16.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_16.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_16.setCheckable(True)
        self.camera2_16.setText('') 
     
        self.camera2_17 = QtWidgets.QPushButton()
        self.camera2_17.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_17.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_17.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_17.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_17.setCheckable(True)
        self.camera2_17.setText('') 
     
        self.camera2_18 = QtWidgets.QPushButton()
        self.camera2_18.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_18.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_18.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_18.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_18.setCheckable(True)
        self.camera2_18.setText('') 
     
        self.camera2_19 = QtWidgets.QPushButton()
        self.camera2_19.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_19.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_19.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_19.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_19.setCheckable(True)
        self.camera2_19.setText('') 
     
        self.camera2_20 = QtWidgets.QPushButton()
        self.camera2_20.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_20.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_20.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_20.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_20.setCheckable(True)
        self.camera2_20.setText('') 
     
        self.camera2_21 = QtWidgets.QPushButton()
        self.camera2_21.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_21.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_21.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_21.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_21.setCheckable(True)
        self.camera2_21.setText('') 
     
        self.camera2_22 = QtWidgets.QPushButton()
        self.camera2_22.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_22.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_22.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_22.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_22.setCheckable(True)
        self.camera2_22.setText('') 
     
        self.camera2_23 = QtWidgets.QPushButton()
        self.camera2_23.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_23.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_23.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_23.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_23.setCheckable(True)
        self.camera2_23.setText('') 
        
        self.camera2_24 = QtWidgets.QPushButton()
        self.camera2_24.setMinimumSize(QtCore.QSize(40,20))
        self.camera2_24.setMaximumSize(QtCore.QSize(40,20))
        self.camera2_24.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera2_24.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera2_24.setCheckable(True)
        self.camera2_24.setText('') 
        
        self.horizontalCamera2.addWidget(self.camera2)
        self.horizontalCamera2.addWidget(self.camera2_all)
        self.horizontalCamera2.addWidget(self.camera2_0)
        self.horizontalCamera2.addWidget(self.camera2_1)
        self.horizontalCamera2.addWidget(self.camera2_2)
        self.horizontalCamera2.addWidget(self.camera2_3)
        self.horizontalCamera2.addWidget(self.camera2_4)
        self.horizontalCamera2.addWidget(self.camera2_5)
        self.horizontalCamera2.addWidget(self.camera2_6)
        self.horizontalCamera2.addWidget(self.camera2_7)
        self.horizontalCamera2.addWidget(self.camera2_8)
        self.horizontalCamera2.addWidget(self.camera2_9)
        self.horizontalCamera2.addWidget(self.camera2_10)
        self.horizontalCamera2.addWidget(self.camera2_11)
        self.horizontalCamera2.addWidget(self.camera2_12)
        self.horizontalCamera2.addWidget(self.camera2_13)
        self.horizontalCamera2.addWidget(self.camera2_14)
        self.horizontalCamera2.addWidget(self.camera2_15)
        self.horizontalCamera2.addWidget(self.camera2_16)
        self.horizontalCamera2.addWidget(self.camera2_17)
        self.horizontalCamera2.addWidget(self.camera2_18)
        self.horizontalCamera2.addWidget(self.camera2_19)
        self.horizontalCamera2.addWidget(self.camera2_20)
        self.horizontalCamera2.addWidget(self.camera2_21)
        self.horizontalCamera2.addWidget(self.camera2_22)
        self.horizontalCamera2.addWidget(self.camera2_23)
        self.horizontalCamera2.addWidget(self.camera2_24)
        
        self.verticalLayoutFrame.addLayout(self.horizontalCamera2)
        
        self.horizontalCamera3 = QtWidgets.QHBoxLayout()
        self.horizontalCamera3.setSpacing(0)       
        self.horizontalCamera3.setObjectName('HorizontalCamera1')
        
        self.camera3 = QtWidgets.QLabel()
        self.camera3.setMinimumSize(QtCore.QSize(60,20))
        self.camera3.setMaximumSize(QtCore.QSize(60,20))
        self.camera3.setStyleSheet('color:white')
        self.camera3.setAlignment(QtCore.Qt.AlignLeft)
        self.camera3.setText('Camera 3')
        
        self.camera3_all = QtWidgets.QPushButton()
        self.camera3_all.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_all.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_all.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_all.setCheckable(True)
        self.camera3_all.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera3_all.setText('') 
        
        self.camera3_0 = QtWidgets.QPushButton()
        self.camera3_0.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_0.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_0.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_0.setCheckable(True)
        self.camera3_0.setStyleSheet("""
                    QPushButton{
                        background-color:white;
                    }
                    QPushButton:checked{
                        background-color: #68BB59;
                        border: none;
                    }
                    """)
        self.camera3_0.setText('') 
     
        self.camera3_1 = QtWidgets.QPushButton()
        self.camera3_1.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_1.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_1.setCheckable(True)
        self.camera3_1.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_1.setText('') 
     
        self.camera3_2 = QtWidgets.QPushButton()
        self.camera3_2.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_2.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_2.setCheckable(True)
        self.camera3_2.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_2.setText('') 
     
        self.camera3_3 = QtWidgets.QPushButton()
        self.camera3_3.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_3.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_3.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_3.setCheckable(True)
        self.camera3_3.setText('') 
     
        self.camera3_4 = QtWidgets.QPushButton()
        self.camera3_4.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_4.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_4.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_4.setCheckable(True)
        self.camera3_4.setText('') 
     
        self.camera3_5 = QtWidgets.QPushButton()
        self.camera3_5.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_5.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_5.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_5.setCheckable(True)
        self.camera3_5.setText('') 
     
        self.camera3_6 = QtWidgets.QPushButton()
        self.camera3_6.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_6.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_6.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_6.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_6.setCheckable(True)
        self.camera3_6.setText('') 
     
        self.camera3_7 = QtWidgets.QPushButton()
        self.camera3_7.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_7.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_7.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_7.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_7.setCheckable(True)
        self.camera3_7.setText('') 
     
        self.camera3_8 = QtWidgets.QPushButton()
        self.camera3_8.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_8.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_8.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_8.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_8.setCheckable(True)
        self.camera3_8.setText('') 
     
        self.camera3_9 = QtWidgets.QPushButton()
        self.camera3_9.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_9.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_9.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_9.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_9.setCheckable(True)
        self.camera3_9.setText('') 
     
        self.camera3_10 = QtWidgets.QPushButton()
        self.camera3_10.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_10.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_10.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_10.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_10.setCheckable(True)
        self.camera3_10.setText('') 
     
        self.camera3_11 = QtWidgets.QPushButton()
        self.camera3_11.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_11.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_11.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_11.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_11.setCheckable(True)
        self.camera3_11.setText('') 
     
        self.camera3_12 = QtWidgets.QPushButton()
        self.camera3_12.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_12.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_12.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_12.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_12.setCheckable(True)
        self.camera3_12.setText('') 
     
        self.camera3_13 = QtWidgets.QPushButton()
        self.camera3_13.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_13.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_13.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_13.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_13.setCheckable(True)
        self.camera3_13.setText('') 
     
        self.camera3_14 = QtWidgets.QPushButton()
        self.camera3_14.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_14.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_14.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_14.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_14.setCheckable(True)
        self.camera3_14.setText('') 
     
        self.camera3_15 = QtWidgets.QPushButton()
        self.camera3_15.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_15.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_15.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_15.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_15.setCheckable(True)
        self.camera3_15.setText('') 
     
        self.camera3_16 = QtWidgets.QPushButton()
        self.camera3_16.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_16.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_16.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_16.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_16.setCheckable(True)
        self.camera3_16.setText('') 
     
        self.camera3_17 = QtWidgets.QPushButton()
        self.camera3_17.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_17.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_17.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_17.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_17.setCheckable(True)
        self.camera3_17.setText('') 
     
        self.camera3_18 = QtWidgets.QPushButton()
        self.camera3_18.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_18.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_18.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_18.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_18.setCheckable(True)
        self.camera3_18.setText('') 
     
        self.camera3_19 = QtWidgets.QPushButton()
        self.camera3_19.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_19.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_19.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_19.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_19.setCheckable(True)
        self.camera3_19.setText('') 
     
        self.camera3_20 = QtWidgets.QPushButton()
        self.camera3_20.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_20.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_20.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_20.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_20.setCheckable(True)
        self.camera3_20.setText('') 
     
        self.camera3_21 = QtWidgets.QPushButton()
        self.camera3_21.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_21.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_21.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_21.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_21.setCheckable(True)
        self.camera3_21.setText('') 
     
        self.camera3_22 = QtWidgets.QPushButton()
        self.camera3_22.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_22.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_22.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_22.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_22.setCheckable(True)
        self.camera3_22.setText('') 
     
        self.camera3_23 = QtWidgets.QPushButton()
        self.camera3_23.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_23.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_23.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_23.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_23.setCheckable(True)
        self.camera3_23.setText('') 
        
        self.camera3_24 = QtWidgets.QPushButton()
        self.camera3_24.setMinimumSize(QtCore.QSize(40,20))
        self.camera3_24.setMaximumSize(QtCore.QSize(40,20))
        self.camera3_24.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera3_24.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera3_24.setCheckable(True)
        self.camera3_24.setText('') 
        
        self.horizontalCamera3.addWidget(self.camera3)
        self.horizontalCamera3.addWidget(self.camera3_all)
        self.horizontalCamera3.addWidget(self.camera3_0)
        self.horizontalCamera3.addWidget(self.camera3_1)
        self.horizontalCamera3.addWidget(self.camera3_2)
        self.horizontalCamera3.addWidget(self.camera3_3)
        self.horizontalCamera3.addWidget(self.camera3_4)
        self.horizontalCamera3.addWidget(self.camera3_5)
        self.horizontalCamera3.addWidget(self.camera3_6)
        self.horizontalCamera3.addWidget(self.camera3_7)
        self.horizontalCamera3.addWidget(self.camera3_8)
        self.horizontalCamera3.addWidget(self.camera3_9)
        self.horizontalCamera3.addWidget(self.camera3_10)
        self.horizontalCamera3.addWidget(self.camera3_11)
        self.horizontalCamera3.addWidget(self.camera3_12)
        self.horizontalCamera3.addWidget(self.camera3_13)
        self.horizontalCamera3.addWidget(self.camera3_14)
        self.horizontalCamera3.addWidget(self.camera3_15)
        self.horizontalCamera3.addWidget(self.camera3_16)
        self.horizontalCamera3.addWidget(self.camera3_17)
        self.horizontalCamera3.addWidget(self.camera3_18)
        self.horizontalCamera3.addWidget(self.camera3_19)
        self.horizontalCamera3.addWidget(self.camera3_20)
        self.horizontalCamera3.addWidget(self.camera3_21)
        self.horizontalCamera3.addWidget(self.camera3_22)
        self.horizontalCamera3.addWidget(self.camera3_23)
        self.horizontalCamera3.addWidget(self.camera3_24)
        
        self.verticalLayoutFrame.addLayout(self.horizontalCamera3)
        
        self.horizontalCamera4 = QtWidgets.QHBoxLayout()
        self.horizontalCamera4.setSpacing(0)       
        self.horizontalCamera4.setObjectName('HorizontalCamera1')
        
        self.camera4 = QtWidgets.QLabel()
        self.camera4.setMinimumSize(QtCore.QSize(60,20))
        self.camera4.setMaximumSize(QtCore.QSize(60,20))
        self.camera4.setStyleSheet('color:white')
        self.camera4.setAlignment(QtCore.Qt.AlignLeft)
        self.camera4.setText('Camera 4')
        
        self.camera4_all = QtWidgets.QPushButton()
        self.camera4_all.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_all.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_all.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_all.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_all.setCheckable(True)
        self.camera4_all.setText('') 
        
        self.camera4_0 = QtWidgets.QPushButton()
        self.camera4_0.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_0.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_0.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_0.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_0.setCheckable(True)
        self.camera4_0.setText('') 
     
        self.camera4_1 = QtWidgets.QPushButton()
        self.camera4_1.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_1.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_1.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_1.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_1.setCheckable(True)
        self.camera4_1.setText('') 
     
        self.camera4_2 = QtWidgets.QPushButton()
        self.camera4_2.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_2.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_2.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_2.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_2.setCheckable(True)
        self.camera4_2.setText('') 
     
        self.camera4_3 = QtWidgets.QPushButton()
        self.camera4_3.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_3.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_3.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_3.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_3.setCheckable(True)
        self.camera4_3.setText('') 
     
        self.camera4_4 = QtWidgets.QPushButton()
        self.camera4_4.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_4.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_4.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_4.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_4.setCheckable(True)
        self.camera4_4.setText('') 
     
        self.camera4_5 = QtWidgets.QPushButton()
        self.camera4_5.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_5.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_5.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_5.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_5.setCheckable(True)
        self.camera4_5.setText('') 
     
        self.camera4_6 = QtWidgets.QPushButton()
        self.camera4_6.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_6.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_6.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_6.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_6.setCheckable(True)
        self.camera4_6.setText('') 
     
        self.camera4_7 = QtWidgets.QPushButton()
        self.camera4_7.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_7.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_7.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_7.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_7.setCheckable(True)
        self.camera4_7.setText('') 
     
        self.camera4_8 = QtWidgets.QPushButton()
        self.camera4_8.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_8.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_8.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_8.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_8.setCheckable(True)
        self.camera4_8.setText('') 
     
        self.camera4_9 = QtWidgets.QPushButton()
        self.camera4_9.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_9.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_9.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_9.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_9.setCheckable(True)
        self.camera4_9.setText('') 
     
        self.camera4_10 = QtWidgets.QPushButton()
        self.camera4_10.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_10.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_10.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_10.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_10.setCheckable(True)
        self.camera4_10.setText('') 
     
        self.camera4_11 = QtWidgets.QPushButton()
        self.camera4_11.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_11.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_11.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_11.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_11.setCheckable(True)
        self.camera4_11.setText('') 
     
        self.camera4_12 = QtWidgets.QPushButton()
        self.camera4_12.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_12.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_12.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_12.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_12.setCheckable(True)
        self.camera4_12.setText('') 
     
        self.camera4_13 = QtWidgets.QPushButton()
        self.camera4_13.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_13.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_13.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_13.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_13.setCheckable(True)
        self.camera4_13.setText('') 
     
        self.camera4_14 = QtWidgets.QPushButton()
        self.camera4_14.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_14.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_14.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_14.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_14.setCheckable(True)
        self.camera4_14.setText('') 
     
        self.camera4_15 = QtWidgets.QPushButton()
        self.camera4_15.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_15.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_15.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_15.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_15.setCheckable(True)
        self.camera4_15.setText('') 
     
        self.camera4_16 = QtWidgets.QPushButton()
        self.camera4_16.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_16.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_16.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_16.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_16.setCheckable(True)
        self.camera4_16.setText('') 
     
        self.camera4_17 = QtWidgets.QPushButton()
        self.camera4_17.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_17.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_17.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_17.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_17.setCheckable(True)
        self.camera4_17.setText('') 
     
        self.camera4_18 = QtWidgets.QPushButton()
        self.camera4_18.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_18.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_18.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_18.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_18.setCheckable(True)
        self.camera4_18.setText('') 
     
        self.camera4_19 = QtWidgets.QPushButton()
        self.camera4_19.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_19.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_19.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_19.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_19.setCheckable(True)
        self.camera4_19.setText('') 
     
        self.camera4_20 = QtWidgets.QPushButton()
        self.camera4_20.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_20.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_20.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_20.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_20.setCheckable(True)
        self.camera4_20.setText('') 
     
        self.camera4_21 = QtWidgets.QPushButton()
        self.camera4_21.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_21.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_21.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_21.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_21.setCheckable(True)
        self.camera4_21.setText('') 
     
        self.camera4_22 = QtWidgets.QPushButton()
        self.camera4_22.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_22.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_22.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_22.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_22.setCheckable(True)
        self.camera4_22.setText('') 
     
        self.camera4_23 = QtWidgets.QPushButton()
        self.camera4_23.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_23.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_23.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_23.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_23.setCheckable(True)
        self.camera4_23.setText('') 
        
        self.camera4_24 = QtWidgets.QPushButton()
        self.camera4_24.setMinimumSize(QtCore.QSize(40,20))
        self.camera4_24.setMaximumSize(QtCore.QSize(40,20))
        self.camera4_24.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.camera4_24.setStyleSheet("""
            QPushButton{
                background-color:white;
            }
            QPushButton:checked{
                background-color: #68BB59;
                border: none;
            }
            """)
        self.camera4_24.setCheckable(True)
        self.camera4_24.setText('') 
        
        self.horizontalCamera4.addWidget(self.camera4)
        self.horizontalCamera4.addWidget(self.camera4_all)
        self.horizontalCamera4.addWidget(self.camera4_0)
        self.horizontalCamera4.addWidget(self.camera4_1)
        self.horizontalCamera4.addWidget(self.camera4_2)
        self.horizontalCamera4.addWidget(self.camera4_3)
        self.horizontalCamera4.addWidget(self.camera4_4)
        self.horizontalCamera4.addWidget(self.camera4_5)
        self.horizontalCamera4.addWidget(self.camera4_6)
        self.horizontalCamera4.addWidget(self.camera4_7)
        self.horizontalCamera4.addWidget(self.camera4_8)
        self.horizontalCamera4.addWidget(self.camera4_9)
        self.horizontalCamera4.addWidget(self.camera4_10)
        self.horizontalCamera4.addWidget(self.camera4_11)
        self.horizontalCamera4.addWidget(self.camera4_12)
        self.horizontalCamera4.addWidget(self.camera4_13)
        self.horizontalCamera4.addWidget(self.camera4_14)
        self.horizontalCamera4.addWidget(self.camera4_15)
        self.horizontalCamera4.addWidget(self.camera4_16)
        self.horizontalCamera4.addWidget(self.camera4_17)
        self.horizontalCamera4.addWidget(self.camera4_18)
        self.horizontalCamera4.addWidget(self.camera4_19)
        self.horizontalCamera4.addWidget(self.camera4_20)
        self.horizontalCamera4.addWidget(self.camera4_21)
        self.horizontalCamera4.addWidget(self.camera4_22)
        self.horizontalCamera4.addWidget(self.camera4_23)
        self.horizontalCamera4.addWidget(self.camera4_24)
        
        self.verticalLayoutFrame.addLayout(self.horizontalCamera4)
    
        self.verticalLayoutMain.addWidget(self.frame) #3
        self.verticalLayoutMain.addItem(spacerItem) #4
         
        self.horizontalOK = QtWidgets.QHBoxLayout()
        self.horizontalOK.setSpacing(0)
        self.horizontalOK.setObjectName('horizontalOk')

        self.forALL = QtWidgets.QCheckBox()
        self.forALL.setFont(font)
        self.forALL.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.forALL.setText('Apply for all other days')
        self.forALL.setStyleSheet("""
                    QCheckBox::indicator{
                        background-color:white;
                        
                    }
                    QCheckBox::indicator:checked{
                        background-color:green;
                    }
                    QCheckBox{
                        color:white
                    }
        """)
        self.forALL.setObjectName('forALL')
        # self.forALL.setChecked(False)
        self.horizontalOK.addItem(spacerItem)
        self.horizontalOK.addWidget(self.forALL)
        
        self.cancelButton = QtWidgets.QPushButton()
        self.cancelButton.setText('Cancel')
        self.cancelButton.setObjectName('CancelButton')
        self.cancelButton.setFont(fontButton)
        self.cancelButton.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.cancelButton.setMaximumSize(QtCore.QSize(75,30))
        self.cancelButton.setMinimumSize(QtCore.QSize(75,30))
        self.cancelButton.setStyleSheet("""
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
        
        self.horizontalOK.addItem(spacerItem)
        self.horizontalOK.addWidget(self.cancelButton)
        self.horizontalOK.addItem(spacerItem)
        
        self.buttonOK = QtWidgets.QPushButton()
        self.buttonOK.setText('OK')
        self.buttonOK.setFont(fontButton)
        self.buttonOK.setObjectName('ButtonOK')
        self.buttonOK.setMaximumSize(QtCore.QSize(75,30))
        self.buttonOK.setMinimumSize(QtCore.QSize(75,30))
        self.buttonOK.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.buttonOK.setStyleSheet("""
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
        
        self.horizontalOK.addWidget(self.buttonOK)
        self.horizontalOK.addItem(spacerItem)
        
        self.horizontalOK.setStretch(0,2)
        self.horizontalOK.setStretch(1,4) 
        self.horizontalOK.setStretch(2,24)       
        self.horizontalOK.setStretch(3,2)        
        self.horizontalOK.setStretch(4,1)        
        self.horizontalOK.setStretch(5,2)        
        self.horizontalOK.setStretch(6,3)        
        
        self.verticalLayoutMain.addLayout(self.horizontalOK) #5
        self.verticalLayoutMain.addItem(spacerItem) #6
        
        self.verticalLayoutMain.setStretch(0,1)
        self.verticalLayoutMain.setStretch(1,2)
        self.verticalLayoutMain.setStretch(2,1)
        self.verticalLayoutMain.setStretch(3,10)
        self.verticalLayoutMain.setStretch(4,1)
        self.verticalLayoutMain.setStretch(5,2)
        self.verticalLayoutMain.setStretch(6,1)
        
        self.setLayout(self.verticalLayoutMain)
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = TimeTable()
    ui.setupUi()
    ui.show()
    sys.exit(app.exec_())        
        
        