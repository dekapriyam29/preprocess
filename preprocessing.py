#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
df= pd.read_csv("/Users/priyamdeka/phd/data/data2/X_variables/days.csv")
df


# In[3]:


df1=pd.read_csv("/Users/priyamdeka/phd/data/data2/1/x_variables1.csv")
df1


# In[4]:


df.drop(index=4368, inplace=True)
df


# In[5]:


df.drop(columns={'Unnamed: 0'}, inplace=True)
df


# In[7]:


df2=pd.concat([df,df1], axis=1)
df2


# In[8]:


df2.rename(columns={"air_temperature[degree celcius]": "air_temperature","air_pressure[mmHg]":"air_pressure", "relative_humidity[%]":"relative_humidity"}, inplace= True)
df2


# In[9]:


df2.reset_index(drop=True, inplace=True)
df2


# In[11]:


# Assuming df2 is your DataFrame
df2.columns = ['hour_sine','hour_cos','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','air_temperature','air_pressure','relative_humidity']
df2


# In[14]:


df2.dtypes


# In[16]:


columns_to_convert = ['hour_sine', 'hour_cos', 'Monday', 'Tuesday', 'Wednesday', 'Thursday']
df2[columns_to_convert] = df2[columns_to_convert].astype(float)

df2


# In[17]:


df2.dtypes


# In[18]:


df2.to_csv("/Users/priyamdeka/phd/data/data2/code_data/1.csv", index=False)


# In[19]:


df3=pd.read_csv('/Users/priyamdeka/phd/data/data2/code_data/y_variables.csv')
df3


# In[20]:


df3.dtypes


# In[ ]:





# In[ ]:




