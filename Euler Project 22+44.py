#!/usr/bin/env python
# coding: utf-8

# In[52]:


## 22


# In[53]:


import numpy as np


# In[54]:


rawData = np.genfromtxt('C:/Users/9502089/Downloads/names.txt', dtype=str, delimiter='","')
rawData[0]


# In[55]:


data = np.sort(my_data)
data[0]


# In[56]:


def getScore(name, index):
    score = 0
    for letter in name:
        score += (ord(letter)-64)
    return score*(index+1)


# In[60]:


getScore('COLIN', 938)


# In[57]:


score = 0
for index, name in enumerate(data):
    score += getScore(name, index)


# In[61]:


score


# In[62]:


## 44


# In[79]:


pentNumbers = []
for i in range(3000):
    pentNumbers.append(int((i+1)*(3*(i+1)-1)/2))


# In[80]:


for numA in pentNumbers:
    for numB in pentNumbers:
        if (numB > numA):
            if ((numB - numA) in pentNumbers):
#                 print('diff')
                if((numB + numA) in pentNumbers):
                    print('bingo')
                    print(numB)
                    print(numA)


# In[ ]:




