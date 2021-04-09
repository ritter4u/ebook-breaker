# import sys, os
# import zlib
# from Crypto.Cipher import AES
from os import listdir
from os.path import isfile, join
from os import walk
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6 import uic

Ui_MainWindow, QtBaseClass = uic.loadUiType("ebook-breaker.ui")


class MyWindow(QMainWindow, Ui_MainWindow):
    docpath = ""

    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.getPath)

    def getPath(self):
        # fname = QFileDialog.getOpenFileName(self)
        # fname = QFileDialog.getOpenFileNames(self)
        mypath = QFileDialog.getExistingDirectory(self)

        f = []
        d1 = []
        d2 = []
        self.docpath = mypath
        for (dirpath, dirnames, filenames) in walk(mypath):
            f.extend(filenames)
            # d1.extend(dirpath)
            # d2.extend(dirnames) #하위폴더 탐색 필요
            # self.listWidget.addItem("aaa")

        for (filename) in f:
            self.listWidget.addItem(filename)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    sys.exit(app.exec())
    #sys.exit(app.exec_())
