#!/usr/bin/env python
# coding: utf-8

# # Write a program that prints the next 20 leap year and sum of digits of leap year must be greater than 16

# In[1]:


#first I need to create function called leap year
def leap_yr(): 
    
    #to get next 20 leap year use for looping starting from range (2020)
    for i in range(2020,2480):
        
        x  = i //1000 
        x1 = (i - x*1000)//100
        x2 = (i - x*1000 - x1*100)//10
        x3 = i - x*1000 - x1*100 - x2*10
        sum_of_digits=(x+x1+x2+x3)     #to get sum of digit this is the logic
      
        #leap year is a year which is divisible by 4 and 400 and 
        #according to the condition sum of digit is > 16 so the below logic is used 
        if i%400==0 or i%4==0 and sum_of_digits>16 :
            print(i)
            
Year=leap_yr()  #here the function is called as Year to get the output


# In[ ]:




