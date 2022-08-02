#!/usr/bin/env python
# coding: utf-8

# In[1]:


#importing Pandas and NumPy
import numpy as np
import pandas as pd


# In[27]:


#uploading .csv file
csv_df = pd.read_csv("FoodBalanceSheets_E_Africa_NOFLAG.csv")


# In[30]:


#reading upload file
csv_df.head()


# In[4]:


#the total sum of Animal Fat produced in 2014 and 2017 respectively.
csv_df.groupby('Item')["Y2014","Y2017"].sum()


# In[6]:


#the mean and standard deviation across the whole dataset for the year 2015 to 3 decimal places.
csv_df.Y2015.describe()


# In[9]:


#the total number of missing data in 2016 to 2 decimal places.
n_of_missing = csv_df.Y2016.isnull().sum()
n_of_missing


# In[11]:


#the total percentage of missing data in 2016 to 2 decimal places.
percent_of_missing = csv_df.Y2016.isnull().sum()* 100 / len(csv_df)
percent_of_missing


# In[12]:


#year had the highest correlation with ‘Element Code'.
csv_df.corr()


# In[13]:


#year has the highest sum of Import Quantity.
csv_df.groupby('Element')["Y2014","Y2015","Y2016","Y2017","Y2018"].sum()


# In[14]:


#the total number of the sum of Production in 2014.
csv_df.groupby('Element')["Y2014"].sum()


# In[15]:


#elements had the highest sum in 2018.
element_H=csv_df.groupby('Element')["Y2018"].sum()
element_H.sort_values()


# In[16]:


#elements had the 3rd lowest sum in 2018.
element_H.sort_values()


# In[22]:


#the total Import Quantity in Algeria in 2018.
csv_df.groupby(['Element','Area'])['Y2018'].sum()


# In[31]:


#the total number of unique countries in the dataset.
csv_df.Area.nunique()

