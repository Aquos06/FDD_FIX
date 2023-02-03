from mainprotol import Protol
import sys
from PyQt5 import QtWidgets

class myHome(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Protol()
        self.ui.setupUi(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myHome()
    window.showFullScreen()
    # window.run()
    sys.exit(app.exec_())