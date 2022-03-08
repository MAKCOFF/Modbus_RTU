# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1299, 727)
        icon = QtGui.QIcon.fromTheme(":/img/logo.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.cbPort = QtWidgets.QComboBox(self.centralWidget)
        self.cbPort.setGeometry(QtCore.QRect(10, 20, 141, 25))
        self.cbPort.setObjectName("cbPort")
        self.cbBaud = QtWidgets.QComboBox(self.centralWidget)
        self.cbBaud.setGeometry(QtCore.QRect(160, 20, 141, 25))
        self.cbBaud.setObjectName("cbBaud")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbBaud.addItem("")
        self.cbDataBits = QtWidgets.QComboBox(self.centralWidget)
        self.cbDataBits.setGeometry(QtCore.QRect(310, 20, 71, 25))
        self.cbDataBits.setObjectName("cbDataBits")
        self.cbDataBits.addItem("")
        self.cbDataBits.addItem("")
        self.cbDataBits.addItem("")
        self.cbDataBits.addItem("")
        self.cbDataBits.addItem("")
        self.cbStopBits = QtWidgets.QComboBox(self.centralWidget)
        self.cbStopBits.setGeometry(QtCore.QRect(390, 20, 71, 25))
        self.cbStopBits.setObjectName("cbStopBits")
        self.cbStopBits.addItem("")
        self.cbStopBits.addItem("")
        self.cbParity = QtWidgets.QComboBox(self.centralWidget)
        self.cbParity.setGeometry(QtCore.QRect(470, 20, 71, 25))
        self.cbParity.setObjectName("cbParity")
        self.cbParity.addItem("")
        self.cbParity.addItem("")
        self.cbParity.addItem("")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(40, 0, 71, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralWidget)
        self.label_2.setGeometry(QtCore.QRect(200, 0, 71, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralWidget)
        self.label_3.setGeometry(QtCore.QRect(320, 0, 61, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralWidget)
        self.label_4.setGeometry(QtCore.QRect(400, 0, 61, 17))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralWidget)
        self.label_5.setGeometry(QtCore.QRect(490, 0, 41, 17))
        self.label_5.setObjectName("label_5")
        self.sbSlaveID = QtWidgets.QSpinBox(self.centralWidget)
        self.sbSlaveID.setGeometry(QtCore.QRect(10, 170, 51, 26))
        self.sbSlaveID.setMinimum(1)
        self.sbSlaveID.setMaximum(32)
        self.sbSlaveID.setObjectName("sbSlaveID")
        self.lSlaveID = QtWidgets.QLabel(self.centralWidget)
        self.lSlaveID.setGeometry(QtCore.QRect(10, 150, 61, 17))
        self.lSlaveID.setObjectName("lSlaveID")
        self.sbAddress = QtWidgets.QSpinBox(self.centralWidget)
        self.sbAddress.setGeometry(QtCore.QRect(370, 170, 61, 26))
        self.sbAddress.setMinimum(0)
        self.sbAddress.setMaximum(65536)
        self.sbAddress.setProperty("value", 0)
        self.sbAddress.setObjectName("sbAddress")
        self.sbCount = QtWidgets.QSpinBox(self.centralWidget)
        self.sbCount.setGeometry(QtCore.QRect(440, 170, 61, 26))
        self.sbCount.setMinimum(1)
        self.sbCount.setMaximum(65536)
        self.sbCount.setObjectName("sbCount")
        self.slaveID_3 = QtWidgets.QLabel(self.centralWidget)
        self.slaveID_3.setGeometry(QtCore.QRect(370, 150, 61, 17))
        self.slaveID_3.setObjectName("slaveID_3")
        self.slaveID_4 = QtWidgets.QLabel(self.centralWidget)
        self.slaveID_4.setGeometry(QtCore.QRect(440, 150, 41, 17))
        self.slaveID_4.setObjectName("slaveID_4")
        self.tableData = QtWidgets.QTableWidget(self.centralWidget)
        self.tableData.setGeometry(QtCore.QRect(10, 240, 421, 421))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableData.sizePolicy().hasHeightForWidth())
        self.tableData.setSizePolicy(sizePolicy)
        self.tableData.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableData.setRowCount(0)
        self.tableData.setColumnCount(3)
        self.tableData.setObjectName("tableData")
        item = QtWidgets.QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableData.setHorizontalHeaderItem(2, item)
        self.tableData.horizontalHeader().setVisible(False)
        self.tableData.horizontalHeader().setHighlightSections(True)
        self.tableData.horizontalHeader().setStretchLastSection(True)
        self.tableData.verticalHeader().setVisible(False)
        self.tableData.verticalHeader().setDefaultSectionSize(21)
        self.tableData.verticalHeader().setStretchLastSection(False)
        self.ptRawData = QtWidgets.QPlainTextEdit(self.centralWidget)
        self.ptRawData.setGeometry(QtCore.QRect(450, 240, 831, 421))
        self.ptRawData.setObjectName("ptRawData")
        self.label_6 = QtWidgets.QLabel(self.centralWidget)
        self.label_6.setGeometry(QtCore.QRect(460, 210, 131, 17))
        self.label_6.setObjectName("label_6")
        self.bRawDataClean = QtWidgets.QPushButton(self.centralWidget)
        self.bRawDataClean.setGeometry(QtCore.QRect(1170, 200, 91, 25))
        self.bRawDataClean.setObjectName("bRawDataClean")
        self.label_7 = QtWidgets.QLabel(self.centralWidget)
        self.label_7.setGeometry(QtCore.QRect(20, 210, 141, 17))
        self.label_7.setObjectName("label_7")
        self.btn_request = QtWidgets.QPushButton(self.centralWidget)
        self.btn_request.setGeometry(QtCore.QRect(560, 80, 91, 41))
        self.btn_request.setObjectName("btn_request")
        # self.btn_request.setEnabled(False)
        self.btn_stop_req = QtWidgets.QPushButton(self.centralWidget)
        self.btn_stop_req.setGeometry(QtCore.QRect(560, 140, 101, 51))
        self.btn_stop_req.setObjectName("btn_stop_req")
        self.widget = QtWidgets.QWidget(self.centralWidget)
        self.widget.setGeometry(QtCore.QRect(220, 80, 135, 112))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")

        self.radio_single_r = QtWidgets.QRadioButton(self.widget)
        self.radio_single_r.setObjectName("radio_single_r")
        self.verticalLayout.addWidget(self.radio_single_r)
        self.radio_cicle_r = QtWidgets.QRadioButton(self.widget)
        self.radio_cicle_r.setObjectName("radio_cicle_r")
        self.verticalLayout.addWidget(self.radio_cicle_r)
        self.radio_cicle_rw = QtWidgets.QRadioButton(self.widget)
        self.radio_cicle_rw.setObjectName("radio_cicle_rw")
        self.verticalLayout.addWidget(self.radio_cicle_rw)
        self.radio_single_w = QtWidgets.QRadioButton(self.widget)
        self.radio_single_w.setObjectName("radio_single_w")
        self.verticalLayout.addWidget(self.radio_single_w)

        self.widget1 = QtWidgets.QWidget(self.centralWidget)
        self.widget1.setGeometry(QtCore.QRect(100, 80, 101, 112))
        self.widget1.setObjectName("widget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget1)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.checkBox_inp = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_inp.setObjectName("checkBox_inp")
        self.verticalLayout_2.addWidget(self.checkBox_inp)
        self.checkBox_hold = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_hold.setObjectName("checkBox_hold")
        self.verticalLayout_2.addWidget(self.checkBox_hold)
        self.checkBox_dis = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_dis.setObjectName("checkBox_dis")
        self.verticalLayout_2.addWidget(self.checkBox_dis)
        self.checkBox_coil = QtWidgets.QCheckBox(self.widget1)
        self.checkBox_coil.setObjectName("checkBox_coil")
        self.verticalLayout_2.addWidget(self.checkBox_coil)

        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1299, 22))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtWidgets.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.cbDataBits.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QMaster - Modbus RTU PC emulator"))
        self.cbBaud.setItemText(0, _translate("MainWindow", "9600"))
        self.cbBaud.setItemText(1, _translate("MainWindow", "19200"))
        self.cbBaud.setItemText(2, _translate("MainWindow", "38400"))
        self.cbBaud.setItemText(3, _translate("MainWindow", "57600"))
        self.cbBaud.setItemText(4, _translate("MainWindow", "115200"))
        self.cbBaud.setItemText(5, _translate("MainWindow", "125000"))
        self.cbBaud.setItemText(6, _translate("MainWindow", "230400"))
        self.cbBaud.setItemText(7, _translate("MainWindow", "250000"))
        self.cbBaud.setItemText(8, _translate("MainWindow", "460800"))
        self.cbBaud.setItemText(9, _translate("MainWindow", "500000"))
        self.cbBaud.setItemText(10, _translate("MainWindow", "1000000"))
        self.cbBaud.setItemText(11, _translate("MainWindow", "2000000"))
        self.cbDataBits.setItemText(0, _translate("MainWindow", "5"))
        self.cbDataBits.setItemText(1, _translate("MainWindow", "6"))
        self.cbDataBits.setItemText(2, _translate("MainWindow", "7"))
        self.cbDataBits.setItemText(3, _translate("MainWindow", "8"))
        self.cbDataBits.setItemText(4, _translate("MainWindow", "9"))
        self.cbStopBits.setItemText(0, _translate("MainWindow", "1"))
        self.cbStopBits.setItemText(1, _translate("MainWindow", "2"))
        self.cbParity.setItemText(0, _translate("MainWindow", "None"))
        self.cbParity.setItemText(1, _translate("MainWindow", "Odd"))
        self.cbParity.setItemText(2, _translate("MainWindow", "Even"))
        self.label.setText(_translate("MainWindow", "Serial port"))
        self.label_2.setText(_translate("MainWindow", "Baudrate"))
        self.label_3.setText(_translate("MainWindow", "Data bits"))
        self.label_4.setText(_translate("MainWindow", "Stop bits"))
        self.label_5.setText(_translate("MainWindow", "Parity"))
        self.lSlaveID.setText(_translate("MainWindow", "Slave ID"))
        self.slaveID_3.setText(_translate("MainWindow", "Address"))
        self.slaveID_4.setText(_translate("MainWindow", "Count"))
        item = self.tableData.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Data type"))
        item = self.tableData.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Address"))
        item = self.tableData.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Value"))
        self.label_6.setText(_translate("MainWindow", "Processing console"))
        self.bRawDataClean.setText(_translate("MainWindow", "Clean"))
        self.label_7.setText(_translate("MainWindow", "Data for transmit to"))
        self.btn_request.setText(_translate("MainWindow", "Request"))
        self.btn_stop_req.setText(_translate("MainWindow", "Stop request"))
        self.radio_single_r.setText(_translate("MainWindow", "Single read"))
        self.radio_cicle_r.setText(_translate("MainWindow", "Cicle read"))
        self.radio_cicle_rw.setText(_translate("MainWindow", "Cicle read/write"))
        self.radio_single_w.setText(_translate("MainWindow", "Single write"))
        self.checkBox_inp.setText(_translate("MainWindow", "INPUT"))
        self.checkBox_hold.setText(_translate("MainWindow", "HOLDING"))
        self.checkBox_dis.setText(_translate("MainWindow", "DISCRETE"))
        self.checkBox_coil.setText(_translate("MainWindow", "COIL"))

# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())