#!/usr/bin/env python
# coding: utf-8

# # Estimating the cost of Equity from historical Price Data

# In[1]:


import pandas as pd


# In[31]:


df=pd.read_excel('price data.xlsx')
df.head()


# # Calculation the Return

# In[32]:


return_tr=df.pct_change()
return_tr.head()


# # Calculating the market risk premium

# In[33]:


risk_free=0.03
return_tr['MRP']=return_tr['Market Portfolio']-risk_free
return_tr.head()


# In[34]:


return_tr=return_tr.dropna()


# # Calculating B

# In[37]:


import statsmodels.api as sm


# In[42]:


x=sm.add_constant(return_tr['MRP'])
y=return_tr['Asset Price']
model=sm.OLS(y,x)
result=model.fit()
result.summary()


# In[43]:


beta=result.params['MRP']
beta


# # Estimating the cost of Equity

# In[47]:


cost_of_equity=risk_free+ beta*(return_tr['Market Portfolio'].mean()-risk_free)
cost_of_equity


# In[ ]:




