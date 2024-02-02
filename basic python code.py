#!/usr/bin/env python
# coding: utf-8

# In[1]:


# basic use of print function 
    
print("hello world!")


# In[2]:


print(6)


# In[3]:


print(True)


# In[4]:


print("india","pakistan","nepal")


# In[5]:


print("india",5,5.5,True)


# In[6]:


print("india","pakistan","nepal",sep="/")


# In[7]:


print("india","pakistan","nepal",sep = "-")


# In[8]:


print("hello",end = " ")
print("World")


# In[9]:


# DATA TYPES

#INTEGERS

print(4)


# In[10]:


print(1e309)


# In[11]:


#float

print(5.5)
print(1.7e308)


# In[12]:


#boolean
print(False)


# In[13]:


# complex
print(2+4j)


# In[14]:


# string
print("hello")
print('hello')
print("""hello""")


# In[15]:


# list 
print([1,2,3,45])


# In[16]:


#tuples
print((3,4,5,6,7))


# In[17]:


#set
print({7,8,5,64})


# In[18]:


#Dictionary
print({"name":"nadir","age":21,"weight":58})


# In[19]:


# Variables
name = "nadir"
print(name)


# In[20]:


a = 5
print(a)


# In[21]:


# python performs dynamic binding
# here is no variable decleration
print(name)


# In[22]:


name = 5
print(name)


# In[23]:


name = True
print(name)


# In[24]:


a = 4;b = 6;c = 8
print(a)
print(b)
print(c)


# In[25]:


a,b,c = 5,7,8
print(a)
print(b)
print(c)


# In[26]:


a = b = c = 6
print(a)
print(b)
print(c)


# In[27]:


# keywords

import keyword
print(keyword.kwlist)


# In[28]:


# identifiers
name = "nadir"
print(name)


# In[29]:


_ = "nadir"
print(_)


# In[30]:


first_name = "mohd"
print(first_name)


# In[31]:


# user taking input through input function

input()


# In[32]:


input("what is your name")


# In[38]:


first_num = int(input("enter the number"))
second_num = int(input("enter the number"))


# In[39]:


print(first_num)
print(second_num)


# In[40]:


result = first_num +second_num
print(result)


# In[41]:


# type function
print(type(first_num))


# In[42]:


first_num


# In[43]:


name


# In[44]:


print(type(name))


# In[45]:


a = 56
print(type(a))


# In[59]:


# type conversion----> conversion of data type from one data type  to another data type.

a = 56
b ='78'
print(type(a))
print(type(b))



# In[60]:


c = a+b
print(c)


# In[61]:


# now
c = a+ int(b)
print(c)


# In[62]:


a = [1,23,4,54,]
print(a)
print(type(a))


# In[63]:


tuple(a)


# In[64]:


name = "674"
print(type(name))


# In[65]:


int(name)


# In[66]:


print(type(int(name)))


# In[ ]:


# there are two types type conversion
# implicit type conversion
# explicit type conversion


# In[67]:


# implicit type conversion.
4+4.5


# In[68]:


5+4+9j


# In[69]:


5.5+6+8j


# In[70]:


# Explicit type conversion
# int

a = '78'
int(a)


# In[71]:


#float

b = 56
float(b)


# In[72]:


c = 56
complex(c)


# In[ ]:


# type conversion is not permanent operation

