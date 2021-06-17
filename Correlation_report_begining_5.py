from PyQt5 import QtWidgets,QtCore
from PyQt5.QtWidgets import QWidget,QLabel,QCheckBox,QPushButton,QApplication,QComboBox,QMessageBox,QFileDialog
from PyQt5.QtCore import QRect
import sys
import warnings;warnings.simplefilter('ignore')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import seaborn as sabrn
import pandas as pd
from pandas import DataFrame,read_excel,concat,ExcelWriter,ExcelFile
import time,datetime,math,os
class App2(QWidget):
    def __init__(self):
        super(App2,self).__init__()  
    def initUI(self):
        LB_Compare=QtWidgets.QDialog()
        LB_Compare.setObjectName("Data_Table_Properties_Window")
        LB_Compare.setWindowTitle('LB Correlation')   
        self.setGeometry(10, 30, 500, 150) #(self.left, self.top, self.width, self.height)
        self.label1 = QLabel("Input File", self)
        self.label1.move(20,20)
        self.label2 = QLabel("Output File", self)
        self.label2.move(20, 50)
        self.input_txt_bx = QtWidgets.QLineEdit(self)
        self.input_txt_bx.move(80, 20)
        self.input_txt_bx.resize(230,20)        
        self.output_file_bx = QtWidgets.QLineEdit(self)
        self.output_file_bx.move(80, 50)
        self.output_file_bx.resize(230,20)        
        self.Column_drp_down = QComboBox(self)
        self.Column_drp_down.setGeometry(QRect(320, 50, 150, 20))#(X,Y,Wid,HIg)
        self.Column_drp_down.setObjectName(("Column_drp_down"))
        self.Box_Plot = QCheckBox('', self)
        self.Box_Plot.move(20, 90)
        self.Box_Plot.setText('Box_Plot')
        self.Histogram = QCheckBox('', self)
        self.Histogram.move(100, 90)
        self.Histogram.setText('Histogram')
        '''self.Cumulative = QCheckBox('', self)
        self.Cumulative.move(180, 90)
        self.Cumulative.setText('Cumulative') '''
        self.Export_sum_table= QCheckBox('', self)
        self.Export_sum_table.move(20, 120)
        self.Export_sum_table.setText("Export_summary_Table")
        browse_button = QPushButton('Browse', self)
        browse_button.setToolTip('This is an example button')
        browse_button.move(320,15)
        browse_button.clicked.connect(self.on_click)
        Ok_button = QPushButton('OK', self)
        Ok_button.setToolTip('This is an example button')
        Ok_button.move(160,120) 
        Ok_button.clicked.connect(self.Generate_plots)
        quit_button = QPushButton('Quit', self)
        quit_button.setToolTip('Close Window')
        quit_button.move(250,120)
        quit_button.clicked.connect(self.close_application)   
        self.show()
    def close_application(self):
        choice = QMessageBox.question(self, 'Message',"Are you sure to quit?", QMessageBox.Yes |QMessageBox.No, QMessageBox.No)
        if choice == QMessageBox.Yes:            
            self.close()             
        else:
            pass
    def on_click(self): 
        global sheet_1,sheet_2,TestNumbers,TestNumber
        self.Column_drp_down.clear()
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName!="":
            self.input_txt_bx.setText(fileName)            
            outputpath=self.input_txt_bx.text();outputpath=os.path.dirname(outputpath)
            outputfilename=self.output_file_bx.text();outputfilename=outputpath+'/'+outputfilename
            Wrkbook=self.input_txt_bx.text()
            #Wrkbook=pd.ExcelFile(x)    
            sheet_1=pd.read_excel(Wrkbook,sheetname=0)
            sheet_2=pd.read_excel(Wrkbook,sheetname=1)            
            options1=list(sheet_1.columns.values)
            for i in range(0,len(options1)):
                self.Column_drp_down.addItem(options1[i])
            TestNumbers=[]
            TestNumbers=list(sheet_1.columns.values)
            self.input_txt_bx.setDisabled(True)
        else:
            self.input_txt_bx.setText("Please select a file")
    def Enable_or_Disable(self):            
        pass  
    def Plot_Histogram(self,Grouped_data,Test_no_name):    
        Grouped_data[Test_no_name].plot(kind='hist', alpha=1, legend=True,edgecolor ='black',stacked=False)
        Lo_Limit=float(Test_no_name.split(';')[2]) if Test_no_name.split(';')[2]!='' else ''
        Hi_Limit=float(Test_no_name.split(';')[3]) if Test_no_name.split(';')[3]!='' else ''
        Lims=[Lo_Limit,Hi_Limit]
        colors=['b','r']
        Labels=['Lo_Limit','Hi_Limit']
        for li,c,lbl in zip(Lims,colors,Labels):
            (plt.axvline(x=li, c=c, label= lbl) ) if li!='' else '' #, label= lbl +'= {}'.format(li)
        #plt.title(Test_no_name)
        return plt
    def Plot_Line_plot(self,Merged_data,Test_no_name,Grouping_column_name):    
        List_of_variables_for_grouping=[i for i in Merged_data[Grouping_column_name].unique()]
        #print(List_of_variables_for_grouping)
        List_of_data_sets={}    
        for i in range(len(List_of_variables_for_grouping)): List_of_data_sets['Data_'+List_of_variables_for_grouping[i]]=Merged_data[Merged_data[Grouping_column_name]==List_of_variables_for_grouping[i]]
        colors=['b','g','r','c','m','y','k']
        symbols=['.','*','+','s','p','D','h','v','o']
        markers=[color+symbol for symbol in symbols for color in colors]        
        for i in range(len(List_of_variables_for_grouping)): plt.plot(List_of_data_sets['Data_'+List_of_variables_for_grouping[i]]['Devices'],List_of_data_sets['Data_'+List_of_variables_for_grouping[i]][Test_no_name],markers[i],label=List_of_variables_for_grouping[i])
        plt.xticks(rotation='vertical')
        plt.xlabel('Devices')
        #plt.title(Test_no_name)
        plt.legend()
        return plt
    def Plot_BOX_plot(self,Merged_data,Test_no_name,Grouping_column_name):    
        List_of_variables_for_grouping=[i for i in Merged_data[Grouping_column_name].unique()]    
        boxgroupedx=Grouping_column_name
        box=sabrn.boxplot(data=Merged_data,x=boxgroupedx, y=Test_no_name,hue=boxgroupedx,width=0.5)
        if len(List_of_variables_for_grouping)<=9:
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), borderaxespad=0., prop={'size': 10})
        elif len(List_of_variables_for_grouping)>9:
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), borderaxespad=0., prop={'size': 6})
        box.set(xlabel='',ylabel='')
        #plt.title('Box plot')    
        plt.xticks( rotation='vertical',fontsize=6)
        plt.legend()
        return plt
    def Get_the_header_table(self,loop_count):
        Table6=['TESSOLVE SEMICONDUCTOR PVT LTD',"PageNumber"]
        Table7=[['Characterization Report',loop_count]]
        Header_table= plt.table(cellText=Table7,colLabels=Table6,cellLoc='center',colLoc='center',loc='top',bbox=[-0.01, 2.32,1.2,0.15])
        Header_table.set_fontsize(16)
        Header_table.scale(2.6,2.6)
        Header_table.auto_set_font_size(False)
        Header_table.auto_set_column_width(True)
        #t2_data=TestNumbers[loop_count].split(';')[0]+TestNumbers[loop_count].split(';')[1]
        t2='%s' %(TestNumbers[loop_count].split(';')[0]+'_'+TestNumbers[loop_count].split(';')[1])
        plt.text(0.10, 0.92, t2, style='normal',fontsize=18,transform=plt.gcf().transFigure,bbox={'facecolor':'none', 'alpha':1, 'pad':5})
        return plt
    def convert_to_Grouped_Data(self,inputfile,Grouping_column_name):
        return inputfile.groupby(Grouping_column_name)
    def Merge_the_data_frames(self,File1,File2):
        New_Data_with_merged=''
        if len(File1.columns.difference(File2.columns))==0:
            New_Data_with_merged=pd.concat([File1,File2])
            print( 'Merging completed')
        elif len(File1.columns.difference(File2.columns))!=0:
            unmatched_column_names=File1.columns.difference(File2.columns)
            print('There are %s unmatching columns are there. Unmatched column names in the file shown below'%len(unmatched_column_names))
            for i in range(len(unmatched_column_names)): print(unmatched_column_names[i])
            Still_want_to_merge_both_the_files=QMessageBox.question(self,'merge','The 2 inputs don"t have some columns matching you still want to proceed',QMessageBox.Yes | QMessageBox.No ,QMessageBox.Yes)       
            if Still_want_to_merge_both_the_files==QMessageBox.Yes:
                New_Data_with_merged=pd.concat([File1,File2])
                print( 'Merging completed')
            elif Still_want_to_merge_both_the_files==QMessageBox.No:
                print(" Merging of the 2 files was unsucessful :-( , Please try again")            
            else:
                print(' Please give a valid input')
        return New_Data_with_merged
    def Get_the_summary_table(self,Summary_table,Test_no_name,Test_column,table_column_header):
        Data_tbl=plt.table(cellText=Summary_table[Summary_table[Test_column]==Test_no_name].values,colLabels=table_column_header,cellLoc='left',colLoc='left',loc='bottom',bbox=[-0.08,-0.4,1.2,0.3])
        return plt
    def Generate_summary_table(self,Merged_data,Grouping_column_name,Test_no_name_list):
        Ref_table=Merged_data[Merged_data[Grouping_column_name].str.contains('ref',case=False)]
        New_board=Merged_data[Merged_data[Grouping_column_name].str.contains('ref',case=False)==False]
        Table_header=['TestNum','TestName','Lo_Limit','Hi_Limit','Unit','SD_Ref_Lot(Bin1)','Mean_Ref_Board','SD_Ref_Board','Mean_New_Board',
                    'SD_New_Board','Delta_Mean','Mean_Shift','Mean_Shift_Criteria','SD_Ratio','Sigma_Spread_Criteria','Passed/Failed']
        Summary_table={'TestNum':[],'TestName':[],'Lo_Limit':[],'Hi_Limit':[],'Unit':[],'SD_Ref_Lot(Bin1)':[],'Mean_Ref_Board':[],'SD_Ref_Board':[],'Mean_New_Board':[],
                    'SD_New_Board':[],'Delta_Mean':[],'Mean_Shift':[],'Mean_Shift_Criteria':[],'SD_Ratio':[],'Sigma_Spread_Criteria':[],'Passed/Failed':[]}
        try:
            for i in range(len(Test_no_name_list)):        
                if (Merged_data[Test_no_name_list[i]].dtype=='float'or Merged_data[Test_no_name_list[i]].dtype=='int64' ) and Test_no_name_list[i].count(';')>=5 :
                    TestNum=Test_no_name_list[i].split(';')[0]               
                    TestName=Test_no_name_list[i].split(';')[1]
                    Lo_Limit=float(Test_no_name_list[i].split(';')[2]) if Test_no_name_list[i].split(';')[2]!='' else ''
                    Hi_Limit=float(Test_no_name_list[i].split(';')[3]) if Test_no_name_list[i].split(';')[3]!='' else ''
                    Unit=Test_no_name_list[i].split(';')[4]
                    SD_Ref_Lot=float(Test_no_name_list[i].split(';')[5]) if Test_no_name_list[i].split(';')[5]!='' else ''
                    Mean_Ref_Board=round(Ref_table[Test_no_name_list[i]].mean(),3)
                    SD_Ref_Board=round(Ref_table[Test_no_name_list[i]].std(),3)
                    Mean_New_Board=round(New_board[Test_no_name_list[i]].mean(),3)
                    SD_New_Board=round(New_board[Test_no_name_list[i]].std(),3)
                    Delta_Mean=round(abs(Mean_Ref_Board-Mean_New_Board),3)
                    Mean_Shift=round((Delta_Mean/(Hi_Limit-Lo_Limit)*100),3) if Hi_Limit!='' and Lo_Limit!='' and type(Hi_Limit)!=str and type(Lo_Limit)!=str and Hi_Limit!=Lo_Limit else 'N/A'
                    Mean_Shift_Criteria=(('Passed' if Delta_Mean< SD_Ref_Lot else 'For Check' ) if SD_Ref_Lot!='' else 'N/A') if Mean_Shift=='N/A' else ('Passed' if Mean_Shift!='N/A' and Mean_Shift<5 else 'Failed')
                    SD_Ratio= round((SD_New_Board/SD_Ref_Board),3) if SD_Ref_Board!='' and SD_New_Board!='' and SD_Ref_Board!=0 and SD_New_Board!=0 else 0
                    Sigma_Spread_Criteria= 'Passed' if SD_Ratio<1.5 else 'For Check'
                    Passed_Failed='Passed' if Mean_Shift_Criteria=='Passed' and Sigma_Spread_Criteria=='Passed' else ('Failed' if Mean_Shift_Criteria=='Failed' else 'For Check')
                    Table_header_val=[TestNum,TestName,Lo_Limit,Hi_Limit,Unit,SD_Ref_Lot,Mean_Ref_Board,SD_Ref_Board,Mean_New_Board,
                        SD_New_Board,Delta_Mean,Mean_Shift,Mean_Shift_Criteria,SD_Ratio,Sigma_Spread_Criteria,Passed_Failed]
                    for j in range(len(Table_header)): Summary_table[Table_header[j]].append(Table_header_val[j])
            Dataframe=pd.DataFrame(Summary_table,columns=Table_header)
            return Dataframe ,Table_header
        except:
            k=QMessageBox.information('Generation aborted!','Sorry :( Found some issue in Generating the Summary table',QMessageBox.Ok,QMessageBox.Ok)
            print('Line Number or Loop Number is ',i,Test_no_name_list[i])
            self.close()
    def Generate_plots(self):
        Merged_Data=self.Merge_the_data_frames(sheet_1,sheet_2)
        Group_by_variable=self.Column_drp_down.currentText()
        Merged_Data_with_Groupby=self.convert_to_Grouped_Data(Merged_Data,Group_by_variable)        
        outputpath=self.input_txt_bx.text();outputpath=os.path.dirname(outputpath)
        outputfilename=self.output_file_bx.text();outputfilename=outputpath+'/'+outputfilename        
        Numberofplotsinpdf=0
        Summary_table,Summary_header=self.Generate_summary_table(Merged_Data,Group_by_variable,TestNumbers)
        if self.Export_sum_table.isChecked()==True:
            writer = pd.ExcelWriter(outputfilename+'_Summary_sheet.xlsx')
            Summary_table.to_excel(writer,'Summary_Stat',columns=Summary_header, header=True, index=False)
            writer.save()
            print('Summary Table exported sucessfully')
        if self.Box_Plot.isChecked()==True:
            Numberofplotsinpdf+=1
        if self.Histogram.isChecked()==True:
            Numberofplotsinpdf+=1
        if Numberofplotsinpdf>=1:
            pdf_pages = PdfPages(outputfilename+'.pdf')
            with pdf_pages as pdf:
                for i in range(len(TestNumbers)):
                    plt.cla()
                    if Merged_Data[TestNumbers[i]].dtype=='float' or Merged_Data[TestNumbers[i]].dtype=='int64':
                        if Numberofplotsinpdf==1:
                            fig = plt.figure(figsize=(20,14))
                            #plt.subplot(1,1,1)
                            if self.Box_Plot.isChecked()==True:
                                Table_attached=False
                                self.Plot_BOX_plot(Merged_Data,TestNumbers[i],Group_by_variable)
                            elif self.Histogram.isChecked()==True:                        
                                Table_attached=False
                                self.Plot_Histogram(Merged_Data_with_Groupby,TestNumbers[i])
                        elif Numberofplotsinpdf==2:
                            if (self.Histogram.isChecked()==True and self.Box_Plot.isChecked()==True):
                                Table_attached=False
                            else:
                                Table_attached=True
                            Line_Plot_plotted=False                    
                            histogramplotted=False
                            fig = plt.figure(figsize=(20,14))
                            plt.subplot(2,1,1)
                            if self.Box_Plot.isChecked()==True and Line_Plot_plotted==False:
                                Table_attached=True
                                self.Plot_BOX_plot(Merged_Data,TestNumbers[i],Group_by_variable)
                                Table_attached=False
                                Line_Plot_plotted=True
                            elif self.Histogram.isChecked()==True and histogramplotted==False:                                                    
                                self.Plot_Histogram(Merged_Data_with_Groupby,TestNumbers[i])                            
                                histogramplotted=True                                           
                            plt.subplot(2,1,2)                        
                            if self.Box_Plot.isChecked()==True and Line_Plot_plotted==False:
                                self.Plot_BOX_plot(Merged_Data,TestNumbers[i],Group_by_variable)
                                Line_Plot_plotted=True
                            elif self.Histogram.isChecked()==True and histogramplotted==False:                        
                                self.Plot_Histogram(Merged_Data_with_Groupby,TestNumbers[i])
                                Table_attached=True
                                histogramplotted=True                  
                            Line_Plot_plotted=False
                            histogramplotted=False
                            plt.subplots_adjust(left=0.1, right=0.85,top=0.89,bottom=0.2)       
                        #Header
                        c=[0.03, 0.09, 0.03, 0.03, 0.02, 0.05, 0.05, 0.05, 0.05, 0.05,0.05,0.05,0.05,0.04,0.05,0.05]
                        DataTable=plt.table(cellText=Summary_table[Summary_table['TestNum']==TestNumbers[i].split(';')[0]].values,colWidths=c,colLabels=Summary_header,cellLoc='left',colLoc='left',loc='bottom',bbox=[-0.08,-0.4,1.2,0.3])
                        DataTable.auto_set_font_size(False)
                        DataTable.set_fontsize(15)
                        DataTable.scale(4,4)
                        #DataTable._cells[(0,0),(0,len(c))].set_facecolor("#56b5fd")
                        DataTable.auto_set_column_width(True)
                        #DataTable.
                        self.Get_the_header_table(i)
                        plt.subplots_adjust(left=0.1, right=0.85,top=0.9,bottom=0.2)
                        pdf.savefig()
                        plt.close()
                        #progress_bar['value']=(i/len(TestNumbers))*100
                    else:
                        print(TestNumbers[i],' column having some issue in the data.  Please make sure no strings are present in the input data columns / Test Numbers')

        QMessageBox.information(self,'Sucessfull !!','Generation Completed',QMessageBox.Ok,QMessageBox.Ok)
        print('Generation completed')
        self.close()        
        
app = QApplication(sys.argv)
k=App2()
k.initUI()
sys.exit(app.exec_())