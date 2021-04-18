# import sys, os
# import zlib
# from Crypto.Cipher import AES

import sys
from os import listdir
from os.path import isfile, join
from os import walk
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6 import uic

Ui_MainWindow, QtBaseClass = uic.loadUiType("ebook-breaker.ui")
#UI_Progress, QtBaseClass = uic.loadUiType("progress.ui")

class MyWindow(QMainWindow, Ui_MainWindow):
    docpath = ""

    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        #UI_Progress.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.convertDrm)
        self.pushButton_2.clicked.connect(self.endApp)
        self.pushButton_3.clicked.connect(self.getPath)
        self.pushButton_4.clicked.connect(self.clearList)

    def clearList(self):
        self.listWidget.clear()
        self.listWidget_2.clear()

    def endApp(self):
        sys.exit()
    def convertDrm(self):
        progress=QProgressDialog(self)
        progress.autoClose()
        progress.open()
        #변환 로직 추가
        #DRM에 따라 변환 변경필요

        progress.close()

    def getPath(self):
        # fname = QFileDialog.getOpenFileName(self)
        # fname = QFileDialog.getOpenFileNames(self)
        mypath = QFileDialog.getExistingDirectory(self)

        f = []
        d1 = []
        d2 = []
        if self.docpath!=mypath:
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
    app.exec()
    #sys.exit(app.exec_())
