# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register_form.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Signup(object):
    def setupUi(self, Signup):
        Signup.setObjectName("Signup")
        Signup.resize(564, 637)
        Signup.setStyleSheet("background-image: url(:/newPrefix/back1.jpg);")
        self.centralwidget = QtWidgets.QWidget(Signup)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 50, 271, 528))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(21)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 2, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem2, 1, 1, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.First_name_label = QtWidgets.QLabel(self.layoutWidget)
        self.First_name_label.setObjectName("First_name_label")
        self.gridLayout.addWidget(self.First_name_label, 0, 0, 1, 1)
        self.firstname_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.firstname_line.setObjectName("firstname_line")
        self.gridLayout.addWidget(self.firstname_line, 0, 2, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem4, 1, 2, 1, 1)
        self.last_name_label = QtWidgets.QLabel(self.layoutWidget)
        self.last_name_label.setObjectName("last_name_label")
        self.gridLayout.addWidget(self.last_name_label, 2, 0, 1, 1)
        self.lastname_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.lastname_line.setObjectName("lastname_line")
        self.gridLayout.addWidget(self.lastname_line, 2, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(18, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 3, 1, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(18, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem6, 3, 2, 1, 1)
        self.username_label = QtWidgets.QLabel(self.layoutWidget)
        self.username_label.setObjectName("username_label")
        self.gridLayout.addWidget(self.username_label, 4, 0, 1, 1)
        self.username_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.username_line.setObjectName("username_line")
        self.gridLayout.addWidget(self.username_line, 4, 2, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(18, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem7, 5, 1, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 5, 2, 1, 1)
        self.phone_number_label = QtWidgets.QLabel(self.layoutWidget)
        self.phone_number_label.setObjectName("phone_number_label")
        self.gridLayout.addWidget(self.phone_number_label, 6, 0, 1, 1)
        self.phone_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.phone_line.setObjectName("phone_line")
        self.gridLayout.addWidget(self.phone_line, 6, 2, 1, 1)
        spacerItem9 = QtWidgets.QSpacerItem(18, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 7, 1, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 7, 2, 1, 1)
        self.email_label = QtWidgets.QLabel(self.layoutWidget)
        self.email_label.setObjectName("email_label")
        self.gridLayout.addWidget(self.email_label, 8, 0, 1, 1)
        self.email_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.email_line.setObjectName("email_line")
        self.gridLayout.addWidget(self.email_line, 8, 2, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(18, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 9, 1, 1, 1)
        spacerItem12 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem12, 9, 2, 1, 1)
        self.pass_label = QtWidgets.QLabel(self.layoutWidget)
        self.pass_label.setObjectName("pass_label")
        self.gridLayout.addWidget(self.pass_label, 10, 0, 1, 1)
        self.pass_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.pass_line.setObjectName("pass_line")
        self.gridLayout.addWidget(self.pass_line, 10, 2, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(18, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem13, 11, 1, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem14, 11, 2, 1, 1)
        self.pass_conf_label = QtWidgets.QLabel(self.layoutWidget)
        self.pass_conf_label.setObjectName("pass_conf_label")
        self.gridLayout.addWidget(self.pass_conf_label, 12, 0, 1, 2)
        self.pass_conf_line = QtWidgets.QLineEdit(self.layoutWidget)
        self.pass_conf_line.setObjectName("pass_conf_line")
        self.gridLayout.addWidget(self.pass_conf_line, 12, 2, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 2, 0, 1, 3)
        spacerItem15 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem15, 3, 1, 1, 1)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem16, 4, 0, 1, 1)
        self.register_button = QtWidgets.QPushButton(self.layoutWidget)
        self.register_button.setObjectName("register_button")
        self.gridLayout_2.addWidget(self.register_button, 4, 1, 1, 1)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem17, 4, 2, 1, 1)
        self.helpbutton = QtWidgets.QPushButton(self.centralwidget)
        self.helpbutton.setGeometry(QtCore.QRect(490, 50, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.helpbutton.setFont(font)
        self.helpbutton.setObjectName("helpbutton")
        Signup.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Signup)
        self.statusbar.setObjectName("statusbar")
        Signup.setStatusBar(self.statusbar)

        self.retranslateUi(Signup)
        QtCore.QMetaObject.connectSlotsByName(Signup)

    def retranslateUi(self, Signup):
        _translate = QtCore.QCoreApplication.translate
        Signup.setWindowTitle(_translate("Signup", "MainWindow"))
        self.label.setText(_translate("Signup", "Register "))
        self.First_name_label.setText(_translate("Signup", "First name "))
        self.last_name_label.setText(_translate("Signup", "Lastname"))
        self.username_label.setText(_translate("Signup", "Username"))
        self.phone_number_label.setText(_translate("Signup", "Phone number"))
        self.email_label.setText(_translate("Signup", "Email "))
        self.pass_label.setText(_translate("Signup", "Password"))
        self.pass_conf_label.setText(_translate("Signup", "Password cofirmation"))
        self.register_button.setText(_translate("Signup", "Register"))
        self.helpbutton.setText(_translate("Signup", "!"))
import register_rc
import test8_rc
