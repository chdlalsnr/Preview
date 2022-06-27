#-*-coding:utf-8-*-
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


data = pd.read_csv("./vgames2.csv")
df = pd.DataFrame(data)
df.dropna(axis=0, inplace=True)
df.drop(['Unnamed: 0'], axis=1, inplace=True)

df_sale = df[['NA_Sales','EU_Sales','JP_Sales','Other_Sales']]
# df_sale.replace('K','000', inplace=True)
# df_sale.replace('M','000000', inplace=True)

year,genre=[],[]
na,eu,jp,ot = [],[],[],[]
for i in range(len(df[['Year']])):
    year.append(df.iloc[i][2])
    genre.append(df.iloc[i][3])
    na.append(df_sale.iloc[i][0])
    eu.append(df_sale.iloc[i][1])
    jp.append(df_sale.iloc[i][2])
    ot.append(df_sale.iloc[i][3])

for i in range(len(na)):
    if ('K' in na[i]):
        na[i] = na[i].replace('K','000')
    if ('M' in na[i]):
        na[i] =na[i].replace('M','000000')
for i in range(len(eu)):
    if ('K' in eu[i]):
        eu[i] = eu[i].replace('K','000')
    if ('M' in eu[i]):
        eu[i] = eu[i].replace('M','000000')
for i in range(len(jp)):
    if ('K' in jp[i]):
        jp[i] = jp[i].replace('K','000')
    if ('M' in jp[i]):
        jp[i] = jp[i].replace('M','000000')
for i in range(len(ot)):
    if ('K' in ot[i]):
        ot[i] = ot[i].replace('K','000')
    if ('M' in ot[i]):
        ot[i] = ot[i].replace('M','000000')

for i in range(len(na)):
    na[i] = float(na[i])
    eu[i] = float(eu[i])
    jp[i] = float(jp[i])
    ot[i] = float(ot[i])

g0,g1,g2,g3 = [],[],[],[]
n0,n1,n2,n3 = [],[],[],[]
e0,e1,e2,e3 = [],[],[],[]
j0,j1,j2,j3 = [],[],[],[]
o0,o1,o2,o3 = [],[],[],[]
for i in range(len(na)):
    if (year[i] > 2000 and year[i] <= 2005):
        g0.append(genre[i])
        n0.append(na[i])
        e0.append(eu[i])
        j0.append(jp[i])
        o0.append(ot[i])
    if (year[i] > 2005 and year[i] <= 2010):
        g1.append(genre[i])
        n1.append(na[i])
        e1.append(eu[i])
        j1.append(jp[i])
        o1.append(ot[i])
    if (year[i] > 2010 and year[i] <= 2015):
        g2.append(genre[i])
        n2.append(na[i])
        e2.append(eu[i])
        j2.append(jp[i])
        o2.append(ot[i])
    if (year[i] > 2015 and year[i] <= 2020):
        g3.append(genre[i])
        n3.append(na[i])
        e3.append(eu[i])
        j3.append(jp[i])
        o3.append(ot[i])

fig,ax = plt.subplots()
hist0 = ax.hist(g0, color='blue', histtype='step', label='2000', weights=na)
hist_eu = ax.hist(genre, color='red', histtype='step', label='EU', weights=eu)
hist_jp = ax.hist(genre, color='orange', histtype='step', label='JP', weights=jp)
hist_ot = ax.hist(genre, color='purple', histtype='step', label='Others', weights=ot)

# plt.title("Sales Amount According to Genre_Normalized")
# plt.xlabel('Genre')
# plt.ylabel('Sales')
# plt.xticks(rotation=45)
# plt.legend()
# ax.yaxis.grid(linestyle='--')
# plt.show()

hist_na1 = ax.hist(g1, color='blue', histtype='step', label='2005', weights=n1, density=True)
hist_eu1 = ax.hist(g1, color='red', histtype='step', label='EU', weights=e1, density=True)
hist_jp1 = ax.hist(g1, color='orange', histtype='step', label='JP', weights=j1, density=True)
hist_ot1 = ax.hist(g1, color='purple', histtype='step', label='Others', weights=o1, density=True)

hist2 = ax.hist(g2, color='blue', histtype='step', label='2010', density=True)
hist_eu2 = ax.hist(g2, color='red', histtype='step', label='EU', weights=e2, density=True)
hist_jp2 = ax.hist(g2, color='orange', histtype='step', label='JP', weights=j2, density=True)
hist_ot2 = ax.hist(g2, color='purple', histtype='step', label='Others', weights=o2, density=True)

hist3 = ax.hist(g3, color='blue', histtype='step', label='2015', density=True)
hist_eu3 = ax.hist(g3, color='red', histtype='step', label='EU', weights=e3, density=True)
hist_jp3 = ax.hist(g3, color='orange', histtype='step', label='JP', weights=j3, density=True)
hist_ot3 = ax.hist(g3, color='purple', histtype='step', label='Others', weights=o3, density=True)

year = [2000,2005,2010,2015]

act = [hist0[0][0],hist1[0][0],hist2[0][0],hist3[0][0]]
adv = [hist0[0][1],hist1[0][1],hist2[0][1],hist3[0][1]]
mis = [hist0[0][2],hist1[0][2],hist2[0][2],hist3[0][2]]
pla = [hist0[0][3],hist1[0][3],hist2[0][3],hist3[0][3]]
spo = [hist0[0][4],hist1[0][4],hist2[0][4],hist3[0][4]]
sim = [hist0[0][5],hist1[0][5],hist2[0][5],hist3[0][5]]
rac = [hist0[0][6],hist1[0][6],hist2[0][6],hist3[0][6]]
str = [hist0[0][7],hist1[0][7],hist2[0][7],hist3[0][7]]
fig = [hist0[0][8],hist1[0][8],hist2[0][8],hist3[0][8]]
sho = [hist0[0][9],hist1[0][9],hist2[0][9],hist3[0][9]]

data = {
    "Action":act,
    "Adventure":adv,
    "Misc":mis,
    "Platform":pla,
    "Sports":spo,
    "Simulation":sim,
    "Racing":rac,
    "Strategy":str,
    "Fighting":fig,
    "Shooting":sho,
}

df_new = pd.DataFrame(data,index=year)
df_new.plot(kind="bar",stacked=True,figsize=(8,6))
plt.legend(loc="lower left",bbox_to_anchor=(1,0.6))
plt.xlabel('Year')
plt.ylabel('Trend')
plt.xticks(rotation=45)
plt.title("Trend Transition Over Year (2000~2020)")

plt.show()