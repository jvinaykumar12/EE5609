#!/usr/bin/env python
# coding: utf-8

# In[18]:


import math
import numpy as np

x = 5
a = -3*x                                
matrix = np.array([[x+a,x,x],[x,x+a,x],[x,x,x+a]])
determinant = np.linalg.det(matrix)
print('Determinant of the given matrix when x = -a is:', determinant)


# In[ ]:




