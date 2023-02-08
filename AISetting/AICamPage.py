from .AICamSettings import AiCamSettings
from pyqt_main import roiwidge
from PyQt5 import QtWidgets, QtGui

class AiPage(QtWidgets.QWidget):
    def setupUi(self):

        super(QtWidgets.QWidget, self)
        self.superLayout = QtWidgets.QVBoxLayout()
        
        self.tabs = QtWidgets.QTabWidget()
        self.tabs.setDocumentMode(True)
        self.tab1 = QtWidgets.QWidget()
        self.tab2 = QtWidgets.QWidget()

        self.tabs.addTab(self.tab1, "AI")
        self.tabs.addTab(self.tab2, "ROI")

        self.tab1.layout = QtWidgets.QVBoxLayout(self)
        self.AI = AiCamSettings()
        self.AI.setupUi()
        self.tab1.layout.addWidget(self.AI)
        self.tab1.setLayout(self.tab1.layout)

        self.tab2.layout = QtWidgets.QVBoxLayout()
        self.ROI = roiwidge()
        self.tab2.layout.addWidget(self.ROI)
        self.tab2.setLayout(self.tab2.layout)

        self.superLayout.addWidget(self.tabs)

        self.setLayout(self.superLayout)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = AiPage()
    ui.setupUi(MainWindow)
    ui.tab.show()
    sys.exit(app.exec_())


