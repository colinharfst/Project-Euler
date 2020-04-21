
# coding: utf-8

# In[19]:


def stringToDict(s):
    d = {}
    for l in s:
        if l in d:
            d[l] = d[l]+1
        else:
            d[l] = 1
    print(s, d)
    return d

def isAnagram(s, r):
    dictA = stringToDict(s)
    dictB = stringToDict(r)
    return dictA == dictB


# In[28]:


isAnagram('accb', 'acbc')


# In[70]:


def reverseSentence(s):
    a = s.split(' ')[::-1]
    n = len(a)
    newSentence = ''
    for i in range(n):
        print(a[i])
        newSentence = newSentence + a[i]
        if i != n-1:
            newSentence = newSentence + ' '
    return newSentence


# In[73]:


reverseSentence('the quick brown fox')


# In[108]:


import math

def sumInRange50(num):
    x = math.floor(num/2)
    newNum = math.floor((num+1)/2)
    while x >= -50 and newNum <= 50:
        print(x, newNum)
        x = x-1
        newNum = newNum+1


# In[109]:


sumInRange50(1)

