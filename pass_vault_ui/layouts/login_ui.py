# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'res/design/login.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from pass_vault_ui.layouts import login_rc


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(669, 549)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(False)
        Form.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(
            QtGui.QPixmap("res/design/../logo/Logo.png"),
            QtGui.QIcon.Normal,
            QtGui.QIcon.Off,
        )
        Form.setWindowIcon(icon)
        Form.setAutoFillBackground(False)
        self.username_input = QtWidgets.QLineEdit(Form)
        self.username_input.setGeometry(QtCore.QRect(260, 280, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(11)
        font.setBold(False)
        self.username_input.setFont(font)
        self.username_input.setText("")
        self.username_input.setObjectName("username_input")
        self.password_input = QtWidgets.QLineEdit(Form)
        self.password_input.setEnabled(True)
        self.password_input.setGeometry(QtCore.QRect(260, 340, 180, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(11)
        font.setBold(False)
        self.password_input.setFont(font)
        self.password_input.setText("")
        self.password_input.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password_input.setClearButtonEnabled(False)
        self.password_input.setObjectName("password_input")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 280, 107, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(14)
        font.setBold(False)
        self.label.setFont(font)
        self.label.setScaledContents(False)
        self.label.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(150, 340, 107, 30))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(14)
        font.setBold(False)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(False)
        self.label_2.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter
        )
        self.label_2.setObjectName("label_2")
        self.login_btn = QtWidgets.QPushButton(Form)
        self.login_btn.setGeometry(QtCore.QRect(180, 400, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(11)
        font.setBold(False)
        self.login_btn.setFont(font)
        self.login_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.login_btn.setAutoDefault(False)
        self.login_btn.setDefault(False)
        self.login_btn.setFlat(False)
        self.login_btn.setObjectName("login_btn")
        self.register_btn = QtWidgets.QPushButton(Form)
        self.register_btn.setGeometry(QtCore.QRect(300, 400, 111, 41))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(11)
        font.setBold(False)
        self.register_btn.setFont(font)
        self.register_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.register_btn.setObjectName("register_btn")
        self.reset_btn = QtWidgets.QPushButton(Form)
        self.reset_btn.setGeometry(QtCore.QRect(450, 340, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(11)
        font.setBold(False)
        self.reset_btn.setFont(font)
        self.reset_btn.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.reset_btn.setObjectName("reset_btn")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(80, 60, 501, 191))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(11)
        font.setBold(False)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.debug_lbl = QtWidgets.QLabel(Form)
        self.debug_lbl.setGeometry(QtCore.QRect(100, 460, 421, 51))
        font = QtGui.QFont()
        font.setFamily("Monospace")
        font.setPointSize(11)
        font.setBold(False)
        self.debug_lbl.setFont(font)
        self.debug_lbl.setText("")
        self.debug_lbl.setObjectName("debug_lbl")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Pass Vault Login"))
        self.label.setText(_translate("Form", "Username"))
        self.label_2.setText(_translate("Form", "Password"))
        self.login_btn.setText(_translate("Form", "Login"))
        self.register_btn.setText(_translate("Form", "Register"))
        self.reset_btn.setText(_translate("Form", "Reset"))
        self.label_3.setText(
            _translate(
                "Form",
                '<html><head/><body><p><img src=":/newPrefix/logo/login_screen.png"/></p></body></html>',
            )
        )
