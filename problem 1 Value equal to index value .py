#!/usr/bin/env python
# coding: utf-8

# In[3]:


#problem: Value equal to index value (School level , GFG)

def value_equal_to_index(arr,n):
    l=[]                       ### according to question first I made an empty list because in given problem we want output as a list## 
    for i in range (n):        ### iteration method here we used and iterate i in our list to check every element
        if i+1==arr[i]:        #### here we used i+1 because in question is given assume first index is start from 1 and than compare 
            l.append(arr[i])
    return l                   ### here we return our final output as a list
obj=value_equal_to_index([15,2,45,12,7],5)
for i in obj:
    print(i)

