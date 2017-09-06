import os
import sklearn
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np
from pandas import *
import pandas as pd
from sklearn import datasets, linear_model
df = pd.read_csv('C:\Users\USER\Desktop\Full.csv',low_memory=False,usecols=[6,25,22,3,43,44,50])
a = raw_input()
b = raw_input()
df1 = df[(df.away_team == a) & (df.home_team == b)]
#df2 = df[(df.away_team == 'Arsenal') & (df.home_team == 'Chelsea')]
#df1 = df[(df.away_team == 'Leicester') | (df.home_team == 'Leicester')]
print df1

x =  DataFrame({'val': [0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09]})
y = df1.home_ratio.values

#x = x.reshape(len(df1.index), 1)
y = y.reshape(len(df1.index), 1)

#x_tes = x.reshape(len(df1.index), 1)
#y_tes = y.reshape(len(df1.index), 1)

regr = linear_model.LinearRegression()
regr.fit(x, y)
plt.scatter(x, y,  color='black')
plt.plot(x, regr.predict(x), color='blue', linewidth=3)
print regr.predict(0.10)
plt.xticks(())
plt.yticks(())
plt.show()


