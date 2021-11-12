#!/usr/bin/env python
# coding: utf-8

# In[1]:


#declare input functon x[n] and impulse function h[n]
input_function = [2,2,1]
impulse_function = [3, 3, 3, 3, 3]

input_function_size = len(input_function)
impulse_function_size = len(impulse_function)


# In[2]:


#declare output function y[n] with appropriate size, and initialize all values to zero.
output_function = [0] * (input_function_size + impulse_function_size - 1)


# In[3]:


#Perform DT Convolution
for x in range(0, input_function_size):
    for y in range(0, impulse_function_size):
        output_function[x + y] += input_function[x] * impulse_function[y]


# In[4]:


#Print output function
print("x[n] = ", input_function)
print("h[n] = ", impulse_function)
print("y[n] = x[n] * h[n] = ", output_function)


# In[ ]:

input("Press Enter to exit program.")




