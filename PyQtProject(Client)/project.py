# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project.ui'
#
# Created: Thu Jun 18 09:40:12 2015
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
        Form.setEnabled(True)
        Form.resize(888, 600)
        Form.setMouseTracking(False)
        self.AddPort = QtGui.QPushButton(Form)
        self.AddPort.setGeometry(QtCore.QRect(20, 430, 82, 23))
        self.AddPort.setObjectName(_fromUtf8("AddPort"))
        self.radioSever = QtGui.QRadioButton(Form)
        self.radioSever.setGeometry(QtCore.QRect(400, 383, 89, 17))
        self.radioSever.setObjectName(_fromUtf8("radioSever"))
        self.radioClient = QtGui.QRadioButton(Form)
        self.radioClient.setGeometry(QtCore.QRect(400, 410, 89, 20))
        self.radioClient.setObjectName(_fromUtf8("radioClient"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 360, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(260, 360, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(340, 40, 54, 12))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(340, 120, 61, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(340, 200, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.OpenLink = QtGui.QPushButton(Form)
        self.OpenLink.setGeometry(QtCore.QRect(220, 470, 81, 21))
        self.OpenLink.setObjectName(_fromUtf8("OpenLink"))
        self.CloseLink = QtGui.QPushButton(Form)
        self.CloseLink.setGeometry(QtCore.QRect(20, 470, 81, 21))
        self.CloseLink.setObjectName(_fromUtf8("CloseLink"))
        self.DeletPort = QtGui.QPushButton(Form)
        self.DeletPort.setGeometry(QtCore.QRect(220, 430, 82, 23))
        self.DeletPort.setObjectName(_fromUtf8("DeletPort"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 101, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.textEditView = QtGui.QTextEdit(Form)
        self.textEditView.setGeometry(QtCore.QRect(10, 40, 301, 291))
        self.textEditView.setObjectName(_fromUtf8("textEditView"))
        self.textEditUser = QtGui.QTextEdit(Form)
        self.textEditUser.setGeometry(QtCore.QRect(340, 70, 181, 31))
        self.textEditUser.setObjectName(_fromUtf8("textEditUser"))
        self.textEditSever = QtGui.QTextEdit(Form)
        self.textEditSever.setGeometry(QtCore.QRect(340, 230, 181, 31))
        self.textEditSever.setObjectName(_fromUtf8("textEditSever"))
        self.textEditIP = QtGui.QTextEdit(Form)
        self.textEditIP.setGeometry(QtCore.QRect(10, 380, 201, 31))
        self.textEditIP.setObjectName(_fromUtf8("textEditIP"))
        self.textEditPort = QtGui.QTextEdit(Form)
        self.textEditPort.setGeometry(QtCore.QRect(260, 380, 81, 31))
        self.textEditPort.setObjectName(_fromUtf8("textEditPort"))
        self.pushButton = QtGui.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(380, 280, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 330, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.lineEditPassword = QtGui.QLineEdit(Form)
        self.lineEditPassword.setGeometry(QtCore.QRect(340, 150, 181, 31))
        self.lineEditPassword.setObjectName(_fromUtf8("lineEditPassword"))
        self.listView = QtGui.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(540, 50, 301, 391))
        self.listView.setObjectName(_fromUtf8("listView"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.AddPort.setText(_translate("Form", "添加监听端口", None))
        self.radioSever.setText(_translate("Form", "服务器端", None))
        self.radioClient.setText(_translate("Form", "客户端", None))
        self.label.setText(_translate("Form", "IP地址", None))
        self.label_2.setText(_translate("Form", "端口", None))
        self.label_3.setText(_translate("Form", "用户名", None))
        self.label_4.setText(_translate("Form", "密码", None))
        self.label_5.setText(_translate("Form", "服务器", None))
        self.OpenLink.setText(_translate("Form", "打开链接", None))
        self.CloseLink.setText(_translate("Form", "关闭链接", None))
        self.DeletPort.setText(_translate("Form", "删除监听端口", None))
        self.label_6.setText(_translate("Form", "链接状态显示", None))
        self.pushButton.setText(_translate("Form", "PushButton", None))
        self.pushButton_2.setText(_translate("Form", "退出", None))

