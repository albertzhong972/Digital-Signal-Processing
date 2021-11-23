#!/usr/bin/env python
# coding: utf-8

# In[6]:


#declare input signal x[n] and impulse response h[n]
input_signal = [2,2,1,3,5,4]
impulse = [1,-1]

input_size = len(input_signal)
impulse_size = len(impulse)


# In[7]:


#declare output function y[n] with appropriate size, and initialize all values to zero.
output_size = (input_size + impulse_size - 1)
output = [0] * output_size


# In[8]:


#Perform DT Convolution (Using Input Side Algorithm)
for x in range(0, input_size):
    for y in range(0, impulse_size):
        output[x + y] += input_signal[x] * impulse[y]


# In[4]:


#Perform DT Convolution (Using Output Side Algorithm)
for x in range(0, output_size):
    output[x] = 0
    for y in range(0, impulse_size):
        if((x - y) < 0):
            continue
        if((x - y) > input_size - 1):
            continue
        output[x] += impulse[y] * input_signal[x - y]


# In[9]:


#Print output function
print("x[n] = ", input_signal)
print("h[n] = ", impulse)
print("y[n] = x[n] * h[n] = ", output)


# In[28]:


#create the x-index arrays for plotting purposes only

input_index = [0] * input_size
for x in range(0, input_size):
    input_index[x] = x;
    
impulse_index = [0] * impulse_size
for x in range(0, impulse_size):
    impulse_index[x] = x;
    
output_index = [0] * output_size
for x in range(0, output_size):
    output_index[x] = x;
    


# In[29]:


#Plot x[n], h[n], and y[n]

import matplotlib.pyplot as plt
import numpy as np


a = np.array(input_index)
x = np.array(input_signal)

b = np.array(impulse_index)
h = np.array(impulse)

c = np.array(output_index)
y = np.array(output)


fig, axs = plt.subplots(3)
fig.suptitle('Discrete Time Convolution')


axs[0].stem(a,x)
axs[0].set_title("Input Signal x[n]")


axs[1].stem(b,h)
axs[1].set_title("Impulse Response h[n]")


axs[2].stem(c,y)
axs[2].set_title("Output Signal y[n]")

fig.set_size_inches(18.5, 10.5) #adjusts size of plots
fig.tight_layout(pad=3.0) #adjusts spacing between plots


# In[9]:


input("Press Enter to exit!")

