#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df1=pd.read_csv("/Users/priyamdeka/phd/data/data2/code_data/1.csv")
df2=pd.read_csv("/Users/priyamdeka/phd/data/data2/code_data/y_variables.csv")
df1


# In[2]:


df2


# In[3]:


# Check for non-numeric values in the DataFrame
non_numeric_rows = df1.apply(lambda row: pd.to_numeric(row, errors='coerce').isnull(), axis=1)
problematic_rows = df1[non_numeric_rows]
print(problematic_rows)


# In[4]:


df1


# In[5]:


df1=df1.astype(float)


# In[6]:


df1.dtypes


# In[7]:


df1.dtypes


# In[8]:


df3=pd.read_csv("/Users/priyamdeka/phd/data/data1/1.csv")
df3


# In[9]:


df3.dtypes


# In[10]:


df1_str = df1.astype(str)
df1_concatenated = df1_str.apply(';'.join, axis=1)
df1['concatenated_features'] = df1_concatenated
df1.drop(df1.columns[:-1], axis=1, inplace=True)
df1['concatenated_features'] = df1['concatenated_features'].astype('object')


# In[11]:


df1.dtypes


# In[12]:


df1


# In[ ]:




