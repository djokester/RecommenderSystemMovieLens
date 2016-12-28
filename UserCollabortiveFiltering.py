import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

#column headers for the dataset
data_cols = ['user id','movie id','rating','timestamp']
item_cols = ['movie id','movie title','release date','video release date','IMDb URL','unknown','Action','Adventure','Animation','Childrens','Comedy','Crime','Documentary','Drama','Fantasy','Film-Noir','Horror','Musical','Mystery','Romance ','Sci-Fi','Thriller','War' ,'Western']
user_cols = ['user id','age','gender','occupation','zip code']

#importing the data files onto dataframes 
users = pd.read_csv('Desktop/ml-100k/u.user', sep='|', names=user_cols, encoding='latin-1')
item = pd.read_csv('Desktop/ml-100k/u.item', sep='|', names=item_cols, encoding='latin-1')
data = pd.read_csv('Desktop/ml-100k/u.data', sep='\t', names=data_cols, encoding='latin-1')

utrain = (data.sort_values('user id'))[:99832]
print(utrain.tail())
utest = (data.sort_values('user id'))[99833:]
print(utest.head())

utrain = utrain.as_matrix(columns = ['user id', 'movie id', 'rating'])
print(utrain)

utest = utest.as_matrix(columns = ['user id', 'movie id', 'rating'])
print(utest)


users_list = []
for i in range(1,943):
    list = []
    for j in range(0,len(utrain)):
        if utrain[j][0] == i:
            list.append(utrain[j])    
        else:
            break
    utrain = utrain[j:]
    users_list.append(list) 
    
print(len(users_list))



    

def EucledianScore(train_user, test_user):
    sum = 0
    for i in test_user:
        score = 0
        for j in train_user:
            if(int(i[1]) == int(j[1])):
                score= ((float(i[2])-float(j[2]))*(float(i[2])-float(j[2])))
        sum = sum + score            
    return(math.sqrt(sum))            

score_list = []               
for i in range(0,942):
    score_list.append([i+1,EucledianScore(users_list[i], utest)])
    


