import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
class Tooltip(QtGui.QWidget):
    def _int_(self,parent=None):
        QtGui.QWidget._int_(self,parent)
        self.setGeometry(300,300,250,150)
        self.setWindowTitle('Tooltip')
        self.setToolTip('This as<b>QWidget</b>widget')
        QtGui.QToolTip.setFont(QtGui.QFont('QldEnglish',10))
        QtGui.QPushButton('close')
        self.statusBar().showMessage('ok')
        #QtGui.show()
app=QtGui.QApplication(sys.argv)
tooltip=Tooltip()
#pd=QtGui.QPushButton('close')
#pd.show()
tooltip.show()
sys.exit(app.exec_())
