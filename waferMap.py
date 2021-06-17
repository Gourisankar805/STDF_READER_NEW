import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from random import randint
import statistics


#df = pd.ExcelFile('E:/tasks/06-09/sample inputs/5974C_1HT9316_DP4279_02_FPC1021_5974C_V2.0_20150525_20160705_16h10.xlsx').parse('Sheet1') #you could add index_col=0 if there's an index
df=pd.read_csv('D:/2360/Scripting_data/Python_trail/Stdffiles/Trail_data/Full_Rec_Summary.csv')
x = df['XCo_ord'].tolist();y = df['YCo_ord'].tolist();sbin = df['SoftBin'].tolist();hbin= df['HardBin'].tolist()
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

'''circle1=plt.Circle((medx,medy),((medx)),color='#cccccc')
plt.gcf().gca().add_artist(circle1)'''
'''circle2=plt.Circle((20,3.2),0.7,color='white')
plt.gcf().gca().add_artist(circle2)'''
#plt.scatter(x, y, s=sbin, marker='s',edgecolors=None,c=['r','g','b'],linewidths=None, alpha=0.99)
'''for i in range(1,len(sbin)):
    if sbin[i]==1:
        plt.plot(x,y,'s', data=sbin, markersize=7,mec='black',c='g')
    else:
        plt.plot(x,y,'s', data=sbin, markersize=7,mec='black',c='r')'''



#for softbin
'''for i,j,k in zip(x,y,sbin):
    if k==1:
        if count==0:
            plt.plot(i,j,'s', markersize=12.6,label='Bin1',mec='black',c='#55ff10')
            count+=1
        else:
            plt.plot(i,j,'s',  markersize=12.6,mec='black',c='#55ff10')

    else:
        q=[]
        for z in range(0,len(s_unique)):
            t=s_unique[z]
            q.append(colors[z])
            if k==t:
                plt.plot(i,j,'s', data=k,markersize=12.6,mec='black',c=colors[z])
                plt.gca().set(xlabel='x', ylabel='y')

        r=0.82
        for h in range(0,len(s_unique)):
            plt.text(0.85, r, ("BIN"+str(s_unique[h])),family="arial", fontsize=5,color=colors[h], transform=plt.gcf().transFigure)
            r-=0.005      

    ax.annotate(str(k),xy=(i,j), fontsize=5.3,verticalalignment='center', horizontalalignment='center')'''
    
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

