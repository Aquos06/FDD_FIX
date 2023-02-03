from PyQt5 import QtCore, QtGui, QtWidgets

class searchBox(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self,parent=None)

        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(12)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.layout =QtWidgets.QVBoxLayout(self.frame)
        self.layout.setSpacing(0)
        self.layout.setObjectName('Layout')

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)

        self.label = QtWidgets.QPushButton(self)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setMinimumSize(QtCore.QSize(300,150))
        self.label.setMaximumSize(QtCore.QSize(300,150))
        self.label.setText("")
        self.label.setObjectName('Label')

        self.horizontalLayout.addWidget(self.label, alignment = QtCore.Qt.AlignVCenter)
        
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)

        self.labelcut = QtWidgets.QLabel(self)
        self.labelcut.setMinimumSize(QtCore.QSize(75,75))
        self.labelcut.setMaximumSize(QtCore.QSize(75,75))
        self.labelcut.setText("")
        
        self.verticalLayout.addWidget(self.labelcut, alignment= QtCore.Qt.AlignHCenter)

        self.information = QtWidgets.QLabel(self)
        self.information.setMinimumSize(QtCore.QSize(150,75))
        self.information.setMaximumSize(QtCore.QSize(150,75))
        self.information.setStyleSheet("color:white")
        self.information.setFont(font)
        self.information.setText('')
        self.information.setAlignment(QtCore.Qt.AlignLeft)
        self.information.setObjectName('Information')
        self.verticalLayout.addWidget(self.information, alignment= QtCore.Qt.AlignHCenter)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.layout.addLayout(self.horizontalLayout)
        