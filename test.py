from pandas import *
import pandas as pd
import scipy.stats
import matplotlib.pyplot as plt
df = pd.read_csv('C:\\Users\\USER\Desktop\\s1617.csv', low_memory=False,usecols=[2,3,4,5])
total_goal_home = (df['FTHG'].sum())
total_goal_away = (df['FTAG'].sum())
gpg_home = total_goal_home/370
gpg_away = total_goal_away/370
home_team = input()
away_team = input()

#predicting home goal

#home att strength
df1 = df[(df.HomeTeam == home_team)]
httg = df1['FTHG'].sum()
div = httg/19
home_att_strg = div/gpg_home
#away defense strength
df2 = df[(df.AwayTeam == away_team)]
attg = df2['FTHG'].sum()
div1 = attg/19
away_def_strg = div1/gpg_home

home_prob = home_att_strg * away_def_strg * gpg_home

#predicting away goal

#away att strength
attg1 = df2['FTAG'].sum()
div2 = attg1/19
away_att_strg = div2/gpg_away
#home defense strength
httg1 = df1['FTAG'].sum()
div3 = httg1/19
home_def_strg = div3/gpg_away

away_prob = away_att_strg * home_def_strg * gpg_away

print(home_prob)
print(away_prob)

print(home_team)
for i in range(0,4):
    print (i , scipy.stats.distributions.poisson.pmf(i,home_prob)*100)

print(away_team)
for j in range(0,4):
    print (j , scipy.stats.distributions.poisson.pmf(j,away_prob)*100)




