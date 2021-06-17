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
class generate_plots_with_summary_table:

    def __init__(self,parent=None):
        self.Parent_window=parent

    def Plot_Histogram(self,Raw_Data,Grouping_column_name,Test_no_name):
            ''' This Function used to Generate the Histogram plot if we provide mandotary items Dataframe name, Column name for which we need to plot the 
        graph and the grouping column if you have any'''
            if type(Grouping_column_name)==str: Grouping_column_name=[Grouping_column_name]
            if len(Grouping_column_name)!=0:Grouped_data=Raw_Data.groupby(Grouping_column_name[0])
            elif len(Grouping_column_name)==0:Grouped_data=Raw_Data
            Grouped_data[Test_no_name].plot(kind='hist', alpha=1, legend=True,edgecolor ='black',stacked=False)
            if self.Parent_window!=None:
                if 'Test_Limit_Details' in self.Parent_window.Loaded_Data_Files[self.Data_Table_Name]: Lo_Limit=float(self.Parent_window.Loaded_Data_Files[self.Data_Table_Name]['Test_Limit_Details'][Test_no_name][0])
                elif 'Test_Limit_Details' not in self.Parent_window.Loaded_Data_Files[self.Data_Table_Name]: Lo_Limit=''
                if 'Test_Limit_Details' in self.Parent_window.Loaded_Data_Files[self.Data_Table_Name]: Hi_Limit=float(self.Parent_window.Loaded_Data_Files[self.Data_Table_Name]['Test_Limit_Details'][Test_no_name][1])
                elif 'Test_Limit_Details' not in self.Parent_window.Loaded_Data_Files[self.Data_Table_Name]: Hi_Limit=''
            elif self.Parent_window==None: Lo_Limit=''; Hi_Limit=''
            Lims=[Lo_Limit,Hi_Limit]
            colors=['b','r']
            Labels=['Lo_Limit','Hi_Limit']
            for li,c,lbl in zip(Lims,colors,Labels):
                (plt.axvline(x=li, c=c, label= lbl) ) if li!='' else '' #, label= lbl +'= {}'.format(li)
            #plt.title(Test_no_name)
            return plt
    def Plot_Line_plot(self,Merged_data,Test_no_name,Grouping_column_name):
        ''' This Function used to Generate the Line plot if we provide mandotary items Dataframe name, Column name for which we need to plot the 
        graph and the grouping column if you have any'''
        if type(Grouping_column_name)==str: Grouping_column_name=[Grouping_column_name]
        if len(Grouping_column_name)!=0: List_of_variables_for_grouping=[i for i in Merged_data[Grouping_column_name[0]].unique()]
        elif len(Grouping_column_name)==0: List_of_variables_for_grouping=[None]
        # Colour codes to the multiple plots we are using    
        colors=['b','g','r','c','m','y','k']
        symbols=['.','*','+','s','p','D','h','v','o']
        # Creating the new data table with the name of unique values in the Grouping column name which will help to generate the plot clear
        List_of_data_sets={}  
        if len(Grouping_column_name)!=0: 
            for i in range(len(List_of_variables_for_grouping)): List_of_data_sets['Data_'+str(List_of_variables_for_grouping[i])]=Merged_data[Merged_data[Grouping_column_name[0]]==List_of_variables_for_grouping[i]]
        elif len(Grouping_column_name)==0:  List_of_data_sets['Data']=Merged_data
        markers=[color+symbol for symbol in symbols for color in colors]    
        if len(Grouping_column_name)!=0:    
            for i in range(len(List_of_variables_for_grouping)): plt.plot(list(List_of_data_sets['Data_'+str(List_of_variables_for_grouping[i])].index),List_of_data_sets['Data_'+str(List_of_variables_for_grouping[i])][Test_no_name],markers[i],label=List_of_variables_for_grouping[i])
        elif len(Grouping_column_name)==0: plt.plot(list(List_of_data_sets['Data'].index),List_of_data_sets['Data'][Test_no_name],markers[0],label=None)
        plt.xticks(rotation='vertical')
        plt.xlabel('Devices')
        #plt.show()
        plt.legend()
        return plt

    def Plot_BOX_plot(self,Merged_data,Test_no_name,Grouping_column_name):
        ''' This Function used to Generate the Box plot if we provide mandotary items Dataframe name, Column name for which we need to plot the 
        graph and the grouping column if you have any'''
        if type(Grouping_column_name)==str: Grouping_column_name=[Grouping_column_name]
        if len(Grouping_column_name)!=0:
            List_of_variables_for_grouping=[i for i in Merged_data[Grouping_column_name[0]].unique()]
            boxgroupedx= Grouping_column_name[1] if len(Grouping_column_name)>1 else Grouping_column_name[0]    
        elif len(Grouping_column_name)==0: List_of_variables_for_grouping=[None];boxgroupedx=None

        if (len(List_of_variables_for_grouping)==1 and List_of_variables_for_grouping[0]=='') or (len(List_of_variables_for_grouping)==1 and List_of_variables_for_grouping[0]!=""): box=sabrn.boxplot(data=Merged_data,x=boxgroupedx, y=Test_no_name,width=0.5)
        elif len(List_of_variables_for_grouping)>1: box=sabrn.boxplot(data=Merged_data,x=boxgroupedx, y=Test_no_name,hue=boxgroupedx,width=0.5)
        if len(List_of_variables_for_grouping)<=9: plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), borderaxespad=0., prop={'size': 10})
        elif len(List_of_variables_for_grouping)>9: plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), borderaxespad=0., prop={'size': 6})
        box.set(xlabel='',ylabel='')
        #plt.title('Box plot')
        plt.xticks(rotation='horizontal',fontsize=6)
        plt.legend()
        return plt

    def rearrange(PVT_corners, data):
        rearranged_data = []
        data_len = len(data)
        boxgroupedx=Dropdown_variable.get()
        unique_count= len(np.unique(sheet_1[boxgroupedx]))
        for i in range(PVT_corners):
            try:
                start, end = int(i*data_len/unique_count), int((i+1)*data_len/unique_count)
                rearranged_data.append(data[start:end])
            except IndexError:
                pass
        return rearranged_data

    def plot_cumulatvie(TestNumber):
        boxgroupedx=Dropdown_variable.get()
        Table_attached=False
        PVT_corners=len(set(sheet_1[boxgroupedx]))
        PVTDATA=rearrange(PVT_corners,sheet_1[TestNumbers[TestNumber]])
        #print(PVTDATA)
        
        colors=['b','g','r','c','m','y','k']
        symbols=['.','*','+','s','p','D','h','v','o']
        LABELS=[]
        for i in range(len(sheet_1[boxgroupedx])):
            if len(LABELS)==0:LABELS.append(sheet_1[boxgroupedx][i])
            if  sheet_1[boxgroupedx][i] not in LABELS:LABELS.append(sheet_1[boxgroupedx][i])
                
        markers=[color+symbol for symbol in symbols for color in colors]
        #with open("test.txt", "a") as myfile:    
        for i in range(len(PVTDATA)):
            #print(len(PVTDATA))
            x_data = np.sort(PVTDATA[i])#;print(PVTDATA[i])
            #myfile.write(PVTDATA[i])
            y_data = np.arange(1, len(x_data)+1)/len(x_data)
            plt.plot(x_data, y_data, markers[i], label=LABELS[i], rasterized=True)
            plt.margins(0.02)
        
        hilimt=float(sheet_2[TestNumbers[TestNumber]][5])
        hilimt1=hilimt
        lowlimt=float(sheet_2[TestNumbers[TestNumber]][6])
        lowlimt1=lowlimt
        Lowspec_min=[lowlimt,lowlimt1]
        Lowspec_max=[0,1]
        Highspec_min=[hilimt,hilimt1]
        Highspec_max=[0,1]
        Table2=FullDataSummaryTable[TestNumber-26]
        if Check_box5_check.get()==1:
            NewCPK=Textbox4.get();NewCPK=float(NewCPK)
            if Table2[0][11]<NewCPK and Table2[0][9]!=0:
                Cal_USL=round(Table2[0][7]+(3*Table2[0][9]*NewCPK),5)
                Cal_LSL=round(Table2[0][7]-(3*Table2[0][9]*NewCPK),5)            
                new_hi_y=[float(Cal_USL),float(Cal_USL)]
                new_lo_y=[float(Cal_LSL),float(Cal_LSL)]
                if Table2[0][12]<NewCPK:
                    plt.plot(new_hi_y,Highspec_max,color='orange', linestyle='dashed')                
                    r2='HighLim :%s' %Table2[0][3]; plt.text(0.86, 0.88, r2, fontsize=8,color='blue', transform=plt.gcf().transFigure)
                    r7='Cal HighLim : %s'%Cal_USL; plt.text(0.86, 0.84, r7, fontsize=8,color='blue', transform=plt.gcf().transFigure)
                if Table2[0][13]<NewCPK:
                    plt.plot(new_lo_y,Lowspec_max,color='orange', linestyle='dashed')
                    r1='LowLim : %s'%Table2[0][2]; plt.text(0.86, 0.89, r1, fontsize=8,color='blue', transform=plt.gcf().transFigure)
                    r6='Cal LowLim : %s'%Cal_LSL; plt.text(0.86, 0.83, r6, fontsize=8,color='blue', transform=plt.gcf().transFigure)
                plt.text(0.86, 0.69, "- - New Lims", fontsize=10,color='orange', transform=plt.gcf().transFigure)
                r3='unit :%s'%Table2[0][4]; plt.text(0.86 ,0.87, r3, fontsize=8,color='blue', transform=plt.gcf().transFigure)
                r4='CPK : %s'%Table2[0][11]; plt.text(0.86, 0.86, r4, fontsize=8,color='blue', transform=plt.gcf().transFigure)
                r5='NewCPK: %s'%NewCPK; plt.text(0.86, 0.85, r5, fontsize=8,color='blue', transform=plt.gcf().transFigure)
        plt.plot(Lowspec_min,Lowspec_max,color='blue')
        plt.plot(Highspec_min,Highspec_max,color='red')
        
        if len(np.unique(sheet_1[boxgroupedx]))<=9:
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), borderaxespad=0., prop={'size': 10})
        elif len(np.unique(sheet_1[boxgroupedx]))>9:
            plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), borderaxespad=0., prop={'size': 6})
        plt.rcParams["axes.edgecolor"] = "0.15"
        plt.rcParams["axes.linewidth"]  = 1.55 
        plt.margins(0.02) # decide how much margin you’d need, for data not to overlap    
        return plt

    def Get_the_header_table(self,loop_count,test_number):
        Table6=['TESSOLVE SEMICONDUCTOR PVT LTD',"PageNumber"]
        Table7=[['Characterization Report',loop_count]]
        TestNumber=test_number
        Header_table= plt.table(cellText=Table7,colLabels=Table6,cellLoc='center',colLoc='center',loc='top',bbox=[-0.08,3.7,1.2,0.22])
        Header_table.set_fontsize(16)
        Header_table.scale(2.6,2.6)
        Header_table.auto_set_font_size(False)
        Header_table.auto_set_column_width(True)
        #t2_data=TestNumbers[loop_count].split(';')[0]+TestNumbers[loop_count].split(';')[1]
        t2='%s' %(TestNumber.split(';')[0]+'_'+TestNumber.split(';')[1])
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
    def Get_the_summary_table(self,Summary_table,Test_no_name,table_column_header):
        Summary_table_=Summary_table.transpose()
        c=[0.1 if i==0 else 0.05 for i in range(len(list(table_column_header)))]
        Data_tbl=plt.table(cellText=[Summary_table_[Test_no_name].values],colWidths=c, colLabels=list(table_column_header),cellLoc='left',colLoc='left',loc='bottom',bbox=[-0.08,-0.6,1.2,0.3])
        Data_tbl.auto_set_font_size(False)
        Data_tbl.set_fontsize(20)
        Data_tbl.auto_set_column_width(True)
        return plt
    def Generate_summary_table1(self,Merged_data,Grouping_column_name,Test_no_name_list):
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
    def Generate_summary_table(self,Data_Table,Test_number_list,Summary_Stat_list):
        ''' This Function takes the data frame and test number list as input and creates the statistic summary table for the same'''
        Data_Table_=Data_Table
        Test_number_list_=Test_number_list
        Summary_Stat_list_=Summary_Stat_list
        self.Stat_item_data=[]
        for i in Summary_Stat_list_:            
            if i=="Min": Min=Data_Table_[Test_number_list_].min();self.Stat_item_data.append(Min.round(5))
            elif i=="Max": Max=Data_Table_[Test_number_list_].max();self.Stat_item_data.append(Max.round(5))
            elif i=="Mean": Mean=Data_Table_[Test_number_list_].mean();self.Stat_item_data.append(Mean.round(5))
            elif i=="Median(P50)": Median=Data_Table_[Test_number_list_].median();self.Stat_item_data.append(Median.round(5))
            elif i=="StdDev": StdDev=Data_Table_[Test_number_list_].std();self.Stat_item_data.append(StdDev.round(5))
            elif i=="P1": P1=Data_Table_[Test_number_list_].quantile(0.01);self.Stat_item_data.append(P1.round(5))
            elif i=="P5": P5=Data_Table_[Test_number_list_].quantile(0.05);self.Stat_item_data.append(P5.round(5))
            elif i=="P10": P10=Data_Table_[Test_number_list_].quantile(0.1);self.Stat_item_data.append(P10.round(5))
            elif i=="P25": P25=Data_Table_[Test_number_list_].quantile(0.25);self.Stat_item_data.append(P25.round(5))
            elif i=="P75": P75=Data_Table_[Test_number_list_].quantile(0.75);self.Stat_item_data.append(P75.round(5))
            elif i=="P90": P90=Data_Table_[Test_number_list_].quantile(0.9);self.Stat_item_data.append(P90.round(5))
            elif i=="P95": P95=Data_Table_[Test_number_list_].quantile(0.95);self.Stat_item_data.append(P95.round(5))
            elif i=="P99": P99=Data_Table_[Test_number_list_].quantile(0.99);self.Stat_item_data.append(P99.round(5))
            elif i=="COUNT": Count=Data_Table_[Test_number_list_].count();self.Stat_item_data.append(Count)
            elif i=="PASS": Pass=Data_Table_[Test_number_list_].min();self.Stat_item_data.append(Pass)
            elif i=="FAIL": Fail=Data_Table_[Test_number_list_].min();self.Stat_item_data.append(Fail)
            elif i=="TOTAL": Total=Data_Table_[Test_number_list_].min();self.Stat_item_data.append(Total)
        
        All_Stat_Summary_Table=DataFrame(self.Stat_item_data,index=Summary_Stat_list_).transpose()
        All_Stat_Summary_Table['Name']=Test_number_list_
        if 'File_Name' in Data_Table_: 
            All_Stat_Summary_Table['File_Name']=[Data_Table_['File_Name'][0] for i in range(len(Test_number_list_))]
            All_Stat_Summary_Table=All_Stat_Summary_Table[list(All_Stat_Summary_Table.columns)[-2:]+list(All_Stat_Summary_Table.columns)[:-2]]
        elif 'File_Name' not in Data_Table_:
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
        if 'File_Name' in All_Stat_Summary_Table: del All_Stat_Summary_Table['File_Name']
        return All_Stat_Summary_Table,All_Stat_Summary_Table.keys()
    def Generate_plots(self,data_table_name,test_number_list,summary_stat_list,plot_list=None,group_by_varible_list=None):
        #Merged_Data=self.Merge_the_data_frames(sheet_1,sheet_2)
        if self.Parent_window!=None:
            self.Raw_Data=self.Parent_window.Loaded_Data_File_Raw_Data[data_table_name]
            self.Data_Table_Name=data_table_name
            Group_by_variable=group_by_varible_list
            Test_number_list_=test_number_list
            Summary_Stat_list_=summary_stat_list
            Plots_List_=plot_list
            if len(Group_by_variable)!=0:Raw_Data_with_Groupby=self.Raw_Data.groupby(Group_by_variable[0])
            elif len(Group_by_variable)==0:Raw_Data_with_Groupby=self.Raw_Data
            '''outputpath=self.Parent_window.Loaded_Data_File_Raw_Data[data_table_name]['File_Name'][0];outputpath=os.path.dirname(outputpath)
            outputfilename=os.path.splitext(self.Parent_window.Loaded_Data_File_Raw_Data[data_table_name]['File_Name'][0])[0];outputfilename=outputfilename'''        
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            outputfilename, sav_type = QFileDialog.getSaveFileName(caption='Export file',directory='',filter="PDF File (*.pdf)", options=options)
            Numberofplotsinpdf=len(Plots_List_)
            Summary_table,Summary_header=self.Generate_summary_table(Data_Table=self.Raw_Data,Test_number_list=Test_number_list_,Summary_Stat_list=Summary_Stat_list_)
            
            if Numberofplotsinpdf>=1:
                pdf_pages = PdfPages(outputfilename+'.pdf')
                with pdf_pages as pdf:
                    Loop_count=0
                    for i in Test_number_list_:
                        Loop_count+=1
                        if self.Raw_Data[i].dtype=='float' or self.Raw_Data[i].dtype=='int64':
                            
                            '''if Numberofplotsinpdf==1:
                                plt.figure(figsize=(20,20))
                                plt.subplot(1,1,1)
                                if 'Box Plot' in Plots_List_:
                                    Table_attached=False
                                    self.Plot_BOX_plot(self.Raw_Data,i,Group_by_variable)
                                elif 'Histogram' in Plots_List_:                        
                                    Table_attached=False
                                    self.Plot_Histogram(self.Raw_Data,Group_by_variable,i)
                                elif 'Line Plot' in Plots_List_:
                                    #plt.subplot(2,1,plt_count);plt_count+=1
                                    self.Plot_Line_plot(self.Raw_Data,i,Group_by_variable)
                                plt.subplots_adjust(left=0.1, right=0.85,top=0.9,bottom=0.2)
                            elif Numberofplotsinpdf==2:                                
                                plt.figure(figsize=(20,20))
                                plt_count=1
                                if 'Box Plot' in Plots_List_:
                                    plt.subplot(Numberofplotsinpdf,1,plt_count);plt_count+=1
                                    self.Plot_BOX_plot(self.Raw_Data,i,Group_by_variable)
                                if  'Histogram' in Plots_List_:
                                    plt.subplot(Numberofplotsinpdf,1,plt_count);plt_count+=1
                                    self.Plot_Histogram(self.Raw_Data,Group_by_variable,i)
                                if  'Line Plot' in Plots_List_:
                                    plt.subplot(Numberofplotsinpdf,1,plt_count);plt_count+=1
                                    self.Plot_Line_plot(self.Raw_Data,i,Group_by_variable)    
                                plt.subplots_adjust(left=0.1, right=0.85,top=0.89,bottom=0.2)
                            elif  Numberofplotsinpdf==3:'''
                            fig = plt.figure(figsize=(20,20))                        
                            #imgplot = plt.imshow('icon_uPN_icon.ico')
                            plt_count=1
                            if 'Box Plot' in Plots_List_:
                                plt.subplot(Numberofplotsinpdf,1,plt_count);plt_count+=1
                                self.Plot_BOX_plot(self.Raw_Data,i,Group_by_variable)
                            if  'Histogram' in Plots_List_:
                                plt.subplot(Numberofplotsinpdf,1,plt_count);plt_count+=1
                                self.Plot_Histogram(self.Raw_Data,Group_by_variable,i)
                            if  'Line Plot' in Plots_List_:
                                plt.subplot(Numberofplotsinpdf,1,plt_count);plt_count+=1
                                self.Plot_Line_plot(self.Raw_Data,i,Group_by_variable)
                            plt.subplots_adjust(left=0.1, right=0.85,top=0.9,bottom=0.2)     
                            #Header
                            #tb=list(Summary_table.loc(i))
                            #DataTable=plt.table(cellText=tb,colWidths=c,colLabels=Summary_header,cellLoc='left',colLoc='left',loc='bottom',bbox=[-0.08,-0.4,1.2,0.3])
                            self.Get_the_summary_table(Summary_table,i,Summary_header)
                            self.Get_the_header_table(Loop_count,test_number=i)
                            plt.subplots_adjust(left=0.1, right=0.85,top=0.9,bottom=0.2)
                            pdf.savefig()
                            plt.close()
                            #progress_bar['value']=(i/len(TestNumbers))*100
                        else:
                            print(i,' column having some issue in the data.  Please make sure no strings are present in the input data columns / Test Numbers')

            self.Parent_window.Messagebox("Generation Sucessful",'info','Completed')
            print('Generation completed')
            #self.close()       