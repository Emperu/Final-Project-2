from PyQt5 import QtWidgets
from gui import Ui_MainWindow
from logic import Logic

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.logic = Logic(self.ui)
        self.ui.setupUi(self, self.logic)


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
