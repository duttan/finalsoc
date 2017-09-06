import matplotlib.pyplot as plt

from sklearn import datasets
from sklearn import svm
import random

from pandas import DataFrame, read_csv
import pandas as pd
import sys
import matplotlib
import numpy as np

from sklearn import linear_model

from sklearn import svm

import time

Location =r'C:\Users\USER\Desktop\Form.csv'
ef = pd.read_csv(Location)

ef = pd.read_csv(Location, header=None)
ef = pd.read_csv(Location, names=['fixture', 'form'])
import os

X_train = ef.fixture[:14]
Y_train = ef.form[:14]

g = X_train
h = Y_train
regr = linear_model.LinearRegression()

regr.fit(X_train.reshape(len(X_train), 1), Y_train)
plt.show()
form2 = regr.predict(16)[0]
form1 = regr.predict(1)[0]

Location = r'C:\Users\USER\Desktop\FullData.csv'
df = pd.read_csv(Location)
df = pd.read_csv(Location, header=None)
df = pd.read_csv(Location,
                 names=['Name', 'Nationality', 'National_Position', 'National_Kit', 'Club', 'Club_Position', 'Club_Kit',
                        'Club_Joining', 'Contract_Expiry', 'Rating', 'Height', 'Weight', 'Preffered_Foot', 'Birth_Date',
                        'Age', 'Preffered_Position', 'Work_Rate', 'Weak_foot', 'Skill_Moves', 'Ball_Control',
                        'Dribbling', 'Marking', 'Sliding_Tackle', 'Standing_Tackle', 'Aggression', 'Reactions',
                        'Attacking_Position', 'Interceptions', 'Vision', 'Composure', 'Crossing', 'Short_Pass',
                        'Long_Pass', 'Acceleration', 'Speed', 'Stamina', 'Strength', 'Balance', 'Agility', 'Jumping',
                        'Heading', 'Shot_Power', 'Finishing', 'Long_Shots', 'Curve', 'Freekick_Accuracy', 'Penalties',
                        'Volleys', 'GK_Positioning', 'GK_Diving', 'GK_Kicking', 'GK_Handling', 'GK_Reflexes'])
import os


# code
def getRate(player_name):
    for b in range(1, df.shape[0]):
        if df.Name[b] == player_name:
            return b


a_attack = []
a_defence = []
a_mid = []
h_attack = []
h_defence = []
h_mid = []

Location = r'/home/cena/Documents/projectFoot/apsv.csv'
dataf = pd.read_csv(Location)
dataf = pd.read_csv(Location, header=None)
dataf = pd.read_csv(Location, names=['V1', 'V2'])
import os

clf = svm.SVC(kernel='rbf', gamma=0.001, C=100)
x, y = dataf.V1[1:11], dataf.V2[1:11]
clf.fit(x.reshape(len(x), 1), y)
x = clf.predict(dataf.V1[9])

mid_apsv = 0
att_apsv = 0
defence_apsv = 0

for n in range(1, dataf.shape[0]):
    if ((dataf.V1[n] % 4 == 0 and dataf.V1[n] / 4 > 4) or (dataf.V1[n] % 10 == 0 and dataf.V1[n] / 10 > 10) or (
                dataf.V1[n] % 16 == 0 and dataf.V1[n] / 16 > 16)):
        x = clf.predict(dataf.V1[n])
        mid_apsv = x[0]
    elif ((dataf.V1[n] % 5 == 0 and dataf.V1[n] / 5 > 5) or (dataf.V1[n] % 11 == 0 and dataf.V1[n] / 11 > 11) or (
                dataf.V1[n] % 17 == 0 and dataf.V1[n] / 17 > 17)):
        x = clf.predict(dataf.V1[n])
        att_apsv = x[0]


def classify(player_position, side, ind):
    if (side == "away"):
        if "W" in player_position or "ST" in player_position:
            a_attack.append(int(ind))
        elif "B" in player_position:
            a_defence.append(int(ind))
        elif "M" in player_position:
            a_mid.append(int(ind))
    elif (side == "home"):
        if "W" in player_position or "ST" in player_position:
            h_attack.append(int(ind))
        elif "B" in player_position:
            h_defence.append(int(ind))
        elif "M" in player_position:
            h_mid.append(int(ind))


h_name = input("Enter team1 name:")
a_name = input("Enter team2 name:")

tot_length = df.shape[0]

a_squad = []
h_squad = []

buff = []

posbuff_a = []

posbuff_h = []

for i in range(1, tot_length):
    if len(a_squad) <= 10:
        if ((a_name == df.Club[i]) & (df.Club_Position[i] != 'Sub') & (df.Club_Position[i] != 'Res')):
            a_squad.append(df.Name[i])
            posbuff_a.append(df.Club_Position[i])
    if len(h_squad) <= 10:
        if ((h_name == df.Club[i]) & (df.Club_Position[i] != 'Sub') & (df.Club_Position[i] != 'Res')):
            h_squad.append(df.Name[i])
            posbuff_h.append(df.Club_Position[i])

a_position = ""
h_position = ""
for j in range(0, len(a_squad)):
    a_position = df.Club_Position[getRate(a_squad[j])]
    h_position = df.Club_Position[getRate(h_squad[j])]
    classify(a_position, "away", getRate(a_squad[j]))
    classify(h_position, "home", getRate(h_squad[j]))
a_attack_rating = 0
a_defence_rating = 0
a_mid_rating = 0
h_attack_rating = 0
h_defence_rating = 0
h_mid_rating = 0

for v in a_attack:
    add = int(df.Short_Pass[v]) * att_apsv + int(df.Crossing[v]) + int(df.Long_Shots[v]) + int(df.Dribbling[v]) + int(
        df.Ball_Control[v]) + int(df.Shot_Power[v]) + int(df.Vision[v])
    a_attack_rating = a_attack_rating + (add / 8)
a_attack_rating = a_attack_rating / len(a_attack)
# a_attack_rating = a_attack_rating*form2


for h in h_attack:
    add = int(df.Short_Pass[h]) * att_apsv + int(df.Crossing[h]) + int(df.Long_Shots[h]) + int(df.Dribbling[h]) + int(
        df.Ball_Control[h]) + int(df.Shot_Power[h]) + int(df.Vision[h])
    h_attack_rating = h_attack_rating + (add / 8)
h_attack_rating = h_attack_rating / len(h_attack)
# h_attack_rating = h_attack_rating*form1
for q in h_mid:
    add = int(df.Short_Pass[q]) * mid_apsv + int(df.Crossing[q]) * mid_apsv + int(df.Long_Shots[q]) + int(
        df.Dribbling[q]) + int(df.Ball_Control[q]) + int(df.Vision[q])
    h_mid_rating = h_mid_rating + (add / 7)
h_mid_rating = h_mid_rating / len(h_mid)
# h_mid_rating = h_mid_rating*form2

for w in a_mid:
    add = int(df.Short_Pass[w]) * mid_apsv + int(df.Crossing[w]) * mid_apsv + int(df.Long_Shots[w]) + int(
        df.Dribbling[w]) + int(df.Ball_Control[w]) + int(df.Vision[w])
    a_mid_rating = h_mid_rating + (add / 7)
a_mid_rating = a_mid_rating / len(a_mid)
# a_mid_rating = a_mid_rating*form1

for r in h_defence:
    add = int(df.Short_Pass[r]) + int(df.Jumping[r]) + int(df.Long_Pass[r]) + int(df.Strength[r]) + int(
        df.Standing_Tackle[r]) + int(df.Sliding_Tackle[r])
    h_defence_rating = h_defence_rating + (add / 6)
h_defence_rating = h_defence_rating / len(h_defence)
# h_defence_rating = h_defence_rating*form2

for e in a_defence:
    add = int(df.Short_Pass[e]) + int(df.Jumping[e]) + int(df.Long_Pass[e]) + int(df.Strength[e]) + int(
        df.Standing_Tackle[e]) + int(df.Sliding_Tackle[e])
    a_defence_rating = a_defence_rating + (add / 6)
a_defence_rating = a_defence_rating / len(a_defence)
# a_defence_rating = a_defence_rating*form1

choi = [0, 1]
posession = random.choice(choi)
a_goals = 0
h_goals = 0
count_time = 0
a_att_chances = 0
a_mid_chances = 0
a_def_chances = 0
h_att_chances = 0
h_mid_chances = 0
h_def_chances = 0

a_att_taken = 0
a_mid_taken = 0
a_def_taken = 0
h_att_taken = 0
h_mid_taken = 0
h_def_taken = 0

# print h_attack_rating
# print a_attack_rating
choi2 = [9, 15, 19]
rancount = random.choice(choi2)

while (count_time < rancount):
    if (posession):
        print
        "home mid posession"
        h_mid_chances = h_mid_chances + 1
        if (((h_mid_taken + 1) * 100 / h_mid_chances) <= h_mid_rating):
            h_mid_taken = h_mid_taken + 1
            h_att_chances = h_att_chances + 1
            print
            "home attack"
            if ((h_att_taken + 1) * 100 / h_att_chances <= h_attack_rating):
                h_goals = h_goals + 1
                h_att_taken = h_att_taken + 1
                print
                "home shot"
                posession = 0
            else:
                a_def_chances = a_def_chances + 1
                if ((a_def_taken + 1) * 100 / a_def_chances <= a_defence_rating):
                    a_def_taken = a_def_taken + 1
                    # print a_def_taken/a_def_chances*100
                    posession = 0
                    print
                    "away clearance"
                    # print a_def_chances
                else:
                    if ((h_att_taken + 1) * 100 / h_att_chances <= h_attack_rating):
                        h_goals = h_goals + 1
                        h_att_taken = h_att_taken + 1
                        posession = 0
                        print
                        "OC shot"
        else:
            posession = 0
    else:
        a_mid_chances = a_mid_chances + 1
        print
        "away mid posession"
        if ((a_mid_taken + 1) * 100 / a_mid_chances <= a_mid_rating):
            a_mid_taken = a_mid_taken + 1
            a_att_chances = a_att_chances + 1
            print
            "away attack"
            if ((a_att_taken + 1) * 100 / a_att_chances <= a_attack_rating):
                a_goals = a_goals + 1
                a_att_taken = a_att_taken + 1
                posession = 1
                print
                "away shot"
            else:
                h_def_chances = h_def_chances + 1
                if ((h_def_taken + 1) * 100 / h_def_chances <= h_defence_rating):
                    h_def_taken = h_def_taken + 1
                    # print h_def_taken/h_def_chances*100
                    posession = 1
                    print
                    "home clearance"
                    # print h_def_chances
                else:
                    if ((a_att_taken + 1) * 100 / a_att_chances <= a_attack_rating):
                        a_goals = a_goals + 1
                        a_att_taken = a_att_taken + 1
                        posession = 1
                        print
                        "away OC"
        else:
            posession = 1
    time.sleep(0.2)
    count_time = count_time + 1

print
h_goals, ':', a_goals