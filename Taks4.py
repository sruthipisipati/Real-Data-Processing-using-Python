#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 21 19:20:42 2018

@author: Sruthi Pisipati
"""

import pandas as pd
from scipy.stats import mode

#-------------------------------------------------------------#
#Importing the data from Others.csv file into dataframe df
#-------------------------------------------------------------#
df_tm = pd.DataFrame()
df = pd.read_csv("Others.csv")
print(df.head())
del df['Unnamed: 0'] # Remove the junk column
print(df.head())
#-------------------------------------------------------------#
#Fetching the data required for Data Quality report related 
# to categorical features
#-------------------------------------------------------------#
for (name,series) in df.iteritems(): 
         count = 0
         ls = []
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
         print("--Cardinality count of unique values:", df[name].unique().size)

         #Mode value
         str = mode(df[name])[0].squeeze()
         print("--Mode value:", str)
         #Mode Frequency 
         for w in df[name]:
             if w == str:
                 count = count + 1
             else:
                 ls.append(w) 
         print("--Mode frequency:",count)
         #Mode Frequency %
         m1 = (count/b)*100
         print("--Mode %:",round(m1,2))
         #2nd Mode                 
         #https://stackoverflow.com/questions/10797819/finding-the-mode-of-a-list        
         str2 = max(set(ls), key=ls.count)        
         print("--2nd Mode:",str2)                
         #2nd Mode Frequency
         count = ls.count(str2)
         print("--2nd Mode frequency:",count)
         #2nd Mode %
         m2 = (count/b)*100
         print("--2nd Mode %:", round(m2,2))
         #Type of attribute
         print("--Type of attribute:", type(name))

