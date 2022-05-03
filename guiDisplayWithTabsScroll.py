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
        MainWindow.resize(1851, 1000)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(240, 20, 1811, 1121))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.DeleteIface_2 = QtWidgets.QCommandLinkButton(self.tab)
        self.DeleteIface_2.setGeometry(QtCore.QRect(1020, 850, 331, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.DeleteIface_2.setFont(font)
        self.DeleteIface_2.setObjectName("DeleteIface_2")
        self.Show_TwinResources = QtWidgets.QCommandLinkButton(self.tab)
        self.Show_TwinResources.setGeometry(QtCore.QRect(1030, 260, 301, 41))
        self.Show_TwinResources.setObjectName("Show_TwinResources")
        self.idLabel_delete = QtWidgets.QLabel(self.tab)
        self.idLabel_delete.setGeometry(QtCore.QRect(800, 780, 141, 41))
        self.idLabel_delete.setObjectName("idLabel_delete")
        self.idInput_delete = QtWidgets.QLineEdit(self.tab)
        self.idInput_delete.setGeometry(QtCore.QRect(960, 780, 400, 50))
        self.idInput_delete.setMinimumSize(QtCore.QSize(400, 50))
        self.idInput_delete.setText("")
        self.idInput_delete.setObjectName("idInput_delete")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 640, 631, 251))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.endpointInput_connect = QtWidgets.QLineEdit(self.layoutWidget)
        self.endpointInput_connect.setMinimumSize(QtCore.QSize(400, 50))
        self.endpointInput_connect.setMaximumSize(QtCore.QSize(400, 16777215))
        self.endpointInput_connect.setText("")
        self.endpointInput_connect.setObjectName("endpointInput_connect")
        self.gridLayout.addWidget(self.endpointInput_connect, 0, 1, 1, 1)
        self.pskIdLabel_connect = QtWidgets.QLabel(self.layoutWidget)
        self.pskIdLabel_connect.setObjectName("pskIdLabel_connect")
        self.gridLayout.addWidget(self.pskIdLabel_connect, 1, 0, 1, 1)
        self.pskLabel_connect = QtWidgets.QLabel(self.layoutWidget)
        self.pskLabel_connect.setObjectName("pskLabel_connect")
        self.gridLayout.addWidget(self.pskLabel_connect, 2, 0, 1, 1)
        self.endpointLavel_connect = QtWidgets.QLabel(self.layoutWidget)
        self.endpointLavel_connect.setObjectName("endpointLavel_connect")
        self.gridLayout.addWidget(self.endpointLavel_connect, 0, 0, 1, 1)
        self.pskIdInput_connect = QtWidgets.QLineEdit(self.layoutWidget)
        self.pskIdInput_connect.setMinimumSize(QtCore.QSize(400, 50))
        self.pskIdInput_connect.setMaximumSize(QtCore.QSize(400, 16777215))
        self.pskIdInput_connect.setText("")
        self.pskIdInput_connect.setObjectName("pskIdInput_connect")
        self.gridLayout.addWidget(self.pskIdInput_connect, 1, 1, 1, 1)
        self.pskInput_connect = QtWidgets.QLineEdit(self.layoutWidget)
        self.pskInput_connect.setMinimumSize(QtCore.QSize(400, 50))
        self.pskInput_connect.setMaximumSize(QtCore.QSize(400, 16777215))
        self.pskInput_connect.setText("")
        self.pskInput_connect.setObjectName("pskInput_connect")
        self.gridLayout.addWidget(self.pskInput_connect, 2, 1, 1, 1)
        self.CreateIface = QtWidgets.QCommandLinkButton(self.tab)
        self.CreateIface.setGeometry(QtCore.QRect(200, 430, 271, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.CreateIface.setFont(font)
        self.CreateIface.setObjectName("CreateIface")
        self.ConnectIface = QtWidgets.QCommandLinkButton(self.tab)
        self.ConnectIface.setGeometry(QtCore.QRect(120, 910, 391, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ConnectIface.setFont(font)
        self.ConnectIface.setObjectName("ConnectIface")
        self.idInput_TwinResouces = QtWidgets.QLineEdit(self.tab)
        self.idInput_TwinResouces.setGeometry(QtCore.QRect(960, 180, 400, 50))
        self.idInput_TwinResouces.setMinimumSize(QtCore.QSize(400, 50))
        self.idInput_TwinResouces.setText("")
        self.idInput_TwinResouces.setObjectName("idInput_TwinResouces")
        self.dataIdLabelInput = QtWidgets.QLabel(self.tab)
        self.dataIdLabelInput.setGeometry(QtCore.QRect(60, 350, 221, 68))
        self.dataIdLabelInput.setObjectName("dataIdLabelInput")
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setGeometry(QtCore.QRect(1050, 120, 321, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.deletTitle = QtWidgets.QLabel(self.tab)
        self.deletTitle.setGeometry(QtCore.QRect(1120, 700, 101, 51))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.deletTitle.setFont(font)
        self.deletTitle.setObjectName("deletTitle")
        self.Display_TwinResouces = QtWidgets.QTextBrowser(self.tab)
        self.Display_TwinResouces.setGeometry(QtCore.QRect(1000, 310, 256, 192))
        self.Display_TwinResouces.setObjectName("Display_TwinResouces")
        self.dataInput = QtWidgets.QLineEdit(self.tab)
        self.dataInput.setGeometry(QtCore.QRect(300, 350, 400, 68))
        self.dataInput.setMaximumSize(QtCore.QSize(400, 16777215))
        self.dataInput.setAlignment(QtCore.Qt.AlignCenter)
        self.dataInput.setPlaceholderText("")
        self.dataInput.setObjectName("dataInput")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(60, 50, 641, 291))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.splitter = QtWidgets.QSplitter(self.layoutWidget_2)
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
        self.splitter_6 = QtWidgets.QSplitter(self.layoutWidget_2)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.descriptionLabel_create = QtWidgets.QLabel(self.splitter_6)
        self.descriptionLabel_create.setObjectName("descriptionLabel_create")
        self.descriptionInput_create = QtWidgets.QLineEdit(self.splitter_6)
        self.descriptionInput_create.setMaximumSize(QtCore.QSize(400, 16777215))
        self.descriptionInput_create.setAlignment(QtCore.Qt.AlignCenter)
        self.descriptionInput_create.setObjectName("descriptionInput_create")
        self.verticalLayout.addWidget(self.splitter_6)
        self.splitter_3 = QtWidgets.QSplitter(self.layoutWidget_2)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.pskIdLabel_create = QtWidgets.QLabel(self.splitter_3)
        self.pskIdLabel_create.setObjectName("pskIdLabel_create")
        self.pskIdInput_create = QtWidgets.QLineEdit(self.splitter_3)
        self.pskIdInput_create.setMaximumSize(QtCore.QSize(400, 16777215))
        self.pskIdInput_create.setAlignment(QtCore.Qt.AlignCenter)
        self.pskIdInput_create.setObjectName("pskIdInput_create")
        self.verticalLayout.addWidget(self.splitter_3)
        self.splitter_5 = QtWidgets.QSplitter(self.layoutWidget_2)
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
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(120, 530, 341, 91))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.idLabel_TwinResouces = QtWidgets.QLabel(self.tab)
        self.idLabel_TwinResouces.setGeometry(QtCore.QRect(810, 180, 141, 41))
        self.idLabel_TwinResouces.setObjectName("idLabel_TwinResouces")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #connect CreateIface button To text Input
        self.CreateIface.clicked.connect(self.CreateLwm2mIfaceF)

        #connect ConnectIface button to text Input
        self.DeleteIface_2.clicked.connect(self.DeleteIfaceF)

        #connect Connect button to text Input
        self.ConnectIface.clicked.connect(self.ConncetToIfaceF)

        #connect ShowTwinResources button to text display
        self.Show_TwinResources.clicked.connect(self.ShowTwinResourcesF) 
        
        
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.DeleteIface_2.setText(_translate("MainWindow", "Delete an Interface"))
        self.Show_TwinResources.setText(_translate("MainWindow", "Show Twin Resouces"))
        self.idLabel_delete.setText(_translate("MainWindow", "Interface Id"))
        self.pskIdLabel_connect.setText(_translate("MainWindow", "PSK id"))
        self.pskLabel_connect.setText(_translate("MainWindow", "PSK"))
        self.endpointLavel_connect.setText(_translate("MainWindow", "Endpoint Name"))
        self.CreateIface.setText(_translate("MainWindow", "Create a lwm2m interface in LO"))
        self.ConnectIface.setText(_translate("MainWindow", "Connect a client to an interface"))
        self.dataIdLabelInput.setText(_translate("MainWindow", "Data Stream Id"))
        self.label_3.setText(_translate("MainWindow", "Get Twin resources "))
        self.deletTitle.setText(_translate("MainWindow", "Delete "))
        self.dataInput.setText(_translate("MainWindow", "Default is set to \"Interface Id\""))
        self.idLabel_create.setText(_translate("MainWindow", "Interface Id"))
        self.descriptionLabel_create.setText(_translate("MainWindow", "Description"))
        self.descriptionInput_create.setText(_translate("MainWindow", "Default is set to \"device for test\""))
        self.pskIdLabel_create.setText(_translate("MainWindow", "PSK Id"))
        self.pskIdInput_create.setText(_translate("MainWindow", "Default is set to Interface Id"))
        self.pskLabel_create.setText(_translate("MainWindow", "PSK"))
        self.pskInput_create.setText(_translate("MainWindow", "Default is already set"))
        self.label_2.setText(_translate("MainWindow", "Connect to an interface"))
        self.idLabel_TwinResouces.setText(_translate("MainWindow", "Interface Id"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))

    def CreateLwm2mIfaceF(self):
            
                global ifaceNumber
                url = "https://integ.m2m.orange.com/api/v1/deviceMgt/devices"

                payload = {
                        "id": "urn:lo:nsid:lwm2m:"+ self.idInpu_create.text(),
                        "name": "Lwm2m device",
                        "description": "device for test",
                        "defaultDataStreamId": "urn:lo:nsid:lwm2m:ifacelwm2m",
                        "interfaces": [
                            {
                                "connector": "lwm2m",
                                "enabled": "true",
                                "definition": {
                                    "endpointName": "balbla",
                                    "security": {
                                        "pskInfo": {
                                            "identity": "pskId",
                                            "secret" : "6d7973656372657470736b617a657274"
                                        }
                                    }
                                }
                            }
                        ]
                    }
                

                #print(type(payload['interfaces'][0]['definition']['endpointName']))
                payload['name'] = self.idInpu_create.text()
                payload['description'] = self.descriptionInput_create.text()
                
                payload['interfaces'][0]['definition']['endpointName'] = "urn:lo:lwm2m:"+ self.idInpu_create.text()
                payload['interfaces'][0]['definition']['security']['pskInfo']['identity'] = self.idInpu_create.text()
                #payload['interfaces'][0]['definition']['security']['pskInfo']['secret'] = self.pskInput_create.text()

                payload = json.dumps(payload)
                
                #To avoid naming conflicts
                

                headers = {
                    'Content-Type': 'application/json',
                    'Accept': 'application/json',
                    'X-API-Key': '1d576207727841a7b9aa2a1f24448f86',
                    'Cookie': 'XSRF-TOKEN=d4af0d8c-5e37-415f-8c72-3da0a7f68c5c'
                }
                response = requests.request("POST", url, headers=headers, data=payload,verify =False)
                print(response.text)
            
    
    def ConncetToIfaceF(self):
        subprocess.Popen(['powershell.exe', "java -jar ./leshan-client-demo.jar "+ "-n "+ "urn:lo:lwm2m:"+ self.endpointInput_connect.text() +" -i "+ self.endpointInput_connect.text()+" -p 6d7973656372657470736b617a657274 -u lwm2m.integ.m2m.orange.com"])

                                                        
    
    def DeleteIfaceF(self):
            url = "https://integ.m2m.orange.com/api/v1/deviceMgt/devices/urn:lo:nsid:lwm2m:"+ self.idInput_delete.text()
            payload={}
            headers = {
            'X-API-Key': '1d576207727841a7b9aa2a1f24448f86'
                    }

            response = requests.request("DELETE", url, headers=headers, data=payload,verify =False)

    def ListTwinResoureces(self):
        url = "https://integ.m2m.orange.com/api/v1/deviceMgt/devices/urn:lo:nsid:lwm2m:"+self.IdInput_TwinRecources.text() +"/twin/supported-objects"
    
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
