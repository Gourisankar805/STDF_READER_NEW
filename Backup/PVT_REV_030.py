from tkinter import *
from tkinter import ttk
import tkinter, tkinter.filedialog, tkinter.constants 
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import warnings;warnings.simplefilter('ignore')
#%matplotlib inline
import matplotlib.pyplot as plt
import seaborn as sabrn
from matplotlib.backends.backend_pdf import PdfPages
import numpy as np
import pandas as pd
from pandas import ExcelFile
from pandas import DataFrame as df
from docx import Document
from docx.shared import Inches
import win32com,os
import time,datetime
import io,sys,math
import gc
from win32com.client import Dispatch, constants
import matplotlib as mpl
import matplotlib.gridspec as gridspec


def plot_box(dataframename,TestNumber,limitsdataframe):    
    global boxgroupedx
    
    boxgroupedx=Dropdown_variable.get()
    #boxgroupedx='pvt'
    #fig, axes = plt.subplots(nrows=1, ncols=1, figsize=(14, 5))
    #fig, axes1 = plt.subplots(nrows=1, ncols=1, figsize=(14, 3))
    try:        
        box=sabrn.boxplot(data=dataframename,x=boxgroupedx, y=TestNumbers[TestNumber],hue='voltage',width=0.5)
        #g=sabrn.boxplot(data=dataframename,x='pvt', y=TestNumbers[TestNumber],hue='voltage',ax=ax_box,width=0.3)
    except:
        box=sabrn.boxplot(data=dataframename,x=boxgroupedx, y=TestNumbers[TestNumber],hue=boxgroupedx,width=0.5)
    if len(np.unique(sheet_1[boxgroupedx]))<=9:
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), borderaxespad=0., prop={'size': 10})
    elif len(np.unique(sheet_1[boxgroupedx]))>9:
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), borderaxespad=0., prop={'size': 6})
    box.set(xlabel='',ylabel='')
    #plt.title('Box plot')    
    plt.xticks( rotation='vertical',fontsize=6)  
    
    hi_x=[-2,50]
    hi_y=[float(limitsdataframe[TestNumbers[TestNumber]][5]),float(limitsdataframe[TestNumbers[TestNumber]][5])]
    lo_x=[-2,50]
    lo_y=[float(limitsdataframe[TestNumbers[TestNumber]][6]),float(limitsdataframe[TestNumbers[TestNumber]][6])]    
    Table2=FullDataSummaryTable[TestNumber-26]                        
    if Check_box5_check.get()==1:
        NewCPK=Textbox4.get();NewCPK=float(NewCPK)
        if Table2[0][11]<NewCPK and Table2[0][9]!=0:
            Cal_USL=round(Table2[0][7]+(3*Table2[0][9]*NewCPK),5)
            Cal_LSL=round(Table2[0][7]-(3*Table2[0][9]*NewCPK),5)                                
            new_hi_y=[float(Cal_USL),float(Cal_USL)]
            new_lo_y=[float(Cal_LSL),float(Cal_LSL)]
            if Table2[0][12]<NewCPK:
                plt.plot(hi_x,new_hi_y,color='orange', linestyle='dashed')                
                r2='HighLim :%s' %Table2[0][3]; plt.text(0.86, 0.88, r2, fontsize=8,color='blue', transform=plt.gcf().transFigure)
                r7='Cal HighLim : %s'%Cal_USL; plt.text(0.86, 0.84, r7, fontsize=8,color='blue', transform=plt.gcf().transFigure)
            if Table2[0][13]<NewCPK:
                plt.plot(lo_x,new_lo_y,color='orange', linestyle='dashed')
                r1='LowLim : %s'%Table2[0][2]; plt.text(0.86, 0.89, r1, fontsize=8,color='blue', transform=plt.gcf().transFigure)
                r6='Cal LowLim : %s'%Cal_LSL; plt.text(0.86, 0.83, r6, fontsize=8,color='blue', transform=plt.gcf().transFigure)
            plt.text(0.86, 0.69, "- - New Lims", fontsize=10,color='orange', transform=plt.gcf().transFigure)
            r3='unit :%s'%Table2[0][4]; plt.text(0.86 ,0.87, r3, fontsize=8,color='blue', transform=plt.gcf().transFigure)
            r4='CPK : %s'%Table2[0][11]; plt.text(0.86, 0.86, r4, fontsize=8,color='blue', transform=plt.gcf().transFigure)
            r5='NewCPK: %s'%NewCPK; plt.text(0.86, 0.85, r5, fontsize=8,color='blue', transform=plt.gcf().transFigure)
    plt.plot(hi_x,hi_y,color='red')
    plt.plot(lo_x,lo_y,color='blue')
    return plt

def plot_hist(Groupedvariable,TestNumber):    
    Groupedvariable.plot(kind='hist', alpha=1, legend=True,edgecolor = 'black',stacked=True)
    if len(np.unique(sheet_1[boxgroupedx]))<=9:
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), borderaxespad=0., prop={'size': 10})
    elif len(np.unique(sheet_1[boxgroupedx]))>9:
        plt.legend(loc='center left', bbox_to_anchor=(1, 0.5), borderaxespad=0., prop={'size': 6})     
    plt.grid(True)
    maxvalue=Groupedvariable.count().max()
    maxvalue1=maxvalue
    hilimt=float(sheet_2[TestNumbers[TestNumber]][5])
    hilimt1=hilimt
    lowlimt=float(sheet_2[TestNumbers[TestNumber]][6])
    lowlimt1=lowlimt
    Lowspec_min=[lowlimt,lowlimt1]
    Lowspec_max=[0,maxvalue]
    Highspec_min=[hilimt,hilimt1]
    Highspec_max=[0,maxvalue]
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
                
    plt.plot(Lowspec_min,Lowspec_max,color='blue',label="Low Lim")
    plt.plot(Highspec_min,Highspec_max,color='red',label="High lim")    
    plt.rcParams["axes.edgecolor"] = "0.15"
    plt.rcParams["axes.linewidth"]  = 1.55   
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
def _Browse_File():    
    filename = tkinter.filedialog.askopenfilename(parent=PVT_USERFORM,title='Choose a file')
    try:
        if filename!="":
            global sheet_1,sheet_2,TestNumbers,TestNumber, Dropdown_variable
            Textbox1.configure(state=NORMAL)
            Textbox1.delete(first=0,last=END)
            Textbox1.insert(0,filename)
            inputfile=Textbox1.get()
            #global outputfilename
            outputpath=Textbox1.get();outputpath=os.path.dirname(outputpath)
            outputfilename=Textbox3.get();outputfilename=outputpath+'/'+outputfilename            
            Wrkbook=pd.ExcelFile(inputfile)
            sheet_1=pd.read_excel(Wrkbook,sheetname=0)
            sheet_2=pd.read_excel(Wrkbook,sheetname=1) 
            options=sheet_1.columns[0:30]
            Dropdown_variable=StringVar(PVT_USERFORM)
            Dropdown_variable.set(options[0])
            dropdown1 = OptionMenu(PVT_USERFORM, Dropdown_variable ,*options)
            dropdown1.pack()
            dropdown1.place(x=270,y=150)    
            TestNumbers=[]
            TestNumbers=list(sheet_1.columns.values)
            #print(len(TestNumbers))
            Textbox1.configure(state=DISABLED)
            clicked=True
        elif filename=="":
            Textbox1.insert(0,"Please select a file")
    except:
        Textbox1.insert(0,"Please select a file")
    
def _Browse_File1():
    Textbox2.configure(state=NORMAL)
    Textbox2.delete(first=0,last=END)
    filename2 = tkinter.filedialog.askopenfilename(parent=PVT_USERFORM,title='Choose a file')
    Textbox2.insert(0,filename2)
    Textbox2.configure(state=DISABLED)
    clicked=True
    
def Generate_plots():
    global Starttime,Endtime,Table1,FullDataSummaryTable,Table_attached,y
    global Documents,outputpath,Numberoftests,ErrorNumber
    if Check_box5_check.get()==1 and Textbox4.get()=="":
        messagebox.showerror('Error','Please insert the CPK value in the box')        
    else:       
        Starttime=time.time()
        Table1=['TestNum','TestName','SPEC LO','SPEC HI','Unit ','Min','Max','Mean','Median','StdDev','Cp','Cpk','CPKL','CPKU']
        #Table11=['TestNum','TestName','LowLim','HighLim','Unit','Min','Max','Mean','Median','StdDev','Cp','Cpk','CPKU','CPKL','Does CPK Violating']
        if Check_box5_check.get()==0:
            Table11=['TestNum','TestName','SPEC LO','SPEC HI','Unit ','Min','Max','Mean','Median','StdDev','Cp','Cpk','CPKL','CPKU','CPK Violation']
            #Table3=[[TestNumbers[TestNumber].split(';')[0],TestNumbers[TestNumber].split(';')[1],LSL,USL,UNIT,Min,Max,Mean,Median,STDDEV,Cp,CPK,CPKU,CPKL,CPKStats]]
        elif Check_box5_check.get()==1:
            Table11=['TestNum','TestName','SPEC LO','SPEC HI','Unit ','Min','Max','Mean','Median','StdDev','Cp','Cpk','CPKL','CPKU','CPK Violation','NewCpk','Caliculated Low Lim',"CaliculatedHigh Lim"]
            #NewCPK=Textbox4.get();NewCPK=float(NewCPK)
            #Cal_USL=round(Table2[0][7]+(3*Table2[0][9]*NewCPK),5)
            #Cal_LSL=round(Table2[0][7]-(3*Table2[0][9]*NewCPK),5)
            #Table3=[[TestNumbers[TestNumber].split(';')[0],TestNumbers[TestNumber].split(';')[1],LSL,USL,UNIT,Min,Max,Mean,Median,STDDEV,Cp,CPK,CPKU,CPKL,CPKStats,Cal_USL,Cal_LSL]]
        FullDataSummaryTable=[]
        FullDataSummaryTable2=[]
        for i in range(26,len(TestNumbers)):
            try:
                TestNumber=i
                k=sheet_1[TestNumbers[TestNumber]]
                UNIT=sheet_2[TestNumbers[TestNumber]][4]
                USL=float(sheet_2[TestNumbers[TestNumber]][5])
                LSL=float(sheet_2[TestNumbers[TestNumber]][6])
                #print(k)
                Min=k.min()
                Max=k.max()
                Mean= k.mean()
                Median= k.median()
                STDDEV= k.std()                
                try:                    
                    if STDDEV>0:        
                        Cp= (USL-LSL)/(6*STDDEV)
                        CPKU= (USL-Mean)/(3*STDDEV)
                        CPKL= (Mean-LSL)/(3*STDDEV)
                        CPK=min(CPKL,CPKU)
                    elif STDDEV==0:
                        Cp= 'N/A'
                        CPKU= 'N/A'
                        CPKL= 'N/A'
                        CPK='N/A'
                except:
                    pass
                if CPK!='N/A':                    
                    if CPK<1.33:
                        CPKStats='CPK Fail'
                    else:
                        CPKStats='CPK Pass' 
                else:
                    CPKStats='N/A'                    
            except:
                pass
                
        #CPKU='{0:.5f}'.format(CPKU);CPKL='{0:.5f}'.format(CPKL)
        #STDDEV='{0:.4f}'.format(STDDEV)    
            try:                
                Table2=[[TestNumbers[TestNumber].split(';')[0],TestNumbers[TestNumber].split(';')[1],round((LSL),5),round((USL),5),UNIT,round((Min),5),
                         round((Max),5),round((Mean),5),round((Median),5),round((STDDEV),5),round((Cp),5),round((CPK),5),round((CPKL),5),round((CPKU),5)]]
            except:
                Table2=[[TestNumbers[TestNumber].split(';')[0],TestNumbers[TestNumber].split(';')[1],LSL,USL,UNIT,Min,Max,Mean,Median,STDDEV,Cp,CPK,CPKL,CPKU]]
            if Check_box5_check.get()==0:
                #Table11=['TestNum','TestName','LowLim','HighLim','Unit','Min','Max','Mean','Median','StdDev','Cp','Cpk','CPKU','CPKL','Does CPK Violating']
                Table3=[[TestNumbers[TestNumber].split(';')[0],TestNumbers[TestNumber].split(';')[1],LSL,USL,UNIT,Min,Max,Mean,Median,STDDEV,Cp,CPK,CPKL,CPKU,CPKStats]]
            elif Check_box5_check.get()==1:
                #Table11=['TestNum','TestName','LowLim','HighLim','Unit','Min','Max','Mean','Median','StdDev','Cp','Cpk','CPKU','CPKL','Does CPK Violating',"CaliculatedHigh Lim",'Caliculated Low Lim']
                NewCPK=Textbox4.get();NewCPK=float(NewCPK)
                if CPK<NewCPK:
                    if CPKU<NewCPK:                        
                        Cal_USL=round(Table2[0][7]+(3*Table2[0][9]*NewCPK),15)
                    else:
                        Cal_USL=' '
                    if CPKL<NewCPK:                        
                        Cal_LSL=round(Table2[0][7]-(3*Table2[0][9]*NewCPK),15)
                    else:
                        Cal_LSL=' '
                else:
                    Cal_LSL=' '
                    Cal_USL=' '
                Table3=[[TestNumbers[TestNumber].split(';')[0],TestNumbers[TestNumber].split(';')[1],LSL,USL,UNIT,Min,Max,Mean,Median,STDDEV,Cp,CPK,CPKL,CPKU,CPKStats,NewCPK,Cal_LSL,Cal_USL]]
            FullDataSummaryTable.append(Table2)
            FullDataSummaryTable2.append(Table3)
        print('Summary sheet created')
        if Check_box6_check.get()==1:
            Sumrysheet=df(FullDataSummaryTable2[0],columns=Table11)
            for i in range(1,len(FullDataSummaryTable2)+1):
                if i<len(FullDataSummaryTable):
                    Sumrysheet.loc[len(Sumrysheet)]=FullDataSummaryTable2[i][0]
                #print(outputfilename)
            outputpath=Textbox1.get();outputpath=os.path.dirname(outputpath)
            outputfilename=Textbox3.get();outputfilename=outputpath+'/'+outputfilename
            writer = pd.ExcelWriter(outputfilename+'_Summery_sheet.xlsx')
            Sumrysheet.to_excel(writer,'Sheet1')
            #df2.to_excel(writer,'Sheet2')
            writer.save()
            print('Summery sheet exported successfully') 
        if Textbox1.get()!="" and Textbox3.get()!="" and Check_box4_check.get()==1:
            try:
                ExcelApp.Quit()
                WordApp.Quit()
            except:
                pass
            outputpath=Textbox1.get();outputpath=os.path.dirname(outputpath)
            outputfilename=Textbox3.get();outputfilename=outputpath+'/'+outputfilename
            
            Numberofplotsinpdf=0
            if Check_box1_check.get()==1:
                Numberofplotsinpdf+=1
            if Check_box2_check.get()==1:
                Numberofplotsinpdf+=1
            if Check_box3_check.get()==1:
                Numberofplotsinpdf+=1
            if Numberofplotsinpdf>=1:
                pdf_pages = PdfPages(outputfilename+'.pdf')
                
            with pdf_pages as pdf:
                for i in range(26,len(TestNumbers)):
                    plt.cla()
                    if Numberofplotsinpdf==1:
                        fig = plt.figure(figsize=(20,13))
                        #plt.subplot(1,1,1)
                        if Check_box1_check.get()==1:
                            Table_attached=False
                            plot_box(sheet_1,i,sheet_2)
                        elif Check_box2_check.get()==1:
                            x=sheet_1[TestNumbers[i]].groupby(sheet_1[boxgroupedx])
                            Table_attached=False
                            plot_hist(x,i)
                        elif Check_box3_check.get()==1:                            
                            plot_cumulatvie(i)                     
                        plt.subplots_adjust(left=0.1, right=0.85,top=0.9,bottom=0.2)
                        plt.text(0.86, 0.22, "- High Lim", fontsize=10,color='red', transform=plt.gcf().transFigure)
                        plt.text(0.86, 0.20, "- Low Lim", fontsize=10,color='blue', transform=plt.gcf().transFigure)
                        Table2=FullDataSummaryTable[i-26]
                        #TEMPREORY FOR FPC                        
                        '''TNum=str(Table2[0][0])
                        if int(TNum[-1])==2:
                            plt.text(0.55, 0.92, "COLD -40C", fontsize=12,color='blue', fontweight='bold', transform=plt.gcf().transFigure)
                        elif int(TNum[-1])==3:
                            plt.text(0.55, 0.92, "ROOM 25C", fontsize=12,color='blue', fontweight='bold', transform=plt.gcf().transFigure)
                        elif int(TNum[-1])==4:
                            plt.text(0.55, 0.92, "HOT 105C", fontsize=12,color='blue', fontweight='bold', transform=plt.gcf().transFigure)'''
                        #Lables
                        Table1=['TestNum','TestName','SPEC LO','SPEC HI','Unit','Min','Max','Mean','Median','StdDev','Cp','Cpk','CPKL','CPKU']  
    
                        
                        #Parametric table at the bottom
                        c=[0.05, 0.09, 0.05, 0.05, 0.02, 0.05, 0.05, 0.05, 0.05, 0.05,0.05,0.05,0.05,0.05]
                        DataTable=plt.table(cellText=Table2,colLabels=Table1,colWidths=c,cellLoc='left',colLoc='left',loc='bottom',bbox=[-0.08,-0.24,1.2,0.1])
                        #DataTable=plt.table(cellText=Table2,colLabels=Table1,colWidths=c,loc='bottom',bbox=[0.25, -0.3, 0.5, 0.3])
                        DataTable.auto_set_font_size(False)
                        #DataTable.set_fontsize(5.5)
                        DataTable.set_fontsize(17)
                        DataTable.scale(4,4)
                        DataTable.auto_set_column_width(True)                        
                        #Header
                        Table6=['GOURISANKAR_TOOL',"PageNumber"]
                        Table7=[['Characterization Report',i-25]]
                        Header_table= plt.table(cellText=Table7,colLabels=Table6,cellLoc='center',colLoc='center',loc='top',bbox=[-0.08, 1.06,1.2,0.08])
                        Header_table.set_fontsize(16)
                        Header_table.scale(2.6,2.6)
                        Header_table.auto_set_font_size(False)
                        Header_table.auto_set_column_width(True)
                        t2='%s | %s' %(Table2[0][0],Table2[0][1])
                        plt.text(0.10, 0.92, t2, style='normal',fontsize=18,transform=plt.gcf().transFigure,bbox={'facecolor':'none', 'alpha':0.5, 'pad':5})
                        #fig=plot_box(sheet_1,i,sheet_2)
                        #pdf_pages.savefig(fig)
                        #plt.tight_layout()
                        pdf.savefig()                    
                        plt.close()                        
                    elif Numberofplotsinpdf==2:
                        if (Check_box2_check.get()==1 and Check_box1_check.get()==1):
                            Table_attached=False
                        else:
                            Table_attached=True
                        boxplotted=False
                        cumulativeplotted=False
                        histogramplotted=False
                        fig = plt.figure(figsize=(20,14))
                        plt.subplot(2,1,1)
                        if Check_box1_check.get()==1 and boxplotted==False:
                            Table_attached=True
                            plot_box(sheet_1,i,sheet_2)
                            Table_attached=False
                            boxplotted=True
                        elif Check_box2_check.get()==1 and histogramplotted==False:
                            x=sheet_1[TestNumbers[i]].groupby(sheet_1[boxgroupedx])                            
                            plot_hist(x,i)                            
                            histogramplotted=True
                        elif Check_box3_check.get()==1 and cumulativeplotted==False:
                            plot_cumulatvie(i)
                            cumulativeplotted=True                            
                        plt.subplot(2,1,2)                        
                        if Check_box1_check.get()==1 and boxplotted==False:
                            plot_box(sheet_1,i,sheet_2)
                            boxplotted=True
                        elif Check_box2_check.get()==1 and histogramplotted==False:
                            x=sheet_1[TestNumbers[i]].groupby(sheet_1[boxgroupedx])
                            plot_hist(x,i)
                            Table_attached=True
                            histogramplotted=True
                        elif Check_box3_check.get()==1 and cumulativeplotted==False:
                            plot_cumulatvie(i)
                            cumulativeplotted=True                            
                        boxplotted=False
                        cumulativeplotted=False
                        histogramplotted=False                        
                        plt.subplots_adjust(left=0.1, right=0.85,top=0.9,bottom=0.2)
                        plt.text(0.86, 0.54, "- High Lim", fontsize=10,color='red', transform=plt.gcf().transFigure)
                        plt.text(0.86, 0.52, "- Low Lim", fontsize=10,color='blue', transform=plt.gcf().transFigure)
                        Table2=FullDataSummaryTable[i-26]
                        '''#TEMPREORY FOR FPC                        
                        TNum=str(Table2[0][0])
                        if int(TNum[-1])==2:
                            plt.text(0.55, 0.92, "COLD -40C", fontsize=12,color='blue', fontweight='bold', transform=plt.gcf().transFigure)
                        elif int(TNum[-1])==3:
                            plt.text(0.55, 0.92, "ROOM 25C", fontsize=12,color='blue', fontweight='bold', transform=plt.gcf().transFigure)
                        elif int(TNum[-1])==4:
                            plt.text(0.55, 0.92, "HOT 105C", fontsize=12,color='blue', fontweight='bold', transform=plt.gcf().transFigure)'''
                        #Lables
                        Table1=['TestNum','TestName','SPEC LO','SPEC HI','Unit','Min','Max','Mean','Median','StdDev','Cp','Cpk','CPKL','CPKU']  
                        #Parametric table at the bottom
                        c=[0.05, 0.09, 0.05, 0.05, 0.02, 0.05, 0.05, 0.05, 0.05, 0.05,0.05,0.05,0.05,0.05]
                        #DataTable=plt.table(cellText=Table2,colLabels=Table1,colWidths=c,cellLoc='left',colLoc='left',loc='bottom',bbox=[-0.08, -0.24,1.2,0.1])
                        DataTable=plt.table(cellText=Table2,colLabels=Table1,colWidths=c,cellLoc='left',colLoc='left',loc='bottom',bbox=[-0.08, -0.4,1.2,0.3])
                        DataTable.auto_set_font_size(False)
                        #DataTable.set_fontsize(5.5)
                        DataTable.set_fontsize(17)
                        DataTable.scale(4,4)
                        DataTable.auto_set_column_width(True)
                        #Header
                        Table6=['GOURISANKAR_TOOL',"PageNumber"]
                        Table7=[['Characterization Report',i-25]]                        
                        Header_table= plt.table(cellText=Table7,colLabels=Table6,cellLoc='center',colLoc='center',loc='top',bbox=[-0.08, 2.32,1.2,0.15])#,bbox=[-0.08, 3.61,1.2,0.22]
                        Header_table.set_fontsize(16)
                        Header_table.scale(2.6,2.6)
                        Header_table.auto_set_font_size(False)
                        Header_table.auto_set_column_width(True)
                        t2='%s | %s' %(Table2[0][0],Table2[0][1])
                        plt.text(0.10, 0.92, t2, style='normal',fontsize=18,transform=plt.gcf().transFigure,bbox={'facecolor':'none', 'alpha':0.5, 'pad':5})
                        #fig=plot_box(sheet_1,i,sheet_2)
                        #pdf_pages.savefig(fig)
                        #plt.tight_layout()
                        pdf.savefig()                    
                        plt.close()
                    elif Numberofplotsinpdf==3:
                        if Check_box1_check.get()==1 and Check_box2_check.get()==1 and Check_box3_check.get()==1:
                            Table_attached=True
                        else:
                            Table_attached=False
                        fig = plt.figure(figsize=(20,20))
                        
                        #imgplot = plt.imshow('icon_uPN_icon.ico')
                        plt.subplot(3,1,1)
                        plot_box(sheet_1,i,sheet_2)
                        
                        x=sheet_1[TestNumbers[i]].groupby(sheet_1[boxgroupedx])
                        plt.subplot(3,1,2)
                        plot_hist(x,i)
                        plt.subplot(3,1,3)
                        plot_cumulatvie(i)
                        plt.subplots_adjust(left=0.1, right=0.85,top=0.9,bottom=0.2)                        
                        plt.text(0.86, 0.68, "- High Lim", fontsize=10,color='red', transform=plt.gcf().transFigure)
                        plt.text(0.86, 0.67, "- Low Lim", fontsize=10,color='blue', transform=plt.gcf().transFigure)
                        Table2=FullDataSummaryTable[i-26]
                        #TEMPREORY FOR FPC                        
                        '''TNum=str(Table2[0][0])#;print(TNum,TNum[-1])
                        if int(TNum[-1])==2:
                            plt.text(0.55, 0.92, "COLD -40C", fontsize=12,color='blue', fontweight='bold', transform=plt.gcf().transFigure)
                        elif int(TNum[-1])==3:
                            plt.text(0.55, 0.92, "ROOM 25C", fontsize=12,color='blue', fontweight='bold', transform=plt.gcf().transFigure)
                        elif int(TNum[-1])==4:
                            plt.text(0.55, 0.92, "HOT 105C", fontsize=12,color='blue', fontweight='bold', transform=plt.gcf().transFigure)'''
                        #lables
                        Table1=['TestNum','TestName','SPEC LO','SPEC HI','Unit','Min','Max','Mean','Median','StdDev','Cp','Cpk','CPKL','CPKU']  
                        #Parametric table at the bottom
                        c=[0.05, 0.09, 0.05, 0.05, 0.02, 0.05, 0.05, 0.05, 0.05, 0.05,0.05,0.05,0.05,0.05]                        
                        DataTable=plt.table(cellText=Table2,colLabels=Table1,colWidths=c,cellLoc='left',colLoc='left',loc='bottom',bbox=[-0.08, -0.4,1.2,0.3])
                        DataTable.auto_set_font_size(False)                        
                        DataTable.set_fontsize(17)
                        DataTable.scale(4,4)
                        DataTable.auto_set_column_width(True) 
                        #Header
                        Table6=['GOURISANKAR_TOOL',"PageNumber"]
                        Table7=[['Characterization Report',i-25]]                        
                        Header_table= plt.table(cellText=Table7,colLabels=Table6,cellLoc='center',colLoc='center',loc='top',bbox=[-0.08, 3.61,1.2,0.22])#,bbox=[0, 3.61,1,0.22])
                        Header_table.auto_set_font_size(False)
                        Header_table.set_fontsize(16)
                        Header_table.scale(2.6,2.6)
                        #Header_table.auto_set_font_size(False)
                        Header_table.auto_set_column_width(True)                        
                        #Test Number at the top
                        t2='%s | %s' %(Table2[0][0],Table2[0][1])
                        plt.text(0.10, 0.92, t2, style='normal',fontsize=18,transform=plt.gcf().transFigure,bbox={'facecolor':'none', 'alpha':0.5, 'pad':5})
                        pdf.savefig()
                        plt.close() 
                    gc.collect()
                    if (i-26) %100==0 and i>=100: time.sleep(0.0003);print('%s tests completed'%(i-26))
            #pdf_pages.close()
            Endtime=time.time();Endtime=Endtime-Starttime
            if Endtime<=3600:
                Endtime=math.ceil(Endtime/60)#;Endtime=math.ceil(Endtime)
                Endtime=str(Endtime)+'Mins'
            else:
                Endtime=math.ceil(Endtime/3600);Endtime=str(Endtime)+'Hrs'                    
            messagebox.showinfo('Done','Generation completed\n Time Taken is %s'%Endtime)
            PVT_USERFORM.destroy()
        else:
            messagebox.showerror('Error','Please select a files and make sure you gave the output file name')    

def Enable_or_Disable():    
    if Check_box5_check.get()==0:
        Textbox4.config(state='disabled')
        Textbox4.update()
    elif Check_box5_check.get()==1:
        Textbox4.config(state='normal')
        Textbox4.update()    

#Userform
#Userform
PVT_USERFORM=Tk()
PVT_USERFORM.geometry("530x230")
#PVT_USERFORM.wm_iconbitmap('C:/Users/2401/Desktop/python/sravn/Python/02-07/Tes_logo.ico')
PVT_USERFORM.title("PVT")
l=LabelFrame(PVT_USERFORM,text="SELECT FILES",width=520,height=200,font=10,bd=3)
l.pack( expand="yes")
l.place(x=2,y=25)

custName = StringVar(None)
custName2 = StringVar(None)
Textbox1 = Entry(l, textvariable=custName)
#Textbox1.grid(column=0,row=1,sticky='W')
Textbox1.pack(padx = 20, pady = 20,anchor='n')
Textbox1.place(y = 5, x = 80, width = 350, height = 20)
browsebutton = Button(l, text="Browse", command=_Browse_File,width=7)
browsebutton.pack(side=RIGHT)   
browsebutton.place(y = 1, x = 440)
label2=Label(l, text="Input File1:")
label2.pack()
label2.place(y = 3, x = 2)

#label5=Label(l, text="Input Field 1:")
#label5.pack()
#label5.place(y = 3, x = 2)
#custName = StringVar(None)
label4=Label(l, text="O/P FileName:")
label4.pack()
label4.place(y = 65, x = 0)

Textbox3= Entry(l)
Textbox3.pack(padx = 20, pady = 20,anchor='n')
Textbox3.place(y = 65, x = 80, width = 350, height = 20)

Textbox4= Entry(l)
Textbox4.pack(padx = 20, pady = 20,anchor='n')
Textbox4.place(y = 152, x = 20, width = 50, height = 20)

#Check Boxes
Check_box1_check = IntVar()
Checkbox1=Checkbutton(PVT_USERFORM,text="BoxPlot",variable = Check_box1_check,onvalue = 1, offvalue = 0)
Checkbox1.pack()
Checkbox1.place(x=8,y=150)
Check_box2_check = IntVar()
Checkbox2=Checkbutton(PVT_USERFORM,text="Histogram",variable = Check_box2_check,onvalue = 1, offvalue = 0)
Checkbox2.pack()
Checkbox2.place(x=75,y=150)
Check_box3_check = IntVar()
Checkbox3=Checkbutton(PVT_USERFORM,text="Cumulative",variable = Check_box3_check,onvalue = 1, offvalue = 0)
Checkbox3.pack()
Checkbox3.place(x=160,y=150)
Check_box4_check = IntVar()
Checkbox4=Checkbutton(PVT_USERFORM,text="PLOTS WITH SUMMARY",variable = Check_box4_check,onvalue = 1, 
                      offvalue = 0,command=Enable_or_Disable)
Checkbox4.pack()
Checkbox4.place(x=2,y=2)
Checkbox4.select()
Check_box5_check = IntVar()
Checkbox5=Checkbutton(PVT_USERFORM,text="Proposed Cpk",variable = Check_box5_check,onvalue = 1, offvalue = 0,
                      command=Enable_or_Disable)
Checkbox5.pack()
Checkbox5.place(x=8,y=172)

Check_box6_check = IntVar()
Checkbox6=Checkbutton(PVT_USERFORM,text="Export summery table",variable = Check_box6_check,onvalue = 1, offvalue = 0,
                     command=Enable_or_Disable)
Checkbox6.pack()
Checkbox6.place(x=110,y=172)
'''
Textbox5= Entry(l)
Textbox5.pack(padx = 20, pady = 20,anchor='n')
Textbox5.place(y = 152, x = 137, width = 50, height = 20)
'''
Checkbox5.deselect()
#Checkbox6.deselect()
#Okay button
ok=Button(l,text="OK",command=Generate_plots)
ok.pack()
ok.place(x=368,y=125,width=50)

#lable5input = StringVar()
#label5=Label(PVT_USERFORM,textvariable=lable5input, relief=RAISED)
#lable5input.set("Ploting not started yet")
#label5.pack()
#Quit button
quit=Button(l,text="Quit",command=PVT_USERFORM.destroy)
quit.pack()
quit.place(x=430,y=125,width=50)
Enable_or_Disable()
PVT_USERFORM.mainloop()
