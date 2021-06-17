# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tool_Main_Frame.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import PyQt5.QtWidgets
from PyQt5.QtWidgets import (QInputDialog,QFileDialog,QMessageBox,QWidget,QMainWindow)
class Ui_Load_STDF(QWidget):
    def _init__(self):
        super().__init__()
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
        fileName=QFileDialog.getOpenFileName(caption='Open file',directory='',filter="STDF Files (*.std *.stdf)")
        if fileName[0]!='':            
            self.Input_textBox.setText(fileName[0])
        else:            
            msg='Please select a File'
            k=self.Messagebox(msg,'criti','Please select a File')
        return fileName
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

class Ui_MainWindow(object):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1390, 914)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        '''self.Stack_Widget=QtGui.QStackedWidget()
        self.setCentralWidget(self.Stack_Widget)'''
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1390, 21))
        self.menubar.setObjectName("menubar")
        self.File = QtWidgets.QMenu(self.menubar)
        self.File.setObjectName("File")
        self.Menu = QtWidgets.QMenu(self.menubar)
        self.Menu.setObjectName("Menu")
        self.View = QtWidgets.QMenu(self.menubar)
        self.View.setObjectName("View")
        self.Data = QtWidgets.QMenu(self.menubar)
        self.Data.setObjectName("Data")
        self.Export = QtWidgets.QMenu(self.Data)
        self.Export.setObjectName("Export")
        self.Import = QtWidgets.QMenu(self.Data)
        self.Import.setObjectName("Import")
        self.Help = QtWidgets.QMenu(self.menubar)
        self.Help.setObjectName("Help")
        self.Editmenu=QtWidgets.QMenu(self.menubar)
        self.Editmenu.setObjectName("Edit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Load = QtWidgets.QAction(MainWindow)
        self.Load.setObjectName("Load")
        self.Save = QtWidgets.QAction(MainWindow)
        self.Save.setObjectName("Save")
        self.Save.setShortcut("Ctrl+S")
        self.Save_As = QtWidgets.QAction(MainWindow)
        self.Save_As.setObjectName("Save_As")
        self.Save_As.setShortcut("Ctrl+Shift+S")
        self.Exit = QtWidgets.QAction(MainWindow)
        self.Exit.setObjectName("Exit")
        self.Exit.setShortcut("Ctrl+Q")
        self.Open = QtWidgets.QAction(MainWindow)
        self.Open.setObjectName("Open")
        self.Open.setShortcut("Ctrl+O")
        self.Load_CSV = QtWidgets.QAction(MainWindow)
        self.Load_CSV.setObjectName("Load_CSV")
        self.Export_Excel = QtWidgets.QAction(MainWindow)
        self.Export_Excel.setObjectName("Export_Excel")
        self.Export_CSV = QtWidgets.QAction(MainWindow)
        self.Export_CSV.setObjectName("Export_CSV")
        self.Export_TXT = QtWidgets.QAction(MainWindow)
        self.Export_TXT.setObjectName("Export_TXT")
        self.Load_STDF = QtWidgets.QAction(MainWindow)
        self.Load_STDF.setObjectName("Load_STDF")
        self.Load_STDF.triggered.connect(self.Open_Load_Action)
        self.Load_Excel = QtWidgets.QAction(MainWindow)
        self.Load_Excel.setObjectName("Load_Excel")
        self.Load_Txt = QtWidgets.QAction(MainWindow)
        self.Load_Txt.setObjectName("Load_Txt")
        self.File.addAction(self.Open)
        self.File.addAction(self.Save)
        self.File.addAction(self.Save_As)
        self.File.addAction(self.Exit)
        self.Export.addAction(self.Export_Excel)
        self.Export.addAction(self.Export_CSV)
        self.Export.addAction(self.Export_TXT)
        self.Import.addAction(self.Load_STDF)
        self.Import.addAction(self.Load_Excel)
        self.Import.addAction(self.Load_Txt)
        self.Data.addAction(self.Import.menuAction())
        self.Data.addAction(self.Export.menuAction())
        self.Help.addSeparator()
        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Menu.menuAction())
        self.menubar.addAction(self.Editmenu.menuAction())
        self.menubar.addAction(self.View.menuAction())
        self.menubar.addAction(self.Data.menuAction())
        self.menubar.addAction(self.Help.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "GOURISANKAR_TOOL"))
        self.File.setTitle(_translate("MainWindow", "File"))
        self.Menu.setTitle(_translate("MainWindow", "Menu"))
        self.View.setTitle(_translate("MainWindow", "View"))
        self.Data.setTitle(_translate("MainWindow", "Data"))
        self.Export.setTitle(_translate("MainWindow", "Export"))
        self.Import.setTitle(_translate("MainWindow", "Import"))
        self.Help.setTitle(_translate("MainWindow", "Help"))
        self.Editmenu.setTitle(_translate('MainWindow','Edit'))
        self.Save.setText(_translate("MainWindow", "Save"))
        self.Save_As.setText(_translate("MainWindow", "Save As.."))
        self.Exit.setText(_translate("MainWindow", "Exit"))
        self.Open.setText(_translate("MainWindow", "Open"))        
        self.Load_CSV.setText(_translate("MainWindow", "Load_CSV"))
        self.Export_Excel.setText(_translate("MainWindow", "Export_Excel"))
        self.Export_CSV.setText(_translate("MainWindow", "Export_CSV"))
        self.Export_TXT.setText(_translate("MainWindow", "Export_TXT"))
        self.Load_STDF.setText(_translate("MainWindow", "Load_STDF"))
        self.Load_Excel.setText(_translate("MainWindow", "Load_Excel"))
        self.Load_Txt.setText(_translate("MainWindow", "Load_Txt"))
    
    def Open_Load_Action(self):
        import sys
        #Load_app = QtWidgets.QApplication(sys.argv)
        Load_STDF = QtWidgets.QWidget()
        Load_STDF_ui = Ui_Load_STDF()
        Load_STDF_ui.setupUi(Load_STDF)
        Load_STDF.show()
        #Load_app.exec_()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

