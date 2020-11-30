import sys

from PyQt5 import QtWidgets

from face import Ui_Dialog


class MyWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    show_out = MyWindow()
    show_out.show()
    app.exec_()
