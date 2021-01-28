#!/usr/bin/env python
# coding: utf-8

# In[ ]:


##Write a function so that the columns of the output matrix are powers of the input vector.
#The order of the powers is determined by the increasing boolean argument. Specifically, when increasing is False, the i-th output column is the input vector raised element-wise to the powerof N - i - 1.


# In[2]:


#creating a matrix with ouput columns based on input vector(N)

import numpy as np
x=np.array([1,2,3,4,5])
N=5
matrix = np.column_stack([x**(N-i-1) for i in range(N)])
print(matrix)


# In[3]:


#similar matrix is created using np.vander function in numpy

import numpy as np
x=np.array([1,2,3,4,5])
N=5
matrix1 = np.vander(x,N,increasing=False)
print(matrix1)


# In[4]:


#the determitant for both the matrices is same
np.linalg.det(matrix)


# In[5]:


np.linalg.det(matrix1)


# In[ ]:




