#!/usr/bin/env python
# coding: utf-8

# In[3]:


import math
import numpy as np
def multiple_iterations(c,y,iterations,w,d):
     for n in range(1,iterations):
        print ("Iteration ", n)
        print ("--------------")
        for i, x in enumerate(y):
            net=np.dot(y[0],np.transpose(w))
            print("Net value:",net)
            out[0]=net
            out[0][out[0]>0]=1
            out[0][out[0]<=0]=-1
            r[0]=d[0]-out[0]
            del_w=c*np.dot(np.transpose(r),y_new)
            w=w+del_w
            print("weight:",w)
            return w
def check_new(weight,final_out):
    for i,x in enumerate(y_new):
        del_w=c*np.dot(np.transpose(r),y)
        weight=weight+del_w
        net=np.dot(y[0],np.transpose(w))
        out[0]=net
        out[0][out[0]>0]=1
        out[0][out[0]<=0]=-1
        r[0]=d[0]-out[0]
        final_out=final_out+r[0]
    return final_out
y=np.array([[10,2,-1],[2,-5,-1],[-5,5,-1]])  
print("Input vlaues",y)
y_new=np.array([[11,3,1],[2,-6,1],[-6,6,1]])
print("Input values:",y_new)
w=np.array([[1,-2,0],[0,-1,2],[1,3,-1]])
print("Intial values of weights",w)
d=np.array([[1,-1,-1],[-1,1,-1],[-1,-1,1]])
print("Teacher value",d)
c=0.5
iterations=7
out=np.zeros((3,3))
r=np.zeros((3,3))
final_weight=multiple_iterations(c,y_new,iterations,w,d)
print ("Final sets of weights: ", final_weight)
final_out = []
print ("Testing")
print ("--------")
final_output=check_new(final_weight,y_new)
print ("Final output: ", final_output)
    


# In[ ]:




