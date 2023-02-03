from .bigscreen import AnotherWindow
import cv2
from PyQt5 import QtWidgets
import sys

class biggerScreen(QtWidgets.QMainWindow):                                    #open window
    def __init__(self,mainwindow): # mode: [0,all] , [1,mask] , [2,temperature]
        super().__init__()
        self.ui = AnotherWindow()
        self.ui.setupUi(mainwindow)
        self.image = cv2.imread('bg.jpg')
        self.ui.login.setText('back')

        


    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = biggerScreen()
    window.showFullScreen()
    window.run()
    sys.exit(app.exec_())
    
