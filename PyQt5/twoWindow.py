# -*- coding: utf-8 -*-

from PyQt4 import QtGui, QtCore
import sys
import design1, design2

class Second(QtGui.QMainWindow, design2.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)
        self.setupUi(self)

class First(QtGui.QMainWindow, design1.Ui_MainWindow):
    def __init__(self, parent=None):
        super(First, self).__init__(parent)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.on_pushButton_clicked)
        self.dialog = Second(self)

    def on_pushButton_clicked(self):
        self.dialog.exec_()

def main():
    app = QtGui.QApplication(sys.argv)
    main = First()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()  
