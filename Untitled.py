#!/usr/bin/env python
# coding: utf-8

# In[1]:


############Import Libraries
import pandas as pd 
import random


# In[2]:
class Model:

    def recommendation(self,id):
        data = pd.read_csv("Data.csv") 
        data['id']=data['id'].astype(str)
        data=data.fillna(0)
        data.head()
        rows=data.loc[(data['id'] == id)]
        userFollow="".join(rows["Follow"].values)
        ran_list=[]
        while len(ran_list)<10:
            ran=random.randint(0,98)
            if ran not in ran_list and str(ran) not in userFollow:
                ran_list.append(ran)
        ran_list
        return ran_list
    #recommendation("1")  
    
    
    # In[13]:
    
    
    def newsfeed(self,typ):
        data = pd.read_csv("NewsFeed.csv") 
        data['id']=data['id'].astype(str)
        data=data.fillna(0)
        data.head()
        data=data[data['Type'].str.contains(typ)]
        content =data["NewsFeed"].tolist()
        return content
    #newsfeed("News")
    
    def __init__(self):
        print("Start Model")
    
    # In[ ]:




