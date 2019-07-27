#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 16 11:46:33 2018

@author: Sruthi Pisipati
"""
import pandas as pd
#-------------------------------------------------------------#
#Importing the data from dataPrep.csv file into dataframe df
#-------------------------------------------------------------#
df = pd.read_csv("dataPrep.csv")
#-------------------------------------------------------------#
#Get types of data
#-------------------------------------------------------------#
print(df.dtypes)
#-------------------------------------------------------------#
#Creating new dataframe
#-------------------------------------------------------------#
df_Q = pd.DataFrame() 
df_NQ = pd.DataFrame()
count_Q = count_NQ = 0
for (key,value) in df.iteritems():
  if value.dtype!='object':  
      df_Q[key] =df[key]
      count_Q = count_Q + 1 #Counting the number of Quantitative attributes
  else:
      df_NQ[key] = df[key]
      count_NQ = count_NQ + 1 #Counting the number of Other attributes
print(df_Q.head())
print(df_NQ.head())
df_Q.to_csv('Quantitative.csv') #Saving data into "Quantitative.csv"
df_NQ.to_csv('Others.csv') #Saving data into "Others.csv"
print("Number of Attributes in Quantitative.csv: %d"%count_Q)
print("Number of Attributes in Others.csv: %d"%count_NQ)