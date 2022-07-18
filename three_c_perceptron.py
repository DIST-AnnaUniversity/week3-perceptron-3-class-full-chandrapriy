#!/usr/bin/env python
# coding: utf-8

# In[5]:


import math
import numpy as np
def multiple_iterations():
    y_new = np.array([[10,2,-1],[2,-5,-1],[-5,5,-1]])
    w = np.array([[1,-2,0],[0,-1,2],[1,3,-1]])
    d = np.array([[1,-1,-1],[-1,1,-1],[-1,-1,1]])
    c=1
    iter=5
    out=np.zeros((3,3))
    r=np.zeros((3,3))
    for i in range(1,iter):
        for n,x in enumerate(y_new):
            net=np.dot(y_new[n],np.transpose(w))
            out[n]=net
            out[n][out[n]>0]=1
            out[n][out[n]<=0]=-1
            r[n]=d[n]-out[n]
            delta_w=0.5*np.dot(np.transpose(r),y_new)
            w=w+delta_w
            print(w)
            return w
def  check_new(weights):
    y_new = np.array([[11,3,1],[2,-6,1],[-6,6,1]])
    out= np.zeros((3,3))
    for n,x in enumerate(y_new):
        net=np.dot(y_new[n],np.transpose(weights))
        out[n]=net
        out[n][out[n]>0]=1
        out[n][out[n]<=0]=-1
        print(out)
        return out
weights = multiple_iterations()
check_new(weights)


# In[ ]:




