import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import randint
import statistics



df = pd.ExcelFile('E:/tasks/20-02-19/sample inputs/5974C_1HT9316_DP4279_02_FPC1021_5974C_V2.0_20150525_20160705_16h10.xlsx').parse('Sheet1') #you could add index_col=0 if there's an index

wafer_id=df['wafer_id'].tolist()
w_unique=[]
for q in wafer_id:
    if q not in w_unique:
            w_unique.append(q)
colors = []
for i in range(100):
    colors.append('#'+'%06X' % randint(0, 0xFFFFFF))

gk = df.groupby('wafer_id')
d = {}
for t in range (0,len(w_unique)):
        d[t]=pd.DataFrame(gk.get_group(w_unique[t]))
        sbin = d[t]['sbin'].tolist();hbin= d[t]['hbin'].tolist()
        s_unique=[];h_unique=[];sbin_count=[];sxtik=[];hbin_count=[];hxtik=[]
        for s in sbin:
            if s not in s_unique:
                    s_unique.append(s)
        for h in hbin:
            if h not in h_unique:
                    h_unique.append(h)
        for i in range (0,len(s_unique)):
            q=sbin.count(s_unique[i])
            sbin_count.append(q)
            sxtik.append('B'+str(s_unique[i]))
        if len(sxtik)<10:
            fig = plt.figure(figsize=(6,5),dpi=150)
        else:
            fig = plt.figure(figsize=(int(len(sxtik)/2),5),dpi=150)
        ax = fig.add_subplot(1,1,1)
        #ax.set_ylim(0,7000)
        plt.bar(sxtik, sbin_count,0.8,color=colors[t])
        for i,j in zip(sxtik,sbin_count):
            ax.annotate(str(j),xy=(i,j), fontsize=7, verticalalignment='right', horizontalalignment='center')
        plt.title("SOFTWARE BINNING FOR WAFER ID "+str(w_unique[t]))
        plt.savefig("sft_wafer ID %s.png" %w_unique[t])
        plt.show()
        
        for i in range (0,len(h_unique)):
            q=hbin.count(h_unique[i])
            hbin_count.append(q)
            hxtik.append('B'+str(h_unique[i]))
        if len(hxtik)<10:
            fig = plt.figure(figsize=(6,5),dpi=150)
        else:
            fig = plt.figure(figsize=(int(len(hxtik)/2),5),dpi=150)
        ax = fig.add_subplot(1,1,1)
        #ax.set_ylim(0,7000)
        plt.bar(hxtik, hbin_count,0.8,color=colors[t])
        for i,j in zip(hxtik,hbin_count):
            ax.annotate(str(j),xy=(i,j), fontsize=7, verticalalignment='right', horizontalalignment='center')
        plt.title("HARDWARE BINNING FOR WAFER ID "+str(w_unique[t]))
        plt.savefig("hrd_wafer ID %s.png" %w_unique[t])
        plt.show()



