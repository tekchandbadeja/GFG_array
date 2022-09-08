#!/usr/bin/env python
# coding: utf-8

# In[5]:


##Palindromic Array 
#Given a Integer array A[] of n elements. Your task is to complete the function PalinArray. 
#Which will return 1 if all the elements of the Array are palindrome otherwise it will return 0.

#Simple approch 1
def PalinArray(arr,n):
    for i in arr:  # here we iterate our i in arr using for loop to check for evere element that presented in array
        j=str(i)    # in array we have integer value , and by the use of slicing we can not reverse  a number so first we changing every number into string 
        if j!=j[::-1]:   ## by this we checking every number that is equal to its reverse or not 
            return False   ## by this if we find any number that is not a palindrome , we return False 
    return True            ###  this line shows if every number is equal to its reverse than finally we getting True as a bollean value
obj=PalinArray([111,222,333,444,555],5)
obj2=PalinArray([121,131,20],3)
if obj2:
    print(1)
else:
    print(0)


# In[11]:


## Big approch 2 

def palin_helper(num):   ### here i made a helper function by that we can find a reverse of any number 
    reverse_num=0
    while num!=0:        #### 426 reverse is like 0*10+6=6
                        ##### 6*10+2=62
                        #####62*10+4=624
        reminder=num%10
        reverse_num=reverse_num*10+reminder
        num=num//10
    return reverse_num       #### by this we returned reverse value of our given number 
        
def Palinarray(arr,n):
    l=[]                  ## here i made a empty list first 
    for i in arr:
        if i==palin_helper(i):        #### check every i to its reverse value  
            l.append(1)               ### if value is equal to its reverse value than append 1
        else:
            l.append(0)               #### if not than append 0
    if l.count(1)==n:                ### this is used because by that if there is n 1 present in our list means every number is palindrome so we can retuen True 
        return True
    else:
        return False         ### this show may be one or more than this not 1 they are 0 so it return False

obj=PalinArray([111,222,333,444,555],5)
obj2=PalinArray([121,131,20],3)
if obj2:
    print(1)
else:
    print(0)
    

