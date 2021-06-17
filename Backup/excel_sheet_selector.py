from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QAbstractTableModel, Qt
import pandas as pd
from pandas import DataFrame as DF
class table_view_model(QAbstractTableModel):

    def __init__(self, data):
        QAbstractTableModel.__init__(self)
        self._data = data

    def rowCount(self, parent=None):
        return self._data.shape[0]

    def columnCount(self, parnet=None):
        return self._data.shape[1]

    def data(self, index, role=Qt.DisplayRole):
        if index.isValid():
            if role == Qt.DisplayRole:
                return str(self._data.iloc[index.row(), index.column()])
        return None

    def headerData(self, col, orientation, role):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return self._data.columns[col]
        return None

class Ui_Sheet_selector(object):
    '''Sheet selector takes the work book name as input and allows the user to select the require sheet he is lookin to add in the tool'''
    def __init__(self,parent=None):
        super(Ui_Sheet_selector,self).__init__()
        self.File_name=""
        self.Parent_window=parent
    def setupUi(self, Sheet_selector):
        self.Sheet_selector1=Sheet_selector
        Sheet_selector.setObjectName("Sheet_selector")
        Sheet_selector.resize(655, 300)
        Sheet_selector.setMaximumSize(QtCore.QSize(655, 300))
        self.groupBox = QtWidgets.QGroupBox(Sheet_selector)
        self.groupBox.setGeometry(QtCore.QRect(0, 3, 651, 291))
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle("Select_the_sheet")
        self.File_name_viewer = QtWidgets.QLineEdit(self.groupBox)
        self.File_name_viewer.setGeometry(QtCore.QRect(10, 20, 521, 21))
        self.File_name_viewer.setInputMask("")
        self.File_name_viewer.setObjectName("File_name_viewer")
        self.Excel_Data_Viewer = QtWidgets.QTableView(self.groupBox)
        self.Excel_Data_Viewer.setGeometry(QtCore.QRect(10, 80, 635, 205)) 
        #self.File_name_viewer.isEnabled(False)
        self.Sheet_names_selector_combo = QtWidgets.QComboBox(self.groupBox)
        self.Sheet_names_selector_combo.setGeometry(QtCore.QRect(10, 50, 521, 21))
        self.Sheet_names_selector_combo.setObjectName("Sheet_names_selector_combo")
        self.Sheet_names_selector_combo.currentTextChanged.connect(self.Show_the_few_data_in_data_table)
        if self.Parent_window!=None:
            self.File_name_viewer.setText(self.Parent_window.File_name)
            self.File_name_viewer.setDisabled(True)
            if len(self.Parent_window.New_excel_data.sheet_names)>0:
                for sheet_name in self.Parent_window.New_excel_data.sheet_names:
                    self.Sheet_names_selector_combo.addItem(sheet_name)
                self.Show_the_few_data_in_data_table()
        self.Ok_buttion = QtWidgets.QPushButton(self.groupBox)
        self.Ok_buttion.setGeometry(QtCore.QRect(540, 50, 75, 23))
        self.Ok_buttion.clicked.connect(self.Create_the_data_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Ok_buttion.sizePolicy().hasHeightForWidth())
        self.Ok_buttion.setSizePolicy(sizePolicy)
        self.Ok_buttion.setObjectName("Ok_buttion")
        self.Ok_buttion.setText('Ok')        
        QtCore.QMetaObject.connectSlotsByName(Sheet_selector)
    def Show_the_few_data_in_data_table(self):
        ''' This function takes the work book sheet name ( Data frame) as input and shows the first few rows(5) in the Table Widget'''
        if self.Sheet_names_selector_combo.currentText()!="":
            sheetname=self.Parent_window.New_excel_data.parse(sheetname=self.Sheet_names_selector_combo.currentText())             
            self.modle=table_view_model(sheetname)                       
            self.Excel_Data_Viewer.setModel(self.modle)
            self.Excel_Data_Viewer.show()
    def Create_the_data_frame(self):
        ''' This Function takes the sheet name from the excel file'''
        if self.Sheet_names_selector_combo.currentText()!="":
            #self.Parent_window.Loaded=self.Parent_window.New_excel_data.parse(sheetname=self.Sheet_names_selector_combo.currentText())
            self.Parent_window.Parent_window.Loaded_Data_File_count.append('File_'+str(len(self.Parent_window.Parent_window.Loaded_Data_File_count)+1))
            self.New_File_Name=self.Parent_window.Parent_window.Loaded_Data_File_count[len(self.Parent_window.Parent_window.Loaded_Data_File_count)-1]
            Temp_file=self.Parent_window.New_excel_data.parse(sheetname=self.Sheet_names_selector_combo.currentText())
            # Converting the DF to Dict for use
            Temp_file1={}
            for name in Temp_file.columns:  Temp_file1[name]=list(Temp_file[name])
            self.Parent_window.Parent_window.Loaded_Data_Files[self.New_File_Name]={'Full_Rec_Summary':Temp_file1}            
            self.Parent_window.Parent_window.Loaded_Data_File_Raw_Data[self.New_File_Name]=DF(Temp_file1)
            #self.Parent_window.Parent_window.Refresh_data_table_items()   
            self.Close_the_excel_sheet_selector()
    def Close_the_excel_sheet_selector(self):
        '''  Closes the current window excel sheet selector'''
        self.Sheet_selector1.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Sheet_selector = QtWidgets.QDialog()
    ui = Ui_Sheet_selector()
    ui.setupUi(Sheet_selector)
    Sheet_selector.show()
    sys.exit(app.exec_())

