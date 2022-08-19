#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests
r=requests.get('https://www.geeksforgeeks.org/python-programming-language/')
print(r)
print(r.content)


# In[ ]:





# In[31]:


import requests
from bs4 import BeautifulSoup as bs
r=requests.get('https://www.geeksforgeeks.org/python-programming-language/')
soup=bs(r.content,"html.parser")
links=soup.find_all('a')
for link in links:
    print(link.get('href'))


# In[33]:


import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.geeksforgeeks.org/python-programming-language/')
soup=BeautifulSoup(r.content,'html.parser')
images_list=[]
images=soup.select('img')
for image in images:
    src=image.get('src')
    alt=image.get('src')
    images_list.append({'src':src,'alt':alt})
    
for image in images_list:
    print(image)


# In[ ]:




