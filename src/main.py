import sys, os
import zlib
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


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.getPath)

    def getPath(self):
        #fname = QFileDialog.getOpenFileName(self)
        #fname = QFileDialog.getOpenFileNames(self)
        mypath = QFileDialog.getExistingDirectory(self)

        f = []
        for (dirpath, dirnames, filenames) in walk(mypath):
            f.extend(filenames)
 #           self.listView.addItem(filenames)
            break

        print(f)

# self.listView = QtGui.QListView(Dialog)
# self.listView.setObjectName(_fromUtf8("listView"))
# entries = ['one','two', 'three']
# model = QtGui.QStandardItemModel()
# self.listView.setModel(model)
# for i in entries:
#     item = QtGui.QStandardItem(i)
#     model.appendRow(item)
# self.gridLayout.addWidget(self.listView, 1, 0, 1, 2)
#
# QListWidget
#
# self.listwidget = QtGui.QListWidget(Dialog)
#
# entries = ['one','two', 'three']
#
# self.listwidget.addItems(entries)
#
# self.gridLayout.addWidget(self.listwidget, 1, 0, 1, 2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MyWindow()
    myWindow.show()
    app.exec()
    #sys.exit(app.exec_())
