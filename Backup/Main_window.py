
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QInputDialog,QFileDialog,QMessageBox,QWidget,QMainWindow,QDialog,QTabWidget,QSizePolicy,QTableWidget,QHBoxLayout,QGridLayout,QTableWidgetItem,QDesktopWidget,QVBoxLayout)
from PyQt5.QtGui import QIcon,QMoveEvent
from PyQt5.QtCore import QAbstractTableModel, Qt
from pandas import DataFrame as DF
import os,sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import random
from load_stdf import Ui_Load_STDF
from data_table_properties_window import Ui_Data_Table_Properties_Window
from export_table_window import Ui_Export_Table_Window
from merge_tables_window import Ui_Insert_Rows,Ui_Insert_Rows_Mismatched_column_window
from select_items_to_plot_window import Ui_Selected_items_to_plot
from yield_report_generation_window import Ui_Yiled_Report_Generation_form

class table_view_model(QAbstractTableModel):
    ''' This function takes the data frame as input and converts the data frame into QTable Model. '''
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

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super(Ui_MainWindow,self).__init__()
        self.setMouseTracking(True)
        #self.set
        self.Loaded_Data_Files={}
        self.Loaded_Data_File_count=[]
        self.Loaded_Data_File_Raw_Data={}
        self.File_Path=[]
        #self.Imported_file_data=[]
        self.Tab_List=[]
        self.Tab_Names=[]
        self.Table_List=[]
        self.File_Table_List={}
        self.Gridlayout_list_pertab={}
        self.Parametric_Summary_Table_count=0
        self.Cancel_buttion_clicked_in_plot_generation=False
    def setupUi(self, MainWindow):
        #global Main_Window
        #QMainWindow.__init__(self)
        self.Main_Window=MainWindow
        self.Main_Window.setObjectName("MainWindow")
        self.Main_Window.setWindowModality(QtCore.Qt.ApplicationModal)
        self.screen = QtWidgets.QDesktopWidget().screenGeometry(0)
        self.Main_Window.resize(self.screen.width(), self.screen.height())        
        self.Main_Window.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(self.Main_Window)
        self.centralwidget.setObjectName("centralwidget")
        # Loaded File list combo box
        self.Loaded_File_List_Combo = QtWidgets.QComboBox(self.centralwidget)
        self.Loaded_File_List_Combo.setGeometry(QtCore.QRect(self.screen.width()-100, 0, 100, 20))
        self.Loaded_File_List_Combo.setObjectName("Loaded_File_List_Combo")
        #self.Loaded_File_List_Combo.currentIndexChanged.connect(self.Change_the_data_table_in_the_current_tab)
        #Tab
        self.tabWidget = QtWidgets.QTabWidget(self.Main_Window)
        self.tabWidget.setGeometry(QtCore.QRect(35, 55,self.screen.width()-150, self.screen.height()-100))#, 1380, 900
        self.tabWidget.setSizePolicy(QSizePolicy.Expanding,QSizePolicy.Expanding)
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.tabCloseRequested.connect(self.CloseTab)
        self.Add_Tab_button_plus=QtWidgets.QToolButton()
        self.Add_Tab_button_plus.setText("+")
        self.tabWidget.setCornerWidget(self.Add_Tab_button_plus,QtCore.Qt.TopLeftCorner)
        self.Add_Tab_button_plus1=QtWidgets.QToolButton()        
        self.Add_Tab_button_plus1.setText("+")
        self.tabWidget.setCornerWidget(self.Add_Tab_button_plus1,QtCore.Qt.TopRightCorner)
        self.Add_Tab_button_plus.clicked.connect(self.Add_Tab)
        self.Add_Tab_button_plus1.clicked.connect(self.Add_Tab)
        
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setObjectName("tabWidget")

        self.dummy_table = QtWidgets.QTableView()
        self.Add_Tool_Bar()
        self.Menu_bar()

       
        #self.Add_Table()
        #self.Dummy_table_fun()
    def Menu_bar(self):
        self.Main_Window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(self.Main_Window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1531, 21))
        self.menubar.setObjectName("menubar")
        self.File = QtWidgets.QMenu(self.menubar)
        self.File.setObjectName("File")
        ## Export Button
        #self.Export = QtWidgets.QMenu(self.File)
        self.Export = QtWidgets.QAction(self.Main_Window)
        self.Export.setObjectName("Export")
        self.Export.triggered.connect(self.Open_Export_Window)
        self.Export.setText('Export')
        self.Export.setShortcut('Ctrl+E')
        # Open From 
        self.Open_From = QtWidgets.QAction(self.File)
        self.Open_From.setObjectName("Open_From")
        self.Open_From.triggered.connect(self.Open_Load_Action)
        self.Open_From.setText('Open_From')
        self.Open_From.setShortcut('Ctrl+O')
        self.Menu = QtWidgets.QMenu(self.menubar)
        self.Menu.setObjectName("Menu")
        self.MarkedRows = QtWidgets.QMenu(self.Menu)
        self.MarkedRows.setObjectName("MarkedRows")
        self.Copy_Special = QtWidgets.QMenu(self.Menu)
        self.Copy_Special.setObjectName("Copy_Special")
        self.Paste_Special = QtWidgets.QMenu(self.Menu)
        self.Paste_Special.setObjectName("Paste_Special")
        self.View = QtWidgets.QMenu(self.menubar)
        self.View.setObjectName("View")
        self.Help = QtWidgets.QMenu(self.menubar)
        self.Help.setObjectName("Help")
        self.Insert = QtWidgets.QMenu(self.menubar)
        self.Insert.setObjectName("Insert")
        self.Tools = QtWidgets.QMenu(self.menubar)
        self.Tools.setObjectName("Tools")
        self.Analysis = QtWidgets.QMenu(self.Tools)
        self.Analysis.setObjectName("Analysis")
        self.Main_Window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(self.Main_Window)
        self.statusbar.setObjectName("statusbar")
        self.Main_Window.setStatusBar(self.statusbar)
        #ACtions
        self.actionLoad = QtWidgets.QAction(self.Main_Window)
        self.actionLoad.setObjectName("actionLoad")
        self.actionSave = QtWidgets.QAction(self.Main_Window)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(self.Main_Window)
        self.actionSave_As.setObjectName("actionSave_As")
        # Exit
        self.Exit_btn = QtWidgets.QAction(self.Main_Window)
        self.Exit_btn.setObjectName("Exit")
        self.Exit_btn.triggered.connect(self.Exit)
        self.Exit_btn.setShortcut("Ctrl+Q")
        self.Exit_btn.setText('Exit')
        self.actionOpen = QtWidgets.QAction(self.Main_Window)
        self.actionOpen.setObjectName("actionOpen")        
        self.actionUndo = QtWidgets.QAction(self.Main_Window)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(self.Main_Window)
        self.actionRedo.setObjectName("actionRedo")
        self.actionCopy = QtWidgets.QAction(self.Main_Window)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(self.Main_Window)
        self.actionPaste.setObjectName("actionPaste")
        self.actionDelete_Active_Page = QtWidgets.QAction(self.Main_Window)
        self.actionDelete_Active_Page.setObjectName("actionDelete_Active_Page")
        self.actionReset_AllFilters = QtWidgets.QAction(self.Main_Window)
        self.actionReset_AllFilters.setObjectName("actionReset_AllFilters")
        self.actionMark_Filtered_Rows = QtWidgets.QAction(self.Main_Window)
        self.actionMark_Filtered_Rows.setObjectName("actionMark_Filtered_Rows")
        self.actionUnmark = QtWidgets.QAction(self.Main_Window)
        self.actionUnmark.setObjectName("actionUnmark")
        self.actionInvert = QtWidgets.QAction(self.Main_Window)
        self.actionInvert.setObjectName("actionInvert")
        self.actionDelete = QtWidgets.QAction(self.Main_Window)
        self.actionDelete.setObjectName("actionDelete")
        self.actionFilter_To = QtWidgets.QAction(self.Main_Window)
        self.actionFilter_To.setObjectName("actionFilter_To")
        self.actionFilter_Out = QtWidgets.QAction(self.Main_Window)
        self.actionFilter_Out.setObjectName("actionFilter_Out")
        self.actionAdd_Marked_to_List = QtWidgets.QAction(self.Main_Window)
        self.actionAdd_Marked_to_List.setObjectName("actionAdd_Marked_to_List")
        self.actionNew_List_from_Marked = QtWidgets.QAction(self.Main_Window)
        self.actionNew_List_from_Marked.setObjectName("actionNew_List_from_Marked")
        self.actionRemove_Marked_From_List = QtWidgets.QAction(self.Main_Window)
        self.actionRemove_Marked_From_List.setObjectName("actionRemove_Marked_From_List")
        self.actionSerach_Marked_in_List = QtWidgets.QAction(self.Main_Window)
        self.actionSerach_Marked_in_List.setObjectName("actionSerach_Marked_in_List")
        self.actionData_for_All_Items = QtWidgets.QAction(self.Main_Window)
        self.actionData_for_All_Items.setObjectName("actionData_for_All_Items")
        self.actionData_for_Marked_Rows = QtWidgets.QAction(self.Main_Window)
        self.actionData_for_Marked_Rows.setObjectName("actionData_for_Marked_Rows")
        self.actionAll_Rows = QtWidgets.QAction(self.Main_Window)
        self.actionAll_Rows.setObjectName("actionAll_Rows")
        self.actionFiltered_Rows = QtWidgets.QAction(self.Main_Window)
        self.actionFiltered_Rows.setObjectName("actionFiltered_Rows")
        self.actionMarked_Rows = QtWidgets.QAction(self.Main_Window)
        self.actionMarked_Rows.setObjectName("actionMarked_Rows")
        self.actionActive_Page = QtWidgets.QAction(self.Main_Window)
        self.actionActive_Page.setObjectName("actionActive_Page")
        self.actionActive_Visualisation = QtWidgets.QAction(self.Main_Window)
        self.actionActive_Visualisation.setObjectName("actionActive_Visualisation")
        self.actionActive_Visualization_Image = QtWidgets.QAction(self.Main_Window)
        self.actionActive_Visualization_Image.setObjectName("actionActive_Visualization_Image")
        self.actionShow_Import_Settings = QtWidgets.QAction(self.Main_Window)
        self.actionShow_Import_Settings.setObjectName("actionShow_Import_Settings")
        self.actionAs_New_Columns = QtWidgets.QAction(self.Main_Window)
        self.actionAs_New_Columns.setObjectName("actionAs_New_Columns")
        self.actionAs_New_Rows = QtWidgets.QAction(self.Main_Window)
        self.actionAs_New_Rows.setObjectName("actionAs_New_Rows")
        self.actionReset_All_Marking = QtWidgets.QAction(self.Main_Window)
        self.actionReset_All_Marking.setObjectName("actionReset_All_Marking")
        self.actionData_Connection_Properties = QtWidgets.QAction(self.Main_Window)
        self.actionData_Connection_Properties.setObjectName("actionData_Connection_Properties")
        self.actionData_Table_Properties = QtWidgets.QAction(self.Main_Window)
        self.actionData_Table_Properties.setObjectName("actionData_Table_Properties")
        self.actionData_Table_Properties.triggered.connect(self.Open_Data_Table_properties_window)
        self.actionColumn_Properties = QtWidgets.QAction(self.Main_Window)
        self.actionColumn_Properties.setObjectName("actionColumn_Properties")
        self.actionDocument_Properties = QtWidgets.QAction(self.Main_Window)
        self.actionDocument_Properties.setObjectName("actionDocument_Properties")
        self.actionData_Function_Properties = QtWidgets.QAction(self.Main_Window)
        self.actionData_Function_Properties.setObjectName("actionData_Function_Properties")
        self.actionFilters = QtWidgets.QAction(self.Main_Window)
        self.actionFilters.setObjectName("actionFilters")
        self.actionData = QtWidgets.QAction(self.Main_Window)
        self.actionData.setObjectName("actionData")
        #Add Data_Table 
        self.Data_Table = QtWidgets.QAction("Data_Table",self.Main_Window)
        self.Data_Table.setObjectName("Data_Table")
        self.Data_Table.triggered.connect(self.Add_Table)
        #Add New_Page/New_Tab
        self.New_Page = QtWidgets.QAction(self.Main_Window)
        self.New_Page.setObjectName("New_Page")
        self.New_Page.triggered.connect(self.Add_Tab)
        self.actionDuplicate_Activate_Page = QtWidgets.QAction(self.Main_Window)
        self.actionDuplicate_Activate_Page.setObjectName("actionDuplicate_Activate_Page")
        self.actionCalculated_Column = QtWidgets.QAction(self.Main_Window)
        self.actionCalculated_Column.setObjectName("actionCalculated_Column")
        self.actionColumns = QtWidgets.QAction(self.Main_Window)
        self.actionColumns.setObjectName("actionColumns")
        #  Inserting Rows / Merging Rows
        self.actionRows = QtWidgets.QAction(self.Main_Window)
        self.actionRows.setObjectName("actionRows")
        self.actionRows.triggered.connect(self.Open_Insert_Rows_window)
        self.actionFind = QtWidgets.QAction(self.Main_Window)
        self.actionFind.setObjectName("actionFind")
        self.actionTest_Summary_Report_TSR_Chart_Galliers = QtWidgets.QAction(self.Main_Window)
        self.actionTest_Summary_Report_TSR_Chart_Galliers.setObjectName("actionTest_Summary_Report_TSR_Chart_Galliers")
        self.actionAnalysis_of_Varicance = QtWidgets.QAction(self.Main_Window)
        self.actionAnalysis_of_Varicance.setObjectName("actionAnalysis_of_Varicance")
        self.actionMeasuement_System_Comparision_MSC_Analysis = QtWidgets.QAction(self.Main_Window)
        self.actionMeasuement_System_Comparision_MSC_Analysis.setObjectName("actionMeasuement_System_Comparision_MSC_Analysis")
        self.actionSPC_Statistical_Process_Controll = QtWidgets.QAction(self.Main_Window)
        self.actionSPC_Statistical_Process_Controll.setObjectName("actionSPC_Statistical_Process_Controll")
        self.Yield_report = QtWidgets.QAction(self.Main_Window)
        self.Yield_report.setObjectName("Yield_Report")
        self.actionFrequency_Pareto = QtWidgets.QAction(self.Main_Window)
        self.actionFrequency_Pareto.setObjectName("actionFrequency_Pareto")
        self.actionClose = QtWidgets.QAction(self.Main_Window)
        self.actionClose.setObjectName("actionClose")
        self.actionAdd_Data_Table = QtWidgets.QAction(self.Main_Window)
        self.actionAdd_Data_Table.setObjectName("actionAdd_Data_Table")
        self.actionReplae_Data_Table = QtWidgets.QAction(self.Main_Window)
        self.actionReplae_Data_Table.setObjectName("actionReplae_Data_Table")
        # Export Items
        self.actionData_to_Excel = QtWidgets.QAction(self.Main_Window)
        self.actionData_to_Excel.setObjectName("actionData_to_Excel")
        self.actionData_CSV = QtWidgets.QAction(self.Main_Window)
        self.actionData_CSV.setObjectName("actionData_CSV")
        self.actionData_to_Text = QtWidgets.QAction(self.Main_Window)
        self.actionData_to_Text.setObjectName("actionData_to_Text")
        #Load Items
        
        self.File.addAction(self.actionOpen)
        self.File.addAction(self.Open_From)
        self.File.addSeparator()
        self.File.addAction(self.actionSave)
        self.File.addAction(self.actionSave_As)
        self.File.addAction(self.actionAdd_Data_Table)
        self.File.addAction(self.actionReplae_Data_Table)
        self.File.addSeparator()
        self.File.addAction(self.Export)#
        self.File.addSeparator()
        self.File.addAction(self.Exit_btn)
        self.MarkedRows.addAction(self.actionUnmark)
        self.MarkedRows.addAction(self.actionInvert)
        self.MarkedRows.addAction(self.actionDelete)
        self.MarkedRows.addAction(self.actionFilter_To)
        self.MarkedRows.addAction(self.actionFilter_Out)
        self.MarkedRows.addSeparator()
        self.MarkedRows.addAction(self.actionAdd_Marked_to_List)
        self.MarkedRows.addAction(self.actionNew_List_from_Marked)
        self.MarkedRows.addAction(self.actionRemove_Marked_From_List)
        self.MarkedRows.addAction(self.actionSerach_Marked_in_List)
        self.Copy_Special.addAction(self.actionData_for_All_Items)
        self.Copy_Special.addAction(self.actionData_for_Marked_Rows)
        self.Copy_Special.addSeparator()
        self.Copy_Special.addAction(self.actionAll_Rows)
        self.Copy_Special.addAction(self.actionFiltered_Rows)
        self.Copy_Special.addAction(self.actionMarked_Rows)
        self.Copy_Special.addSeparator()
        self.Copy_Special.addAction(self.actionActive_Page)
        self.Copy_Special.addAction(self.actionActive_Visualisation)
        self.Copy_Special.addAction(self.actionActive_Visualization_Image)
        self.Paste_Special.addAction(self.actionShow_Import_Settings)
        self.Paste_Special.addSeparator()
        self.Paste_Special.addAction(self.actionAs_New_Columns)
        self.Paste_Special.addAction(self.actionAs_New_Rows)
        self.Menu.addAction(self.actionUndo)
        self.Menu.addAction(self.actionRedo)
        self.Menu.addSeparator()
        self.Menu.addAction(self.actionCopy)
        self.Menu.addAction(self.Copy_Special.menuAction())
        self.Menu.addAction(self.actionPaste)
        self.Menu.addAction(self.Paste_Special.menuAction())
        self.Menu.addSeparator()
        self.Menu.addAction(self.actionDelete_Active_Page)
        self.Menu.addSeparator()
        self.Menu.addAction(self.actionReset_AllFilters)
        self.Menu.addAction(self.actionMark_Filtered_Rows)
        self.Menu.addAction(self.MarkedRows.menuAction())
        self.Menu.addAction(self.actionReset_All_Marking)
        self.Menu.addSeparator()
        self.Menu.addAction(self.actionData_Connection_Properties)
        self.Menu.addAction(self.actionData_Table_Properties)
        self.Menu.addAction(self.actionColumn_Properties)
        self.Menu.addSeparator()
        self.Menu.addAction(self.actionDocument_Properties)
        self.Menu.addAction(self.actionData_Function_Properties)
        self.View.addAction(self.actionFilters)
        self.View.addAction(self.actionData)
        self.View.addAction(self.Data_Table)
        self.Help.addSeparator()
        self.Insert.addAction(self.New_Page)
        self.Insert.addAction(self.actionDuplicate_Activate_Page)
        self.Insert.addSeparator()
        self.Insert.addAction(self.actionCalculated_Column)
        self.Insert.addSeparator()
        self.Insert.addAction(self.actionColumns)
        self.Insert.addAction(self.actionRows)
        self.Analysis.addAction(self.actionTest_Summary_Report_TSR_Chart_Galliers)
        self.Analysis.addAction(self.actionAnalysis_of_Varicance)
        self.Analysis.addAction(self.actionMeasuement_System_Comparision_MSC_Analysis)
        self.Analysis.addAction(self.actionSPC_Statistical_Process_Controll)
        self.Analysis.addAction(self.Yield_report)
        self.Yield_report.triggered.connect(self.Open_Yiled_Report_window)
        self.Analysis.addAction(self.actionFrequency_Pareto)
        self.Tools.addAction(self.actionFind)
        self.Tools.addSeparator()
        self.Tools.addAction(self.Analysis.menuAction())
        self.menubar.addAction(self.File.menuAction())
        self.menubar.addAction(self.Menu.menuAction())
        self.menubar.addAction(self.View.menuAction())
        self.menubar.addAction(self.Help.menuAction())
        self.menubar.addAction(self.Insert.menuAction())
        self.menubar.addAction(self.Tools.menuAction())
        self.retranslateUi(self.Main_Window)        
        QtCore.QMetaObject.connectSlotsByName(self.Main_Window)
    def retranslateUi(self,Main_Window):
        _translate = QtCore.QCoreApplication.translate
        self.Main_Window.setWindowTitle(_translate("MainWindow", "GOURISANKAR_TOOL"))
        self.File.setTitle(_translate("MainWindow", "File"))
        #self.Export.setTitle(_translate("MainWindow", "Export"))
        #self.Open_From.setTitle(_translate("MainWindow", "Open From"))
        self.Menu.setTitle(_translate("MainWindow", "Edit"))
        self.MarkedRows.setTitle(_translate("MainWindow", "MarkedRows"))
        self.Copy_Special.setTitle(_translate("MainWindow", "Copy Special"))
        self.Paste_Special.setTitle(_translate("MainWindow", "Paste Special"))
        self.View.setTitle(_translate("MainWindow", "View"))
        self.Help.setTitle(_translate("MainWindow", "Help"))
        self.Insert.setTitle(_translate("MainWindow", "Insert"))
        self.Tools.setTitle(_translate("MainWindow", "Tools"))
        self.Analysis.setTitle(_translate("MainWindow", "Analysis"))
        self.actionLoad.setText(_translate("MainWindow", "Load_STDF"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As.."))
        #self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
        self.actionDelete_Active_Page.setText(_translate("MainWindow", "Delete Active Page"))
        self.actionReset_AllFilters.setText(_translate("MainWindow", "Reset AllFilters"))
        self.actionMark_Filtered_Rows.setText(_translate("MainWindow", "Mark Filtered Rows"))
        self.actionUnmark.setText(_translate("MainWindow", "Unmark"))
        self.actionInvert.setText(_translate("MainWindow", "Invert"))
        self.actionDelete.setText(_translate("MainWindow", "Delete"))
        self.actionFilter_To.setText(_translate("MainWindow", "Filter To"))
        self.actionFilter_Out.setText(_translate("MainWindow", "Filter Out"))
        self.actionAdd_Marked_to_List.setText(_translate("MainWindow", "Add Marked to List"))
        self.actionNew_List_from_Marked.setText(_translate("MainWindow", "New List from Marked"))
        self.actionRemove_Marked_From_List.setText(_translate("MainWindow", "Remove Marked From List"))
        self.actionSerach_Marked_in_List.setText(_translate("MainWindow", "Serach Marked in List"))
        self.actionData_for_All_Items.setText(_translate("MainWindow", "Data for All Items"))
        self.actionData_for_Marked_Rows.setText(_translate("MainWindow", "Data for Marked Items"))
        self.actionAll_Rows.setText(_translate("MainWindow", "All Rows"))
        self.actionFiltered_Rows.setText(_translate("MainWindow", "Filtered Rows"))
        self.actionMarked_Rows.setText(_translate("MainWindow", "Marked Rows"))
        self.actionActive_Page.setText(_translate("MainWindow", "Active Page"))
        self.actionActive_Visualisation.setText(_translate("MainWindow", "Active Visualization"))
        self.actionActive_Visualization_Image.setText(_translate("MainWindow", "Active Visualization Image"))
        self.actionShow_Import_Settings.setText(_translate("MainWindow", "Show Import Settings"))
        self.actionAs_New_Columns.setText(_translate("MainWindow", "As New Columns"))
        self.actionAs_New_Rows.setText(_translate("MainWindow", "As New Rows"))
        self.actionReset_All_Marking.setText(_translate("MainWindow", "Reset All Marking"))
        self.actionData_Connection_Properties.setText(_translate("MainWindow", "Data Connection Properties"))
        self.actionData_Table_Properties.setText(_translate("MainWindow", "Data Table Properties"))
        self.actionColumn_Properties.setText(_translate("MainWindow", "Column Properties"))
        self.actionDocument_Properties.setText(_translate("MainWindow", "Document Properties"))
        self.actionData_Function_Properties.setText(_translate("MainWindow", "Data Function Properties"))
        self.actionFilters.setText(_translate("MainWindow", "Filters"))
        self.actionData.setText(_translate("MainWindow", "Data"))
        self.New_Page.setText(_translate("MainWindow", "New Page"))
        self.actionDuplicate_Activate_Page.setText(_translate("MainWindow", "Duplicate Activate Page"))
        self.actionCalculated_Column.setText(_translate("MainWindow", "Calculated Column"))
        self.actionColumns.setText(_translate("MainWindow", "Columns"))
        self.actionRows.setText(_translate("MainWindow", "Rows"))
        self.actionFind.setText(_translate("MainWindow", "Find"))
        self.actionTest_Summary_Report_TSR_Chart_Galliers.setText(_translate("MainWindow", "Test Summary Report ( TSR) & Chart Galliers"))
        self.actionAnalysis_of_Varicance.setText(_translate("MainWindow", "Analysis of Varicance"))
        self.actionMeasuement_System_Comparision_MSC_Analysis.setText(_translate("MainWindow", "Measuement System Comparision ( MSC) Analysis"))
        self.actionSPC_Statistical_Process_Controll.setText(_translate("MainWindow", "Statistical Process Control ( SPC)"))
        self.Yield_report.setText(_translate("MainWindow", "Yield Report Generation"))
        self.actionFrequency_Pareto.setText(_translate("MainWindow", "Frequency Pareto"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.actionAdd_Data_Table.setText(_translate("MainWindow", "Add Data Table"))
        self.actionReplae_Data_Table.setText(_translate("MainWindow", "Replae Data Table"))
        self.actionData_to_Excel.setText(_translate("MainWindow", "Data to Excel"))
        self.actionData_CSV.setText(_translate("MainWindow", "Data to CSV"))
        self.actionData_to_Text.setText(_translate("MainWindow", "Data to Text"))
        '''self.actionSTDF_V4.setText(_translate("MainWindow", "STDF (V4)"))
        self.actionEXCEL.setText(_translate("MainWindow", "EXCEL"))
        self.actionCSV.setText(_translate("MainWindow", "CSV"))
        self.actionTEXT.setText(_translate("MainWindow", "TEXT"))'''
    def Add_Tab(self):
        '''Add the Tab to the window as Many times as we run this action'''
        # Tab Widget
        self.Tab_List.append('Page'+str(len(self.Tab_List)))
        if len(self.Tab_List)>0:
            self.Tab_List[len(self.Tab_List)-1] = QtWidgets.QWidget()
            if 'Page'+str(len(self.Tab_List)) not in self.Tab_Names:
                self.tabWidget.addTab(self.Tab_List[len(self.Tab_List)-1], 'Page'+str(len(self.Tab_List)))
                self.Tab_Names.append('Page'+str(len(self.Tab_List)))
            elif 'Page'+str(len(self.Tab_List)) in self.Tab_Names:
                self.tabWidget.addTab(self.Tab_List[len(self.Tab_List)-1], 'Page'+str(len(self.Tab_List)+1))
        self.tabWidget.setCurrentWidget(self.Tab_List[len(self.Tab_List)-1])    
        #self.Refresh_data_table_items()
    def Add_plot(self):

        self.Add_plot_dialog = QtWidgets.QDialog()
        self.Add_plot_cls=Ui_Selected_items_to_plot(self)
        self.Add_plot_cls.setupUi(self.Add_plot_dialog)
        self.Add_plot_cls.get_the_loaded_Datatables_details()
        self.Add_plot_cls.Add_the_items_stat_items_graph_items_to_list()
        self.Add_plot_dialog.exec_()
        ## Dynamic plot##
        # a figure instance to plot on
        if self.Cancel_buttion_clicked_in_plot_generation==True:
            self.figure = plt.figure()
            # this is the Canvas Widget that displays the `figure`
            # it takes the `figure` instance as a parameter to __init__
            self.canvas = FigureCanvas(self.figure)
            # this is the Navigation widget
            # it takes the Canvas widget and a parent
            self.toolbar = NavigationToolbar(self.canvas, self)
            # Just some button connected to `plot` method
            self.button = QtWidgets.QPushButton('Plot')
            self.button.clicked.connect(self.plot)
            # set the layout
            self.Add_Tab()
            layout = QVBoxLayout(self.Tab_List[len(self.Tab_List)-1])
            layout.addWidget(self.toolbar)
            layout.addWidget(self.canvas)
            layout.addWidget(self.button)
            self.plot()
            #self.Tab_List[len(self.Tab_List)-1].setLayout(layout)
            #self.setLayout(layout)
    def plot(self):
        ''' plot some random stuff '''
        # random data
        New_File_Name='Parametric_Summary_Table'+str(self.Parametric_Summary_Table_count)
        Test_names=list(self.Loaded_Data_File_Raw_Data['Parametric_Summary_Table1']['Name'])
        # instead of ax.hold(False)
        self.figure.clear()
        # create an axis
        ax = self.figure.add_subplot(111)
        
        # discards the old graph
        # ax.hold(False) # deprecated, see above
        # plot data
        data = list(self.Loaded_Data_File_Raw_Data['File_1'][Test_names[0]])
        if data !="": ax.plot(data, '*-')
        # refresh canvas
        self.canvas.draw()
    def Add_Table(self):
        '''Add the data table widgets to the current window.'''
        if len(self.Loaded_Data_File_count)>=len(self.Table_List) and len(self.Loaded_Data_File_count)!=0:
            if len(self.Tab_List)==0:
                self.Add_Tab()
                self.tabWidget.setCurrentIndex(0)
            if self.Tab_List[self.tabWidget.currentIndex()] not in self.Gridlayout_list_pertab.keys():
                self.Gridlayout_list_pertab[self.Tab_List[self.tabWidget.currentIndex()]]=QtWidgets.QGridLayout(self.Tab_List[self.tabWidget.currentIndex()])
            self.Convert_Loaded_data_to_data_table()
            self.File_Table_List[self.Loaded_Data_File_count[len(self.Loaded_Data_File_count)-1]].setParent(self.Tab_List[self.tabWidget.currentIndex()])
            #self.File_Table_List[self.Loaded_Data_File_count[len(self.Loaded_Data_File_count)-1]].setParent(self.Gridlayout_list_pertab[self.Tab_List[self.tabWidget.currentIndex()]])
            self.Gridlayout_list_pertab[self.Tab_List[self.tabWidget.currentIndex()]].addWidget(self.File_Table_List[self.Loaded_Data_File_count[len(self.Loaded_Data_File_count)-1]],0,0)
        elif len(self.Loaded_Data_File_count)!=0 and len(self.Tab_List)!=0 and len(self.Table_List)!=0:
            self.grid_layout=QtWidgets.QGridLayout(self.Tab_List[self.tabWidget.currentIndex()])
            self.Table_List[len(self.Table_List)-1].setParent(self.Tab_List[self.tabWidget.currentIndex()])
            self.grid_layout.addWidget(self.Table_List[len(self.Table_List)-1],0,0)
    def Check_item_exist_in_combo(self,new_item,Combo_list):
        ''' This Function takes 2 Aruguments the item --> the string to check in the list and the Combo_list in which we need to delete the data. '''
        new_item=new_item
        item_exist=False
        if new_item!="" :
            for i in range(0,Combo_list.count()):
                if Combo_list.itemText(i)==new_item:
                    item_exist=True
                    break
        return item_exist
    def Write_raw_data_into_data_table(self,Table,Data_Frame):
        '''Write the data into the data table created in Add_Table_Function'''        
        self.Row_count,self.Column_Count=self.Loaded_Data_File_Raw_Data[self.Loaded_Data_File_count[len(self.Loaded_Data_File_count)-1]].shape
        Table.setColumnCount(self.Column_Count)
        Table.setRowCount(self.Row_count)
        ## Adding the Header values
        self.Header_values=[]
        for column,key in enumerate(self.Loaded_Data_Files[self.Loaded_Data_File_count[len(self.Loaded_Data_File_count)-1]]['Full_Rec_Summary']):
            self.Header_values.append(key)
            for row, item in enumerate(self.Loaded_Data_Files[self.Loaded_Data_File_count[len(self.Loaded_Data_File_count)-1]]['Full_Rec_Summary'][key]):
                val= QTableWidgetItem(str(item))
                Table.setItem(row,column, val)        
        Table.setHorizontalHeaderLabels(self.Header_values)
        #Table.setRowHeight(4,4)
    def CloseTab(self):
        '''Closes the current tab'''        
        temp=self.Tab_Names.pop(self.tabWidget.currentIndex())
        self.Tab_List.remove(self.Tab_List[self.tabWidget.currentIndex()])
        self.tabWidget.removeTab(self.tabWidget.currentIndex())
    def Add_Tool_Bar(self):
        ''' Adds the Icons and actions the created tool bar'''       
        icon_foldername=os.path.dirname(os.path.realpath(__file__))+"\\Icons\\" 
        self.Tool_Bar=self.Main_Window.addToolBar('ToolBar')        
        self.Add_Data_Table_Icon = QtWidgets.QAction(self.Main_Window)
        self.Add_Data_Table_Icon.setObjectName("actionExit")
        self.Add_Data_Table_Icon.triggered.connect(self.Add_Table)
        self.Add_Data_Table_Icon.setIcon(QtGui.QIcon(icon_foldername+"Add_Data_Table.png"))
        self.Tool_Bar.addAction(self.Add_Data_Table_Icon)

        self.Export_Data_Table_Icon = QtWidgets.QAction(self.Main_Window)
        self.Export_Data_Table_Icon.setObjectName("actionExit")
        self.Export_Data_Table_Icon.triggered.connect(self.Open_Export_Window)
        self.Export_Data_Table_Icon.setIcon(QtGui.QIcon(icon_foldername+"Export_Data_Table.png"))
        self.Tool_Bar.addAction(self.Export_Data_Table_Icon)
        
        self.Plots_Icon = QtWidgets.QAction(self.Main_Window)
        self.Plots_Icon.setObjectName("actionExit")
        self.Plots_Icon.triggered.connect(self.Add_plot)
        self.Plots_Icon.setIcon(QtGui.QIcon(icon_foldername+"Histogram.png"))
        self.Tool_Bar.addAction(self.Plots_Icon)

        self.Load_File_Icon = QtWidgets.QAction(self.Main_Window)        
        self.Load_File_Icon.setObjectName("actionExit")
        self.Load_File_Icon.triggered.connect(self.Open_Load_Action)
        self.Load_File_Icon.setIcon(QtGui.QIcon(icon_foldername+"Load_File.png"))
        self.Tool_Bar.addAction(self.Load_File_Icon)

        self.Yield_Report_Icon = QtWidgets.QAction(self.Main_Window)        
        self.Yield_Report_Icon.setObjectName("actionExit")
        self.Yield_Report_Icon.triggered.connect(self.Open_Yiled_Report_window)
        self.Yield_Report_Icon.setIcon(QtGui.QIcon(icon_foldername+"Yield_report.png"))
        self.Tool_Bar.addAction(self.Yield_Report_Icon)

    def Open_Load_Action(self):
        '''Opens the Load window and send the File name selected in load window to this main window, using the QtCore.pyqtsignal.'''        
        self.Load_STDF = QtWidgets.QDialog()
        self.Load_window=Ui_Load_STDF(self)
        self.Load_window.setupUi(self.Load_STDF)            
        self.Load_STDF.exec_()
        self.Refresh_data_table_items()
        #self.Store_the_Data()
    def Open_Export_Window(self):
        ''' Load the the Export_Table_Window.py which allows us to opne the export table window and show the loaded file
        data in the Drop down button , which helps the user to select the file he is looking for and export those files'''
        self.Export_Table_Window = QtWidgets.QDialog()
        self.Export_Table_Window_Cls = Ui_Export_Table_Window(self)
        self.Export_Table_Window_Cls.setupUi(self.Export_Table_Window)
        self.Export_Table_Window_Cls.Add_Loaded_Tables_Data()
        self.Export_Table_Window.exec_()
    def Open_Data_Table_properties_window(self):
        self.Open_Data_table_proerties_win1=QtWidgets.QDialog()
        self.Open_Data_table_proerties=Ui_Data_Table_Properties_Window(self)
        self.Open_Data_table_proerties.setupUi(self.Open_Data_table_proerties_win1)
        self.Open_Data_table_proerties.Add_Loaded_Data_into_list_box()
        self.Open_Data_table_proerties_win1.exec_()
    def Exit(self):
        self.Title='Delete the Data table'
        self.Msg='Are you sure want to delete the Tool..?\t if yes all data will be lost'
        self.Reply=self.Messagebox(self.Msg,'que',self.Title)
        if self.Reply==QtWidgets.QMessageBox.Yes:
            self.Main_Window.close()
        elif self.Reply==QtWidgets.QMessageBox.No:
            pass
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
    def resizeEvent(self, event):# QResizeEvent
        print("w=`{}`, h=`{}`".format(event.size().width(), event.size().height())) 
        #super(Ui_MainWindow, self).resizeEvent(event)
    def moveEvent(self, event):# QMoveEvent
        print("x=`{}`, y=`{}`".format(event.pos().x(), event.pos().y()))
        #super(Ui_MainWindow, self).moveEvent(event)
    def Open_Insert_Rows_window(self):
        '''Opens the Merge table window'''
        self.Insert_Rows = QtWidgets.QDialog()
        self.Insert_Rows_Window = Ui_Insert_Rows(self)
        self.Insert_Rows_Window.setupUi(self.Insert_Rows)
        self.Insert_Rows_Window.Get_the_loaded_file_details()
        self.Insert_Rows.exec_()
        self.Refresh_data_table_items()
    def Open_Yiled_Report_window(self):
        '''Opens the Merge table window'''
        self.Yield_report = QtWidgets.QDialog()
        self.Yield_report_Window = Ui_Yiled_Report_Generation_form(self)
        self.Yield_report_Window.setupUi(self.Yield_report)
        self.Yield_report_Window.Get_the_loaded_file_details()
        self.Yield_report.exec_()
        self.Refresh_data_table_items()
    def Refresh_data_table_items(self):
        ''' Refresh data in the data table, '''
        #self.Loaded_File_List_Combo.clear()
        if len(self.Loaded_Data_File_count)>len(self.File_Table_List):
            self.Convert_Loaded_data_to_data_table()
        for item in self.Loaded_Data_File_Raw_Data.keys(): 
            item_exist=self.Check_item_exist_in_combo(item,self.Loaded_File_List_Combo)
            if item_exist==False:  self.Loaded_File_List_Combo.addItem(item)
    def Change_the_data_table_in_the_current_tab(self):
        ''' Updates the data table in the current tab in python'''
        #self.Refresh_data_table_items()
        if self.Loaded_File_List_Combo.currentText()!='':
            self.Gridlayout_list_pertab[self.Tab_List[self.tabWidget.currentIndex()]].addWidget(self.File_Table_List[self.Loaded_File_List_Combo.currentText()])
        #print('gouri')
    def Convert_Loaded_data_to_data_table(self):
        '''  Converts the data into data table'''
        if len(self.Loaded_Data_File_count)>len(self.File_Table_List):
            for item in list(set(self.Loaded_Data_File_count)-set(self.File_Table_List)):
                if item!=None:
                    self.Table_List.append(QtWidgets.QTableView())
                    self.File_Table_List[item]=self.Table_List[len(self.Table_List)-1]
                    #self.File_Table_List[item].setParent(self.Tab_List[self.tabWidget.currentIndex()])
                    self.File_Table_List[item].setGeometry(QtCore.QRect(0, 0, self.screen.width()-50, self.screen.height()-150))
                    self.File_Table_List[item].setFocusPolicy(QtCore.Qt.NoFocus)
                    self.File_Table_List[item].setObjectName("Table"+str(len(self.Table_List)-1))
                    self.File_Table_List[item].resize
                    self.Loaded_Data_File_Raw_Data[item]=self.Loaded_Data_File_Raw_Data[item].sort_index(axis=1, level=None, ascending=False, inplace=False, kind='quicksort', na_position='last', sort_remaining=True, by=None)
                    self.modle=table_view_model(self.Loaded_Data_File_Raw_Data[item])
                    self.File_Table_List[item].setModel(self.modle)
                    #self.File_Table_List[item].show()
                #self.Write_raw_data_into_data_table(self.File_Table_List[item],self.Loaded_Data_File_Raw_Data[item])'''
    def Summary_table_funs(self):
        ''' Give the summary table based on the data selected'''
        kkk=pandas.pivot_table(self.Loaded_Data_File_Raw_Data['File_1'],values='HardBin',index=['Hbin_nam'],columns=['File_Name'],aggfunc=np.count_nonzero)
    def Export_all_Record_details_in_the_file(self):
        for i in self.Loaded_Data_Files['File_1'].keys():
            kk=self.Loaded_Data_Files['File_1'][i]
            kk2=DF(kk)
            kk2.to_csv('%s.csv'%i,index=False)
        print('All Records exported')
if __name__ == "__main__":
    import sys
    Main_Application = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui_Main_Window = Ui_MainWindow()
    ui_Main_Window.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(Main_Application.exec_())
