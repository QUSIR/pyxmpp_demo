#!/usr/bin/python -u
# -*- coding:cp936 -*-
from decimal import *
from PyQt4.QtGui import *
from PyQt4.Qt import *
from PyQt4.QtCore import *
from project_ui import Ui_Form

data=None

import sys
class ExampleList(QWidget):
    def __init__(self,args=None):
        #self.parent=parent
        super(ExampleList, self).__init__(args)
        list_data=[1,2,3,4]
        lm=MyListMode(list_data,self)
        self.lv=QListView()
        #self.lv.
        #self.lv=Ui_Form.listView
        #self.lv=QWidgetku
        #self.lv.setToolTip('listview')
        self.lv.setModel(lm)
        #self.lv.removeAction(0,1)
        #self.la= MyItemMode()
        self.lv.clicked.connect(self.indexMove)
        layot=QVBoxLayout()
        layot.addWidget(self.lv)
        self.setLayout(layot)
    def additem(self,data):
        lk=MyListMode(data,self)
    def indexMove(self,text):
        #print u'��ѡ�����{0}'.format(text.row())
        #print dir(text)
        print text.row()
       # return text.row()
        data=[1,2,6]
        data[0]='dfsad  '+ ' da'
        lk=MyListMode(data,self)

        self.lv.setModel(lk)
        '''
        layot=QVBoxLayout()
        layot.addWidget(self.lv)
        self.setLayout(layot)
        '''
        #if text.row()==0:#obj.row()ָ������
        #    self.lv.setModel(self.la)
    def pask(self):
        pass
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
class MyItemMode(QStandardItemModel):
    def __init__(self,parnet=None):
        super(QStandardItemModel,self).__init__(parnet)
        for i in xrange(10):
            item=QStandardItem('items%d'%i)
            item.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)#ItemIsUserCheckable�����벻����
            #ItemIsEnabled���ڽ���
            item.setData(QVariant(Qt.Checked),Qt.CheckStateRole)#Checked����Ƿ�ѡ��
            #CheckStateRole����Ƿ�ѡ���״̬
            self.appendRow(item)#����һ�а�����Ŀ�� ����б�Ҫ,�������ӵĴ�С��Ŀ��
    def paintStart(self):
        l=[]
        for i in xrange(self.rowCount()):
            l.append(self.item(i).ckeckState())
        print l
#self.setCentralWidget(view)����λ��

app =QApplication(sys.argv)
x = ExampleList()
x.show()
sys.exit(app.exec_())
