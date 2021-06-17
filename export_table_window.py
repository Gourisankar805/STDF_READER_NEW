
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from pandas import DataFrame as DF
class Ui_Export_Table_Window(object):
    def __init__(self, parent=None):
        super(Ui_Export_Table_Window).__init__()
        self.Parent_window=parent
    def setupUi(self, Export_Table_Window):
        self.Export_Table_Window=Export_Table_Window
        Export_Table_Window.setObjectName("Export_Table_Window")
        Export_Table_Window.setWindowModality(QtCore.Qt.ApplicationModal)
        
        Export_Table_Window.resize(412, 118)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Export_Table_Window.sizePolicy().hasHeightForWidth())
        Export_Table_Window.setSizePolicy(sizePolicy)
        Export_Table_Window.setMaximumSize(QtCore.QSize(420, 133))
        Export_Table_Window.setMouseTracking(True)
        #Export_Table_Window.setTabletTracking(True)
        Export_Table_Window.setWindowTitle('Export_Table_Window')
        self.groupBox = QtWidgets.QGroupBox(Export_Table_Window)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 391, 101))
        self.groupBox.setMouseTracking(False)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setTitle('Data Tables')
        self.Loaded_File_List_Combo = QtWidgets.QComboBox(self.groupBox)
        self.Loaded_File_List_Combo.setGeometry(QtCore.QRect(10, 20, 371, 21))
        self.Loaded_File_List_Combo.setObjectName("Loaded_File_List_Combo")
        #self.comboBox.addItem("Items")
        self.Ok_button = QtWidgets.QPushButton(self.groupBox)
        self.Ok_button.setGeometry(QtCore.QRect(210, 60, 75, 23))
        self.Ok_button.setObjectName("Ok_button")
        self.Ok_button.setText("Ok")
        self.Ok_button.clicked.connect(self.Export_Table_okay)
        self.Help = QtWidgets.QPushButton(self.groupBox)
        self.Help.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.Help.setObjectName("Help")
        self.Help.setText('Help')
        self.Cancel_button = QtWidgets.QPushButton(self.groupBox)
        self.Cancel_button.setGeometry(QtCore.QRect(300, 60, 75, 23))
        self.Cancel_button.setObjectName("Cancel_button")
        self.Cancel_button.setText('Cancel')
        self.Cancel_button.clicked.connect(self.Close_Export_Window)        
        QtCore.QMetaObject.connectSlotsByName(Export_Table_Window)

    def Close_Export_Window(self):
        ''' Used to close the open current Export Table Window'''
        self.Export_Table_Window.close()
    def Add_Loaded_Tables_Data(self):
        '''  Add Loaded Tables Data Function works only if there is a Parent window assgined to this Export TAble 
        Window.  It is Designed to take the data from the table we loaded in the tool and access the the names of it'''
        if self.Parent_window!=None:
            for i in self.Parent_window.Loaded_Data_Files.keys():                
                self.Loaded_File_List_Combo.addItem(i)#+'\t'+self.Parent_window.Loaded_Data_Files[i]['FAR_Rec_summary']['File_Name'][0])
    def Export_Table_okay(self):
        '''Opens the save file windows and Save / Export the data into csv and Excel'''
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, sav_type = QFileDialog.getSaveFileName(caption='Export file',directory='',filter="CSV File (*.csv);;Excel File (*.xls *.xlsx);;Text File (*.txt)", options=options) #;;All Files (*.*)
        if fileName and self.Parent_window!=None:
            self.Data=DF(self.Parent_window.Loaded_Data_File_Raw_Data[self.Loaded_File_List_Combo.currentText()])            
            if sav_type=='CSV File (*.csv)':
                self.Data.to_csv(fileName+'.csv',index=False)                
            elif sav_type=='Excel File (*.xls *.xlsx)':
                self.Data.to_excel(fileName+'.xlsx',index=False)                
            elif sav_type=='Text File (*.txt)':
                self.Data.to_csv(fileName+'.txt', header=True, index=None,sep='\t')                
            try:
                self.Limit_file=DF(self.Parent_window.Loaded_Data_Files[self.Loaded_File_List_Combo.currentText()]['Test_Limit_Details'])
                if sav_type=='CSV File (*.csv)':               
                    self.Limit_file.to_csv(fileName+'_Limits'+'.csv',index=False)
                elif sav_type=='Excel File (*.xls *.xlsx)':                
                    self.Limit_file.to_excel(fileName+'_Limits'+'.xlsx',index=False)
                elif sav_type=='Text File (*.txt)':
                    self.Limit_file.to_csv(fileName+'_Limits'+'.txt', header=True, index=None,sep='\t')
            except:
                pass
        self.Close_Export_Window()
            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Export_Table_Window = QtWidgets.QWidget()
    ui = Ui_Export_Table_Window()
    ui.setupUi(Export_Table_Window)
    Export_Table_Window.show()
    sys.exit(app.exec_())

