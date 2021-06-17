import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import randint
import statistics


df = pd.ExcelFile('C:/Users/2360/Desktop/Bharatesh/Marginal_Dies_Wafer202123_SBIN37.xlsx').parse('Sheet1') #you could add index_col=0 if there's an index
x = df['x'].tolist();y = df['y'].tolist();sbin = df['sbin'].tolist();hbin= df['hbin'].tolist()
s_unique=[];h_unique=[]
for s in sbin:
    if s not in s_unique:
        if s!=1:
            s_unique.append(s)
for h in hbin:
    if h not in h_unique:
        if h!=1:
            h_unique.append(h)
medx=m=statistics.median(x);medy=m=statistics.median(y)
mx=max(x)+10;my=max(y)+10
count=0
#cmap = plt.get_cmap('viridis')
#colors = cmap(np.linspace(0, 1, len(s_unique)))
'''filepath="E:/tasks/06-09/INPUT_FOR_WAFER_MAP.xlsx"

Wrkbook=pd.ExcelFile(filepath)'''
colors = []
for i in range(200):
    colors.append('#'+'%06X' % randint(0, 0xFFFFFF))

fig=plt.figure(figsize=((medx/2),(medy/2)),dpi=200)
ax = fig.add_subplot(111)

circle1=plt.Circle((medx,medy),((medx)),color='#cccccc')
plt.gcf().gca().add_artist(circle1)
#for hardbin
for i,j,k in zip(x,y,hbin):
    if k==1:
        if count==0:
            plt.plot(i,j,'s', markersize=12.6,label='Bin1',mec='black',c='#55ff10')
            count+=1
        else:
            plt.plot(i,j,'s',  markersize=12.6,mec='black',c='#55ff10')

    else:
        q=[]
        for z in range(0,len(h_unique)):
            t=h_unique[z]
            q.append(colors[z])
            if k==t:
                plt.plot(i,j,'s', data=k,markersize=12.6,mec='black',c=colors[z])
                plt.gca().set(xlabel='x', ylabel='y')

        r=0.82
        for h in range(0,len(h_unique)):
            plt.text(0.85, r, ("BIN"+str(h_unique[h])),family="arial", fontsize=5,color=colors[h], transform=plt.gcf().transFigure)
            r-=0.009      

    ax.annotate(str(k),xy=(i,j), fontsize=5.3,verticalalignment='center', horizontalalignment='center')
    
    
'''for i,j,k in zip(x,y,sbin):
        ax.annotate(str(k),xy=(i,j), fontsize=5.3,verticalalignment='center', horizontalalignment='center')'''
        


plt.xlim(0, mx)
plt.ylim(0, my)
plt.legend()
plt.savefig('samples.png')
plt.show()

