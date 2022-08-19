#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats


# In[9]:


df=pd.read_csv("C:\\Users\\MOUNIKA\\Downloads\\Ecommerce Purchases.csv")


# In[ ]:


1013


# In[23]:


x=df.iloc[0:11,10]
x


# In[25]:


y=df.iloc[0:11,13]
y


# In[26]:


plt.scatter(x,y)


# In[38]:


plt.scatter(x,y)
plt.xlabel("House area")
plt.ylabel("Selling Price")
plt.title("House Price")


# In[36]:


lr=stats.linregress()


# In[ ]:





# In[ ]:




