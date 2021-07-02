#!/usr/bin/env python
# coding: utf-8

# In[7]:


import random


# # Travelling Salesman problem
# 

# # for any sample dataset,implement order encoding for TSP

# In[8]:


def tsp(n):
    
    p = random.sample(range(n),n)

    random.shuffle(p)
    
    return p

n_cities = int(input('No. of cities '))

p1 = tsp(n_cities)
print("Parent 1: ",p1)
p2 = tsp(n_cities)
print("Parent 2: ",p2)


# In[ ]:




