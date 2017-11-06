# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Studly_Case_Converter.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import random

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(851, 410)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 230, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.Convert)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 831, 111))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 130, 831, 81))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(10, 320, 781, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 851, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.pushButton.setText(_translate("MainWindow", "Convert", None))
        self.label.setText(_translate("MainWindow", "INSTRUCTIONS:\n"
		"1. Paste or Type the text in the Box above (make sure that there are not any \"Enters\" or line breaks)\n"
		"2. Press Convert\n"
		"3. Check the Converted.txt file in the directory of this program", None))



    def Convert(self, MainWindow):
        #        
        original = self.plainTextEdit.toPlainText()
        numberOfLetters = len(original)
        counter = 0
        appendConverted = []

        randomNum = random.randint(0,1)

        if randomNum == 0:
                        decidingFactor = False 

        else:
                decidingFactor = True


        

        while counter != numberOfLetters:

                self.number = int((counter/numberOfLetters)*100)
                self.progressBar.setValue(self.number)

                if decidingFactor == True:
                        tempLetter = original[counter]
                        tempLetter = tempLetter.upper()
                        appendConverted.append(tempLetter)
                        decidingFactor = False

                else:
                        tempLetter = original[counter]
                        tempLetter = tempLetter.lower()
                        appendConverted.append(tempLetter)
                        decidingFactor = True

                counter += 1


        self.progressBar.setValue(100)
        converted = ''.join(appendConverted)


        
        result = QtGui.QMessageBox.information(QWidget(), 'Yay', "Conversion Complete!", QMessageBox.Ok)



        f = open('Converted.txt','w')
        f.write(converted)
        f.close()


        
        result = QtGui.QMessageBox.information(QWidget(), 'Yay', "Text File Generated!", QMessageBox.Ok)






if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

