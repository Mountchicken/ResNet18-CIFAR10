# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\LearningStuff\DLcode\Pytorch\Smile Face Detection\widget.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AreYouSmling(object):
    def setupUi(self, AreYouSmling):
        AreYouSmling.setObjectName("AreYouSmling")
        AreYouSmling.resize(710, 537)
        self.label = QtWidgets.QLabel(AreYouSmling)
        self.label.setGeometry(QtCore.QRect(40, 30, 271, 261))
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(AreYouSmling)
        self.label_2.setGeometry(QtCore.QRect(430, 60, 251, 191))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(72)
        self.label_2.setFont(font)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(AreYouSmling)
        self.label_3.setGeometry(QtCore.QRect(110, 300, 131, 41))
        font = QtGui.QFont()
        font.setFamily("黑体")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(AreYouSmling)
        self.pushButton.setGeometry(QtCore.QRect(70, 360, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(AreYouSmling)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 410, 211, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(14)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(AreYouSmling)
        self.pushButton_3.setGeometry(QtCore.QRect(470, 370, 151, 71))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_4 = QtWidgets.QLabel(AreYouSmling)
        self.label_4.setGeometry(QtCore.QRect(480, 320, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe UI Emoji")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.retranslateUi(AreYouSmling)
        QtCore.QMetaObject.connectSlotsByName(AreYouSmling)

    def retranslateUi(self, AreYouSmling):
        _translate = QtCore.QCoreApplication.translate
        AreYouSmling.setWindowTitle(_translate("AreYouSmling", "Form"))
        self.pushButton.setText(_translate("AreYouSmling", "Load From Testset"))
        self.pushButton_2.setText(_translate("AreYouSmling", "Load From File"))
        self.pushButton_3.setText(_translate("AreYouSmling", "Predict"))

