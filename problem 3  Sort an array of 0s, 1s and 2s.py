#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Sort an array of 0s, 1s and 2s we have given an array and we have to sort it 
# apporach 1:
def sort_0_1_2(arr):
    arr.sort()       ### this is a built-in function of python to sort an array   
    
    return arr      #### here sorting takes O(nlogN) time , but we can optimize it .
obj=sort_0_1_2([1,0,0,2,1,0,0,2])
print(obj)


# In[9]:


#apporach 2
           ### " DUTCH NATIONAL FLAG ALGORITHM "
## here we use iteration method ,in which something that is less to an specific value comes on left side and grater value comes on right and rest is eual to our assumption so it remain in middle 
def sort_0_1_2(arr):
    low=0
    mid=0
    high=len(arr)-1
    while mid<=high:
        if arr[mid]==0:
            arr[mid],arr[low]=arr[low],arr[mid]   ### here we swapped both number and increment mid and low to its next value 
            mid=mid+1
            low=low+1
        if arr[mid]==1:
            mid=mid+1                 # nothing to change we want to put 1 in between 0 and 2 so we are on that , so increment needed only 
        if arr[mid]==2:
            arr[mid],arr[high]=arr[high],arr[mid]
            high=high-1         ### this part indicating that you swapped 2 on the right side so now check 1 less part of array 
    return arr
print(sort_0_1_2([1,0,0,2,1,0,0,2,0,0,1,1,2,2,1,1,2,1,1,1,1,1,1,1,1,0,0,0,0,0,0,2,2,2,2,2,1,1,1,1,1]))
        
    


# In[ ]:




