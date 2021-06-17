import os
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from NewWindow import SecondWindow

class Window(QtWidgets.QWidget):
    textChanged = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        self.img =QtWidgets.QLabel()
        self.relleno=QtWidgets.QLabel()
        self.btn_load = QtWidgets.QPushButton('Load')
        self.ld = QtWidgets.QPushButton('ld')
        self.width = 400
        self.height = 150
        self.filename=[]
        self.list1=[]
        self.init_ui()

    def init_ui(self):
        self.img.setPixmap(QtGui.QPixmap("someimage.png"))

        h_final = QtWidgets.QHBoxLayout(self)
        h_final.addWidget(self.img)
        h_final.addWidget(self.btn_load)
        h_final.addWidget(self.ld)
        self.btn_load.clicked.connect(self.loadafile)
        self.ld.clicked.connect(self.lld)
        self.setWindowTitle('This is main window')
        self.setGeometry(600,150,self.width,self.height)

        self.show()
    def lld(self):
        print(self.filename) 
    @QtCore.pyqtSlot()
    def loadafile(self):
        
        filename, _  = QtWidgets.QFileDialog.getOpenFileName(self, 'Open File', os.getenv('HOME'))
        with open(filename, 'r') as f:
            file_text = f.read()
            self.textChanged.emit(file_text)
        #s.show()
        #self.filename=filename
        #self.list1.append(self.filename)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Window()
    s = SecondWindow()
    s.kk.connect(main.filename.append)
    main.textChanged.connect(s.text.append)
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()