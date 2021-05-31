# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(611, 418)
        MainWindow.setStyleSheet("background-image: url(:/newPrefix/back1.jpg);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setGeometry(QtCore.QRect(30, 140, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.username_label.setFont(font)
        self.username_label.setObjectName("username_label")
        self.pass_label = QtWidgets.QLabel(self.centralwidget)
        self.pass_label.setGeometry(QtCore.QRect(40, 210, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.pass_label.setFont(font)
        self.pass_label.setObjectName("pass_label")
        self.line_for_username = QtWidgets.QLineEdit(self.centralwidget)
        self.line_for_username.setGeometry(QtCore.QRect(230, 140, 181, 31))
        self.line_for_username.setObjectName("line_for_username")
        self.line_for_pass = QtWidgets.QLineEdit(self.centralwidget)
        self.line_for_pass.setGeometry(QtCore.QRect(230, 210, 181, 31))
        self.line_for_pass.setObjectName("line_for_pass")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 20, 81, 61))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Login_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Login_Button.setGeometry(QtCore.QRect(280, 270, 93, 28))
        self.Login_Button.setObjectName("Login_Button")
        self.Register_Button = QtWidgets.QPushButton(self.centralwidget)
        self.Register_Button.setGeometry(QtCore.QRect(290, 360, 71, 21))
        self.Register_Button.setObjectName("Register_Button")
        self.no_account_label = QtWidgets.QLabel(self.centralwidget)
        self.no_account_label.setGeometry(QtCore.QRect(290, 350, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(5)
        self.no_account_label.setFont(font)
        self.no_account_label.setObjectName("no_account_label")
        self.helpbutton = QtWidgets.QPushButton(self.centralwidget)
        self.helpbutton.setGeometry(QtCore.QRect(530, 30, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.helpbutton.setFont(font)
        self.helpbutton.setObjectName("helpbutton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.username_label.setText(_translate("MainWindow", "Username/Phone number"))
        self.pass_label.setText(_translate("MainWindow", "Password"))
        self.label.setText(_translate("MainWindow", "SPS"))
        self.Login_Button.setText(_translate("MainWindow", "Login"))
        self.Register_Button.setText(_translate("MainWindow", "Register"))
        self.no_account_label.setText(_translate("MainWindow", "Don\'t have an account"))
        self.helpbutton.setText(_translate("MainWindow", "!"))
import test3_rc
