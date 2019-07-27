#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 15:23:31 2018

@author: Sruthi Pisipati
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
list_sp = []
#-------------------------------------------------------------#
#Importing the data from dataPrep.csv file into dataframe df
#-------------------------------------------------------------#
df = pd.read_csv("Quantitative.csv")
#-------------------------------------------------------------#
#print(df.head())
for (name,series) in df.iteritems(): 
    if name != 'Unnamed: 0':
         a = sum(df[name].isnull().values.ravel())
         b = df[name].size 
         print("-------------------------------")
         print("ANALYZED ATTRIBUTE NAME:", name)
         print("-------------------------------")
         #Count of records
         print("--Count of records:", b)
         #Count of missing values
         print("--Count of missing values:",a) 
         #Missing values %    
         print("--Ratio of missing values:", (a/b )*100)
         #Cardinality count of unique values
         print("--Cardinality count of unique values", df[name].unique().size)
         #Minimum value
         print("--Minimum value:", df[name].min())
         #First quarter value
         print("--1st quarter value:", df[name].quantile(.25))
         #Median value
         print("--Median:", df[name].median())
         #3rd quarter value
         print("--3rd quarter value:", df[name].quantile(.75))
         #Maximum value
         print("--Max value:", df[name].max())
         #Mean value
         print("--Mean value:", df[name].mean())
         #Standard deviation
         print("--Standard deviation:", df[name].std())
         #Variance 
         print("--Variance:", df[name].var())
         #Range of attribute
         range = df[name].max() - df[name].min()
         print("--Range:", range)
#-------------------------------------------------------------#
#-------Plotting Histograms
#-------------------------------------------------------------# 
         ax1 = df[name].plot.hist(bins = 10)         
         ax1.set_title('Attribute:' +df[name].name+'-Histogram with 20 bins')
         ax1.set_xlabel(df[name].name)
         ax1.set_ylabel('Count')
         fig1 = ax1.figure
         fig1.set_size_inches(8,3)
         fig1.tight_layout(pad=1)
         fig1.savefig(df[name].name+'_hist.png',dpi=600)
         plt.close(fig1)
         print("Plotting for attribute" +df[name].name+'has been completed\n')
##-------------------------------------------------------------#
##-------Plotting Violinplots
##-------------------------------------------------------------#               
         ax2 = sns.violinplot(x=df[name])
         fig2 = ax2.figure
         fig2.set_size_inches(8,3)
         fig2.tight_layout(pad=1)
         fig2.savefig(df[name].name+'_violin_plot.png',dpi=600)
         plt.close(fig2)
         print("Violin Plotting for attribute" +df[name].name+'has been completed\n')
#-------------------------------------------------------------#
#-------Plotting Scatterplot Matrix
#-------------------------------------------------------------#  
for (name,series) in df.iteritems(): 
    if name != 'Unnamed: 0':
     list_sp.append(name) 
print(list_sp) 
SPMdf = df[[list_sp[0],list_sp[1],list_sp[2],list_sp[3],list_sp[4],
            list_sp[5],list_sp[6],list_sp[7],list_sp[8]]]
sns.set(style="ticks")
ax3 = sns.pairplot(SPMdf) 
ax3.savefig("Scatter_plot_all_attributes.png")
plt.close()
print("Scatter Plot for all attributes has been completed\n")
#-------------------------------------------------------------#
#-------Covariance & Heatmap of Covariance
#-------------------------------------------------------------# 
covariance = SPMdf.cov()
print(covariance)
ax4 = sns.heatmap(covariance,vmax = 1,vmin = 20)
figure = ax4.get_figure()    
figure.savefig("Cov_heatmap_attributes.png", dpi=400)
plt.close(figure)
print("Covariance Heatmap for all attributes has been completed\n")
#-------------------------------------------------------------#
#-------Correlation & Heatmap of Correlation
#-------------------------------------------------------------#  
correlations = SPMdf.corr()
print(correlations)
ax5 = sns.heatmap(correlations)
figure = ax5.get_figure()    
figure.savefig("Cor_heatmap_attributes.png", dpi=400) 
plt.close(figure)
print("Correlation Heatmap for all attributes has been completed\n")
 
