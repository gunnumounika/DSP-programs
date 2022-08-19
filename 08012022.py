#!/usr/bin/env python
# coding: utf-8

# In[5]:


print("hello")


# In[35]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns


# In[36]:


#How many records are present in the dataset?


# In[37]:


df.shape[0]


# In[39]:


#Print the metadata information of the dataset


# In[38]:


df.info()


# In[40]:


df


# In[ ]:


#How many no. of movies got released in each genre?


# df.Genre.value_counts()

# In[41]:


df.Genre.value_counts()


# In[42]:


df.Genre.max()


# In[44]:


df.Genre=df.Genre.str.strip()


# In[47]:


df[['Genre','Release Time']].sort_values('Release Time')


# In[ ]:





# In[23]:


dc=df[['SlNo','Release Date']]
dc


# In[24]:


df['MovieName']


# In[26]:


df["ReleaseTime"]


# In[27]:


df['Genre']


# In[28]:


df['BoxOfficeCollection']


# In[30]:


df['YoutubeViews']


# In[31]:


df['YoutubeLikes']


# In[32]:


df['YoutubeDislikes']


# In[ ]:




