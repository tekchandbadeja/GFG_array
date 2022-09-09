#!/usr/bin/env python
# coding: utf-8

# In[9]:


#Minimum number of jumps  [JUMP GAME ]
#Given an array of N integers arr[] where each element represents the max length of the jump that can be made forward from that element. 
#Find the minimum number of jumps to reach the end of the array

                   ### there may be two to three approach possible one is Native or brut force approch by that time complexibity come O(n*2)
def minium_jump(arr,n):     ### if we use dp method we need some other arrray to store due to this space complexibility will increase 
                             ### so best method to come here iteration through whole array
    if n<=1:                     ## only one or or may be no element present in array 
        return 0
    if arr[0]==0:           ### if first element is zero than we can not jump , so our answer according to problem comes -1
        return -1
    jump=0                     ## this I finally want and take in starting as 0
    max_range=0           ### this show maxium how far can I go from my point 
    halt=0                    #### this is like a secene of film if only good secene occur than I chage halt value to max_range
    i=0            ### by this we traversal for every element in array
    while i<n-1:
        max_range=max(max_range,i+arr[i])       ### we updated max_range by everyindexing value of array 
        if max_range>n-1:       #### eg( 9,1,1,1,1) here at initial max_range become 9 and that is greater than its length its mean we reached upto end of array so we simple increment our jump to 1 and return it 
            jump=jump+1
            return jump
        if i==halt:            #### if my i ==halt means I checked all elemnt between halt and i halt can help us to reach end of the array by minium number of jumps 
            halt=max_range
            jump=jump+1
        if halt>=n-1:          ##try to dry run code you getter better idea 
            return jump
        
        i=i+1  ## by this we are checking every element of our array
    return -1      ## we can not reach upto end at finallt so return -1
print(minium_jump([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9],11))
print(minium_jump([1, 4, 3, 2, 6, 7],6))
    
        


# In[ ]:




