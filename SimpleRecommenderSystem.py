#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 24 22:57:52 2016

@author: djokester
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#column headers for the dataset
data_cols = ['user id','item id','rating','timestamp']
item_cols = ['movie id','movie title','release date','video release date','IMDb URL','unknown','Action','Adventure','Animation','Childrens','Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance ','Sci-Fi','Thriller','War' ,'Western']
user_cols = ['id','age','gender','occupation','zip code']

#importing the data files onto dataframes 
users = pd.read_csv('Desktop/ml-100k/u.user', sep='|', names=user_cols, encoding='latin-1')
item = pd.read_csv('Desktop/ml-100k/u.item', sep='|', names=item_cols, encoding='latin-1')
data = pd.read_csv('Desktop/ml-100k/u.data', sep='\t', names=data_cols, encoding='latin-1')

#printing the head of these dataframes()
print("Users Head")
print(users.head())
print("\nItems Head")
print(item.head())
print("\nData Head")
print(data.head())

#printing the details of these dataframes() 
print(users.info())
print(item.info())
print(data.info())

