# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'project_client.ui'
#
# Created: Fri Jun 26 09:47:09 2015
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
        Form.resize(648, 423)
        self.listView = QtGui.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(10, 60, 351, 221))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.pushButtonDelete = QtGui.QPushButton(Form)
        self.pushButtonDelete.setGeometry(QtCore.QRect(70, 290, 75, 23))
        self.pushButtonDelete.setObjectName(_fromUtf8("pushButtonDelete"))
        self.pushButtonAdd = QtGui.QPushButton(Form)
        self.pushButtonAdd.setGeometry(QtCore.QRect(490, 330, 75, 23))
        self.pushButtonAdd.setObjectName(_fromUtf8("pushButtonAdd"))
        self.pushButtonStop = QtGui.QPushButton(Form)
        self.pushButtonStop.setGeometry(QtCore.QRect(70, 320, 75, 23))
        self.pushButtonStop.setObjectName(_fromUtf8("pushButtonStop"))
        self.pushButtonStart = QtGui.QPushButton(Form)
        self.pushButtonStart.setGeometry(QtCore.QRect(230, 320, 75, 23))
        self.pushButtonStart.setObjectName(_fromUtf8("pushButtonStart"))
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(60, 360, 51, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 81, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButtonTest = QtGui.QPushButton(Form)
        self.pushButtonTest.setGeometry(QtCore.QRect(230, 290, 75, 23))
        self.pushButtonTest.setObjectName(_fromUtf8("pushButtonTest"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(390, 40, 241, 141))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(20, 110, 54, 12))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 54, 12))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 54, 12))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 20, 54, 12))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEditSeverIP = QtGui.QLineEdit(self.groupBox)
        self.lineEditSeverIP.setGeometry(QtCore.QRect(70, 20, 161, 20))
        self.lineEditSeverIP.setObjectName(_fromUtf8("lineEditSeverIP"))
        self.lineEditSeverPort = QtGui.QLineEdit(self.groupBox)
        self.lineEditSeverPort.setGeometry(QtCore.QRect(70, 50, 161, 20))
        self.lineEditSeverPort.setObjectName(_fromUtf8("lineEditSeverPort"))
        self.lineEditSeverUser = QtGui.QLineEdit(self.groupBox)
        self.lineEditSeverUser.setGeometry(QtCore.QRect(70, 80, 161, 20))
        self.lineEditSeverUser.setObjectName(_fromUtf8("lineEditSeverUser"))
        self.lineEditSeverPassword = QtGui.QLineEdit(self.groupBox)
        self.lineEditSeverPassword.setGeometry(QtCore.QRect(70, 110, 161, 20))
        self.lineEditSeverPassword.setObjectName(_fromUtf8("lineEditSeverPassword"))
        self.groupBox_2 = QtGui.QGroupBox(Form)
        self.groupBox_2.setGeometry(QtCore.QRect(390, 190, 241, 131))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(20, 20, 54, 12))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_11 = QtGui.QLabel(self.groupBox_2)
        self.label_11.setGeometry(QtCore.QRect(20, 100, 54, 12))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_10 = QtGui.QLabel(self.groupBox_2)
        self.label_10.setGeometry(QtCore.QRect(20, 70, 54, 12))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 51, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEditClientrIP = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditClientrIP.setGeometry(QtCore.QRect(70, 10, 161, 20))
        self.lineEditClientrIP.setObjectName(_fromUtf8("lineEditClientrIP"))
        self.lineEditClientPort = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditClientPort.setGeometry(QtCore.QRect(70, 40, 161, 20))
        self.lineEditClientPort.setObjectName(_fromUtf8("lineEditClientPort"))
        self.lineEditClientUser = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditClientUser.setGeometry(QtCore.QRect(70, 70, 161, 20))
        self.lineEditClientUser.setObjectName(_fromUtf8("lineEditClientUser"))
        self.lineEditClientPassword = QtGui.QLineEdit(self.groupBox_2)
        self.lineEditClientPassword.setGeometry(QtCore.QRect(70, 100, 161, 20))
        self.lineEditClientPassword.setObjectName(_fromUtf8("lineEditClientPassword"))
        self.label_12 = QtGui.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(20, 40, 351, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.LinkPassword = QtGui.QLineEdit(Form)
        self.LinkPassword.setGeometry(QtCore.QRect(340, 380, 131, 20))
        self.LinkPassword.setObjectName(_fromUtf8("LinkPassword"))
        self.label_8 = QtGui.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(210, 360, 81, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_13 = QtGui.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(360, 360, 81, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(500, 360, 81, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.radioButtonautomatic = QtGui.QRadioButton(Form)
        self.radioButtonautomatic.setGeometry(QtCore.QRect(430, 330, 41, 17))
        self.radioButtonautomatic.setObjectName(_fromUtf8("radioButtonautomatic"))
        self.radioButtonmanual = QtGui.QRadioButton(Form)
        self.radioButtonmanual.setGeometry(QtCore.QRect(580, 330, 51, 20))
        self.radioButtonmanual.setObjectName(_fromUtf8("radioButtonmanual"))
        self.lineEditSever = QtGui.QLineEdit(Form)
        self.lineEditSever.setGeometry(QtCore.QRect(10, 380, 161, 20))
        self.lineEditSever.setObjectName(_fromUtf8("lineEditSever"))
        self.LinkUser = QtGui.QLineEdit(Form)
        self.LinkUser.setGeometry(QtCore.QRect(190, 380, 141, 20))
        self.LinkUser.setObjectName(_fromUtf8("LinkUser"))
        self.LinkSeverUser = QtGui.QLineEdit(Form)
        self.LinkSeverUser.setGeometry(QtCore.QRect(480, 380, 151, 20))
        self.LinkSeverUser.setObjectName(_fromUtf8("LinkSeverUser"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.lineEditSeverIP, self.lineEditSeverPort)
        Form.setTabOrder(self.lineEditSeverPort, self.lineEditSeverUser)
        Form.setTabOrder(self.lineEditSeverUser, self.lineEditSeverPassword)
        Form.setTabOrder(self.lineEditSeverPassword, self.lineEditClientrIP)
        Form.setTabOrder(self.lineEditClientrIP, self.lineEditClientPort)
        Form.setTabOrder(self.lineEditClientPort, self.lineEditClientUser)
        Form.setTabOrder(self.lineEditClientUser, self.lineEditClientPassword)
        Form.setTabOrder(self.lineEditClientPassword, self.lineEditSever)
        Form.setTabOrder(self.lineEditSever, self.LinkUser)
        Form.setTabOrder(self.LinkUser, self.LinkPassword)
        Form.setTabOrder(self.LinkPassword, self.LinkSeverUser)
        Form.setTabOrder(self.LinkSeverUser, self.radioButtonautomatic)
        Form.setTabOrder(self.radioButtonautomatic, self.radioButtonmanual)
        Form.setTabOrder(self.radioButtonmanual, self.pushButtonAdd)
        Form.setTabOrder(self.pushButtonAdd, self.pushButtonDelete)
        Form.setTabOrder(self.pushButtonDelete, self.pushButtonTest)
        Form.setTabOrder(self.pushButtonTest, self.pushButtonStop)
        Form.setTabOrder(self.pushButtonStop, self.pushButtonStart)
        Form.setTabOrder(self.pushButtonStart, self.listView)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.pushButtonDelete.setText(_translate("Form", "删除", None))
        self.pushButtonAdd.setText(_translate("Form", "增加", None))
        self.pushButtonStop.setText(_translate("Form", "停止", None))
        self.pushButtonStart.setText(_translate("Form", "启动", None))
        self.label_6.setText(_translate("Form", "服务器", None))
        self.label_7.setText(_translate("Form", "链接状态显示", None))
        self.pushButtonTest.setText(_translate("Form", "测试链接", None))
        self.groupBox.setTitle(_translate("Form", "远程链接", None))
        self.label_5.setText(_translate("Form", "密码", None))
        self.label_4.setText(_translate("Form", "用户名", None))
        self.label_2.setText(_translate("Form", "远程端口", None))
        self.label.setText(_translate("Form", "远程IP", None))
        self.groupBox_2.setTitle(_translate("Form", "本地连接", None))
        self.label_9.setText(_translate("Form", "本地IP", None))
        self.label_11.setText(_translate("Form", "密码", None))
        self.label_10.setText(_translate("Form", "用户名", None))
        self.label_3.setText(_translate("Form", "本地端口", None))
        self.label_12.setText(_translate("Form", "远程IP       用户 端口 本地IP   用户 端口 状态", None))
        self.label_8.setText(_translate("Form", "本地用户名", None))
        self.label_13.setText(_translate("Form", "本地用户密码", None))
        self.label_14.setText(_translate("Form", "远程用户名", None))
        self.radioButtonautomatic.setText(_translate("Form", "自动", None))
        self.radioButtonmanual.setText(_translate("Form", "手动", None))

