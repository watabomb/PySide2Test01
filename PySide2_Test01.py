# -*- coding: utf-8 -*-
import sys
import os

# PySide
from PySide2 import QtCore, QtWidgets
from shiboken2 import wrapInstance
 
from sys import exit, argv
from PySide2.QtWidgets import QApplication, QLabel

class MainWindow(QLabel):
    def __init__(self):
        super().__init__()
        self.setText(u'ファイルをここに置くと、ファイル名をここに表示する')
        self.setAlignment(QtCore.Qt.AlignCenter)
        self.setSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        filename = os.path.abspath(event.mimeData().urls()[0].path())
        self.setText(filename)

if __name__ == '__main__':
    app = QApplication(argv)
    w = MainWindow()
    w.show()
    exit(app.exec_())
