# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:34:08 2018

@author: zhangyuchen
"""

import pandas as pd
import numpy as np
from numpy import mean, median, ptp, var, std
import math
#read data
file = 'https://s3.cn-north-1.amazonaws.com.cn/static-documents/nd002/stroopdata.csv'
data = pd.read_csv(file)

#add one colunm Incongruent - Congruent
data["Diff (In - Con)"] = data["Incongruent"] - data["Congruent"]

n = len(data) #sample size
factor = math.sqrt(n/(n-1)) #correction factor

#calculate statistics
#########集中趋势测量############################################
#mean
Con_mean = mean(data["Congruent"])
In_mean = mean(data["Incongruent"])
Diff_mean = mean(data["Diff (In - Con)"])

d1 = [Con_mean,Con_mean,Diff_mean]

#median
Con_median = median(data["Congruent"])
In_median = median(data["Incongruent"])
Diff_median = median(data["Diff (In - Con)"])

d2 = [Con_median,In_median,Diff_median]

##########变异测量##############################################
#极差
Con_ptp = ptp(data["Congruent"])
In_ptp = ptp(data["Incongruent"])
Diff_ptp = ptp(data["Diff (In - Con)"])

d3 = [Con_ptp,In_ptp,Diff_ptp]

#标准差
Con_std = std(data["Congruent"])*factor
In_std = std(data["Incongruent"])*factor
Diff_std = std(data["Diff (In - Con)"])*factor

d4 = [Con_std,In_std,Diff_std]

#变异系数
Con_n = Con_mean/Con_std
In_n = In_mean/In_std
Diff_n = Diff_mean/Diff_std

d5 = [Con_n,In_n,Diff_n]

index = list(data)
output = pd.DataFrame(list(zip(d1,d2,d3,d4,d5)), index = index, columns = ['mean','median','range','standard deviation','coefficient of variation'])
for i in list(output):
    print(i, '\n', output[i], '\n')