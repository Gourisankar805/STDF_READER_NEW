# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Merge_Tables_Window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from pandas import DataFrame as DF
class Ui_Insert_Rows(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(Ui_Insert_Rows,self).__init__()
        self.Parent_window=parent
    def setupUi(self, Insert_Rows):
        self.Insert_Rows_window=Insert_Rows
        Insert_Rows.setObjectName("Insert_Rows")
        Insert_Rows.resize(765, 307)
        Insert_Rows.setMinimumSize(QtCore.QSize(765, 134))
        Insert_Rows.setMaximumSize(QtCore.QSize(2000, 2000))
        Insert_Rows.setWindowTitle("Insert rows - Select Source")
        self.groupBox = QtWidgets.QGroupBox(Insert_Rows)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 746, 301))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(180, 50, 451, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.Add_rows_to_combo = QtWidgets.QComboBox(self.groupBox)
        self.Add_rows_to_combo.setGeometry(QtCore.QRect(140, 20, 601, 22))
        self.Add_rows_to_combo.setObjectName("comboBox")
        self.Add_rows_from_combo = QtWidgets.QComboBox(self.groupBox)
        self.Add_rows_from_combo.setGeometry(QtCore.QRect(640, 50, 101, 22))
        self.Add_rows_from_combo.setObjectName("comboBox_2")
        self.Add_rows_from_combo.currentIndexChanged.connect(self.select_the_from_table)
        self.Add_rows_from_combo.addItem("Select")
                
        #self.lineEdit.setText('gouri')
        self.Back_button = QtWidgets.QPushButton(self.groupBox)
        self.Back_button.setGeometry(QtCore.QRect(380, 270, 75, 23))
        self.Back_button.setObjectName("pushButton")
        self.Back_button.setText('Back')
        self.Back_button.setEnabled(False)
        self.Next_button = QtWidgets.QPushButton(self.groupBox)
        self.Next_button.setGeometry(QtCore.QRect(460, 270, 75, 23))
        self.Next_button.setObjectName("Next_button")
        self.Next_button.setText("Next")
        self.Next_button.setEnabled(False)
        #self.Next_button.clicked.connect(self.open_mismatched_columns_window)
        self.Finish_button = QtWidgets.QPushButton(self.groupBox)
        self.Finish_button.setGeometry(QtCore.QRect(550, 270, 75, 23))
        self.Finish_button.setObjectName("Finish_button")
        self.Finish_button.setText('Finish')
        self.Finish_button.clicked.connect(self.Get_the_File_names_to_merge)
        self.Cancel_button = QtWidgets.QPushButton(self.groupBox)
        self.Cancel_button.setGeometry(QtCore.QRect(640, 270, 75, 23))
        self.Cancel_button.setObjectName("Cancel_button")
        self.Cancel_button.setText("Cancel")
        self.Cancel_button.clicked.connect(self.Close_the_insert_row_window)
        self.Help_button = QtWidgets.QPushButton(self.groupBox)
        self.Help_button.setGeometry(QtCore.QRect(10, 270, 75, 23))
        self.Help_button.setObjectName("Help_button")
        self.Help_button.setText('Help')
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(10, 20, 121, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 131, 16))
        self.label_2.setObjectName("label_2")
        self.label.setText("Add rows to Data Table :")
        self.label_2.setText("Add rows from Data Table :")        
        QtCore.QMetaObject.connectSlotsByName(Insert_Rows)
        Insert_Rows.setTabOrder(self.Add_rows_to_combo, self.lineEdit)
        Insert_Rows.setTabOrder(self.lineEdit, self.Add_rows_from_combo)
        Insert_Rows.setTabOrder(self.Add_rows_from_combo, self.Help_button)
        Insert_Rows.setTabOrder(self.Help_button, self.Back_button)
        Insert_Rows.setTabOrder(self.Back_button, self.Next_button)
        Insert_Rows.setTabOrder(self.Next_button, self.Finish_button)
        Insert_Rows.setTabOrder(self.Finish_button, self.Cancel_button)
    def open_mismatched_columns_window(self):
        ''' Opens the mismatched data window '''
        self.Insert_Rows_window.hide()
        self.Mismatched_column_win = QtWidgets.QDialog()
        self.mismatched_col_window = Ui_Insert_Rows_Mismatched_column_window(self)
        self.mismatched_col_window.setupUi(self.Mismatched_column_win)
        #self.Mismatched_column_win.show()
        self.Mismatched_column_win.exec_()
    def Close_the_insert_row_window(self):
        '''Closes the insert rows window '''
        self.Insert_Rows_window.close()
    def Get_the_loaded_file_details(self):
        '''Gets the loaded file data into this window'''
        if self.Parent_window!=None:
            for i in self.Parent_window.Loaded_Data_Files.keys():                
                self.Add_rows_to_combo.addItem(i)
                self.Add_rows_from_combo.addItem(i)
            if len(self.Parent_window.Loaded_Data_Files)>0: self.Add_rows_to_combo.setCurrentIndex(0)
            #self.File1=self.Add_rows_to_combo.currentText()
            #print('ff')
    def select_the_from_table(self):
        ''' Select the Data loaded from table'''
        txt=self.Add_rows_from_combo.currentText()
        self.lineEdit.setText(txt)
        #print('came')
    def Get_the_File_names_to_merge(self):
        ''' Takes the input from both the files and covert into data frame for further operations.  '''
        self.New_File_Name,self.Ok_pressed=QtWidgets.QInputDialog.getText(self,'Rename Table','Enter the New name',QtWidgets.QLineEdit.Normal,'')
        if self.Parent_window!=None and self.Ok_pressed==True and self.New_File_Name !='' :
            self.File1=self.Add_rows_to_combo.currentText()
            self.File2=self.lineEdit.text()            
            self.File1_DF=DF(self.Parent_window.Loaded_Data_File_Raw_Data[self.File1])
            if self.File2!="" and self.File2!='Select': self.File2_DF=DF(self.Parent_window.Loaded_Data_File_Raw_Data[self.File2])
            if self.File1_DF.empty==False and self.File2_DF.empty==False:
                Temp_file=self.Merge_the_data_frames(self.File1_DF,self.File2_DF)
                # Converting the DF to Dict for use
                Temp_file1={}
                for name in Temp_file.columns:  Temp_file1[name]=list(Temp_file[name])
                self.Parent_window.Loaded_Data_Files[self.New_File_Name]={'Full_Rec_Summary':Temp_file1}
                self.Parent_window.Loaded_Data_File_count.append(self.New_File_Name)
                self.Parent_window.Loaded_Data_File_Raw_Data[self.New_File_Name]=DF(Temp_file1)     
                self.Parent_window.Refresh_data_table_items()   
                self.Close_the_insert_row_window()
        elif self.Ok_pressed==True and self.New_File_Name =='' :
            self.Parent_window.Messagebox('Enter the file name','info','Please enter the name')
    def Merge_the_data_frames(self,File1,File2):
        New_Data_with_merged=''
        if len(File1.columns.difference(File2.columns))==0:
            New_Data_with_merged=pd.concat([File1,File2])
            print( 'Merging completed')
        elif len(File1.columns.difference(File2.columns))!=0:
            unmatched_column_names=File1.columns.difference(File2.columns)
            print('There are %s unmatching columns are there. Unmatched column names in the file shown below'%len(unmatched_column_names))
            for i in range(len(unmatched_column_names)): print(unmatched_column_names[i])
            Still_want_to_merge_both_the_files=QtWidgets.QMessageBox.question(self,'merge','The 2 inputs don"t have some columns matching you still want to proceed',QMessageBox.Yes | QMessageBox.No ,QMessageBox.Yes)       
            if Still_want_to_merge_both_the_files==QtWidgets.QMessageBox.Yes:
                New_Data_with_merged=pd.concat([File1,File2])
                print( 'Merging completed')
            elif Still_want_to_merge_both_the_files==QtWidgets.QMessageBox.No:
                print(" Merging of the 2 files was unsucessful :-( , Please try again")            
            else:
                print(' Please give a valid input')
        return New_Data_with_merged
    
class Ui_Insert_Rows_Mismatched_column_window(QtWidgets.QDialog):
    def __init__(self,parent=None):
        super(Ui_Insert_Rows_Mismatched_column_window,self).__init__()
        self.Parent_window=parent
        
    def setupUi(self, Form):
        self.Insert_Mismatched_column_window=Form
        Form.setObjectName("Form")
        Form.resize(746, 307)
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(10, 30, 731, 191))
        self.listView.setObjectName("listView")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 141, 16))
        self.label.setObjectName("label")
        self.Back_button = QtWidgets.QPushButton(Form)
        self.Back_button.setGeometry(QtCore.QRect(400, 270, 75, 23))
        self.Back_button.setObjectName("pushButton")
        self.Back_button.clicked.connect(self.Open_Insert_rows_window)
        self.Finish_button = QtWidgets.QPushButton(Form)
        self.Finish_button.setGeometry(QtCore.QRect(570, 270, 75, 23))
        self.Finish_button.setObjectName("Finish_button")
        self.Next_button = QtWidgets.QPushButton(Form)
        self.Next_button.setGeometry(QtCore.QRect(480, 270, 75, 23))
        self.Next_button.setObjectName("Next_button")
        self.Help_button = QtWidgets.QPushButton(Form)
        self.Help_button.setGeometry(QtCore.QRect(30, 270, 75, 23))
        self.Help_button.setObjectName("Help_button")
        self.Cancel_button = QtWidgets.QPushButton(Form)
        self.Cancel_button.setGeometry(QtCore.QRect(660, 270, 75, 23))
        self.Cancel_button.setObjectName("Cancel_button")
        self.Cancel_button.clicked.connect(self.Close_the_Insert_Mismatched_column_window)
        self.Clear_All_button = QtWidgets.QPushButton(Form)
        self.Clear_All_button.setGeometry(QtCore.QRect(660, 230, 75, 23))
        self.Clear_All_button.setObjectName("Clear_All_button")
        self.Select_All_button = QtWidgets.QPushButton(Form)
        self.Select_All_button.setGeometry(QtCore.QRect(580, 230, 75, 23))
        self.Select_All_button.setObjectName("Select_All_button")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Insert rows - Mismatached columns"))
        self.label.setText(_translate("Form", "Mismatched columns names:"))
        self.Back_button.setText(_translate("Form", "Back"))
        self.Finish_button.setText(_translate("Form", "Finish"))
        self.Next_button.setText(_translate("Form", "Next"))
        self.Help_button.setText(_translate("Form", "Help"))
        self.Cancel_button.setText(_translate("Form", "Cancel"))
        self.Clear_All_button.setText(_translate("Form", "Clear All"))
        self.Select_All_button.setText(_translate("Form", "Select All"))
    def Open_Insert_rows_window(self):
        ''' Opens the insert rows window'''
        self.Insert_Mismatched_column_window.close()
        self.Parent_window.Insert_Rows_window.show()
        #self.Insert_Rows_window.show()
    def Close_the_Insert_Mismatched_column_window(self):

        '''Closes the insert rows window '''
        if self.Parent_window!=None: self.Parent_window.close()
        self.Insert_Mismatched_column_window.close()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Insert_Rows = QtWidgets.QWidget()
    ui = Ui_Insert_Rows()
    ui.setupUi(Insert_Rows)
    Insert_Rows.show()
    sys.exit(app.exec_())

