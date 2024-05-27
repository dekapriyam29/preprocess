#!/usr/bin/env python
# coding: utf-8

# In[11]:


import pandas as pd
import numpy as np
df= pd.read_csv("/Users/priyamdeka/Downloads/Load_data_new.csv")
print (df)


# In[12]:


df=df.drop(columns=["air_pressure[mmHg]","air_temperature[degree celcius]","relative_humidity[%]","wind_speed[M/S]","solar_irridiation[W/m²]","total_cloud_cover[from ten]","electricity_demand_values[kw]"],axis=1)
df


# In[13]:


df=df.drop(list(range(0,59184))+list(range(64991,70080)))
df


# In[15]:


df['Time'] = pd.to_datetime(df['Time'])
df = df.set_index('Time')
df["heat_demand_values[kw]"] = df["heat_demand_values[kw]"].interpolate(method='time')
df


# In[16]:


df.to_csv("/Users/priyamdeka/phd/data/data2/y_variable/HL_interpolated.csv")


# In[17]:


df.to_excel("/Users/priyamdeka/phd/data/data2/y_variable/HL.xlsx")


# In[18]:


df1=pd.read_csv("/Users/priyamdeka/phd/data/data2/y_variable/HL.csv")
df1


# In[19]:


df1['Time'] = pd.to_datetime(df1['Time'])
df1 = df1.set_index('Time')
df1["heat_demand_values[kw]"] = df1["heat_demand_values[kw]"].interpolate(method='time')
df1


# In[20]:


df1.to_csv("/Users/priyamdeka/phd/data/data2/y_variable/heatingloads_inter.csv")


# In[21]:


df2=pd.read_csv("/Users/priyamdeka/phd/data/data2/y_variable/heatingloads_inter.csv")
df2


# In[22]:


df2=df2.drop(list(range(0,719))+list(range(5088,5807)))
df2


# In[23]:


df2=df2.drop(index=719)
df2


# In[24]:


df2.to_csv("/Users/priyamdeka/phd/data/data2/y_variable/hl_interpolated.csv")


# In[ ]:




