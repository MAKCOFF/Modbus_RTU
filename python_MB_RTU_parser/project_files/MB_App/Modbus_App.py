from PyQt5 import QtCore, QtGui, QtWidgets


class UiGETMBRegisters(object):

    def __init__(self):
        self.push_button = QtWidgets.QPushButton(get_mb_registers)
        self.label = QtWidgets.QLabel(get_mb_registers)
        self.label_2 = QtWidgets.QLabel(get_mb_registers)
        self.lineEdit_3 = QtWidgets.QLineEdit(get_mb_registers)
        self.label_5 = QtWidgets.QLabel(get_mb_registers)
        self.lineEdit = QtWidgets.QLineEdit(get_mb_registers)
        self.label_4 = QtWidgets.QLabel(get_mb_registers)
        self.lineEdit_2 = QtWidgets.QLineEdit(get_mb_registers)
        self.label_3 = QtWidgets.QLabel(get_mb_registers)
        self.checkBox_2 = QtWidgets.QCheckBox(get_mb_registers)
        self.checkBox_4 = QtWidgets.QCheckBox(get_mb_registers)
        self.checkBox_3 = QtWidgets.QCheckBox(get_mb_registers)
        self.checkBox = QtWidgets.QCheckBox(get_mb_registers)

    def setup_ui(self, get_mb_registers):
        get_mb_registers.setObjectName("GETMBRegisters")
        get_mb_registers.resize(845, 787)
        self.checkBox.setGeometry(QtCore.QRect(30, 220, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.checkBox.setFont(font)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_3.setGeometry(QtCore.QRect(30, 350, 191, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_3.setFont(font)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4.setGeometry(QtCore.QRect(30, 290, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_4.setFont(font)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_2.setGeometry(QtCore.QRect(30, 150, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)
        self.checkBox_2.setObjectName("checkBox_2")
        self.label_3.setGeometry(QtCore.QRect(130, 80, 111, 61))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setAutoFillBackground(False)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 430, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4.setGeometry(QtCore.QRect(130, 440, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setAutoFillBackground(False)
        self.label_4.setTextFormat(QtCore.Qt.AutoText)
        self.label_4.setScaledContents(False)
        self.label_4.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        self.lineEdit.setGeometry(QtCore.QRect(30, 80, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5.setGeometry(QtCore.QRect(130, 530, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setAutoFillBackground(False)
        self.label_5.setTextFormat(QtCore.Qt.AutoText)
        self.label_5.setScaledContents(False)
        self.label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 520, 51, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setInputMethodHints(QtCore.Qt.ImhDigitsOnly)
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_2.setGeometry(QtCore.QRect(30, 720, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label.setGeometry(QtCore.QRect(290, 60, 501, 601))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setAutoFillBackground(True)
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label.setInputMethodHints(QtCore.Qt.ImhNone)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(1)
        self.label.setMidLineWidth(0)
        self.label.setText("")
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.label.setObjectName("label")
        self.push_button.setGeometry(QtCore.QRect(560, 690, 231, 51))
        self.push_button.setObjectName("pushButton")

        self.re_translate_ui(get_mb_registers)
        QtCore.QMetaObject.connectSlotsByName(get_mb_registers)

    def re_translate_ui(self, get_mb_registers):
        _translate = QtCore.QCoreApplication.translate
        get_mb_registers.setWindowTitle(_translate("GETMBRegisters", "MB App"))
        get_mb_registers.setToolTip(_translate("GETMBRegisters", "<html><head/><body><p><br/></p></body></html>"))
        self.checkBox.setText(_translate("GETMBRegisters", "Coils registers "))
        self.checkBox_3.setText(_translate("GETMBRegisters", "Holding registers"))
        self.checkBox_4.setText(_translate("GETMBRegisters", "Input registers"))
        self.checkBox_2.setText(_translate("GETMBRegisters", "Discrete inputs "))
        self.label_3.setText(_translate("GETMBRegisters", "Slave address (1-247)"))
        self.label_4.setText(_translate("GETMBRegisters", "Begin address"))
        self.label_5.setText(_translate("GETMBRegisters", "Length"))
        self.label_2.setText(_translate("GETMBRegisters", "For CP-10-2014"))
        self.push_button.setText(_translate("GETMBRegisters", "GET DATA REGISTERS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    get_mb_registers = QtWidgets.QDialog()
    ui = UiGETMBRegisters()
    ui.setup_ui(get_mb_registers)
    get_mb_registers.show()
    sys.exit(app.exec_())