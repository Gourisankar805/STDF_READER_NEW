
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QInputDialog,QFileDialog,QMessageBox,QWidget)
from rev003p9_finalysing_stdf_reader import READ_THE_STDF_FILE
from excel_sheet_selector import Ui_Sheet_selector
import time,sys
import pandas as pd
from pandas import DataFrame as DF

class Ui_Load_STDF( QtWidgets.QDialog):
    File_Name_to_export=QtCore.pyqtSignal(list)

    def __init__(self,parent=None):
        super(Ui_Load_STDF,self).__init__()
        self.File_name=""
        self.Parent_window=parent
        self.Imported_file_data=[]
        self.STDF_DATA={}
        #self.Raw_Data_DF=None
        '''self.LdStdf = QtWidgets.QDialog()
        self.setupUi(self.LdStdf)'''
    def setupUi(self, Load_STDF):
        global Load_STDF1
        Load_STDF1=Load_STDF
        Load_STDF.setObjectName("Load_STDF")
        Load_STDF.resize(581, 89)
        self.Load_group_box = QtWidgets.QGroupBox(Load_STDF)
        self.Load_group_box.setGeometry(QtCore.QRect(10, 0, 561, 81))
        self.Load_group_box.setTitle("")
        self.Load_group_box.setObjectName("groupBox")
        self.Load_progressBar = QtWidgets.QProgressBar(self.Load_group_box)
        self.Load_progressBar.setGeometry(QtCore.QRect(10, 50, 471, 16))
        self.Load_progressBar.setProperty("value", 0)
        self.Load_progressBar.setMaximum(100)        
        self.Load_progressBar.setObjectName("progressBar")
        self.Import_button = QtWidgets.QPushButton(self.Load_group_box)
        self.Import_button.setGeometry(QtCore.QRect(480, 10, 75, 23))
        self.Import_button.setShortcut("Ctrl+Shift+I")
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
        self.Load_button.clicked.connect(self.Load_Action)
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
        fileName=QFileDialog.getOpenFileName(caption='Open file',directory='',filter="STDF Files (*.std *.stdf);;Excel Files (*.xlsx *.xls);;CSV Files (*.csv);;All Files (*.*)")
        if fileName[0]!='':            
            self.Input_textBox.setText(fileName[0])
            self.File_name=fileName[0]
            self.File_Type=fileName[1]
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
    def Store_the_Data(self):
        ''' Stores the loaded Data into Dictnory for ease of access'''                    
       # self.STDF_DATA={}
        #self.Load_window.File_Name_to_export.connect(self.Imported_file_data.append)
        #self.Load_window.File_Name_to_export.connect(self.Ldd())
        if self.Parent_window!=None:
            self.Parent_window.File_Path.append(self.File_name)
            self.Rec_Summary_list=['FAR_Rec_summary','ATR_Rec_summary','MIR_Rec_Summary','SDR_Rec_Summary', 'PMR_Rec_Summary','WCR_Rec_Summary'
            ,'WIR_Rec_Summary','PIR_Rec_Summary','PRR_Rec_Summary','MPR_Rec_Summary','WRR_Rec_Summary','TSR_Rec_Summary','HBR_Rec_Summary',
            'SBR_Rec_Summary','PCR_Rec_Summary','MRR_Rec_Summary','BPS_Rec_Summary','DTR_Rec_Summary','PGR_Rec_Summary', 'RDR_Rec_Summary'
            ,'GDR_Rec_Summary','Test_Details','Test_Flag_Details','PTR_Rec_Summary','FTR_Rec_Summary','Full_Rec_Summary','Test_Limit_Details']
            if len(self.Raw_Data.Clubbed_Record_Details)>1:
                for i in range(len(self.Rec_Summary_list)):                
                    self.STDF_DATA[self.Rec_Summary_list[i]]=self.Raw_Data.Clubbed_Record_Details[i]
            if self.Parent_window!=None:
                self.Parent_window.Loaded_Data_File_count.append('File_'+str(len(self.Parent_window.Loaded_Data_File_count)+1))
                self.Parent_window.Loaded_Data_Files[self.Parent_window.Loaded_Data_File_count[len(self.Parent_window.Loaded_Data_File_count)-1]]=self.STDF_DATA
                self.Parent_window.Loaded_Data_File_Raw_Data[self.Parent_window.Loaded_Data_File_count[len(self.Parent_window.Loaded_Data_File_count)-1]]=DF(self.Raw_Data.Full_Rec_Summary)
            #self.STDF_DATA.clear()
            self.Imported_file_data=[]
            self.STDF_DATA={}
    #@QtCore.pyqtSlot()
    def Load_Action(self):
        '''Sends the input name to main windows'''        
        if self.File_name!=None:
            if self.File_Type=="STDF Files (*.std *.stdf)":
                self.Raw_Data=READ_THE_STDF_FILE(parent=self)
                self.Raw_Data.Start_process(self.File_name,Load_STDF1)
                self.Store_the_Data()
                #Load_STDF1.close()
            elif self.File_Type=="Excel Files (*.xlsx *.xls)":
                self.Load_the_excel_file(self.File_name)
            elif self.File_Type=="CSV Files (*.csv)":
                print('on hold')            
            self.Load_progressBar.setValue(50)
            
            #if self.Parent_window!=None: self.Parent_window.Refresh_data_table_items()
            
            Load_STDF1.close()           
        else:
            
            self.Messagebox('Please select the file then try to load','warn','Please browse the file')
        #self.quit()
    def Load_the_excel_file(self,filepath):
        ''' Load the Excel file in the path'''
        self.New_excel_data=pd.ExcelFile(filepath)
        self.Sheet_selector = QtWidgets.QDialog()
        self.Sheet_selector_cls = Ui_Sheet_selector(parent=self)
        self.Sheet_selector_cls.setupUi(self.Sheet_selector)
        self.Sheet_selector.exec_()
        print('reading_completed')
def Load_the_win():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Load_STDF11 = QtWidgets.QDialog()
    ui = Ui_Load_STDF()
    ui.setupUi(Load_STDF11)
    Load_STDF1.exec_()
    sys.exit(app.exec_())
if __name__ == '__main__':
    Load_the_win()