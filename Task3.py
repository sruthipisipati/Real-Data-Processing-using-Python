#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 10:16:10 2018

@author: Sruthi Pisipati
"""
from scipy.stats import zscore
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

threshold_max = 2
threshold_min = -2
df_new = pd.DataFrame()
df_final = df_new
ls = []
#-------------------------------------------------------------#
#Importing the data from Quantitative.csv file into dataframe df
#-------------------------------------------------------------#
df = pd.read_csv("Quantitative.csv")
print(df.head(5))
del df['Unnamed: 0'] # Remove the junk column
df_out = df.copy(deep = True)
print(df_out.tail(5))
##----------------------------------------------------------------#
##Preparing the Boxplots before removing outliers and normalizing
##----------------------------------------------------------------#
for (name,series) in df.iteritems(): 
      ax = sns.boxplot(x=df[name])
      ax.set_title('Attribute:' +df[name].name+'-Boxplot')
      ax.set_xlabel(df[name].name)
      ax.set_ylabel('Count')
      fig = ax.figure
      fig.set_size_inches(8,3)
      fig.tight_layout(pad=1)
      fig.savefig(df[name].name+'_.png',dpi=600)
      plt.close(fig)
      print("Box Plotting for attribute" +df[name].name+'has been completed\n')
##-------------------------------------------------------------#
##Normalizing data by z-score method to identify and remove
## outliers      
##-------------------------------------------------------------#
df = df.apply(zscore) # Normalization
#-------------------------------------------------------------#
#Identifying Outliers using Z-score method
#Reference : https://towardsdatascience.com/ways-to-detect-and-remove-the-outliers-404d16608dba
#-------------------------------------------------------------#
for (name,series) in df.iteritems(): 
    print("-----------------------------------------------------")
    print("Identifying Z-score > 2 or Z-score < -2 for Attribute:"+df[name].name) 
    print(np.where((df[name] > threshold_max) | (df[name] < threshold_min)))
    print("-----------------------------------------------------")
##-------------------------------------------------------------#
##Applying Clamp transformation to replace outliers with 
## threshold values      
##-------------------------------------------------------------#    
for (name,series) in df.iteritems(): 
    df[name][df[name]< threshold_min ] = threshold_min
    df[name][df[name]> threshold_max ] = threshold_max    
    
df_clamped = df.copy(deep = True)     
##-------------------------------------------------------------#
## Since the data is already normalized , proceeding to next 
## step    
##-------------------------------------------------------------#
#df = df.apply(zscore) # Normalization
df_normal = df.copy(deep = True)  
##-------------------------------------------------------------#
##Saving the clamped values & normalized values in new dataframe
## along with old attribute values
##-------------------------------------------------------------#
print("===============")
print(df_out.tail(5)) 
print("===============")
for (name,series) in df_out.iteritems():
    str1 = df_out[name].name
    str2 = '_ClampedValues'
    str3 = '_ClampedNormalizedValues'
    df_new[str1] = df_out[name]
    df_new[str1+str2] = df[name]
    df_new[str1+str3] = df[name]
    ls.append(str1)
    ls.append(str1+str2)
    ls.append(str1+str3)
print(df_new.tail(5))    
##-------------------------------------------------------------#
##Mapping the values from df_clamped & df_normal to the new 
## dataframe which contains the old column & new columns    
##-------------------------------------------------------------#    
for (name,series) in df_clamped.iteritems():
    str1 = df_clamped[name].name
    df_new[str1+str2] = df_clamped[name]

for (name,series) in df_normal.iteritems():
    str1 = df_normal[name].name
    df_new[str1+str3] = df_normal[name]
##-------------------------------------------------------------#
##Rearranging the columns as per the required format i.e.
## Column-1 : Attr 4 , Column-2 : Attr 4_ClampedValues
## Column-3 : Attr 4_ClampedNormalizedValues    
##-------------------------------------------------------------# 
i = 0
for(name,series) in df_new.iteritems():
    if df_new[name].name == ls[i]:
     df_final[name] =  df_new[name]
print("-----------------------------------------------------")
print("Table containing old column & new columns of attributes")  
print("-----------------------------------------------------")    
print(df_final.tail(5))    

###----------------------------------------------------------------#
###Saving the new data frame into csv
###https://stackoverflow.com/questions/16923281/pandas-writing-dataframe-to-csv-file 
###----------------------------------------------------------------#
df_final.to_csv('QTransferred.csv', sep='\t')
###----------------------------------------------------------------#
###Preparing the Boxplots for the normalized values
###----------------------------------------------------------------#
for (name,series) in df.iteritems(): 
      ax = sns.boxplot(x=df[name])
      ax.set_title('Attribute:' +df[name].name+'-Boxplot')
      ax.set_xlabel(df[name].name)
      ax.set_ylabel('Count')
      fig = ax.figure
      fig.set_size_inches(8,3)
      fig.tight_layout(pad=1)
      fig.savefig(df[name].name+'_Normalized.png',dpi=600)
      plt.close(fig)
      print("Plotting for attribute" +df[name].name+'has been completed\n')
##-------------------------------------------------------------#
##-------Plotting Scatterplot Matrix
##-------------------------------------------------------------# 
list_sp =[]      
for (name,series) in df.iteritems(): 
     list_sp.append(name) 
print(list_sp) 
SPMdf = df[[list_sp[0],list_sp[1],list_sp[2],list_sp[3],list_sp[4],
            list_sp[5],list_sp[6],list_sp[7],list_sp[8]]]
sns.set(style="ticks")
ax3 = sns.pairplot(SPMdf) 
ax3.savefig("Scatter_plot_all_attributes_normalized.png")
plt.close()
print("Scatter Plot for all attributes has been completed\n")    
