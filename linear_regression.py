#!/usr/bin/env python
# coding: utf-8

# In[34]:


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

x=[73.84701702,68.78190405,74.11010539,69.22708106,67.10453999,70.3439986]
x=np.array(x)
y=[241.8935632,162.3104725,212.7408556,185.9160215,165.3738242,177.4732819]
y=np.array(y)
 

fig = plt.figure()
ax = plt.axes()
ax.plot()
plt.scatter(x, y)
plt.show()
 
 
x_mean=x.mean()
#print(x_mean)
y_mean=y.mean()
#print(y_mean)
xy=(x-x_mean)*(y-y_mean)
x2=(x-x_mean)**2
b1=xy.sum()/x2.sum()
b0=y_mean-b1*x_mean
#print(xy)
#print(x2)
#print(b1)
#print(b0)


# calcculate mean
x_mean=x.mean()
y_mean=y.mean()
xy=(x-x_mean)*(y-y_mean)
x2=(x-x_mean)**2
b1=xy.sum()/x2.sum()
b0=y_mean-b1*x_mean
print(b0,b1)
y1=b0+b1*x
plt.scatter(x,y,color="red")
plt.plot(x,y1,"bs-")
for i in range(1,len(x),1):
    plt.plot([x[i],x[i]],[y[i],y1[i]])
plt.show()



# In[ ]:





# In[ ]:





# In[35]:


#calculating error
error=y-y1
SSE=(error**2).sum()
print("SSE:"+str(SSE))

reg=y1-y.mean()
SSR=(reg**2).sum()
print("SSR:"+str(SSR))
SST=SSR+SSE
print("SST:"+str(SST))
r_sqr=SSR/SST
print("R_SQR:"+str(r_sqr))


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[19]:


sum_x_sqr=(x**2).sum()
sum_x=x.sum()
sum_y=y.sum()
sum_xy=(x*y).sum()
n=len(x)
b01=(sum_x_sqr*sum_y-sum_x*sum_xy)/(n*sum_x_sqr-sum_x**2)
b11=(sum_y-b0*n)/sum_x
print(b0,b1)
print(b01,b11)


# In[7]:


import math
r=0.8
N=61
t=(math.sqrt(N-2))/(math.sqrt(1-(r**2)))
print(t)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[8]:


import math
r=0.2
N=32
t=(math.sqrt(N-2))/(math.sqrt(1-(r**2)))
print(t)


# In[7]:



import matplotlib.pyplot as m
x = [1,1,2,3,4,5,6] 
y = [1,3,4,4,5,8,9]     
m.plot(x, y) 
m.show()
  


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[2]:





# In[ ]:




