#!/usr/bin/env python
# coding: utf-8

# In[126]:


import pandas as pd
df=pd.read_excel(r'C:\\Users\\MOUNIKA\\Desktop\\numpy\\marks.xlsx')
print(df)


# In[127]:


df.isnull().sum()


# In[128]:


df.isnull().sum().sum()


# In[129]:


dn=df.dropna(axis=0)
print(dn)


# In[130]:


dn.isnull().sum()


# In[131]:


dn.isnull().sum().sum()


# In[132]:


dc=df.dropna(axis=1)
print(dc)


# In[133]:


dc.isnull().sum()


# In[134]:


df


# In[135]:


da=df['Telugu'].fillna(100)
print(da)


# In[136]:


da.isnull().sum().sum()


# In[137]:


df


# In[138]:


import numpy as no
ds=df['Roll_no'].fillna(df['Roll_no'].mean())
print(ds)


# In[139]:


dd=df["Telugu"].fillna(df["Telugu"].mode()[0])


# In[140]:


print(dd)


# In[141]:


dd=df["Telugu"].fillna(df["Telugu"].mode()[0])


# In[142]:


print(dd)


# In[143]:


dc=df["Maths"].fillna(df["Maths"].mode()[0])


# In[144]:


dc


# In[145]:


dc.isnull().sum()


# In[146]:


df.isnull().sum()


# In[147]:


import numpy as np
import pandas as pd
df=pd.read_excel('C:\\Users\\MOUNIKA\\Desktop\\numpy\\marks.xlsx')


# In[148]:


df


# In[149]:


test=pd.series(range(6))
test.loc[2:4]=np.nan
test


# In[ ]:


df.loc[2:4]=np.nan


# In[ ]:


test=df.series(range(6))


# In[ ]:


df


# In[ ]:


df.loc[2:6]=np.nan
df.fillna(method="ffill")


# In[ ]:


df=pd.read_excel('C:\\Users\\MOUNIKA\\Desktop\\numpy\\marks.xlsx')


# In[ ]:


df


# In[ ]:


df.loc[2:4]=np.nan
print(df)
df.interpolate()


# In[ ]:


ds=df.dropn("Telugu").axis[1]


# In[ ]:


ds=pd.read_excel('C:\\Users\\MOUNIKA\\Desktop\\csv_file.xlsx')


# In[ ]:


ds=pd.read_excel('C:\\Users\\MOUNIKA\\Desktop\\milage.csv.xlsx')


# In[ ]:


ds


# In[ ]:


ds['city_mpg']=234/ds['city_mpg']


# In[ ]:


ds.rename(columns={'city_mpg':'city_L/100'},inplace=1)


# In[ ]:


ds


# In[155]:


import numpy as np
ds=pd.read_excel('C:\\Users\\MOUNIKA\\Desktop\\milage.csv.xlsx')


# In[151]:


ds


# In[168]:


ds.tail[5]


# In[153]:


ds['city_mpg']=ds['city_mpg'].astype['int']


# In[166]:


ds.tail[5]


# In[159]:


data={'month':['january','february','march','april','may'],'expense':[1200,1300,1400,1500,1500]}


# In[160]:


data


# In[165]:


data.tail[3]


# In[163]:


df


# In[164]:


df.tail(5)


# In[172]:


data={'month':['january','february','march','april','may'],'expense':[1200,1300,1400,1500,1500]}
df=pd.DataFrame[data,columns=['month','expense']


# In[ ]:




