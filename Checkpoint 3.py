#!/usr/bin/env python
# coding: utf-8

# In[3]:


def multiply_list(items):
    tot = 1
    for x in items:
        tot *= x
    return tot
print(multiply_list([2,3,6]))


# In[5]:


def last(n): return n[-1]

def sort_list_last(tuples):
  return sorted(tuples, key=last)

print(sort_list_last([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))


# In[6]:


from collections import Counter
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
d = Counter(d1) + Counter(d2)
print(d)


# In[7]:



n=int(input("Input a number "))
d = dict()

for x in range(1,n+1):
    d[x]=x*x

print(d) 


# In[8]:


price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
print( sorted(price, key=lambda x: float(x[1]), reverse=True))


# In[ ]:




