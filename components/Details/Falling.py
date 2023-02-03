from .FallDetail import FallDetail
from PyQt5 import QtWidgets
import sys

class Falling(QtWidgets.QWidget): 
    def __init__(self):
        super().__init__()
        self.ui = FallDetail()
        self.ui.setupUi(self)
        
    def close(self):
        self.ui.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Falling()
    MainWindow.show()
    sys.exit(app.exec())