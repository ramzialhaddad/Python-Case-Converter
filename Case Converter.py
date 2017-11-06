# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Studly_Case_Converter.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4.QtGui import *
from PyQt4 import QtCore, QtGui
import os
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
        MainWindow.resize(936, 704)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(270, 460, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton.clicked.connect(self.Convert)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 10, 921, 261))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plainTextEdit.sizePolicy().hasHeightForWidth())
        self.plainTextEdit.setSizePolicy(sizePolicy)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 310, 581, 131))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAutoFillBackground(False)
        self.label.setTextFormat(QtCore.Qt.LogText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName(_fromUtf8("label"))
        self.progressBar = QtGui.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(60, 540, 781, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(30, 280, 221, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(20)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_3 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_3.setGeometry(QtCore.QRect(30, 360, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(20)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_4.setGeometry(QtCore.QRect(30, 400, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(20)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(30, 320, 221, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(20)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.pushButton_2 = QtGui.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 590, 371, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.radioButton_5 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_5.setGeometry(QtCore.QRect(30, 440, 211, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Comic Sans MS"))
        font.setPointSize(20)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 936, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Case Converter", None))
        self.pushButton.setText(_translate("MainWindow", "Convert", None))
        self.label.setText(_translate("MainWindow", "INSTRUCTIONS:\n"
"1. Paste or Type the text in the Box above\n"
" (make sure that there are not any \"Enters\" or line breaks)\n"
"2.Choose one of the Case Types\n"
"3. Press Convert\n"
"4. Check the Converted.txt file in the directory of this program", None))
        self.radioButton.setText(_translate("MainWindow", "lower case", None))
        self.radioButton_3.setText(_translate("MainWindow", "sTuDlY cAsE", None))
        self.radioButton_4.setText(_translate("MainWindow", "snake_case", None))
        self.radioButton_2.setText(_translate("MainWindow", "HIGHER CASE", None))
        self.pushButton_2.setText(_translate("MainWindow", "View File", None))
        self.radioButton_5.setText(_translate("MainWindow", "Camel Case", None))


    def Convert(self, MainWindow):
        def sTuDlYcOnVeRt(self, MainWindow):
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


        def snek_convert(self, MainWindow):
            original = self.plainTextEdit.toPlainText()
            numberOfLetters = len(original)
            counter = 0

            appendConverted = []

            while counter != numberOfLetters:
                self.number = int((counter/numberOfLetters)*100)
                self.progressBar.setValue(self.number)

                tempLetter = original[counter]
                if tempLetter == " ":
                    tempLetter = "_"
                    appendConverted.append(tempLetter)

                else:
                    appendConverted.append(tempLetter)

                counter += 1


            self.progressBar.setValue(100)
            converted = ''.join(appendConverted)

            result = QtGui.QMessageBox.information(QWidget(), 'Yay', "Conversion Complete!", QMessageBox.Ok)

            f = open('Converted.txt','w')
            f.write(converted)
            f.close()

            result = QtGui.QMessageBox.information(QWidget(), 'Yay', "Text File Generated!", QMessageBox.Ok)


        def HIGHERCASE(self, MainWindow):
            original = self.plainTextEdit.toPlainText()
            numberOfLetters = len(original)
            counter = 0
            appendConverted = []

            while counter != numberOfLetters:
                self.number = int((counter/numberOfLetters)*100)
                self.progressBar.setValue(self.number)

                tempLetter = original[counter]
                tempLetter = tempLetter.upper()
                appendConverted.append(tempLetter)

                counter += 1


            self.progressBar.setValue(100)
            converted = ''.join(appendConverted)

            result = QtGui.QMessageBox.information(QWidget(), 'Yay', "Conversion Complete!", QMessageBox.Ok)

            f = open('Converted.txt','w')
            f.write(converted)
            f.close()

            result = QtGui.QMessageBox.information(QWidget(), 'Yay', "Text File Generated!", QMessageBox.Ok)




        def lowercase (self, MainWindow):
            original = self.plainTextEdit.toPlainText()
            numberOfLetters = len(original)
            counter = 0
            appendConverted = []

            while counter != numberOfLetters:
                self.number = int((counter/numberOfLetters)*100)
                self.progressBar.setValue(self.number)

                tempLetter = original[counter]
                tempLetter = tempLetter.lower()
                appendConverted.append(tempLetter)

                counter += 1


            self.progressBar.setValue(100)
            converted = ''.join(appendConverted)

            result = QtGui.QMessageBox.information(QWidget(), 'Yay', "Conversion Complete!", QMessageBox.Ok)

            f = open('Converted.txt','w')
            f.write(converted)
            f.close()

            result = QtGui.QMessageBox.information(QWidget(), 'Yay', "Text File Generated!", QMessageBox.Ok)

        def CamelCase(self, MainWindow):
            original = self.plainTextEdit.toPlainText()
            numberOfLetters = len(original)
            counter = 0

            appendConverted = []

            tempLetter = original[counter]
            tempLetter = tempLetter.upper()
            appendConverted.append(tempLetter)
            counter += 1

            while counter != numberOfLetters:
                self.number = int((counter/numberOfLetters)*100)
                self.progressBar.setValue(self.number)

                tempLetter = original[counter]
                if tempLetter == " ":
                    appendConverted.append(tempLetter)
                    counter += 1
                    tempLetter = original[counter]
                    tempLetter = tempLetter.upper()
                    appendConverted.append(tempLetter)

                else:
                    appendConverted.append(tempLetter)

                counter += 1


            self.progressBar.setValue(100)
            converted = ''.join(appendConverted)

            result = QtGui.QMessageBox.information(QWidget(), 'Yay', "Conversion Complete!", QMessageBox.Ok)

            f = open('Converted.txt','w')
            f.write(converted)
            f.close()

            result = QtGui.QMessageBox.information(QWidget(), 'Yay', "Text File Generated!", QMessageBox.Ok)


        #---------------------------------------------------------------------------------------------------------#
        # We finished writing all the definitions so we dont get errors
        # Lets check whether any of the radio boxes are checked

        # checking if the lower case button is checked
        if self.radioButton.isChecked():
            lowercase(self, MainWindow)

        # HIGHER CASE radio button
        elif self.radioButton_2.isChecked():
            HIGHERCASE(self, MainWindow)

        # sTuDlYcAsE radio button
        elif self.radioButton_3.isChecked():
            sTuDlYcOnVeRt(self, MainWindow)

        #Snek_Case radio button
        elif self.radioButton_4.isChecked():
            snek_convert(self, MainWindow)

        elif self.radioButton_5.isChecked():
            CamelCase(self, MainWindow)

        # well the user is dumb and didn't read the instructions, better send him a message box!
        else:
            result = QtGui.QMessageBox.information(QWidget(), 'Are you Ok?', "Hey, you messed up pick an option to convert and read the instructions while you're at it!", QMessageBox.Ok)



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
