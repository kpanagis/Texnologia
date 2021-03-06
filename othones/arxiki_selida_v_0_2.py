# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arxiki_selida.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Main_Page(object):
    def setupUi(self, Main_Page):
        Main_Page.setObjectName("Main_Page")
        Main_Page.resize(610, 616)
        Main_Page.setStyleSheet("background-image: url(:/newPrefix/back1.jpg);")
        self.centralwidget = QtWidgets.QWidget(Main_Page)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(110, 40, 367, 446))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(17, 33, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 2)
        spacerItem1 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.vehicleselect_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.vehicleselect_button.setFont(font)
        self.vehicleselect_button.setObjectName("vehicleselect_button")
        self.gridLayout.addWidget(self.vehicleselect_button, 2, 1, 1, 3)
        spacerItem2 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 2, 4, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(17, 34, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem3, 3, 1, 1, 2)
        spacerItem4 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 4, 0, 1, 1)
        self.manageprofile_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.manageprofile_button.setFont(font)
        self.manageprofile_button.setObjectName("manageprofile_button")
        self.gridLayout.addWidget(self.manageprofile_button, 4, 1, 1, 2)
        spacerItem5 = QtWidgets.QSpacerItem(17, 33, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem5, 5, 1, 1, 2)
        spacerItem6 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 6, 0, 1, 1)
        self.update_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.update_button.setFont(font)
        self.update_button.setObjectName("update_button")
        self.gridLayout.addWidget(self.update_button, 6, 1, 1, 3)
        spacerItem7 = QtWidgets.QSpacerItem(13, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 6, 4, 1, 1)
        spacerItem8 = QtWidgets.QSpacerItem(17, 34, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 7, 1, 1, 2)
        self.offers_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.offers_button.setFont(font)
        self.offers_button.setObjectName("offers_button")
        self.gridLayout.addWidget(self.offers_button, 8, 1, 2, 2)
        spacerItem9 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem9, 9, 0, 1, 1)
        spacerItem10 = QtWidgets.QSpacerItem(17, 33, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 10, 1, 1, 2)
        spacerItem11 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem11, 11, 0, 2, 1)
        self.Review_button = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Review_button.setFont(font)
        self.Review_button.setObjectName("Review_button")
        self.gridLayout.addWidget(self.Review_button, 11, 1, 2, 2)
        spacerItem12 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem12, 4, 4, 1, 1)
        spacerItem13 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem13, 9, 4, 1, 1)
        spacerItem14 = QtWidgets.QSpacerItem(17, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem14, 11, 4, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 1, 1, 3)
        self.helpbutton = QtWidgets.QPushButton(self.centralwidget)
        self.helpbutton.setGeometry(QtCore.QRect(550, 50, 21, 41))
        font = QtGui.QFont()
        font.setPointSize(23)
        self.helpbutton.setFont(font)
        self.helpbutton.setObjectName("helpbutton")
        Main_Page.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Main_Page)
        self.statusbar.setObjectName("statusbar")
        Main_Page.setStatusBar(self.statusbar)

        self.retranslateUi(Main_Page)
        QtCore.QMetaObject.connectSlotsByName(Main_Page)

    def retranslateUi(self, Main_Page):
        _translate = QtCore.QCoreApplication.translate
        Main_Page.setWindowTitle(_translate("Main_Page", "MainWindow"))
        self.vehicleselect_button.setText(_translate("Main_Page", "Vehicle Selection"))
        self.manageprofile_button.setText(_translate("Main_Page", "Manage Profile"))
        self.update_button.setText(_translate("Main_Page", "Update Situation"))
        self.offers_button.setText(_translate("Main_Page", "Offers"))
        self.Review_button.setText(_translate("Main_Page", "Review"))
        self.label.setText(_translate("Main_Page", "Homepage"))
        self.helpbutton.setText(_translate("Main_Page", "!"))
import test3_rc
