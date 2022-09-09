#!/usr/bin/env python
# coding: utf-8

# In[1]:


## First and last occurrences of x

def first_occurence(arr,n,key): ### by this function we will get first index of of our x , so here I used simple binary search method
    si=0
    li=n-1
    ans=-1       ## initial we assign ans as -1
    while (si<=li):
        mid=(si+li)//2
        if arr[mid]==key:
            ans=mid           ### by this we are updating ans value to topmost left occuring of x
            li=mid-1         ### this is work here like a "GAME PLAYER" by this we are always trying to choose left most part of our array because left occurence we can find inly left side 
        elif arr[mid]<key:
            si=mid+1
        elif arr[mid]>key:
            li=mid-1
    return ans                ### " TIME COMPEXITY"= O(log(n))


# In[6]:


def last_occurence(arr,n,key):
    si=0
    li=n-1
    ans=-1
    while (si<=li):
        mid=(si+li)//2
        if arr[mid]==key:
            ans=mid
            si=mid+1    #### every thing is same like previous but this is GAME CHANGER because it's help us to go right side of array
        elif arr[mid]<key:
            si=mid+1
        elif arr[mid]>key:
            li=mid-1
    return ans              ### "TIME COMPLEXITY "==O(log(n))


# In[8]:


def first_last_of_x(arr,n,x):
    ans1=first_occurence(arr,n,x)      ## by this we returning first occurence of x and storing its value in ans1
    ans2=last_occurence(arr,n,x)       ## by this we returning last occurence of x and storing its value in ans2
    return ans1,ans2                ##by this we will get our output as a TUPLE 


# Time complexity==(log(n)+log(n))
#                ==log(n**2)   by log property 
#                ==2*(log(n))






first_last_of_x([1, 3, 5, 5, 5, 5, 7, 123, 125],9,7)
first_last_of_x([1, 3, 5, 5, 5, 5, 67, 123, 125],9,5)

