#!/usr/bin/python -u
# -*- coding:cp936 -*-

import sys
#出错日志
import logging
#本地化字符编码
import locale
#编码处理
import codecs
import pdb
import threading
import time
#获取ID库
import uuid
#异常库
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

from project_sever import Ui_Form


logging.basicConfig(level=logging.DEBUG,
                format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                datefmt='%a, %d %b %Y %H:%M:%S',
                filename='myapp.log',
                filemode='w')

#################################################################################################
#定义一个StreamHandler，将INFO级别或更高的日志信息打印到标准错误，并将其添加到当前的日志处理对象#
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)
#################################################################################################

'''
logging.debug('This is debug message')
logging.info('This is info message')
logging.warning('This is warning message')
'''

#全局变量
PyFrom = Ui_Form()
import im_tcp_tunneler
#列表显示
listviewdata=None
#列表位置
listnumber=None
#默认链接
configurationuser = 'e@localhost'
#configurationuser ='e@www.baidu.com'
configurationpassword = '123456'
configurationsever ='localhost'
configurationtosever='f@localhost'
#提示框显示
EdittextView=None
#启动线程状态机
state=False
#链接列表
clientdatalist=[]
#校验暂存
userdata=[]
configuser=None
configsever=None
'''
#按键触发
self.connect(self.ui.OpenLink, QtCore.SIGNAL("clicked()"), startxmpp)
self.connect(self.ui.CloseLink, QtCore.SIGNAL("clicked()"), closexmpp)
#复选框
self.ui.radioSever.setChecked(True)
#编辑框
severaddress=PyFrom.textEditSever.toPlainText()
self.ui.textEditUser.setPlainText('e')
#密码输入框
self.ui.lineEditPassword.setEchoMode(QtGui.QLineEdit.Password)
#列表控件
data=[1,2,3,4]
lk=MyListMode(data,self)
self.ui.listView.setModel(lk)
self.ui.listView.clicked.connect(self.indexMove)
#文件读取
f=open('tunnels.conf','r')
print f.read()
#按钮状态
PyFrom.OpenLink.setEnabled(False)
#提示框
reply = QtGui.QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QtGui.QMessageBox.Yes |
            QtGui.QMessageBox.No, QtGui.QMessageBox.No)
QtGui.QMessageBox.question( self, "PyQT", "warning" )
'''
import resources
def update_tunnels(filename):
    ns = {}
    execfile(filename, ns)
    globals().update(ns)
class MyForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = PyFrom
        self.state=state
        self.ui.setupUi(self)
        #self.addnum=0
        #self.userdata=[]
        self.cmdcliend=None
        self.ui.lineEditPassword.setEchoMode(QtGui.QLineEdit.Password)
        #设置标题和图标
        self.setWindowTitle('Sever')
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        #self.setWindowIcon(QtGui.QIcon('min.ico'))
        #self.setWindowIcon(QtGui.QIcon(':/new/prefix/icon.ico'))
        self.ui.pushButtonStart.setEnabled(True)
        self.ui.pushButtonStop.setEnabled(False)
        #调试用
        update_tunnels('configuration.txt')
        self.ui.lineEditUser.setText(configurationuser)
        self.ui.lineEditPassword.setText(configurationpassword)
        self.ui.lineEditSever.setText(configurationsever)
        #单击事件关联
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.WindowCloseButtonHint | Qt.CustomizeWindowHint)

        self.ui.pushButtonStart.clicked.connect(self.startxmpp)
        self.ui.pushButtonStop.clicked.connect(self.closexmpp)
    #读取列表位置

    def startxmpp(self,data):
        update_tunnels('configuration.txt')
        logging.debug('start xmppp 1')
        update_tunnels('configuration.txt')
        logging.debug('start xmppp 2')
        configurationuser=str(self.ui.lineEditUser.text())
        logging.debug('start xmppp 3')
        configurationpassword=str(self.ui.lineEditPassword.text())
        global  configuser
        configuser=configurationuser+'@'+configurationsever
        global  configsever
        configsever=configurationtosever+'@'+configurationsever
        logging.debug('start xmppp 4')
        if configuser==None or configuser=='' or configurationpassword==None or configurationpassword=='':
            logging.debug('start xmppp 5')
            reply = QtGui.QMessageBox.question(self, 'Error',
            u'输入参数出错', QtGui.QMessageBox.Yes)
        else:
            logging.debug('start xmppp 6')
            self.client=None
            logging.debug('start xmppp 7')
            globals().update()
            logging.debug('start xmppp 8')
            self.cmdclient = Client(JID(configuser), configurationpassword,None)
            logging.debug('start xmppp 9')
            #im_tcp_tunneler.setup_tunnels(self,'tunnels.conf')
            t = threading.Thread(target=xmppcmdlink, args=(self,))
            logging.debug('start xmppp 10')
            #创建守护进程
            t.setDaemon(True)
            logging.debug('start xmppp 11')
            t.start()
            logging.debug('start xmppp 12')
    def closexmpp(self):
        deletealldata(userdata)
        self.ui.pushButtonStart.setEnabled(True)
        self.ui.pushButtonStop.setEnabled(False)

        self.ui.lineEditSever.setEnabled(True)
        self.ui.lineEditUser.setEnabled(True)
        self.ui.lineEditPassword.setEnabled(True)
        #send_xmpp_message(self.cmdclient,configurationuser,configurationtosever,'ALLDELETE')
        #删除所有链接
        leng=len(clientdatalist)
        if leng!=0:
            while len(clientdatalist):
                clientdatalist[0].disconnect()
                del  clientdatalist[0]
            '''
            for i in range(leng):
                clientdatalist[i].disconnect()
                del clientdatalist[i]
            '''
        #deletealldata(userdata)
        send_xmpp_message(self.cmdclient,configuser,configsever,'ALLDELETE')
        self.cmdclient.disconnect()
def xmpplink(client,self,to_jid, from_jid, num):
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
    logging.debug('creating client...')
    print u"connecting..."
    try:
     client.connect()
     #暂时关闭
    except :
        #链接异常
        print 'error'
        logging.debug('link error')
    print u"looping..."
    #更改按钮状态
    try:
        #连接成功
        data='OK !'+str(num)
        send_xmpp_cmd(self.client,to_jid, from_jid, data)
        client.loop(1)

    except KeyboardInterrupt:
        print u"disconnecting..."
        logging.debug('disconnecting...')
        client.disconnect()
    print u"exiting..."
    logging.debug('exiting...')
def xmppcmdlink(self):
    logging.debug('start xmppp 13')
    locale.setlocale(locale.LC_CTYPE, "")
    logging.debug('start xmppp 14')
    encoding = locale.getlocale()[1]
    logging.debug('start xmppp 15')
    if not encoding:
        encoding = "us-ascii"
    logging.debug('start xmppp 16')
    sys.stdout = codecs.getwriter(encoding)(sys.stdout, errors = "replace")
    logging.debug('start xmppp 17')
    sys.stderr = codecs.getwriter(encoding)(sys.stderr, errors = "replace")
    logging.debug('start xmppp 18')
    logger = logging.getLogger()
    logging.debug('start xmppp 19')
    logger.addHandler(logging.StreamHandler())
    logging.debug('start xmppp 20')
    #logger.setLevel(logging.INFO) # change to DEBUG for higher verbosity
    print u"creating client..."
    logging.debug('creating client...')
    print u"connecting..."
    if self.state==False:
        self.state=True
        try:
         self.cmdclient.connect()
         self.state=False
         self.ui.pushButtonStart.setEnabled(False)

         self.ui.lineEditSever.setEnabled(False)
         self.ui.lineEditUser.setEnabled(False)
         self.ui.lineEditPassword.setEnabled(False)
         logging.debug('link xmpp')
        except Exception:
        #except :
            #链接异常
            print 'error'
            logging.debug('link error...')
            self.ui.pushButtonStart.setEnabled(True)
            reply = QtGui.QMessageBox.question(self, 'Error',
                u'连接出错', QtGui.QMessageBox.Yes)
        print u"looping..."
        logging.debug('looping...')
        #td = sys.exc_info()
        #更改按钮状态
        self.ui.pushButtonStop.setEnabled(True)
        try:
            #连接成功
            self.cmdclient.loop(1)
            self.state=False
        except KeyboardInterrupt:
            print u"disconnecting..."
            logging.debug('disconnecting...')
            self.cmdclient.disconnect()
            reply = QtGui.QMessageBox.question(self, 'Error',
                u'连接出错', QtGui.QMessageBox.Yes)
        print u"exiting..."
        logging.debug('exiting...')
#消息处理初始化
class MsgHandler(object):
    #消息处理
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
    #XMPP数据接收相应
    def message(self,stanza):
        if stanza.get_type() == 'chat':
            im_tcp_tunneler.handle_message(self,stanza.get_from_jid().as_unicode(),
                                 stanza.get_to_jid().as_unicode(),
                                 stanza.get_body())
        return True
    #消息输出
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
        logging.debug(msg)
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
        logging.debug(msg)
        return stanza.make_accept_response()
#链接版本初始化
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
#XMPP连接初始化
class Client(JabberClient):
    def __init__(self, jid, password, tls_cacerts):
        # if bare JID is provided add a resource -- it is required
        if not jid.resource:
            jid=JID(jid.node, jid.domain, "tunneler")
        #TLSSettings用来扩充C/S模式验证能力的机制
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
    #未用
    def stream_state_changed(self,state,arg):
        print "*** State changed: %s %r ***" % (state,arg)
        logging.debug("*** State changed: %s %r ***" % (state,arg))
    #未用
    def print_roster_item(self,item):
        if item.name:
            name=item.name
        else:
            name=u""
        print (u'%s "%s" subscription=%s groups=%s'
                % (unicode(item.jid), name, item.subscription,
                    u",".join(item.groups)) )
        logging.debug(u'%s "%s" subscription=%s groups=%s'
                % (unicode(item.jid), name, item.subscription,
                    u",".join(item.groups)))
    #未用
    def roster_updated(self,item=None):
        if not item:
            print u"My roster:"
            logging.debug('My roster:')
            for item in self.roster.get_items():
                self.print_roster_item(item)
            return
        print u"Roster item updated:"
        logging.debug('Roster item updated:')
        self.print_roster_item(item)
def send_xmpp_message(client,from_jid, to_jid, txt):
    msg = Message(stanza_type = 'chat',
                  from_jid = JID(from_jid),
                  to_jid = JID(to_jid),
                  body = txt)
    client.stream.send(msg)
im_tcp_tunneler.send_xmpp_message = send_xmpp_message
def closesever(self,to_jid, from_jid,num):
    print 'delete sever'
    logging.debug('delete sever')
    '''
    leng=len(clientdatalist)
    if leng>=2  and num+1<leng:
        clientdatalist[num].disconnect()
        data='DELETE !'+str(num)
        send_xmpp_cmd(self.client,to_jid, from_jid, data)
        clientdatalist[num]=clientdatalist[num+1]
        userdata[num]=userdata[num+1]
        del clientdatalist[num]
        del userdata[num]
    elif leng==(num+1):
    '''
    clientdatalist[num].disconnect()
    data='DELETE !'+str(num)
    send_xmpp_cmd(self.client,to_jid, from_jid, data)
    del userdata[num]
    del clientdatalist[num]
im_tcp_tunneler.closesever=closesever
def closeseveror(self,to_jid, from_jid,num):

    logging.debug('delete sever')
    '''
    leng=len(clientdatalist)
    if leng>=2  and num+1<leng:
        clientdatalist[num].disconnect()
        data='DELETE !'+str(num)
        send_xmpp_cmd(self.client,to_jid, from_jid, data)
        clientdatalist[num]=clientdatalist[num+1]
        userdata[num]=userdata[num+1]
        del clientdatalist[num]
        del userdata[num]
    elif leng==(num+1):
    '''
    if len(clientdatalist)!=0:
        for i in range(len(num)):
            clientdatalist[num[i]].disconnect()
            userdata[num[i]]='!'
            clientdatalist[num[i]]='!'

        j=0
        i=0
        while len(num)!=j:
            if userdata[i]=='!':
                del userdata[i]
                del clientdatalist[i]
                i=0
                j=j+1
            i=i+1
            if i==len(clientdatalist): i=0
        print 'delete sever'
    '''
    clientdatalist[num].disconnect()
    data='DELETE !'+str(num)
    send_xmpp_cmd(self.client,to_jid, from_jid, data)
    del userdata[num]
    del clientdatalist[num]
    '''
im_tcp_tunneler.closeseveror=closeseveror
def deletealldata(data):
    print 'delete all data'
    leng=len(data)
    if leng!=0:
        while len(data):
            del data[0]
def addsever(self,data,to_jid, from_jid):
    print 'add  sever'
    logging.debug('add sever')
    runadd=True
    if len(userdata)!=0:
        for i in range(len(userdata)):
            if data[0]==userdata[i]:
                runadd=False
                data='OK !'+data[3]
                send_xmpp_cmd(self.client,to_jid, from_jid, data)
    if runadd==True:
        #self.addnum=int(data[2])
        num =int(data[3])
        client=Client(JID(data[0]), data[1],None)
        t = threading.Thread(target=xmpplink, args=(client,self,to_jid, from_jid, num,))
            #创建守护进程
        t.setDaemon(True)
        t.start()
        userdata.append(data[0])
        clientdatalist.append(client)
im_tcp_tunneler.addsever=addsever
def send_xmpp_cmd(client,from_jid, to_jid, txt):
    msg = Message(stanza_type = 'chat',
                  from_jid = JID(from_jid),
                  to_jid = JID(to_jid),
                  body = txt)
    client.stream.send(msg)
im_tcp_tunneler.send_xmpp_cmd = send_xmpp_cmd
def get_client_jid(client):
    #编码转换
    return client.stream.my_jid.as_unicode()
im_tcp_tunneler.get_client_jid = get_client_jid
if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    #读取默认配置文档
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())



