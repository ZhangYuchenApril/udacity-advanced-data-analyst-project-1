# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:39:04 2018

@author: zhangyuchen
"""

import pandas as pd
from numpy import mean, std
import math
from scipy import stats

# load data
file = 'https://s3.cn-north-1.amazonaws.com.cn/static-documents/nd002/stroopdata.csv'
data = pd.read_csv(file)
n = len(data) #sample size
factor = math.sqrt(n/(n-1)) #correction factor

#mean
Con_mean = mean(data["Congruent"])
In_mean = mean(data["Incongruent"])

#unbiased standard deviation
Con_std = std(data["Congruent"])*factor
In_std = std(data["Incongruent"])*factor

#print(factor, Con_mean, In_mean, Con_std, In_std)
(statistic, pvalue) = stats.ttest_ind_from_stats(mean1=Con_mean, std1=Con_std, nobs1=n, 
                                                 mean2=In_mean, std2=In_std, nobs2=n)

print ("t statistic is: ", statistic)
print ("pvalue is: ", pvalue)

# Don't assume equal population variance
(statistic, pvalue) = stats.ttest_ind_from_stats(mean1=Con_mean, std1=Con_std, nobs1=n, 
                                                 mean2=In_mean, std2=In_std, nobs2=n, equal_var=False)

print ("t statistic is: ", statistic)
print ("pvalue is: ", pvalue)