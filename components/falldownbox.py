from PyQt5 import QtCore, QtGui, QtWidgets

class Box(QtWidgets.QWidget):
    def __init__(self, parent = None):
        QtWidgets.QWidget.__init__(self, parent=None)

        font = QtGui.QFont()       
        font.setFamily("Ubuntu Mono")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(80)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)

        self.layout = QtWidgets.QVBoxLayout(self.frame)
        self.layout.setSpacing(0)
        self.layout.setObjectName("Layout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("HorizontalLayout")

        self.label = QtWidgets.QPushButton(self)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.label.setMinimumSize(QtCore.QSize(150, 150))
        self.label.setMaximumSize(QtCore.QSize(150, 150))
        self.label.setStyleSheet("background:#07111a;")
        self.label.setText("")
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label) #Horizontal 0

        self.information = QtWidgets.QLabel(self)
        self.information.setMinimumSize(QtCore.QSize(400, 15))
        self.information.setMaximumSize(QtCore.QSize(400, 100))
        self.information.setFont(font)
        self.information.setStyleSheet("background:#07111a;\n"
                                  "color:white;")
        self.information.setText("")
        self.information.setObjectName("Information")

        spacerItem = QtWidgets.QSpacerItem(15, 10, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem) #Horizontal 1
        self.horizontalLayout.addWidget(self.information) #Horizontal2

        self.horizontalLayout.setStretch(0,5)
        self.horizontalLayout.setStretch(1,1)
        self.horizontalLayout.setStretch(2,5)

        self.layout.addLayout(self.horizontalLayout)
        
        self.layout.setStretch(0,10)
        
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = Box()
    win.show()
    sys.exit(app.exec_())
