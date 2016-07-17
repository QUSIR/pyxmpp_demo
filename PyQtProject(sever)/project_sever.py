# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_sever.ui'
#
# Created: Fri Jun 26 09:50:38 2015
#      by: PyQt4 UI code generator 4.10.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(441, 151)
        self.lineEditPassword = QtGui.QLineEdit(Form)
        self.lineEditPassword.setGeometry(QtCore.QRect(80, 70, 161, 20))
        self.lineEditPassword.setObjectName(_fromUtf8("lineEditPassword"))
        self.pushButtonStart = QtGui.QPushButton(Form)
        self.pushButtonStart.setGeometry(QtCore.QRect(290, 40, 111, 31))
        self.pushButtonStart.setObjectName(_fromUtf8("pushButtonStart"))
        self.pushButtonStop = QtGui.QPushButton(Form)
        self.pushButtonStop.setGeometry(QtCore.QRect(290, 90, 111, 31))
        self.pushButtonStop.setObjectName(_fromUtf8("pushButtonStop"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 40, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(10, 110, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEditUser = QtGui.QLineEdit(Form)
        self.lineEditUser.setGeometry(QtCore.QRect(80, 40, 161, 20))
        self.lineEditUser.setObjectName(_fromUtf8("lineEditUser"))
        self.lineEditSever = QtGui.QLineEdit(Form)
        self.lineEditSever.setGeometry(QtCore.QRect(80, 100, 161, 20))
        self.lineEditSever.setObjectName(_fromUtf8("lineEditSever"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEditUser, self.lineEditPassword)
        Form.setTabOrder(self.lineEditPassword, self.lineEditSever)
        Form.setTabOrder(self.lineEditSever, self.pushButtonStart)
        Form.setTabOrder(self.pushButtonStart, self.pushButtonStop)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButtonStart.setText(_translate("Form", "启动", None))
        self.pushButtonStop.setText(_translate("Form", "停止", None))
        self.label.setText(_translate("Form", "用户名", None))
        self.label_2.setText(_translate("Form", "密码", None))
        self.label_3.setText(_translate("Form", "服务器", None))

