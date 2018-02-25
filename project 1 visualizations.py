# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:36:48 2018

@author: zhangyuchen
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 01:19:17 2018

@author: zhangyuchen
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

#prepare data
file = 'https://s3.cn-north-1.amazonaws.com.cn/static-documents/nd002/stroopdata.csv'
data = pd.read_csv(file)

#add one colunm Incongruent - Congruent
data["Diff (In - Con)"] = data["Incongruent"] - data["Congruent"]

#画直方图
fig, ax = plt.subplots(3, 1, figsize=(6,8),sharex='col', sharey='row')
fig.text(0.5, 0.04, 'Time (s)', ha='center', va='center', fontsize=12)
fig.text(0.06, 0.5, 'Frequency', ha='center', va='center', rotation='vertical', fontsize=12)
for i in range(3):
    j = list(data)[i]
    dt = data[j]
    ax[i].hist(dt)
    ax[i].set_title(j + ' Time (fixed bin size)')


#画概率分布图
#for i in list(data):
#    dt = data[i]
#    sns.set_style('dark')  
#    n = int((max(dt) - min(dt)) / 2)
#    sns.distplot(dt, bins=8, hist=True, kde=False, vertical=False)
#    plt.xlabel('Time (s)', fontsize=12)
#    plt.ylabel('Frequency', fontsize=12)
#    plt.title(i + ' Time (fixed bin size)')

fig = plt.figure() 
sns.set(style="white", palette="muted", color_codes=True)
colors = ['r','b','y'] 
for i,c in list(zip(list(data),colors)):
    dt = data[i]
    ax=sns.kdeplot(dt,color=c)
    
plt.xlabel('Time (s)', fontsize=12)
plt.ylabel('Probability Density', fontsize=12)

#画散点图
fig = plt.figure()   
x = data['Congruent']
y = data['Incongruent']
plt.scatter(x,y)  
plt.xlabel('time - congruent condition (s)',fontsize = 12)  
plt.ylabel('time - incongruent condition (s)',fontsize = 12)