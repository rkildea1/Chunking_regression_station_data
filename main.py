import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
%matplotlib inline




a = pd.read_fwf("//ghcnd-stations.txt",
               header=None,colspecs=((0,11),(13,20), (22,30),(32,37),(39,40),(42,71),(73,75),(77,79),(81,85)))
a.columns =['ID', 'LATITUDE', 'LONGITUDE', 'ELEVATION', 'STATE', 'NAME', 'GSN FLAG', 'HCN/CRN FLAG', 'WMO ID']


#picking two stations to play around with 

subset = a[a['HCN/CRN FLAG'] != 'nan']
count = 0
max_count = 2
station_ids = []
x = subset['ID'].unique()
y = x[:2]
for i in y:
    station_ids.append(i)


subset = a[a["GSN FLAG"] == "SN"]
count = 0
max_count = 25
station_ids = []
x = subset['ID'].unique()
y = x[:5]
for i in y:
    station_ids.append(i)


##Station ID's selected are: AE000041196 & AG000060590 (both have GSN flags)

import pandas as pd

file = "//ghcnd_daily.csv"

chunksize = 20000
df_chunks = []

for df in pd.read_csv(file, chunksize=chunksize, iterator=True):
    df_f = df.loc[(df['id']=="AE000041196")|(df['id']=="AG000060590")]
    df_chunks.append(df_f)

reduced_df = pd.concat(df_chunks)
    
df_AE000041196 = reduced_df.loc[(reduced_df['id']=="AE000041196")]
df_AG000060590 = reduced_df.loc[(reduced_df['id']=="AG000060590")]

#create a list of the column headers for the temps
x = df_AE000041196.columns.to_list()
x
cols_list = ["id","year","month"]
for l in x:
    if "value" in l:
        cols_list.append(l)
       
       
       
#Create new data frames which only have the data columns that i want (i.e., what is in the list i created in the last step)
df_AE000041196_temps = df_AE000041196.loc[:,cols_list]
df_AG000060590_temps = df_AG000060590.loc[:,cols_list]


#copy the temps and add on the average value 

#copy
df_AE000041196_w_avg = df_AE000041196_temps.copy()
df_AG000060590_w_avg = df_AG000060590_temps.copy()

#replace the -9999's with 0
df_AE000041196_w_avg.replace(to_replace = -9999, value = 0, inplace = True)
df_AG000060590_w_avg.replace(to_replace = -9999, value = 0, inplace = True)

#calculate the mean
df_AE000041196_w_avg['average'] = df_AE000041196_w_avg[cols_list].mean(axis=1)
df_AG000060590_w_avg['average'] = df_AG000060590_w_avg[cols_list].mean(axis=1)


#Now for each of the weather stations, generate a separate plot of the monthly max temperatures 
#over time (starting with the earliest and finishing with the latest) and show a regression line on the plot
#first thing i need to do is split each df into individual ones based on month. 

df_AE000041196_w_avg_JAN = df_AE000041196_w_avg.loc[(reduced_df['month']==1)]
df_AE000041196_w_avg_FEB = df_AE000041196_w_avg.loc[(reduced_df['month']==2)]
df_AE000041196_w_avg_MAR = df_AE000041196_w_avg.loc[(reduced_df['month']==3)]
df_AE000041196_w_avg_APR = df_AE000041196_w_avg.loc[(reduced_df['month']==4)]
df_AE000041196_w_avg_MAY = df_AE000041196_w_avg.loc[(reduced_df['month']==5)]
df_AE000041196_w_avg_JUN = df_AE000041196_w_avg.loc[(reduced_df['month']==6)]
df_AE000041196_w_avg_JUL = df_AE000041196_w_avg.loc[(reduced_df['month']==7)]
df_AE000041196_w_avg_AUG = df_AE000041196_w_avg.loc[(reduced_df['month']==8)]
df_AE000041196_w_avg_SEP= df_AE000041196_w_avg.loc[(reduced_df['month']==9)]
df_AE000041196_w_avg_OCT = df_AE000041196_w_avg.loc[(reduced_df['month']==10)]
df_AE000041196_w_avg_NOV = df_AE000041196_w_avg.loc[(reduced_df['month']==11)]
df_AE000041196_w_avg_DEC = df_AE000041196_w_avg.loc[(reduced_df['month']==12)]

df_AG000060590_w_avg_JAN = df_AG000060590_w_avg.loc[(reduced_df['month']==1)]
df_AG000060590_w_avg_FEB = df_AG000060590_w_avg.loc[(reduced_df['month']==2)]
df_AG000060590_w_avg_MAR = df_AG000060590_w_avg.loc[(reduced_df['month']==3)]
df_AG000060590_w_avg_APR = df_AG000060590_w_avg.loc[(reduced_df['month']==4)]
df_AG000060590_w_avg_MAY = df_AG000060590_w_avg.loc[(reduced_df['month']==5)]
df_AG000060590_w_avg_JUN = df_AG000060590_w_avg.loc[(reduced_df['month']==6)]
df_AG000060590_w_avg_JUL = df_AG000060590_w_avg.loc[(reduced_df['month']==7)]
df_AG000060590_w_avg_AUG = df_AG000060590_w_avg.loc[(reduced_df['month']==8)]
df_AG000060590_w_avg_SEP= df_AG000060590_w_avg.loc[(reduced_df['month']==9)]
df_AG000060590_w_avg_OCT = df_AG000060590_w_avg.loc[(reduced_df['month']==10)]
df_AG000060590_w_avg_NOV = df_AG000060590_w_avg.loc[(reduced_df['month']==11)]
df_AG000060590_w_avg_DEC = df_AG000060590_w_avg.loc[(reduced_df['month']==12)]

fig, axes = plt.subplots(3, 4, figsize=(20, 12))
fig.suptitle('AE000041196')
fig = fig.tight_layout(pad=3)
sns.regplot(ax = axes[0,0], x = "year",y = "average", data = df_AE000041196_w_avg_JAN) 
sns.regplot(ax = axes[0,1], x = "year",y = "average", data = df_AE000041196_w_avg_FEB) 
sns.regplot(ax = axes[0,2], x = "year",y = "average", data = df_AE000041196_w_avg_MAR) 
sns.regplot(ax = axes[0,3], x = "year",y = "average", data = df_AE000041196_w_avg_APR) 
sns.regplot(ax = axes[1,0], x = "year",y = "average", data = df_AE000041196_w_avg_MAY) 
sns.regplot(ax = axes[1,1], x = "year",y = "average", data = df_AE000041196_w_avg_JUN) 
sns.regplot(ax = axes[1,2], x = "year",y = "average", data = df_AE000041196_w_avg_JUL) 
sns.regplot(ax = axes[1,3], x = "year",y = "average", data = df_AE000041196_w_avg_AUG) 
sns.regplot(ax = axes[2,0], x = "year",y = "average", data = df_AE000041196_w_avg_SEP) 
sns.regplot(ax = axes[2,1], x = "year",y = "average", data = df_AE000041196_w_avg_OCT) 
sns.regplot(ax = axes[2,2], x = "year",y = "average", data = df_AE000041196_w_avg_NOV) 
sns.regplot(ax = axes[2,3], x = "year",y = "average", data = df_AE000041196_w_avg_DEC)


fig, axes = plt.subplots(3, 4, figsize=(20, 12))
fig.suptitle('AG000060590')
fig = fig.tight_layout(pad=3)
sns.regplot(ax = axes[0,0], x = "year",y = "average", data = df_AG000060590_w_avg_JAN) 
sns.regplot(ax = axes[0,1], x = "year",y = "average", data = df_AG000060590_w_avg_FEB) 
sns.regplot(ax = axes[0,2], x = "year",y = "average", data = df_AG000060590_w_avg_MAR) 
sns.regplot(ax = axes[0,3], x = "year",y = "average", data = df_AG000060590_w_avg_APR) 
sns.regplot(ax = axes[1,0], x = "year",y = "average", data = df_AG000060590_w_avg_MAY) 
sns.regplot(ax = axes[1,1], x = "year",y = "average", data = df_AG000060590_w_avg_JUN) 
sns.regplot(ax = axes[1,2], x = "year",y = "average", data = df_AG000060590_w_avg_JUL) 
sns.regplot(ax = axes[1,3], x = "year",y = "average", data = df_AG000060590_w_avg_AUG) 
sns.regplot(ax = axes[2,0], x = "year",y = "average", data = df_AG000060590_w_avg_SEP) 
sns.regplot(ax = axes[2,1], x = "year",y = "average", data = df_AG000060590_w_avg_OCT) 
sns.regplot(ax = axes[2,2], x = "year",y = "average", data = df_AG000060590_w_avg_NOV) 
sns.regplot(ax = axes[2,3], x = "year",y = "average", data = df_AG000060590_w_avg_DEC)



    #df_AG000060590_w_avg_JAN
x = df_AG000060590_w_avg['year']
y = df_AG000060590_w_avg['average']
plt.plot(x, y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b) 


    #df_AE000041196_w_avg
x = df_AE000041196_w_avg['year']
y = df_AE000041196_w_avg['average']
plt.plot(x, y)
m, b = np.polyfit(x, y, 1)
plt.plot(x, m*x + b) 
