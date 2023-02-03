from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QButtonGroup, QHeaderView


class Ui_Form(QtWidgets.QWidget):
    def __init__(self, parent: None):
        
        super(QtWidgets.QWidget, self).__init__(parent)
        self.gridLayout_2 = QtWidgets.QVBoxLayout(self)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName('horizontalLayout')

        self.verticalLayoutleft = QtWidgets.QVBoxLayout()
        self.verticalLayoutleft.setSpacing(0)
        self.verticalLayoutleft.setObjectName('verticalLayoutLeft')

        self.ROILabel = QtWidgets.QLabel()
        self.ROILabel.setFixedSize(QtCore.QSize(1000,600))
        # self.ROILabel.setMaximumSize(QtCore.QSize(1000,600))
        self.ROILabel.setText('')
        self.verticalLayoutleft.addWidget(self.ROILabel)

        self.graphicsView = QtWidgets.QGraphicsView(self.ROILabel)
        self.graphicsView.setMouseTracking(True)
        self.graphicsView.setTabletTracking(True)
        self.graphicsView.setObjectName("graphicsView")
        #
        self.gridLayout = QtWidgets.QVBoxLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSpacing(0)

        # draw roi :下拉框
        self.comboBox = QtWidgets.QComboBox()
        # self.comboBox.setObjectName("comboBox")
        # 下拉框个数
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox)
        # draw minimum roi :下拉框
        self.detect_size = QtWidgets.QComboBox()
        # self.detect_size.setObjectName("detects size")
        # 下拉框个数
        self.detect_size.addItem("")
        self.detect_size.addItem("")
        self.detect_size.addItem("")
        self.gridLayout.addWidget(self.detect_size)
        # form function button - draw Person roi

        self.horizontalChoose = QtWidgets.QHBoxLayout()
        self.horizontalChoose.setSpacing(0)
        self.horizontalChoose.setObjectName('horizontalChoose')
        
        self.Person_ROI = QtWidgets.QCheckBox()
        self.Person_ROI.setObjectName("Person")
        self.horizontalChoose.addWidget(self.Person_ROI)
        # form function button - draw PPE roi
        self.PPE_ROI = QtWidgets.QCheckBox()
        self.PPE_ROI.setObjectName("PPE")
        self.horizontalChoose.addWidget(self.PPE_ROI)
        # form function button - draw Falldown roi
        self.Falldown_ROI = QtWidgets.QCheckBox()
        self.Falldown_ROI.setObjectName("Falldown")
        self.Falldown_ROI.setChecked(True)
        self.horizontalChoose.addWidget(self.Falldown_ROI)

        self.gridLayout.addLayout(self.horizontalChoose)

        # form
        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)  # 設置tablewidget不可編輯
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.NoSelection)  # 設置tablewidget不可被選取
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)

        self.header = self.tableWidget.horizontalHeader()
        self.header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        self.header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)

        # form title style
        self.tableWidget.verticalHeader().setFixedWidth(50)
        self.tableWidget.verticalHeader().setVisible(False)
        # form content row1
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        # form content row2 - delete specific roi
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)

        self.gridLayout.addWidget(self.tableWidget)
        # form layout
        self.horizontalLayout.addLayout(self.verticalLayoutleft)
        self.horizontalLayout.addLayout(self.gridLayout)
        # function button overview
        self.gridLayout_3 = QtWidgets.QHBoxLayout()
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        # form function button - clear all roi
        self.ClearROIButton = QtWidgets.QPushButton()
        self.ClearROIButton.setObjectName("ClearROIButton")
        # self.ClearROIButton.setText("CLEARs")
        self.gridLayout_3.addWidget(self.ClearROIButton)
        # form function button - confirm roi and save
        self.confirmROIButton = QtWidgets.QPushButton()
        self.confirmROIButton.setObjectName("confirmROIButton")
        self.gridLayout_3.addWidget(self.confirmROIButton)

        self.verticalLayoutleft.addLayout(self.gridLayout_3)
        self.gridLayout_2.addLayout(self.horizontalLayout)
        # function layout
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText("ROI")
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText("delete")
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText("")
        # 下拉式表單選項 : roi 形狀
        self.comboBox.setItemText(0, "draw Rect ROI")
        self.comboBox.setItemText(1, "draw MultiRect ROI")
        # 下拉式表單選項 : 偵測大小限制 roi
        self.detect_size.setItemText(2, "draw minimum")
        self.detect_size.setItemText(1, "draw maximum")
        self.detect_size.setItemText(0, "ROI")
        #
        self.Person_ROI.setText("Person ROI")
        self.PPE_ROI.setText("PPE ROI")
        self.Falldown_ROI.setText("Falldown ROI")

        self.ClearROIButton.setText("ClearROI")
        # draw ROI confirm
        self.confirmROIButton.setText("draw ROI finish")

