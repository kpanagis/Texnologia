# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Select_Time_Of_Reservation.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Select_Available_Time(object):
    def setupUi(self, Select_Available_Time):
        Select_Available_Time.setObjectName("Select_Available_Time")
        Select_Available_Time.resize(506, 600)
        Select_Available_Time.setStyleSheet("background-image: url(:/newPrefix/back1.jpg);")
        self.centralwidget = QtWidgets.QWidget(Select_Available_Time)
        self.centralwidget.setObjectName("centralwidget")
        self.select_time_of_reservation_label = QtWidgets.QLabel(self.centralwidget)
        self.select_time_of_reservation_label.setGeometry(QtCore.QRect(50, 50, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.select_time_of_reservation_label.setFont(font)
        self.select_time_of_reservation_label.setObjectName("select_time_of_reservation_label")
        self.Time_of_reservation_label = QtWidgets.QLabel(self.centralwidget)
        self.Time_of_reservation_label.setGeometry(QtCore.QRect(160, 230, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Time_of_reservation_label.setFont(font)
        self.Time_of_reservation_label.setObjectName("Time_of_reservation_label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(50, 160, 403, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Select_parking_spot_label = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Select_parking_spot_label.setFont(font)
        self.Select_parking_spot_label.setObjectName("Select_parking_spot_label")
        self.gridLayout.addWidget(self.Select_parking_spot_label, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(18, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.Address_city_zipnumber = QtWidgets.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.Address_city_zipnumber.setFont(font)
        self.Address_city_zipnumber.setObjectName("Address_city_zipnumber")
        self.gridLayout.addWidget(self.Address_city_zipnumber, 0, 2, 1, 1)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(110, 290, 279, 26))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.From = QtWidgets.QLabel(self.layoutWidget1)
        self.From.setObjectName("From")
        self.gridLayout_2.addWidget(self.From, 0, 0, 1, 1)
        self.time_From = QtWidgets.QTimeEdit(self.layoutWidget1)
        self.time_From.setObjectName("time_From")
        self.gridLayout_2.addWidget(self.time_From, 0, 1, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 1, 1, 1)
        self.To = QtWidgets.QLabel(self.layoutWidget1)
        self.To.setObjectName("To")
        self.gridLayout_3.addWidget(self.To, 0, 2, 1, 1)
        self.time_To = QtWidgets.QTimeEdit(self.layoutWidget1)
        self.time_To.setObjectName("time_To")
        self.gridLayout_3.addWidget(self.time_To, 0, 3, 1, 1)
        self.layoutWidget2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget2.setGeometry(QtCore.QRect(90, 480, 310, 32))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.layoutWidget2)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.Back_Button = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Back_Button.setFont(font)
        self.Back_Button.setObjectName("Back_Button")
        self.gridLayout_4.addWidget(self.Back_Button, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(108, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_4.addItem(spacerItem2, 0, 1, 1, 1)
        self.ProceedButton = QtWidgets.QPushButton(self.layoutWidget2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.ProceedButton.setFont(font)
        self.ProceedButton.setObjectName("ProceedButton")
        self.gridLayout_4.addWidget(self.ProceedButton, 0, 2, 1, 1)
        Select_Available_Time.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Select_Available_Time)
        self.statusbar.setObjectName("statusbar")
        Select_Available_Time.setStatusBar(self.statusbar)

        self.retranslateUi(Select_Available_Time)
        QtCore.QMetaObject.connectSlotsByName(Select_Available_Time)

    def retranslateUi(self, Select_Available_Time):
        _translate = QtCore.QCoreApplication.translate
        Select_Available_Time.setWindowTitle(_translate("Select_Available_Time", "MainWindow"))
        self.select_time_of_reservation_label.setText(_translate("Select_Available_Time", "Select  Time Of Reservation"))
        self.Time_of_reservation_label.setText(_translate("Select_Available_Time", "Time Of Reservation"))
        self.Select_parking_spot_label.setText(_translate("Select_Available_Time", "Selected Parking Spot"))
        self.Address_city_zipnumber.setText(_translate("Select_Available_Time", "Address/City/Zip Number"))
        self.From.setText(_translate("Select_Available_Time", "From"))
        self.To.setText(_translate("Select_Available_Time", "To"))
        self.Back_Button.setText(_translate("Select_Available_Time", "Back"))
        self.ProceedButton.setText(_translate("Select_Available_Time", "Proceed"))
import test9_rc
