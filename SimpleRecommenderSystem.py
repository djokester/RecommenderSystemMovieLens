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
data_cols = ['user id','movie id','rating','timestamp']
item_cols = ['movie id','movie title','release date','video release date','IMDb URL','unknown','Action','Adventure','Animation','Childrens','Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance ','Sci-Fi','Thriller','War' ,'Western']
user_cols = ['user id','age','gender','occupation','zip code']

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
print('\n',users.info())
print('\n',item.info())
print('\n',data.info())

#Using Pandas to manipulate the data 

#Create one data frame from the three
dataset = pd.merge(pd.merge(item, data),users)
print(dataset.head())

#Create dataframes with mean rating and total number of ratings
ratings_total = dataset.groupby('movie title').size()

rt = (dataset.groupby('movie title'))['movie title','rating']
ratings_mean = (rt.mean())

#modify those dataframes so that we can merge the two 
ratings_total = pd.DataFrame({'movie title':ratings_total.index, 'total ratings': ratings_total.values})
ratings_mean['movie title'] = ratings_mean.index

final = pd.merge(ratings_mean, ratings_total).sort_values(by = 'total ratings', ascending= False)
print(final.head())
print(final.describe())

final = final[:300].sort_values(by = 'rating', ascending = False)
print(final.head())

