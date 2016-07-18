#!/usr/bin/python -u
# -*- coding:cp936 -*-

import sys
#������־
import logging
#���ػ��ַ�����
import locale
#���봦��
import codecs
import pdb
import threading
import time
#��ȡID��
import uuid
#�쳣��
import traceback
import socket
import struct
import pprint
from pyxmpp.all import JID,Iq,Presence,Message,StreamError
from pyxmpp.jabber.client import JabberClient
from pyxmpp.interface import implements
from pyxmpp.interfaces import *
from pyxmpp.streamtls import TLSSettings
from PyQt4 import QtCore, QtGui
from decimal import *
from PyQt4.QtGui import *
from PyQt4.Qt import *
from PyQt4.QtCore import *

from project_client import Ui_Form
#ȫ�ֱ���
PyFrom = Ui_Form()
import im_tcp_tunneler
from Openfileconfig import Openconfig
#�б���ʾ
listviewdata=[]
#�б�λ��
listnumber=0
#Ĭ������
configurationuser = 'f@localhost'
configurationpassword = '123456'
configurationsever ='localhost'
configurationtosever='e@localhost'
#��ʾ����ʾ
#EdittextView=None
#�����߳�״̬��
state=False
#�����б�
clientdatalist=[]
#����״̬��ʾ
linviewdata=''
#�������ӱ�־
#testlink=False
#�ļ�·��
filepath= None
#�ļ��洢
#configsave=None
#У���ݴ�
userdata=[]
configuser=None
configsever=None
'''
#��������
self.connect(self.ui.OpenLink, QtCore.SIGNAL("clicked()"), startxmpp)
self.connect(self.ui.CloseLink, QtCore.SIGNAL("clicked()"), closexmpp)
#��ѡ��
self.ui.radioSever.setChecked(True)
#�༭��
severaddress=PyFrom.textEditSever.toPlainText()
self.ui.textEditUser.setPlainText('e')
#���������
self.ui.lineEditPassword.setEchoMode(QtGui.QLineEdit.Password)
#�б�ؼ�
data=[1,2,3,4]
lk=MyListMode(data,self)
self.ui.listView.setModel(lk)
self.ui.listView.clicked.connect(self.indexMove)
#�ļ���ȡ
f=open('tunnels.conf','r')
print f.read()
#��ť״̬
PyFrom.OpenLink.setEnabled(False)
#��ʾ��
reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
QtGui.QMessageBox.question( self, "PyQT", "warning" )
#�б����
self.clientdatalist.append(self.client)
del self.clientdatalist[0]
#listview�ؼ�������ʾ
strlist=QStringList()
strlist.append('jer')
self.sde=QStringListModel(strlist)
self.ui.listView.setModel(self.sde)
strlist.append('fea')
self.sde=QStringListModel(strlist)
#sde.rowCount()
self.ui.listView.setModel(self.sde)
'''
logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

#################################################################################################
#����һ��StreamHandler����INFO�������ߵ���־��Ϣ��ӡ����׼���󣬲�������ӵ���ǰ����־�������#
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################
def update_tunnels(filename):
    ns = {}
    execfile(filename, ns)
    globals().update(ns)
class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
    #def __init__(self,parent=None,parnet=None,*args):
        """���ݣ�һ�б��е�ÿ����Ŀ��һ����"""
        QtGui.QWidget.__init__(self, parent)
        #super(MyForm, self).__init__(parent)
        update_tunnels('configuration.txt')
        self.ui = PyFrom
        self.state=state
        self.listnumber=0
        self.addnum=0
        self.listviewdata=[]
        self.ui.setupUi(self)
        self.cmdcliend=None
        #self.client=[]
        self.client=None
        #������Ϣ
        self.clientlinkuser=None
        self.clientlinkpassword=None
        self.clientlinkport=None
        self.linksever=configurationsever
        self.severlinkuser=None
        self.severlinkpassword=None
        self.severlinkport=None
        self.ui.pushButtonAdd.setEnabled(False)
        #self.ui.radioButtonautomatic.setCheckable(True)
        #self.ui.radioButtonmanual.setCheckable(False)
        self.configsave=[]

        self.ui.lineEditClientPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.ui.lineEditSeverPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.ui.LinkPassword.setEchoMode(QtGui.QLineEdit.Password)

        #�����¼�����
        self.ui.listView.clicked.connect(self.indexMove)
        self.ui.pushButtonStart.clicked.connect(self.startxmpp)
        self.ui.pushButtonStop.clicked.connect(self.closexmpp)
        self.ui.pushButtonAdd.clicked.connect(self.SendSeverXMPP)
        self.ui.pushButtonDelete.clicked.connect(self.CloseSeverXMPP)
        self.ui.pushButtonTest.clicked.connect(self.testlink)

        self.ui.pushButtonStart.setEnabled(True)
        self.ui.pushButtonStop.setEnabled(False)
        #ˢ�±�־
        self.refresh=False
        #��ѡ��
        self.model= None

        self.setWindowTitle('Client')
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        #�򿪲˵�
        loadconfig = QtGui.QAction(QtGui.QIcon('open.ico'), 'Open', self)
        loadconfig.setShortcut('Ctrl+Q')
        loadconfig.setStatusTip('Exit application')
        #self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('closexmpp()'))
        loadconfig.triggered.connect(self.OpenFile)
        #����˵�
        savaconfig = QtGui.QAction(QtGui.QIcon('save.ico'), 'Save', self)
        savaconfig.setShortcut('Ctrl+S')
        savaconfig.setStatusTip('Exit application')
        #self.connect(exit, QtCore.SIGNAL('triggered()'), QtCore.SLOT('closexmpp()'))
        savaconfig.triggered.connect(self.saveFile)

        self.statusBar()
        #�ر������С��
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.CustomizeWindowHint)
        #File�˵�
        menubar = self.menuBar()
        file = menubar.addMenu('&File')
        file.addAction(loadconfig)
        file.addAction(savaconfig)
        '''
        #�ļ�����
        fil=Openconfig()
        er=fil.readfile('config.txt')
        data='192.681.56.1 a 123456 45 152.165.12.1 b 123456 85\n'
        fil.resetwrite('config.txt',data)
        fil.addwrite('config.txt',data)
        '''
        self.ui.lineEditClientrIP.setText('192.168.123.122')
        self.ui.lineEditClientUser.setText('chgkj')
        self.ui.lineEditClientPassword.setText('123456')
        self.ui.lineEditClientPort.setText('80')
        self.ui.lineEditSeverIP.setText('192.168.123.122')
        self.ui.lineEditSeverUser.setText('shgkj')
        self.ui.lineEditSeverPassword.setText('123456')
        self.ui.lineEditSeverPort.setText('8080')
        self.ui.lineEditSever.setText('192.168.123.122')
        self.ui.LinkUser.setText(configurationuser)
        self.ui.LinkPassword.setText(configurationpassword)
        self.ui.LinkSeverUser.setText(configurationtosever)
        '''
        strlist=QStringList()
        strlist.append('hello')
        strm=QStringListModel(strlist)
        strm.setStringList(strlist)
        self.ui.listView=QListView(strm)
        '''

        #self._filter = Filter()
        #self.ui.textEditSeverIP.installEventFilter(self._filter)
        self.ui.listView.installEventFilter(self)
        #listView�ؼ���ѡ
        self.ui.listView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        '''
        #self.view=None
        listvew = threading.Thread(target=self.viewlist, args=(self))
        #objectview=Threadview
        '''
        #�¼����߳�ˢ����ʾ
        self.listview=updatelistview()
        self.listview.updateText.connect(self.viewlist)
        #self.listview.addseverthread()
        '''
        t = threading.Timer(5.0, self.listview.addseverthread)
        t.start()
        '''
        #self.installEventFilter(self)

        self.clientuserlink=[]
        self.severuserlink=[]
        #ɾ����־
        self.deleteview=[]
        #self.ui.textEditSever.setFocusPolicy(Qt.StrongFocus)
        '''
        self.ee=[]
        ProduceList('as',self.ee,10)
        '''
        listvew = threading.Thread(target=self.updatalistview, args=())
        #�����ػ�����
        listvew.setDaemon(True)
        listvew.start()
    '''
    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.WindowActivate:
            print "widget window has gained focus 1"
        elif event.type()== QtCore.QEvent.WindowDeactivate:
            print "widget window has lost focus 2"
        elif event.type()== QtCore.QEvent.FocusIn:
            print "widget has gained keyboard focus 2"
        elif event.type()== QtCore.QEvent.FocusOut:
            print "widget has lost keyboard focus 4"
    '''
    '''
    def focusInEvent(self, event):
        print ('Got focus')

    def focusOutEvent(self, event):
        print('Lost focus')
    '''
    def eventFilter(self, widget, event):
        # FocusOut event
        if event.type() == QtCore.QEvent.FocusOut:
            # do custom stuff
            print 'focus out'
            self.refresh=False
            # return False so that the widget will also handle the event
            # otherwise it won't focus out
            #ע��Ҫ�з���ֵ  ��Ȼ��� TypeError: invalid result type from mouseoverEvent.eventFilter()
            return False
        if event.type()==QtCore.QEvent.FocusIn:
            print 'focus in'
            self.refresh=True
            return False
        else:
            # we don't care about other events
            return False
    def updatalistview(self):
        while True:
            #if self.refresh==False:
                time.sleep(1)
                self.listview.addseverthread()
    def viewlist(self):
        #while True:
            #ÿ������ִ��
            #time.sleep(3)
            #print 'view'
            if self.refresh==False:
                #strlist=QStringList()
                #strlist.append('jer')
                self.model = QStandardItemModel(self.ui.listView)
                for food in listviewdata:
                       item = QStandardItem(food)
                        # Add a checkbox to it
                       item.setCheckable(True)
                        # Add the item to the model
                       self.model.appendRow(item)
                '''
                self.itemview=QStandardItem(listviewdata)
                self.itemview.setCheckable(True)
                model.appendRow(self.itemview)
                '''

                self.ui.listView.setModel(self.model)

               # sde=QStringListModel(listviewdata)
               # self.ui.listView.setModel(sde)
                #setPlainText('ok')
                #lk=MyListMode(listviewdata,self)
                #self.ui.listView.setModel(lk)
                #PyFrom.textEditView.setPlainText(str(EdittextView))
                #self.update()
                #self.repaint()
    def OpenFile(self):
        #print 'open file'
        '''
        filename = QtGui.QFileDialog.getOpenFileName(self, 'Open file',
                    '/home','Document files (*.conf );;All files(*.*)')
        '''
        filepath = QtGui.QFileDialog.getOpenFileName(self, 'Open file',QDir.currentPath()+'/config.conf',
                    'Document files (*.conf )')
        if str(filepath) is not '':
            fil=Openconfig()
            self.configsave=fil.readfile(filepath)
        for i in range(len(self.configsave)):
            AddSeverToXMPP(self,self.linksever,self.configsave[i])
        #fname = open(filename)
        #data = fname.read()
        #self.textEdit.setText(data)
        print filepath
    def saveFile(self):
        print 'load'
        filepath = QtGui.QFileDialog.getSaveFileName(self, 'Save file',QDir.currentPath()+'/config.conf',
                    'Document files (*.conf )',)
        if str(filepath) is not '':
            #print 'none'
            fil=Openconfig()
            fil.resetwrite(filepath,self.configsave)

    #��ȡ�б�λ��
    def indexMove(self,text):
        self.listnumber=text.row()
        #self.sde.index(row)
       # self.sde.rowCount()
        modelindexs = self.ui.listView.selectedIndexes()
        self.deleteview=[]
        for i in range(len(listviewdata)):
            if self.model.item(i).checkState()==2:
                self.deleteview.append(i)
        print len(modelindexs)
        print self.listnumber
    def startxmpp(self):
        #addseverthread(self)

        update_tunnels('configuration.txt')
        configurationuser=str(self.ui.LinkUser.text())
        configurationpassword=str(self.ui.LinkPassword.text())
        configurationtosever=str(self.ui.LinkSeverUser.text())
        self.linksever=str(self.ui.lineEditSever.text())

        global configuser
        configuser=configurationuser+'@'+configurationsever
        global configsever
        configsever=configurationtosever+'@'+configurationsever
        #������������
        ProduceList(str(self.ui.lineEditSeverUser.text()),self.severuserlink,100)
        username=str(self.ui.lineEditSeverUser.text())
        username='c'+username[1:]
        #username=strnset(username,'s',1)
        ProduceList(username,self.clientuserlink,100)



        if configuser==None or configuser=='' or configurationpassword==None or configurationpassword=='':
            reply = QtGui.QMessageBox.question(self, 'Error',
            u'�����ĵ�����', QtGui.QMessageBox.Yes)
        else:
            self.cmdcliend = Client(JID(configuser), configurationpassword,None)
            t = threading.Thread(target=xmppcmdlink, args=(self,))
            #�����ػ�����
            t.setDaemon(True)
            t.start()
    def closexmpp(self):
        #userdata=[]
        self.addnum=0
        self.ui.pushButtonStart.setEnabled(True)
        self.ui.pushButtonTest.setEnabled(True)
        self.ui.pushButtonStop.setEnabled(False)
        self.ui.pushButtonAdd.setEnabled(False)
        setContorlNoEnable(self)
        #ɾ����������
        '''
        data=[]
        lk=MyListMode(data,self)
        self.ui.listView.setModel(lk)
        '''
        #del clientdatalist
        leng=len(clientdatalist)
        if leng!=0:
            while len(clientdatalist):
                clientdatalist[0].disconnect()
                del clientdatalist[0]
            #ѭ��ɾ��Զ��
               # clientdatalist[i].disconnect()
                data='CMD CLOSE !%s' % str(0)
        #ɾ��XPMPP����  ��SOCK����
                send_xmpp_cmd(self.cmdcliend,configuser, configsever, data)
                #del clientdatalist[i]
        '''
        leng=len(listviewdata)
        if leng!=0:
            for i in range(leng):
                del listviewdata[i]
        '''
        '''
        deletealldata(listviewdata)
        deletealldata(userdata)
        deletealldata(self.configsave)
        '''
        deletealldata(listviewdata)
        deletealldata(userdata)
        deletealldata(self.configsave)
        self.cmdcliend.disconnect()
    #����
    '''
    def viewlist(self):
    #while True:
        #ÿ������ִ��
        time.sleep(5)
        print 'view'
        strlist=QStringList()
        strlist.append('jer')
        sde=QStringListModel(strlist)
        self.ui.listView.setModel(sde)
    '''
    def testlink(self):
        print 'test link'
        send_xmpp_cmd(self.cmdcliend,configuser, configsever, 'TESTLINK')
#����ָ��
    def SendSeverXMPP(self):
        print 'send add port'
        clentlinkip=self.ui.lineEditClientrIP.text()
        clientlinkport=self.ui.lineEditClientPort.text()
        severlinkip=self.ui.lineEditSeverIP.text()
        severlinkport=self.ui.lineEditSeverPort.text()
        linksever=self.ui.lineEditSever.text()
        #er=self.ui.radioButtonmanual.isCheckable()
        #�Զ����ֶ����
        if self.ui.radioButtonmanual.isChecked():
            clientlinkuser=self.ui.lineEditClientUser.text()
            clientlinkpassword=self.ui.lineEditClientPassword.text()
            severlinkuser=self.ui.lineEditSeverUser.text()
            severlinkpassword=self.ui.lineEditSeverPassword.text()
        else:
            clientlinkuser=self.clientuserlink[self.addnum]
            clientlinkpassword=self.clientuserlink[self.addnum]
            severlinkuser=self.severuserlink[self.addnum]
            severlinkpassword=self.severuserlink[self.addnum]
        #���ظ�
        startsend=False
        for i in listviewdata:
            if i.find(clientlinkuser)!=-1 or i.find(severlinkuser)!=-1:
                reply = QtGui.QMessageBox.question(self, 'Error',
                u'���ظ����', QtGui.QMessageBox.Yes)
                startsend=True
            else: startsend=False
        if startsend==False or len(listviewdata)==0:
            data=[]

            data.append(str(severlinkip))
            data.append(str(severlinkuser))
            data.append(str(severlinkpassword))
            data.append(str(severlinkport))
            data.append(str(clentlinkip))
            data.append(str(clientlinkuser))
            data.append(str(clientlinkpassword))
            data.append(str(clientlinkport))


            self.configsave.append(data)

            AddSeverToXMPP(self,linksever,data)
            '''
            linviewdata=u'  δ����'
            data=str(severlinkip)+'  '+str(severlinkport)+'  '+str(severlinkuser)+'  '+str(clentlinkip)+'  '+str(clientlinkport)+'  '+str(clientlinkuser)+linviewdata
            listviewdata.append(data)
            self.client.append(Client(JID(clientlinkuser+'@'+linksever), clientlinkpassword,None))
            lk=MyListMode(listviewdata,self)
            self.ui.listView.setModel(lk)
            data=[]
            data.append(clentlinkip+':'+str(clientlinkport))
            data.append(severlinkip+':'+str(severlinkport))
            data.append(severlinkuser+'@'+linksever)
            #��������SOCK������
            im_tcp_tunneler.setup_tunnels(self.client[self.addnum],data)
            t = threading.Thread(target=xmpplink, args=(self.client[self.addnum],))
            #�����ػ�����
            t.setDaemon(True)
            t.start()
            #�洢����
            clientdatalist.append(self.client[self.addnum])
            #���Ϳ�������
            data=severlinkuser+'@'+linksever+'!'+severlinkpassword+'!'+linksever+'!'+str(self.addnum)
            data='CMD ADD !%s ' % data
            send_xmpp_cmd(self.cmdcliend,configurationuser, configurationtosever, data)
            self.addnum=self.addnum+1
            '''
    #pass
    def CloseSeverXMPP(self):
        self.refresh==True
            #num=self.listnumber
        leng=len(self.deleteview)
        for i in range(len(self.deleteview)):
            num=self.deleteview[i]
            if self.addnum!=0:
                self.addnum=self.addnum-1
                #self.addnum=self.addnum-len(self.deleteview)
                '''
                leng=len(listviewdata)
                if leng>=2  and num+1<leng:
                    clientdatalist[num].disconnect()
                    listviewdata[num]=listviewdata[num+1]
                    userdata[num]=userdata[num+1]
                    clientdatalist[num]=clientdatalist[num+1]
                    del(listviewdata[num])
                    del (userdata[num])
                    del clientdatalist[num]
                elif leng==(num+1):
                '''

                clientdatalist[num].disconnect()
                listviewdata[num]='!'
                userdata[num]='!'
                self.configsave[num]='!'
                clientdatalist[num]='!'
                '''
                data=''
                for i in range(len(listviewdata)):
                    data='!'+str(self.deleteview[i])
                data='CMD CLOSE %s' % data
                data='CMD CLOSE !%s' % str(self.listnumber)
                #ɾ��XPMPP����  ��SOCK����
                send_xmpp_cmd(self.cmdcliend,configurationuser, configurationtosever, data)
                '''
                '''
                del(listviewdata[num])
                del (userdata[num])
                del  self.configsave[num]
                del clientdatalist[num]
                '''
            '''
            lk=MyListMode(listviewdata,self)
            self.ui.listView.setModel(lk)
            '''
        #  linviewdata
        '''
        er=len(listviewdata)
        for j in range(len(listviewdata)):
            if listviewdata[j]=='!':
                del(listviewdata[j])
                del (userdata[j])
                del  self.configsave[j]
                del clientdatalist[j]
                j=0
        '''
        data=''
        for i in range(leng):
            data=data+'!'+str(self.deleteview[i])
        data='CMD OR CLOSE%s' % data
        #ɾ��XPMPP����  ��SOCK����
        send_xmpp_cmd(self.cmdcliend,configuser, configsever, data)
        j=0
        i=0
        while len(self.deleteview)!=j:
            if listviewdata[i]=='!':
                del(listviewdata[i])
                del (userdata[i])
                del  self.configsave[i]
                del clientdatalist[i]
                i=0
                j=j+1
            i=i+1
            if i==len(listviewdata): i=0


        self.refresh==False
def ProduceList(data,list,leng):
    for i in range(leng):
        s='%04d'%i
        list.append(data+s)
    return  list
def deletealldata(data):
    print 'delete all data'
    leng=len(data)
    if leng!=0:
        while len(data):
            del data[0]
        '''
        for i in range(leng):
            del data[i]
        '''
'''
class Filter(QtCore.QObject):
    def eventFilter(self, widget, event):
        # FocusOut event
        if event.type() == QtCore.QEvent.FocusOut:
            # do custom stuff
            print 'focus out'
            # return False so that the widget will also handle the event
            # otherwise it won't focus out
            #ע��Ҫ�з���ֵ  ��Ȼ��� TypeError: invalid result type from mouseoverEvent.eventFilter()
            return False
        if event.type()==QtCore.QEvent.FocusIn:
            print 'focus in'
            return False
        else:
            # we don't care about other events
            return False
'''
def AddSeverToXMPP(self,linksever,data):
    runadd=True
    if len(userdata)!=0:
        for i in range(len(userdata)):
            if data[1]==userdata[i]:
                runadd=False
    if self.ui.pushButtonStart.isEnabled()==False and runadd==True:
        linksever=str(linksever)
        linviewdata=u'  δ����'
        usdata=data[0]+' '+data[1]+' '+data[3]+' '+data[4]+' '+data[5]+' '+data[7]+' '\
               +linviewdata
        print 'addsevertoxmpp'
        listviewdata.append(usdata)
        #self.client.append(Client(JID(data[5]+'@'+linksever), data[6],None))
        self.client=Client(JID(data[5]+'@'+linksever),data[6],None)
        '''
        lk=MyListMode(listviewdata,self)
        self.ui.listView.setModel(lk)
        '''
        dedata=[]
        dedata.append(data[4]+':'+data[7])
        dedata.append(data[0]+':'+data[3])

        dedata.append(data[1]+'@'+linksever)
        #��������SOCK������
        #im_tcp_tunneler.setup_tunnels(self.client[self.addnum],dedata)
        im_tcp_tunneler.setup_tunnels(self.client,dedata)
        #t = threading.Thread(target=xmpplink, args=(self.client[self.addnum],))
        t=threading.Thread(target=xmpplink,args=(self.client,))
        #�����ػ�����
        t.setDaemon(True)
        t.start()
        #�洢����
        #clientdatalist.append(self.client[self.addnum])
        clientdatalist.append(self.client)
        #���Ϳ�������
        dedata=data[1]+'@'+linksever+'!'+data[2]+'!'+linksever+'!'+str(self.addnum)
        dedata='CMD ADD !%s ' % dedata
        send_xmpp_cmd(self.cmdcliend,configuser, configsever, dedata)
        userdata.append(data[1])
        self.addnum=self.addnum+1
    else:
        if runadd==False:
            reply = QtGui.QMessageBox.question(self, 'Error',
            u'�Ѵ��ڸ��û�', QtGui.QMessageBox.Yes)
        else:
            reply = QtGui.QMessageBox.question(self, 'Error',
            u'δ��������', QtGui.QMessageBox.Yes)
class updatelistview(QtCore.QObject):
    updateText = QtCore.pyqtSignal(str)
    def addseverthread(self):

        listvew = threading.Thread(target=self.monitor_vector, args=())
        #�����ػ�����
        listvew.setDaemon(True)
        listvew.start()
        '''
        t_monitor = threading.Thread(self.viewlist, args=(self,))
        t_monitor.daemon = True
        t_monitor.setName('monitor')
        t_monitor.start()
        '''
    def monitor_vector(self):
        self.updateText.emit('updated list')

'''
def addseverthread(self):
        listvew = threading.Thread(target=viewlist, args=(self,))
        #�����ػ�����
        listvew.setDaemon(True)
        listvew.start()
'''
#�������������ʱ��
def updatestate(self,num):
    print 'add port ok'
    if len(listviewdata)!=0:
        linviewdata=u'  δ����'
        i=listviewdata[num].find(linviewdata)
        if i!=-1:
            listviewdata[num]=listviewdata[num][0:i]
            linviewdata=u'  ������'
            listviewdata[num]=listviewdata[num]+linviewdata
im_tcp_tunneler.updatestate=updatestate
def judgelink(self):
    print 'return link'
    PyFrom.pushButtonTest.setEnabled(False)
im_tcp_tunneler.judgelink=judgelink
#�������ر�ʱ��
def updatelink(self):
    print 'sever is close'
    #EdittextView=EdittextView+u'Զ�̷������ѹر�'
    leng=len(listviewdata)
    for num in range(leng):
        linviewdata=u'  ������'
        i=listviewdata[num].find(linviewdata)
        if i!=-1:
            listviewdata[num]=listviewdata[num][0:i]
           # listviewdata[0]=''
            linviewdata=u'  δ����'
            listviewdata[num]=listviewdata[num]+linviewdata
    #����״̬
im_tcp_tunneler.updatelink=updatelink
#�ڹرյ�������ʱ��
'''
def deletestate(self,num):
    print 'DELETE'
    #EdittextView=EdittextView+u'�ѹرյ�������'
    if len(listviewdata)!=0:
        linviewdata=u'  ������'
        i=listviewdata[num].find(linviewdata)
        if i!=-1:
            listviewdata[num]=listviewdata[num][0:i]
           # listviewdata[0]=''
            linviewdata=u'  δ����'
            listviewdata[num]=listviewdata[num]+linviewdata
            #�б�λ��
            #listnumber=listnumber+1
        #����״̬
im_tcp_tunneler.deletestate=deletestate
'''
#strlist=QStringList()
'''
def viewlist(self):

    while True:
        #ÿ������ִ��
        time.sleep(3)
        print 'view'
        #strlist=QStringList()
        strlist.append('jer')
        sde=QStringListModel(strlist)
        #self.ui.listView.setModel(sde)
        PyFrom.listView.setModel(sde)
        #setPlainText('ok')
        #lk=MyListMode(listviewdata,self)
        #self.ui.listView.setModel(lk)
        #PyFrom.textEditView.setPlainText(str(EdittextView))
        #self.update()
        #self.repaint()
'''
def xmpplink(client):
    locale.setlocale(locale.LC_CTYPE, "")
    encoding = locale.getlocale()[1]
    if not encoding:
        encoding = "us-ascii"
    sys.stdout = codecs.getwriter(encoding)(sys.stdout, errors = "replace")
    sys.stderr = codecs.getwriter(encoding)(sys.stderr, errors = "replace")
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.INFO) # change to DEBUG for higher verbosity
    print u"creating client..."
    print u"connecting..."
    try:
     client.connect()
     #��ʱ�ر�
    except :
        #�����쳣
        print 'connect error'
    print u"looping..."
    #���İ�ť״̬
    try:
        #���ӳɹ�
        client.loop(1)
    except KeyboardInterrupt:
        print u"disconnecting..."
        client.disconnect()
    print u"exiting..."
def xmppcmdlink(self):
    locale.setlocale(locale.LC_CTYPE, "")
    encoding = locale.getlocale()[1]
    if not encoding:
        encoding = "us-ascii"
    sys.stdout = codecs.getwriter(encoding)(sys.stdout, errors = "replace")
    sys.stderr = codecs.getwriter(encoding)(sys.stderr, errors = "replace")
    logger = logging.getLogger()
    logger.addHandler(logging.StreamHandler())
    print u"creating client..."
    print u"connecting..."
    setControlsEnable(self)
    if self.state==False:
        self.state=True
        try:
         self.cmdcliend.connect()
         self.state=False
         #��ʱ�ر�
         self.ui.pushButtonStart.setEnabled(False)
        except :
            #�����쳣
            print 'connect error'
            self.ui.pushButtonStart.setEnabled(True)
            reply = QtGui.QMessageBox.question(self, 'Error',
                u'���ӳ���', QtGui.QMessageBox.Yes)
        print u"looping..."
        #���İ�ť״̬
        self.ui.pushButtonStop.setEnabled(True)
        self.ui.pushButtonAdd.setEnabled(True)
        try:
            #���ӳɹ�
            self.cmdcliend.loop(1)
            self.state=False
        except KeyboardInterrupt:
            print u"disconnecting..."
            self.client.disconnect()
            reply = QtGui.QMessageBox.question(self, 'Error',
                u'���ӳ���', QtGui.QMessageBox.Yes)
        print u"exiting..."
'''
class MyListMode(QAbstractListModel):
    def __init__(self,datain,parnet=None,*args):
        """���ݣ�һ�б��е�ÿ����Ŀ��һ����"""
        super(MyListMode,self).__init__(parnet,*args)
        self.listdata=datain
    #��2�������ǹ涨�õ�
    def rowCount(self,parent=QModelIndex()):
        return len(self.listdata)
    def data(self,index,row):#isValid()�Ƿ���Ч��
        if index.isValid() and row==Qt.DisplayRole:#�ؼ��������ı�����ʽ����
            return QVariant(self.listdata[index.row()])#QVariant�����һ�������Qt������������
        else:
            return QVariant()
'''
#��Ϣ�����ʼ��
class MsgHandler(object):
    #��Ϣ����
    implements(IMessageHandlersProvider, IPresenceHandlersProvider)
    def __init__(self, client):
        """Just remember who created this."""
        self.client = client
    def get_message_handlers(self):
        return [
            ("normal", self.message),
            ]
    def get_presence_handlers(self):
        return [
            (None, self.presence),
            ("unavailable", self.presence),
            ("subscribe", self.presence_control),
            ("subscribed", self.presence_control),
            ("unsubscribe", self.presence_control),
            ("unsubscribed", self.presence_control),
            ]
    #XMPP���ݽ�����Ӧ
    def message(self,stanza):
        if stanza.get_type() == 'chat':
            im_tcp_tunneler.handle_message(self,stanza.get_from_jid().as_unicode(),
                                             stanza.get_to_jid().as_unicode(),
                                             stanza.get_body())
        return True
    #��Ϣ���
    def presence(self,stanza):
        """Handle 'available' (without 'type') and 'unavailable' <presence/>."""
        msg=u"%s has become " % (stanza.get_from())
        t=stanza.get_type()
        if t=="unavailable":
            msg+=u"unavailable"
        else:
            msg+=u"available"
        show=stanza.get_show()
        if show:
            msg+=u"(%s)" % (show,)
        status=stanza.get_status()
        if status:
            msg+=u": "+status
        print msg
    def presence_control(self,stanza):
        msg=unicode(stanza.get_from())
        t=stanza.get_type()
        if t=="subscribe":
            msg+=u" has requested presence subscription."
        elif t=="subscribed":
            msg+=u" has accepted our presence subscription request."
        elif t=="unsubscribe":
            msg+=u" has canceled his subscription of our."
        elif t=="unsubscribed":
            msg+=u" has canceled our subscription of his presence."
        print msg
        return stanza.make_accept_response()
#���Ӱ汾��ʼ��
class VersionHandler(object):
    implements(IIqHandlersProvider, IFeaturesProvider)
    def __init__(self, client):
        """Just remember who created this."""
        self.client = client
    def get_features(self):
        """Return namespace which should the client include in its reply to a
        disco#info query."""
        return ["jabber:iq:version"]
    def get_iq_get_handlers(self):
        """Return list of tuples (element_name, namespace, handler) describing
        handlers of <iq type='get'/> stanzas"""
        return [
            ("query", "jabber:iq:version", self.get_version),
            ]
    def get_iq_set_handlers(self):
        """Return empty list, as this class provides no <iq type='set'/> stanza handler."""
        return []
    def get_version(self,iq):
        iq=iq.make_result_response()
        q=iq.new_query("jabber:iq:version")
        q.newTextChild(q.ns(),"name","TCP Tunneler Bot")
        q.newTextChild(q.ns(),"version","1.0")
        return iq
def setControlsEnable(self):
    print 'setEnable'
    '''
    self.ui.textEditClientrIP.setEnabled(False)
    self.ui.lineEditClientPassword.setEnabled(False)
    self.ui.textEditClientUser.setEnabled(False)
    self.ui.textEditClientPort.setEnabled(False)
    self.ui.lineEditSeverPassword.setEnabled(False)
    self.ui.textEditSeverIP.setEnabled(False)
    self.ui.textEditSeverPort.setEnabled(False)
    self.ui.textEditSeverUser.setEnabled(False)
    '''
    self.ui.lineEditSever.setEnabled(False)
    self.ui.LinkUser.setEnabled(False)
    self.ui.LinkPassword.setEnabled(False)
    self.ui.LinkSeverUser.setEnabled(False)
def setContorlNoEnable(self):
    print 'setNoEnable'
    '''
    self.ui.textEditClientrIP.setEnabled(True)
    self.ui.lineEditClientPassword.setEnabled(True)
    self.ui.textEditClientUser.setEnabled(True)
    self.ui.textEditClientPort.setEnabled(True)
    self.ui.lineEditSeverPassword.setEnabled(True)
    self.ui.textEditSeverIP.setEnabled(True)
    self.ui.textEditSeverPort.setEnabled(True)
    self.ui.textEditSeverUser.setEnabled(True)
    '''
    self.ui.lineEditSever.setEnabled(True)
    self.ui.LinkUser.setEnabled(True)
    self.ui.LinkPassword.setEnabled(True)
    self.ui.LinkSeverUser.setEnabled(True)
#XMPP���ӳ�ʼ��
class Client(JabberClient):
    def __init__(self, jid, password, tls_cacerts):
        # if bare JID is provided add a resource -- it is required
        #״̬��־λ
        #self.linkstate=None
        if not jid.resource:
            jid=JID(jid.node, jid.domain, "tunneler")
        #TLSSettings��������C/Sģʽ��֤�����Ļ���
        if tls_cacerts:
            if tls_cacerts == 'tls_noverify':
                tls_settings = TLSSettings(require = True, verify_peer = False)
            else:
                tls_settings = TLSSettings(require = True, cacert_file = tls_cacerts)
        else:
            tls_settings = None
        JabberClient.__init__(self, jid, password,
                disco_name="TCP Tunneler Bot", disco_type="bot",
                tls_settings = tls_settings)
        # add the separate components
        self.interface_providers = [
            VersionHandler(self),
            MsgHandler(self),
            ]
    #δ��
    def stream_state_changed(self,state,arg):
        print "*** State changed: %s %r ***" % (state,arg)
    #δ��
    def print_roster_item(self,item):
        if item.name:
            name=item.name
        else:
            name=u""
        print (u'%s "%s" subscription=%s groups=%s'
                % (unicode(item.jid), name, item.subscription,
                    u",".join(item.groups)) )
    #δ��
    def roster_updated(self,item=None):
        if not item:
            print u"My roster:"
            for item in self.roster.get_items():
                self.print_roster_item(item)
            return
        print u"Roster item updated:"
        self.print_roster_item(item)
def send_xmpp_cmd(client,from_jid, to_jid, txt):
    msg = Message(stanza_type = 'chat',
                  from_jid = JID(from_jid),
                  to_jid = JID(to_jid),
                  body = txt)
    client.stream.send(msg)
def send_xmpp_message(client,from_jid, to_jid, txt):
    msg = Message(stanza_type = 'chat',
                  from_jid = JID(from_jid),
                  to_jid = JID(to_jid),
                  body = txt)
    client.stream.send(msg)
im_tcp_tunneler.send_xmpp_message = send_xmpp_message

def get_client_jid(client):
    #����ת��
    return client.stream.my_jid.as_unicode()
im_tcp_tunneler.get_client_jid = get_client_jid
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    #��ȡĬ�������ĵ�
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())


