# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '_Load_STDF_File.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QInputDialog,QFileDialog,QMessageBox,QWidget)

class Ui_Load_STDF( QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(Ui_Load_STDF,self).__init__(parent)
        self.File_name=""
        
    def setupUi(self, Load_STDF):
        Load_STDF.setObjectName("Load_STDF")
        Load_STDF.resize(581, 89)
        self.Load_group_box = QtWidgets.QGroupBox(Load_STDF)
        self.Load_group_box.setGeometry(QtCore.QRect(10, 0, 561, 81))
        self.Load_group_box.setTitle("")
        self.Load_group_box.setObjectName("groupBox")
        self.Load_progressBar = QtWidgets.QProgressBar(self.Load_group_box)
        self.Load_progressBar.setGeometry(QtCore.QRect(10, 50, 471, 16))
        self.Load_progressBar.setProperty("value", 0)
        self.Load_progressBar.setObjectName("progressBar")
        self.Import_button = QtWidgets.QPushButton(self.Load_group_box)
        self.Import_button.setGeometry(QtCore.QRect(480, 10, 75, 23))
        self.Import_button.setObjectName("Import_button")
        self.File_name=self.Import_button.clicked.connect(self.openFileNameDialog)
        #self.pushButton.clicked.connect()
        self.Input_textBox = QtWidgets.QLineEdit(self.Load_group_box)
        self.Input_textBox.setGeometry(QtCore.QRect(60, 10, 411, 31))
        self.Input_textBox.setObjectName("Input_textBox")        
        self.Input_txtbx_lbl = QtWidgets.QLabel(self.Load_group_box)
        self.Input_txtbx_lbl.setGeometry(QtCore.QRect(10, 20, 47, 13))
        self.Input_txtbx_lbl.setObjectName("Input_txtbx_lbl")
        self.Load_button = QtWidgets.QPushButton(self.Load_group_box)
        self.Load_button.setGeometry(QtCore.QRect(480, 50, 75, 23))
        self.Load_button.setObjectName("Load_button")
        self.retranslateUi(Load_STDF)
        QtCore.QMetaObject.connectSlotsByName(Load_STDF)

    def retranslateUi(self, Load_STDF):
        _translate = QtCore.QCoreApplication.translate
        Load_STDF.setWindowTitle(_translate("Load_STDF", "Load File"))
        self.Import_button.setText(_translate("Load_STDF", "Import"))
        self.Input_txtbx_lbl.setText(_translate("Load_STDF", "Load_File"))
        self.Load_button.setText(_translate("Load_STDF", "Load"))
    def openFileNameDialog(self):
        '''Opens Files diralog to browse the data'''
        fileName=QFileDialog.getOpenFileName(caption='Open file',directory='',filter="STDF Files (*.std *.stdf);;All Files (*.*)")
        if fileName[0]!='':            
            self.Input_textBox.setText(fileName[0])
            self.File_name=fileName[0]
        else:            
            msg='Please select a File'
            k=self.Messagebox(msg,'criti','Please select a File')
        return fileName[0]
    def Messagebox(self,msg_text,msgtype='info',title='Message Box'):
        ''' Message is a function to call the message box in PyQt Quickly.  msgtype can be (info, warn,que,criti).
            msg_text is the msg you want to display, Title will be window Title'''
        if msgtype=='info':
            reply=QMessageBox.information(self,title,msg_text,QMessageBox.Ok ,QMessageBox.Ok)
        elif msgtype=='warn':
            reply=QMessageBox.warning(self,title,msg_text,QMessageBox.Ok ,QMessageBox.Ok)
        elif msgtype=='que':
            reply=QMessageBox.question(self,title,msg_text,QMessageBox.Yes | QMessageBox.No ,QMessageBox.Yes)
        elif msgtype=='criti':
            reply=QMessageBox.critical(self,title,msg_text,QMessageBox.Ok | QMessageBox.Cancel ,QMessageBox.Ok)
        return reply
    def Get_the_file_name(self):
        ''' Returns the imported file name'''
        self.Load_STDF = QtWidgets.QDialog()
        ui = Ui_Load_STDF()
        ui.setupUi(self.Load_STDF)
        if self.Load_STDF.exec():
            self.Load_STDF.hide()
            return self.File_name
    #return self.File_name
'''if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Load_STDF = QtWidgets.QWidget()
    ui = Ui_Load_STDF()
    ui.setupUi(Load_STDF)
    Load_STDF.show()
    sys.exit(app.exec_())
'''
