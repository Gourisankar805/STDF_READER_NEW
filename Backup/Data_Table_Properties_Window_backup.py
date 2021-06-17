# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Data_Table_Properties_Window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Data_Table_Properties_Window(QtWidgets.QDialog):
    def __init__(self,ParentWindow=None):
        super(Ui_Data_Table_Properties_Window,self).__init__()
        self.Parent_window=ParentWindow
    def setupUi(self, Data_Table_Properties_Window):
        global Data_Table_properties_win
        self.Data_Table_properties_win=Data_Table_Properties_Window
        Data_Table_Properties_Window.setObjectName("Data_Table_Properties_Window")
        Data_Table_Properties_Window.resize(659, 210)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Data_Table_Properties_Window.sizePolicy().hasHeightForWidth())
        Data_Table_Properties_Window.setSizePolicy(sizePolicy)
        Data_Table_Properties_Window.setMaximumSize(QtCore.QSize(659, 210))
        self.groupBox_2 = QtWidgets.QGroupBox(Data_Table_Properties_Window)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 641, 201))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.Data_Table_List = QtWidgets.QListWidget(self.groupBox_2)
        self.Data_Table_List.setGeometry(QtCore.QRect(10, 20, 501, 171))
        self.Data_Table_List.setObjectName("Data_Table_List")
        self.groupBox = QtWidgets.QGroupBox(self.groupBox_2)
        self.groupBox.setGeometry(QtCore.QRect(520, 20, 111, 170))
        self.groupBox.setMaximumSize(QtCore.QSize(111, 170))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setGeometry(QtCore.QRect(10, 10, 90, 23))
        self.pushButton.setObjectName("pushButton")
        self.Delete_button = QtWidgets.QPushButton(self.groupBox)
        self.Delete_button.setGeometry(QtCore.QRect(10, 70, 90, 23))
        self.Delete_button.setObjectName("Delete")
        self.Delete_button.setText("Delete")
        self.Delete_button.clicked.connect(self.Delete_the_data_item_in_data_table)
        self.pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 100, 90, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.Close_button = QtWidgets.QPushButton(self.groupBox)
        self.Close_button.setGeometry(QtCore.QRect(10, 130, 90, 23))
        self.Close_button.setObjectName("Close")
        self.Close_button.setText("Close")
        self.Close_button.clicked.connect(self.clsoe_the_window)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(10, 40, 90, 23))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Data_Table_Properties_Window)
        QtCore.QMetaObject.connectSlotsByName(Data_Table_Properties_Window)

    def retranslateUi(self, Data_Table_Properties_Window):
        _translate = QtCore.QCoreApplication.translate
        Data_Table_Properties_Window.setWindowTitle(_translate("Data_Table_Properties_Window", "Data Table Properties"))
        self.groupBox_2.setTitle(_translate("Data_Table_Properties_Window", "Data Tables"))
        self.pushButton.setText(_translate("Data_Table_Properties_Window", "Rename"))
        #self.pushButton_3.setText(_translate("Data_Table_Properties_Window", "Delete"))
        self.pushButton_4.setText(_translate("Data_Table_Properties_Window", "Set As Default"))
        self.comboBox.setItemText(0, _translate("Data_Table_Properties_Window", "Refresh Data"))
        self.comboBox.setItemText(1, _translate("Data_Table_Properties_Window", "With Prompt"))
        self.comboBox.setItemText(2, _translate("Data_Table_Properties_Window", "With out Prompt"))
    def clsoe_the_window(self):
        ''' closes the Window '''
        self.Data_Table_properties_win.close()
    
    def Add_Loaded_Data_into_list_box(self,Dict_object):
        '''Shows the Loaded data table name'''
        global Data_table_dict
        Data_table_dict=Dict_object
        for i in Dict_object.keys():
            self.Data_Table_List.addItem(i)
    def Delete_the_data_item_in_data_table(self):
        '''Delets the selected Items from the list box and from the original file also , the is from the data base.  If you delete the file it will be delete permanently you can't even undo it '''
        self.Title='Delete the Data table'
        self.Msg='Are you sure want to delete the Data table' +self.Data_Table_List.currentItem().text()
        self.Reply=self.Parent_window.Messagebox(self.Msg,'que',self.Title)
        if self.Reply==QtWidgets.QMessageBox.Yes:
            self.temp=self.Parent_window.Loaded_Data_Files.pop(self.Data_Table_List.currentItem().text())
            self.Parent_window.Loaded_Data_File_count.remove(self.Data_Table_List.currentItem().text())
            self.Data_Table_List.takeItem(self.Data_Table_List.currentRow())
            print('%s Deleted from the data base' %(self.Data_Table_List.currentItem().text()))
        elif self.Reply==QtWidgets.QMessageBox.No:
            pass
        

        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Data_Table_Properties_Window = QtWidgets.QDialog()
    ui = Ui_Data_Table_Properties_Window()
    ui.setupUi(Data_Table_Properties_Window)
    Data_Table_Properties_Window.show()
    sys.exit(app.exec_())

