# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'guiTest.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from asyncio import streams
import requests
import subprocess
import json
from subprocess import check_output
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1447, 1025)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.CreateIface = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.CreateIface.setGeometry(QtCore.QRect(160, 480, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CreateIface.setFont(font)
        self.CreateIface.setObjectName("CreateIface")
        self.ConnectIface = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.ConnectIface.setGeometry(QtCore.QRect(210, 950, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ConnectIface.setFont(font)
        self.ConnectIface.setObjectName("ConnectIface")
        self.idInput_delete = QtWidgets.QLineEdit(self.centralwidget)
        self.idInput_delete.setGeometry(QtCore.QRect(950, 850, 400, 50))
        self.idInput_delete.setMinimumSize(QtCore.QSize(400, 50))
        self.idInput_delete.setText("")
        self.idInput_delete.setObjectName("idInput_delete")
        self.idLabel_delete = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_delete.setGeometry(QtCore.QRect(780, 860, 141, 41))
        self.idLabel_delete.setObjectName("idLabel_delete")
        self.dataInput = QtWidgets.QLineEdit(self.centralwidget)
        self.dataInput.setGeometry(QtCore.QRect(260, 400, 400, 68))
        self.dataInput.setMaximumSize(QtCore.QSize(400, 16777215))
        self.dataInput.setAlignment(QtCore.Qt.AlignCenter)
        self.dataInput.setPlaceholderText("")
        self.dataInput.setObjectName("dataInput")
        self.dataIdLabelInput = QtWidgets.QLabel(self.centralwidget)
        self.dataIdLabelInput.setGeometry(QtCore.QRect(20, 400, 221, 68))
        self.dataIdLabelInput.setObjectName("dataIdLabelInput")
        self.deletTitle = QtWidgets.QLabel(self.centralwidget)
        self.deletTitle.setGeometry(QtCore.QRect(1070, 780, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.deletTitle.setFont(font)
        self.deletTitle.setObjectName("deletTitle")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 30, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(90, 560, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1010, 170, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.idInput_TwinResouces = QtWidgets.QLineEdit(self.centralwidget)
        self.idInput_TwinResouces.setGeometry(QtCore.QRect(920, 230, 400, 50))
        self.idInput_TwinResouces.setMinimumSize(QtCore.QSize(400, 50))
        self.idInput_TwinResouces.setText("")
        self.idInput_TwinResouces.setObjectName("idInput_TwinResouces")
        self.idLabel_TwinResouces = QtWidgets.QLabel(self.centralwidget)
        self.idLabel_TwinResouces.setGeometry(QtCore.QRect(770, 230, 141, 41))
        self.idLabel_TwinResouces.setObjectName("idLabel_TwinResouces")
        self.Display_TwinResouces = QtWidgets.QTextBrowser(self.centralwidget)
        self.Display_TwinResouces.setGeometry(QtCore.QRect(995, 360, 400, 192))
        self.Display_TwinResouces.setObjectName("Display_TwinResouces")
        self.Show_TwinResources = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.Show_TwinResources.setGeometry(QtCore.QRect(900, 310, 301, 41))
        self.Show_TwinResources.setObjectName("Show_TwinResources")
        self.DeleteIface_2 = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.DeleteIface_2.setGeometry(QtCore.QRect(1030, 930, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.DeleteIface_2.setFont(font)
        self.DeleteIface_2.setObjectName("DeleteIface_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 100, 641, 291))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.widget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.idLabel_create = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Myanmar Text")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.idLabel_create.setFont(font)
        self.idLabel_create.setObjectName("idLabel_create")
        self.idInpu_create = QtWidgets.QLineEdit(self.splitter)
        self.idInpu_create.setMaximumSize(QtCore.QSize(400, 16777215))
        self.idInpu_create.setText("")
        self.idInpu_create.setObjectName("idInpu_create")
        self.verticalLayout.addWidget(self.splitter)
        self.splitter_6 = QtWidgets.QSplitter(self.widget)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.descriptionLabel_create = QtWidgets.QLabel(self.splitter_6)
        self.descriptionLabel_create.setObjectName("descriptionLabel_create")
        self.descriptionInput_create = QtWidgets.QLineEdit(self.splitter_6)
        self.descriptionInput_create.setMaximumSize(QtCore.QSize(400, 16777215))
        self.descriptionInput_create.setAlignment(QtCore.Qt.AlignCenter)
        self.descriptionInput_create.setObjectName("descriptionInput_create")
        self.verticalLayout.addWidget(self.splitter_6)
        self.splitter_3 = QtWidgets.QSplitter(self.widget)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.pskIdLabel_create = QtWidgets.QLabel(self.splitter_3)
        self.pskIdLabel_create.setObjectName("pskIdLabel_create")
        self.pskIdInput_create = QtWidgets.QLineEdit(self.splitter_3)
        self.pskIdInput_create.setMaximumSize(QtCore.QSize(400, 16777215))
        self.pskIdInput_create.setAlignment(QtCore.Qt.AlignCenter)
        self.pskIdInput_create.setObjectName("pskIdInput_create")
        self.verticalLayout.addWidget(self.splitter_3)
        self.splitter_5 = QtWidgets.QSplitter(self.widget)
        self.splitter_5.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_5.setObjectName("splitter_5")
        self.pskLabel_create = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.pskLabel_create.setFont(font)
        self.pskLabel_create.setObjectName("pskLabel_create")
        self.pskInput_create = QtWidgets.QLineEdit(self.splitter_5)
        self.pskInput_create.setMaximumSize(QtCore.QSize(400, 16777215))
        self.pskInput_create.setAlignment(QtCore.Qt.AlignCenter)
        self.pskInput_create.setObjectName("pskInput_create")
        self.verticalLayout.addWidget(self.splitter_5)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(20, 680, 631, 251))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pskIdLabel_connect = QtWidgets.QLabel(self.widget1)
        self.pskIdLabel_connect.setObjectName("pskIdLabel_connect")
        self.gridLayout.addWidget(self.pskIdLabel_connect, 1, 0, 1, 1)
        self.endpointInput_connect = QtWidgets.QLineEdit(self.widget1)
        self.endpointInput_connect.setMinimumSize(QtCore.QSize(400, 50))
        self.endpointInput_connect.setMaximumSize(QtCore.QSize(400, 16777215))
        self.endpointInput_connect.setText("")
        self.endpointInput_connect.setObjectName("endpointInput_connect")
        self.gridLayout.addWidget(self.endpointInput_connect, 0, 1, 1, 1)
        self.pskInput_connect = QtWidgets.QLineEdit(self.widget1)
        self.pskInput_connect.setMinimumSize(QtCore.QSize(400, 50))
        self.pskInput_connect.setMaximumSize(QtCore.QSize(400, 16777215))
        self.pskInput_connect.setText("")
        self.pskInput_connect.setObjectName("pskInput_connect")
        self.gridLayout.addWidget(self.pskInput_connect, 2, 1, 1, 1)
        self.pskLabel_connect = QtWidgets.QLabel(self.widget1)
        self.pskLabel_connect.setObjectName("pskLabel_connect")
        self.gridLayout.addWidget(self.pskLabel_connect, 2, 0, 1, 1)
        self.endpointLavel_connect = QtWidgets.QLabel(self.widget1)
        self.endpointLavel_connect.setObjectName("endpointLavel_connect")
        self.gridLayout.addWidget(self.endpointLavel_connect, 0, 0, 1, 1)
        self.pskIdInput_connect = QtWidgets.QLineEdit(self.widget1)
        self.pskIdInput_connect.setMinimumSize(QtCore.QSize(400, 50))
        self.pskIdInput_connect.setMaximumSize(QtCore.QSize(400, 16777215))
        self.pskIdInput_connect.setText("")
        self.pskIdInput_connect.setObjectName("pskIdInput_connect")
        self.gridLayout.addWidget(self.pskIdInput_connect, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #connect ShowTwinResources button to text display
        self.Show_TwinResources.clicked.connect(self.ShowTwinResourcesF)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CreateIface.setText(_translate("MainWindow", "Create a lwm2m interface in LO"))
        self.ConnectIface.setText(_translate("MainWindow", "Connect a client to an interface"))
        self.idLabel_delete.setText(_translate("MainWindow", "Interface Id"))
        self.dataInput.setText(_translate("MainWindow", "Default is set to \"Interface Id\""))
        self.dataIdLabelInput.setText(_translate("MainWindow", "Data Stream Id"))
        self.deletTitle.setText(_translate("MainWindow", "Delete "))
        self.label.setText(_translate("MainWindow", "Create an Interface"))
        self.label_2.setText(_translate("MainWindow", "Connect to an interface"))
        self.label_3.setText(_translate("MainWindow", "Get Twin resources "))
        self.idLabel_TwinResouces.setText(_translate("MainWindow", "Interface Id"))
        self.Show_TwinResources.setText(_translate("MainWindow", "Show Twin Resouces"))
        self.DeleteIface_2.setText(_translate("MainWindow", "Delete an Interface"))
        self.idLabel_create.setText(_translate("MainWindow", "Interface Id"))
        self.descriptionLabel_create.setText(_translate("MainWindow", "Description"))
        self.descriptionInput_create.setText(_translate("MainWindow", "Default is set to \"device for test\""))
        self.pskIdLabel_create.setText(_translate("MainWindow", "PSK Id"))
        self.pskIdInput_create.setText(_translate("MainWindow", "Default is set to Interface Id"))
        self.pskLabel_create.setText(_translate("MainWindow", "PSK"))
        self.pskInput_create.setText(_translate("MainWindow", "Default is already set"))
        self.pskIdLabel_connect.setText(_translate("MainWindow", "PSK id"))
        self.pskLabel_connect.setText(_translate("MainWindow", "PSK"))
        self.endpointLavel_connect.setText(_translate("MainWindow", "Endpoint Name"))

    def ShowTwinResourcesF(self):
        url = "https://integ.m2m.orange.com/api/v1/deviceMgt/devices/urn:lo:nsid:lwm2m:ouss/twin/supported-objects"

        payload={}
        headers = {
            'X-API-Key': '1d576207727841a7b9aa2a1f24448f86',
            'Cookie': 'XSRF-TOKEN=6247a9f8-7cab-47b4-9706-1df68f174806'
                }

        response = requests.request("GET", url, headers=headers, data=payload,verify = False)

        print(response.text)
        self.Display_TwinResouces.setText(response.text)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
