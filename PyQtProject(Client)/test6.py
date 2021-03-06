#!/usr/bin/python -u
# -*- coding:cp936 -*-
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import sys

app = QApplication(sys.argv)

# Our main window will be a QListView
list = QListView()
list.setWindowTitle('Example List')
list.setMinimumSize(600, 400)

# Create an empty model for the list's data
model = QStandardItemModel(list)

# Add some textual items
foods = [
    'Cookie dough', # Must be store-bought
    'Hummus', # Must be homemade
    'Spaghetti', # Must be saucy
    'Dal makhani', # Must be spicy
    'Chocolate whipped cream' # Must be plentiful
]

for food in foods:
    # create an item with a caption
    item = QStandardItem(food)

    # add a checkbox to it
    #开启打勾
    item.setCheckable(True)
    if item.isCheckable()==True:
        print 'check true'
        #打勾
        #item.setCheckState(Qt.Checked)
        #item.setCheckState(Qt.Unchecked)
        et=item.checkState()
        #et=item.isDragEnabled()
        print et
        #if item.is
    # Add the item to the model
    model.appendRow(item)
def on_item_changed(item):
    # If the changed item is not checked, don't bother checking others
    if not item.checkState():
        return

    # Loop through the items until you get None, which
    # means you've passed the end of the list
    '''
    i = 0
    while model.item(i):
        if not model.item(i).checkState():
            return
        i += 1
    '''
    #判断是否打勾没有则为零  打勾为2
    print model.item(0).checkState()
    #app.quit()

model.itemChanged.connect(on_item_changed)
# Apply the model to the list view
list.setModel(model)
 
# Show the window and run the app
list.show()
app.exec_()