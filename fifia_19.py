#!/usr/bin/env python
# coding: utf-8

# In[25]:


import numpy as np
import scipy as ss
from collections import Counter
import math
from scipy import stats
import pandas as pd
data=pd.read_csv("")
#print(data.columns)

traindf=pd.readcsv('')
y=traindf['Overall']>=87
x=traindf.copy()
del x['Overall']
feature_name=list(x.columns)
num_feats=30
print(feature_name)
def cor_selector(x,y,num_feats):
    cor_list=[]
    feature_name=x.columns.tolist()
    for i in x.columns.tolist():
        cor=np.corrcoef(x[i],y)[0,1]
        cor_list.append(cor)
        cor_list=[0 if np.isnan(i) else i for i in cor_list]
        cor_feature=x.iloc[:,np.argsort(np.abs(cor_list))[-num_feats:]].columns.tolist()
        cor_support=[True if i in cor_feature else False for i in feature_name]
        return cor_support, cor_feature
cor_support,cor_feature= cor_selector(x,y,num_feats)
print(str(cor_feature)),'selected features'
cor_feature
    


# In[27]:


cd C:\Users\XUB\Downloads\data_sets-master (1)\data_sets-master


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





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[3]:


cd Downloads\data_sets-master\data_sets-master


# In[ ]:





# In[ ]:




