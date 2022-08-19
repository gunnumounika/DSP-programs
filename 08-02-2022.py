#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello")


# In[2]:


import numpy as np
import pandas as pd


# In[4]:


d=pd.read_csv("C:\\Users\\MOUNIKA\\Downloads\\IPL.csv")


# In[5]:


df=pd.DataFrame(d)


# In[7]:


df


# In[26]:


#Finding metadata of the DataFrame


# In[27]:


list(df.columns)


# In[34]:


#Finding Summary of the DataFrame


# In[28]:


df.info()


# In[10]:


#Displaying first few records of the DataFrame


# In[24]:


pd.set_option('display.max_columns',5)


# In[25]:


df.head(6)


# In[30]:


#Transpose of the above dataframe


# In[31]:


df.head(5).transpose()


# list(df.columns)

# 

# In[32]:


#To find the shape of the dataframe


# In[33]:


df.shape


# In[37]:


df.loc[2:5]


# In[38]:


df.iloc[0:5]


# In[49]:


df[-10:]


# In[50]:


#Selecting Column by Column Names


# In[51]:


df['PLAYER NAME'][0:6]


# In[52]:


#Selecting more columns by their names


# In[53]:


df[['PLAYER NAME','COUNTRY']][0:5]


# In[54]:


#Selecting Rows and Columns by indexes


# In[56]:


df.iloc[0:4,0:7]


# In[ ]:




