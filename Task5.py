#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 18:46:28 2018

@author: Sruthi Pisipati
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df_new = pd.DataFrame()
#-------------------------------------------------------------#
#Importing the data from dataPrep.csv file into dataframe df
#-------------------------------------------------------------#
df = pd.read_csv("Quantitative.csv")
del df['Unnamed: 0'] # Remove the junk column
df_sorted = df
df_not_binned = df.copy(deep = True)
#print(df.head(5))   
df_sorted.values.sort(axis=0) # Sort all the values
##----------------------------------------------------------------#
##Preparing sorted values with new column names
##----------------------------------------------------------------#
for (name,series) in df_sorted.iteritems():
    str1 = df_sorted[name].name
    str2 = '_BIN'
    df_new[str1+str2] = df[name]
df_bins = df_new    
arr = np.arange(start= 0,stop = len(df_bins),step=50)
print(arr)
##----------------------------------------------------------------#
##Preparing 50 bins 20 times (1000/50) for each column in 
##sorted columns such that each bin contains average value of that 
##bin  
##----------------------------------------------------------------#  
for (name,series) in df_new.iteritems(): 
   for i in np.arange(0,20):
        val = 0
        bin_avg = 0
        if i == 19:
            val = len(df_bins)
            bin_avg = (df_new[name][arr[i]] + df_new[name][val-1])/2
            df_bins[name][arr[i]:val] = bin_avg
        else: 
            val = arr[i+1] - 1  
            bin_avg = (df_new[name][arr[i]] + df_new[name][val])/2
            df_bins[name][arr[i]:val] = bin_avg  
##----------------------------------------------------------------#
##Prepare a new dataframe which contains old & new values for each
## column in the original dataframe    
## https://pandas.pydata.org/pandas-docs/stable/merging.html     
##----------------------------------------------------------------#
print(df_bins.head(5))   
print(df.head(5))    
df_final = df.append(df_bins,ignore_index=True)
print(df_final.head(5)) 
##----------------------------------------------------------------#
##Handling NaNs in the newly merged dataframe and adding the 
## values from binned dataframe  
## 
##----------------------------------------------------------------#
for (name,series) in df_final.iteritems():
    for(name1,series1) in df_bins.iteritems():
        if df_final[name].name == df_bins[name1].name:
            df_final[name] = df_bins[name1]

print(df_final.head(5)) 
##----------------------------------------------------------------#
##Saving the new data frame into csv
##https://stackoverflow.com/questions/16923281/pandas-writing-dataframe-to-csv-file 
##----------------------------------------------------------------#
df_final.to_csv('QuantitativeBinned.csv', sep='\t')


# ##----------------------------------------------------------------#
###Generating Correlation matrix for not binned version 
###----------------------------------------------------------------#  
list_sp = []
for (name,series) in df_not_binned.iteritems(): 
     list_sp.append(name) 
SPMdf = df_not_binned[[list_sp[0],list_sp[1],list_sp[2],list_sp[3],list_sp[4],
            list_sp[5],list_sp[6],list_sp[7],list_sp[8]]]     
##-------------------------------------------------------------#
##-------Correlation & Heatmap of Correlation for not binned
##-------version
##-------------------------------------------------------------#  
correlations = SPMdf.corr()
print(correlations)
ax5 = sns.heatmap(correlations)
figure = ax5.get_figure() 
figure.set_size_inches(8,3)
figure.tight_layout(pad=1)    
figure.savefig("Cor_heatmap_Not_Binned_attributes.png", dpi=400) 
plt.close(figure)
print("Correlation Heatmap for all not binned attributes has been completed\n")      
#
# ##----------------------------------------------------------------#
###Generating Correlation matrix for binned version 
###----------------------------------------------------------------#  
list = []
for (name,series) in df_bins.iteritems(): 
     list.append(name)
print(list)     
SPMdf_binned = df_bins[[list[0],list[1],list[2],list[3],list[4],
            list[5],list[6],list[7],list[8]]]      
###-------------------------------------------------------------#
###-------Correlation & Heatmap of Correlation for binned
###-------version
###-------------------------------------------------------------#  
correlations = SPMdf_binned.corr()
print(correlations)
ax5 = sns.heatmap(correlations)
figure = ax5.get_figure() 
figure.set_size_inches(8,3)
figure.tight_layout(pad=1)   
figure.savefig("Cor_heatmap_Binned_attributes.png", dpi=400) 
plt.close(figure)
print("Correlation Heatmap for all binned attributes has been completed\n")     
 