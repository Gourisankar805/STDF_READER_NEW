
from PyQt5 import QtCore, QtGui, QtWidgets
from pandas import DataFrame as DF
from plots_and_summary_table import generate_plots_with_summary_table

class Ui_Selected_items_to_plot(object):
    def __init__(self,parent=None):
        super(Ui_Selected_items_to_plot,self).__init__()        
        self.Parent_window=parent
        #,'P1':perce,'P5','P10','P25','P75','P90','P95','P99','COUNT','PASS','FAIL','TOTAL'}
    def setupUi(self, Selected_items_to_plot):
        self.Selected_items_to_plot1=Selected_items_to_plot
        Selected_items_to_plot.setObjectName("Selected_items_to_plot")
        self.screen = QtWidgets.QDesktopWidget().screenGeometry(0)

        Selected_items_to_plot.resize(self.screen.width()-400, self.screen.height()-120)
        self.data_Table_list_Combo = QtWidgets.QComboBox(Selected_items_to_plot)
        self.data_Table_list_Combo.setGeometry(QtCore.QRect(150, 20, self.screen.width()-560, 22))
        self.data_Table_list_Combo.setObjectName("data_Table_list_Combo")
        self.data_Table_list_Combo.currentTextChanged.connect(self.fill_the_data_from_selected_data_table_in_the_list_box)
        
        #Hights and Widths
        self.List_height=self.screen.height()-250
        self.List_Width=self.screen.width()-946

        self.label = QtWidgets.QLabel(Selected_items_to_plot)
        self.label.setGeometry(QtCore.QRect(40, 20, 100, 13))
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(Selected_items_to_plot)
        self.tabWidget.setGeometry(QtCore.QRect(10, 50, self.screen.width()-410, self.List_height+45))
        self.tabWidget.setObjectName("tabWidget")
        self.tabWidget.currentChanged.connect(self.Tab_changed_event)

        
        # Summary Stat Tab
        self.Summary_Stat = QtWidgets.QWidget()
        self.Summary_Stat.setObjectName("Summary_Stat")
        self.Add_items_Summary_Stat = QtWidgets.QPushButton(self.Summary_Stat)
        self.Add_items_Summary_Stat.setGeometry(QtCore.QRect(self.List_Width+20, 120, 75, 25))
        self.Add_items_Summary_Stat.setObjectName("Add_items_Summary_Stat")
        self.Add_All_items_Summary_Stat = QtWidgets.QPushButton(self.Summary_Stat)
        self.Add_All_items_Summary_Stat.setGeometry(QtCore.QRect(self.List_Width+20, 150, 75, 25))
        self.Add_All_items_Summary_Stat.setObjectName("Add_All_items_Summary_Stat")
        self.remove_Item_Summary_Stat = QtWidgets.QPushButton(self.Summary_Stat)
        self.remove_Item_Summary_Stat.setGeometry(QtCore.QRect(self.List_Width+20, 180, 75, 25))
        self.remove_Item_Summary_Stat.setObjectName("remove_Item_Summary_Stat")        
        self.remove_All_items_Summary_Stat = QtWidgets.QPushButton(self.Summary_Stat)
        self.remove_All_items_Summary_Stat.setGeometry(QtCore.QRect(self.List_Width+20, 210, 75, 25))
        self.remove_All_items_Summary_Stat.setObjectName("remove_All_items_Summary_Stat")

        self.selected_Test_Number_list_Summary_Stat = QtWidgets.QListWidget(self.Summary_Stat)
        self.selected_Test_Number_list_Summary_Stat.setGeometry(QtCore.QRect(520, 10, self.List_Width, self.List_height))
        self.selected_Test_Number_list_Summary_Stat.setObjectName("selected_Test_Number_list_Summary_Stat")

        self.all_Test_Number_List_Summary_Stat = QtWidgets.QListWidget(self.Summary_Stat)
        self.all_Test_Number_List_Summary_Stat.setGeometry(QtCore.QRect(10, 10, self.List_Width, self.List_height))
        self.all_Test_Number_List_Summary_Stat.setObjectName("all_Test_Number_List_Summary_Stat")
        self.tabWidget.addTab(self.Summary_Stat, "Summary_Stat")

        # Column Selection Tab
        self.Column_Selection = QtWidgets.QWidget()
        self.Column_Selection.setObjectName("Column_Selection")
        self.groupBox = QtWidgets.QGroupBox(self.Column_Selection)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 951, 621))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")        
        self.Add_items = QtWidgets.QPushButton(self.groupBox)
        self.Add_items.setGeometry(QtCore.QRect(self.List_Width+20, 150, 75, 25))
        self.Add_items.setObjectName("Add_items")
        self.Add_All_items = QtWidgets.QPushButton(self.groupBox)
        self.Add_All_items.setGeometry(QtCore.QRect(self.List_Width+20, 180, 75, 25))
        self.Add_All_items.setObjectName("Add_All_items")
        self.remove_Item = QtWidgets.QPushButton(self.groupBox)
        self.remove_Item.setGeometry(QtCore.QRect(self.List_Width+20, 210, 75, 25))
        self.remove_Item.setObjectName("remove_Item")
        self.remove_All_items = QtWidgets.QPushButton(self.groupBox)
        self.remove_All_items.setGeometry(QtCore.QRect(self.List_Width+20, 240, 75, 25))
        self.remove_All_items.setObjectName("remove_All_items")
        self.all_Test_number_search_filter = QtWidgets.QLineEdit(self.groupBox)
        self.all_Test_number_search_filter.setGeometry(QtCore.QRect(10, 10, self.List_Width, 20))
        self.all_Test_number_search_filter.setObjectName("all_Test_number_search_filter")
        self.selected_Test_number_search_filter = QtWidgets.QLineEdit(self.groupBox)
        self.selected_Test_number_search_filter.setGeometry(QtCore.QRect(520, 10, self.List_Width, 20))
        self.selected_Test_number_search_filter.setObjectName("selected_Test_number_search_filter")
        self.tabWidget.addTab(self.Column_Selection, "Column_Selection")
        self.all_Test_Number_List = QtWidgets.QListWidget(self.groupBox)
        self.all_Test_Number_List.setGeometry(QtCore.QRect(10, 40, self.List_Width+10, self.List_height-40))
        self.all_Test_Number_List.setObjectName("all_Test_Number_List")
        self.selected_Test_Number_list = QtWidgets.QListWidget(self.groupBox)
        self.selected_Test_Number_list.setGeometry(QtCore.QRect(520, 40, self.List_Width+10, self.List_height-40))
        self.selected_Test_Number_list.setObjectName("selected_Test_Number_list")
        
        # Graphs Tab
        self.Graphs = QtWidgets.QWidget()
        self.Graphs.setObjectName("Graphs")        
        self.Add_items_Graphs = QtWidgets.QPushButton(self.Graphs)
        self.Add_items_Graphs.setGeometry(QtCore.QRect(440, 120, 75, 25))
        self.Add_items_Graphs.setObjectName("Add_items_Graphs")
        self.remove_All_items_Graphs = QtWidgets.QPushButton(self.Graphs)
        self.remove_All_items_Graphs.setGeometry(QtCore.QRect(440, 210, 75, 25))
        self.remove_All_items_Graphs.setObjectName("remove_All_items_Graphs")
        self.Add_All_items_Graphs = QtWidgets.QPushButton(self.Graphs)
        self.Add_All_items_Graphs.setGeometry(QtCore.QRect(440, 150, 75, 25))
        self.Add_All_items_Graphs.setObjectName("Add_All_items_Graphs")
        self.remove_Item_Graphs = QtWidgets.QPushButton(self.Graphs)
        self.remove_Item_Graphs.setGeometry(QtCore.QRect(440, 180, 75, 25))
        self.remove_Item_Graphs.setObjectName("remove_Item_Graphs")
        self.tabWidget.addTab(self.Graphs, "Graphs")
        self.all_Test_Number_List_Graphs = QtWidgets.QListWidget(self.Graphs)
        self.all_Test_Number_List_Graphs.setGeometry(QtCore.QRect(160, 10, self.List_Width-150, self.List_height))
        self.all_Test_Number_List_Graphs.setObjectName("all_Test_Number_List_Graphs")
        self.selected_Test_Number_list_Graphs = QtWidgets.QListWidget(self.Graphs)
        self.selected_Test_Number_list_Graphs.setGeometry(QtCore.QRect(530, 10, self.List_Width-150, self.List_height))
        self.selected_Test_Number_list_Graphs.setObjectName("selected_Test_Number_list_Graphs")

        # Group By column Selection Tab
        self.Column_Selection = QtWidgets.QWidget()
        self.Column_Selection.setObjectName("Group_Column_Selection")
        self.groupBox = QtWidgets.QGroupBox(self.Column_Selection)
        self.groupBox.setGeometry(QtCore.QRect(0, 10, 951, 621))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")        
        self.Add_items_group_by_column = QtWidgets.QPushButton(self.groupBox)
        self.Add_items_group_by_column.setGeometry(QtCore.QRect(self.List_Width+20, 150, 75, 25))
        self.Add_items_group_by_column.setObjectName("Add_items_group_by_column")
        self.Add_All_items_group_by_column = QtWidgets.QPushButton(self.groupBox)
        self.Add_All_items_group_by_column.setGeometry(QtCore.QRect(self.List_Width+20, 180, 75, 25))
        self.Add_All_items_group_by_column.setObjectName("Add_All_items_group_by_column")
        self.remove_Item_group_by_column = QtWidgets.QPushButton(self.groupBox)
        self.remove_Item_group_by_column.setGeometry(QtCore.QRect(self.List_Width+20, 210, 75, 25))
        self.remove_Item_group_by_column.setObjectName("remove_Item_group_by_column")
        self.remove_All_items_group_by_column = QtWidgets.QPushButton(self.groupBox)
        self.remove_All_items_group_by_column.setGeometry(QtCore.QRect(self.List_Width+20, 240, 75, 25))
        self.remove_All_items_group_by_column.setObjectName("remove_All_items_group_by_column")
        self.all_Test_number_search_filter = QtWidgets.QLineEdit(self.groupBox)
        self.all_Test_number_search_filter.setGeometry(QtCore.QRect(10, 10, self.List_Width, 20))
        self.all_Test_number_search_filter.setObjectName("all_Test_number_search_filter")
        self.selected_Test_number_search_filter = QtWidgets.QLineEdit(self.groupBox)
        self.selected_Test_number_search_filter.setGeometry(QtCore.QRect(520, 10, self.List_Width, 20))
        self.selected_Test_number_search_filter.setObjectName("selected_Test_number_search_filter")
        self.tabWidget.addTab(self.Column_Selection, "Group_by_Column_Selection")
        self.all_Test_Number_List_group_by_column = QtWidgets.QListWidget(self.groupBox)
        self.all_Test_Number_List_group_by_column.setGeometry(QtCore.QRect(10, 40, self.List_Width+10, self.List_height-40))
        self.all_Test_Number_List_group_by_column.setObjectName("all_Test_Number_List_group_by_column")
        self.selected_Test_Number_list_group_by_column = QtWidgets.QListWidget(self.groupBox)
        self.selected_Test_Number_list_group_by_column.setGeometry(QtCore.QRect(520, 40, self.List_Width+10, self.List_height-40))
        self.selected_Test_Number_list_group_by_column.setObjectName("selected_Test_Number_list")

        # Buttion Declaration
        self.Okay_button = QtWidgets.QPushButton(Selected_items_to_plot)
        self.Okay_button.setGeometry(QtCore.QRect(730, self.List_height+100, 75, 25))
        self.Okay_button.setObjectName("Okay_button")
        self.Okay_button.setText('Okay')
        self.Okay_button.clicked.connect(self.Okay_button_clicked)
        # 
        self.Generate_report = QtWidgets.QPushButton(Selected_items_to_plot)
        self.Generate_report.setGeometry(QtCore.QRect(600, self.List_height+100, 100, 25))
        self.Generate_report.setObjectName("Generate_Report")
        self.Generate_report.setText('Generate Report')
        self.Generate_report.clicked.connect(self.Generate_the_plot_report)

        self.Cancel_button = QtWidgets.QPushButton(Selected_items_to_plot)
        self.Cancel_button.setGeometry(QtCore.QRect(820, self.List_height+100, 75, 25))
        self.Cancel_button.setObjectName("Cancel_button")
        self.Cancel_button.setText('Cancel')
        self.Cancel_button.clicked.connect(self.Close_window)

        ##
        self.all_Test_Number_List_Graphs.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.all_Test_Number_List_Summary_Stat.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.all_Test_Number_List.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.all_Test_Number_List_group_by_column.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.selected_Test_Number_list_Graphs.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.selected_Test_Number_list_Summary_Stat.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.selected_Test_Number_list.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.selected_Test_Number_list_group_by_column.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        
        self.Add_items.setText(">")        
        self.Add_All_items.setText(">>>")
        self.remove_Item.setText("<")
        self.remove_All_items.setText("<<<")

        self.Add_items_group_by_column.setText(">")        
        self.Add_All_items_group_by_column.setText(">>>")
        self.remove_Item_group_by_column.setText("<")
        self.remove_All_items_group_by_column.setText("<<<")

        self.Add_items_Summary_Stat.setText(">")
        self.Add_All_items_Summary_Stat.setText(">>>")        
        self.remove_Item_Summary_Stat.setText("<")
        self.remove_All_items_Summary_Stat.setText("<<<")

        self.Add_items_Graphs.setText(">")
        self.Add_All_items_Graphs.setText(">>>")
        self.remove_Item_Graphs.setText("<")
        self.remove_All_items_Graphs.setText("<<<")
        #Assigning buttion items

        self.Add_items.clicked.connect(self.Add_the_itmes_to_selected_columns)      
        self.Add_All_items.clicked.connect(self.Add_All_the_itmes_to_selected_columns)
        self.remove_Item.clicked.connect(self.Remove_items_from_Seleced_Test_Number_list)
        self.remove_All_items.clicked.connect(self.Remove_all_items_from_Seleced_Test_Number_list)

        self.Add_items_Summary_Stat.clicked.connect(self.Add_the_itmes_to_selected_columns)
        self.Add_All_items_Summary_Stat.clicked.connect(self.Add_All_the_itmes_to_selected_columns)       
        self.remove_Item_Summary_Stat.clicked.connect(self.Remove_items_from_Seleced_Test_Number_list)
        self.remove_All_items_Summary_Stat.clicked.connect(self.Remove_all_items_from_Seleced_Test_Number_list)

        self.Add_items_Graphs.clicked.connect(self.Add_the_itmes_to_selected_columns)
        self.Add_All_items_Graphs.clicked.connect(self.Add_All_the_itmes_to_selected_columns)
        self.remove_Item_Graphs.clicked.connect(self.Remove_items_from_Seleced_Test_Number_list)
        self.remove_All_items_Graphs.clicked.connect(self.Remove_all_items_from_Seleced_Test_Number_list)

        self.Add_items_group_by_column.clicked.connect(self.Add_the_itmes_to_selected_columns)
        self.Add_All_items_group_by_column.clicked.connect(self.Add_All_the_itmes_to_selected_columns)
        self.remove_Item_group_by_column.clicked.connect(self.Remove_items_from_Seleced_Test_Number_list)
        self.remove_All_items_group_by_column.clicked.connect(self.Remove_all_items_from_Seleced_Test_Number_list)
        #self.retranslateUi(Selected_items_to_plot)
        self.tabWidget.setCurrentIndex(0)        
        self.label.setText("Data Table Name:")        
        QtCore.QMetaObject.connectSlotsByName(Selected_items_to_plot)
    def Close_window(self):        
        ''' Closes the Active window'''
        if self.Parent_window==True : self.Parent_window.Cancel_buttion_clicked_in_plot_generation=True
        self.Selected_items_to_plot1.close()
        
    def get_the_loaded_Datatables_details(self):
        ''' Will take the Pandas Data Frame from the parent window and takes the file names and adds to the combo box.
            Shows the column values into the lists'''
        if self.Parent_window!=None:
            self.data_Table_list_Combo.addItems(self.Parent_window.Loaded_Data_File_count)
        #self.fill_the_data_from_data_inthe_list_box()
    def fill_the_data_from_selected_data_table_in_the_list_box(self):
        ''' The function looks for the data items currently in the the combo box, gets the data of the data frame
        then takes the column names of the data frame and loads in to list box1'''
        if self.Parent_window!=None:
            self.all_Test_Number_List.clear()
            self.all_Test_Number_List_group_by_column.clear()
            self.selected_Test_Number_list.clear()
            self.selected_Test_Number_list_group_by_column.clear()
            Parametric_table_list=[]
            Non_Parametric_table_list=[]
            for item in list(self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()].columns):
                if self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][item].dtype == float or self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][item].dtype == int:
                    Parametric_table_list.append(item)
                else: Non_Parametric_table_list.append(item)
            #self.all_Test_Number_List.addItems(list(self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()].columns))
            self.all_Test_Number_List.addItems(Parametric_table_list)
            self.all_Test_Number_List_group_by_column.addItems(Non_Parametric_table_list)
    def Add_the_itmes_to_selected_columns(self):
        ''' This function selects the items in the  "self.all_Test_Number_List" list box and adds the selected items in
         the "self.selected_Test_Number_list" list box'''      
        k=self.List_box1.selectedItems()
        Item_list=[str(self.List_box1.selectedItems()[i].text()) for i in range(len(k))]
        self.List_box2.addItems(Item_list)
        for i in k: self.List_box1.takeItem(self.List_box1.row(i))
    def Remove_items_from_Seleced_Test_Number_list(self):
        ''' This Function removes the items in self.selected_Test_Number_list and add the items into self.all_Test_Number_List list'''
        k=self.List_box2.selectedItems()
        Item_list=[str(self.List_box2.selectedItems()[i].text()) for i in range(len(k))]
        self.List_box1.addItems(Item_list)
        for i in k: self.List_box2.takeItem(self.List_box2.row(i))
    def Add_All_the_itmes_to_selected_columns(self):
        ''' This function selects the All items in the  "self.all_Test_Number_List" list box and add the selected items in
         the "self.selected_Test_Number_list" list box'''
        self.List_box1.selectAll()
        k=self.List_box1.selectedItems()
        Item_list=[str(self.List_box1.selectedItems()[i].text()) for i in range(len(k))]
        self.List_box2.addItems(Item_list)
        for i in k: self.List_box1.takeItem(self.List_box1.row(i))
    def Remove_all_items_from_Seleced_Test_Number_list(self):
        ''' This Function removes the all items in self.selected_Test_Number_list and add the items into self.all_Test_Number_List list'''
        self.List_box2.selectAll()
        k=self.List_box2.selectedItems()
        Item_list=[str(self.List_box2.selectedItems()[i].text()) for i in range(len(k))]
        self.List_box1.addItems(Item_list)
        for i in k: self.List_box2.takeItem(self.List_box2.row(i))
    def Add_the_items_stat_items_graph_items_to_list(self):
        '''This is funtion will add the basic Items to the Statistic summary main table an graph table'''
        Stat_items=['Min','Max','Mean','Median(P50)','StdDev','P1','P5','P10','P25','P75','P90','P95','P99']#,'COUNT','PASS','FAIL','TOTAL']
        Graph_items=['Histogram','Box Plot','Line Plot']#,'Noraml Quantiles','Run Chart']
        self.all_Test_Number_List_Graphs.addItems(Graph_items)
        self.all_Test_Number_List_Summary_Stat.addItems(Stat_items)
    def Tab_changed_event(self):
        ''' This function assins the list variable to new variable based on currnt index'''
        if self.tabWidget.currentIndex()==0:
            self.List_box1=self.all_Test_Number_List_Summary_Stat
            self.List_box2=self.selected_Test_Number_list_Summary_Stat
        elif self.tabWidget.currentIndex()==1:
            self.List_box1=self.all_Test_Number_List
            self.List_box2=self.selected_Test_Number_list
        elif self.tabWidget.currentIndex()==2: 
            self.List_box1=self.all_Test_Number_List_Graphs
            self.List_box2=self.selected_Test_Number_list_Graphs
        elif self.tabWidget.currentIndex()==3: 
            self.List_box1=self.all_Test_Number_List_group_by_column
            self.List_box2=self.selected_Test_Number_list_group_by_column
    def Okay_button_clicked(self):
        '''  This Fucntion takes the inputs from the 3 selected Items list boxs and Creates the Summary table and Plots'''
        self.selected_Test_Number_list_items=[self.selected_Test_Number_list.item(i).text()  for i in range(self.selected_Test_Number_list.count())]
        self.selected_Test_Number_list_Graphs_items=[self.selected_Test_Number_list_Graphs.item(i).text()  for i in range(self.selected_Test_Number_list_Graphs.count())]
        self.selected_Test_Number_list_Summary_Stat_items=[self.selected_Test_Number_list_Summary_Stat.item(i).text()  for i in range(self.selected_Test_Number_list_Summary_Stat.count())]
        self.selected_Test_Number_list_group_by_column=[self.selected_Test_Number_list_group_by_column.item(i).text()  for i in range(self.selected_Test_Number_list_group_by_column.count())]
        self.Current_data_table_name=self.data_Table_list_Combo.currentText()
        #print('Gouri')
        self.Stat_item_data=[]
        for i in self.selected_Test_Number_list_Summary_Stat_items:            
            if i=="Min": Min=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].min();self.Stat_item_data.append(Min)
            elif i=="Max": Max=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].max();self.Stat_item_data.append(Max)
            elif i=="Mean": Mean=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].mean();self.Stat_item_data.append(Mean)
            elif i=="Median(P50)": Median=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].median();self.Stat_item_data.append(Median)
            elif i=="StdDev": StdDev=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].std();self.Stat_item_data.append(StdDev)
            elif i=="P1": P1=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].quantile(0.01);self.Stat_item_data.append(P1)
            elif i=="P5": P5=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].quantile(0.05);self.Stat_item_data.append(P5)
            elif i=="P10": P10=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].quantile(0.1);self.Stat_item_data.append(P10)
            elif i=="P25": P25=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].quantile(0.25);self.Stat_item_data.append(P25)
            elif i=="P75": P75=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].quantile(0.75);self.Stat_item_data.append(P75)
            elif i=="P90": P90=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].quantile(0.9);self.Stat_item_data.append(P90)
            elif i=="P95": P95=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].quantile(0.95);self.Stat_item_data.append(P95)
            elif i=="P99": P99=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].quantile(0.99);self.Stat_item_data.append(P99)
            elif i=="COUNT": Count=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].count();self.Stat_item_data.append(Count)
            elif i=="PASS": Pass=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].min();self.Stat_item_data.append(Pass)
            elif i=="FAIL": Fail=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].min();self.Stat_item_data.append(Fail)
            elif i=="TOTAL": Total=self.Parent_window.Loaded_Data_File_Raw_Data[self.data_Table_list_Combo.currentText()][self.selected_Test_Number_list_items].min();self.Stat_item_data.append(Total)
        
        All_Stat_Summary_Table=DF(self.Stat_item_data,index=self.selected_Test_Number_list_Summary_Stat_items).transpose()
        All_Stat_Summary_Table['Name']=self.selected_Test_Number_list_items
        All_Stat_Summary_Table['File_Name']=[self.data_Table_list_Combo.currentText() for i in range(len(self.selected_Test_Number_list_items))]
        All_Stat_Summary_Table=All_Stat_Summary_Table[list(All_Stat_Summary_Table.columns)[-1:]+list(All_Stat_Summary_Table.columns)[:-1]]
        if self.Parent_window!=None:
            New_File_Name='Parametric_Summary_Table'+str(self.Parent_window.Parametric_Summary_Table_count+1)
            self.Parent_window.Loaded_Data_File_count.append(New_File_Name)
            self.Parent_window.Parametric_Summary_Table_count+=1
            Temp_file=All_Stat_Summary_Table
            Temp_file1={}
            for name in Temp_file.columns:  Temp_file1[name]=list(Temp_file[name])
            self.Parent_window.Loaded_Data_Files[New_File_Name]={'Full_Rec_Summary':Temp_file1}
            self.Parent_window.Loaded_Data_File_Raw_Data[New_File_Name]=All_Stat_Summary_Table
            #self.Parent_window.Loaded_Data_File_Raw_Data
        print('done')        
        #self.selected_Test_Number_list_items=[self.selected_Test_Number_list.item(i).text() in for i in range(self.selected_Test_Number_list.count())]
    def Generate_the_plot_report(self):
        ''' This Function will take the input from all the list boxes like
        Test details, Data table name, Group by columns , different plots names to plots.
        Using that info the function will generate the pdf report with graphs and summary table.'''
        self.selected_Test_Number_list_items=[self.selected_Test_Number_list.item(i).text()  for i in range(self.selected_Test_Number_list.count())]
        self.selected_Test_Number_list_Graphs_items=[self.selected_Test_Number_list_Graphs.item(i).text()  for i in range(self.selected_Test_Number_list_Graphs.count())]
        self.selected_Test_Number_list_Summary_Stat_items=[self.selected_Test_Number_list_Summary_Stat.item(i).text()  for i in range(self.selected_Test_Number_list_Summary_Stat.count())]
        self.selected_Test_Number_list_group_by_column=[self.selected_Test_Number_list_group_by_column.item(i).text()  for i in range(self.selected_Test_Number_list_group_by_column.count())]
        self.Current_data_table_name=self.data_Table_list_Combo.currentText()
        self.Generate_report=generate_plots_with_summary_table(self.Parent_window)
        self.Generate_report.Generate_plots(data_table_name= self.Current_data_table_name,
        test_number_list=self.selected_Test_Number_list_items,summary_stat_list=self.selected_Test_Number_list_Summary_Stat_items,plot_list=self.selected_Test_Number_list_Graphs_items,group_by_varible_list= self.selected_Test_Number_list_group_by_column)
        self.Close_window()
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Selected_items_to_plot = QtWidgets.QWidget()
    ui = Ui_Selected_items_to_plot()
    ui.setupUi(Selected_items_to_plot)
    Selected_items_to_plot.show()
    sys.exit(app.exec_())

