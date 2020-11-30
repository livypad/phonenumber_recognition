
from PyQt5 import QtWidgets

import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from face import Ui_Dialog
import sys


class MyWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    myshow = MyWindow()
    myshow.show()
    app.exec_()
