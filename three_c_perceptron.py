#!/usr/bin/env python
# coding: utf-8

# In[14]:


import math
import numpy as np
def multiple_iterations():
     for n in range(1,iterations):
        print ("Iteration ", n)
        print ("--------------")
        y=np.array([[10,2,-1],[2,-5,-1],[-5,5,-1]])  
        print("Input vlaues",y)
        w=np.array([[1,-2,0],[0,-1,2],[1,3,-1]])
        print("Intial values of weights",w)
        d=np.array([[1,-1,-1],[-1,1,-1],[-1,-1,1]])
        print("Teacher value",d)
        c=1
        out=np.zeros((3,3))
        r=np.zeros((3,3))
        net=np.dot(y[0],np.transpose(w))
        print("Net value:",net)
        out[0]=net
        out[0][out[0]>0]=1
        out[0][out[0]<=0]=-1
        r[0]=d[0]-out[0]
        del_w=0.5*np.dot(np.transpose(r),y)
        w=w+del_w
        print(w)
def check_new(weight):
    for i,x in enumerate(y_new):
        del_w=0.5*np.dot(np.transpose(r),y_new)
        weight=weight+del_w
        net=np.dot(y_new[0],np.transpose(w))
        out[0]=net
        out[0][out[0]>0]=1
        out[0][out[0]<=0]=-1
        r[0]=d[0]-out[0]
    return weight
iterations=6
y_new=np.array([[11,3,1],[2,-6,1],[-6,6,1]])
print("New Input values:",y_new)
final_weight=multiple_iterations()
print ("Testing")
print ("--------")
final_output=check_new(y_new)
print ("Final output: ", final_output)
    


# In[ ]:




