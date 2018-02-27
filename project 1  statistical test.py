# -*- coding: utf-8 -*-
"""
Created on Sun Feb 25 22:39:04 2018

@author: zhangyuchen
"""

import pandas as pd
from numpy import mean, std
import math
import scipy
from scipy import stats

# load data
file = 'https://s3.cn-north-1.amazonaws.com.cn/static-documents/nd002/stroopdata.csv'
data = pd.read_csv(file)
n = len(data) #sample size
factor = math.sqrt(n/(n-1)) #correction factor

data["Diff (In - Con)"] = data["Incongruent"] - data["Congruent"]

#mean
Diff_mean = mean(data["Diff (In - Con)"])

#unbiased standard deviation
Diff_std = std(data["Diff (In - Con)"])*factor

t_statistics = Diff_mean/Diff_std*math.sqrt(n)
p_value = 1 - stats.t.cdf(t_statistics, df = n-1)

sta,p = scipy.stats.ttest_1samp(data["Diff (In - Con)"], 0)
print ("t statistics is: ", t_statistics)
print ("p value is: ", p_value)
print(sta,p)
