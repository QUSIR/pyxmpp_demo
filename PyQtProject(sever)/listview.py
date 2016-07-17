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
        #print u'你选择的是{0}'.format(text.row())
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
        #if text.row()==0:#obj.row()指定的项
        #    self.lv.setModel(self.la)
    def pask(self):
        pass
class MyListMode(QAbstractListModel):
    def __init__(self,datain,parnet=None,*args):
        """数据：一列表中的每个项目是一个行"""
        super(MyListMode,self).__init__(parnet,*args)
        self.listdata=datain
    #这2个方法是规定好的
    def rowCount(self,parent=QModelIndex()):
        return len(self.listdata)
    def data(self,index,row):#isValid()是否有效的
        if index.isValid() and row==Qt.DisplayRole:#关键数据以文本的形式呈现
            return QVariant(self.listdata[index.row()])#QVariant类就像一个最常见的Qt联盟数据类型
        else:
            return QVariant()
class MyItemMode(QStandardItemModel):
    def __init__(self,parnet=None):
        super(QStandardItemModel,self).__init__(parnet)
        for i in xrange(10):
            item=QStandardItem('items%d'%i)
            item.setFlags(Qt.ItemIsUserCheckable|Qt.ItemIsEnabled)#ItemIsUserCheckable接受与不接受
            #ItemIsEnabled用于交互
            item.setData(QVariant(Qt.Checked),Qt.CheckStateRole)#Checked检查是否选中
            #CheckStateRole检查是否选择的状态
            self.appendRow(item)#附加一行包含项目。 如果有必要,列数增加的大小项目。
    def paintStart(self):
        l=[]
        for i in xrange(self.rowCount()):
            l.append(self.item(i).ckeckState())
        print l
#self.setCentralWidget(view)中央位置

app =QApplication(sys.argv)
x = ExampleList()
x.show()
sys.exit(app.exec_())
