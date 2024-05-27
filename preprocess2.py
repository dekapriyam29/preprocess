#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
df=pd.read_excel('/Users/priyamdeka/phd/data/data2/timestamps_weekdays.xlsx')
df


# In[2]:


df.columns


# In[3]:



import pandas as pd
import numpy as np

file_path = "/Users/priyamdeka/phd/data/data2/timestamps_weekdays.xlsx"
df = pd.read_excel(file_path)
print(df.head())
timestamp_column = 'time'
df[timestamp_column] = pd.to_datetime(df[timestamp_column], format='%d/%m/%Y %H:%M')
df['time_in_hours'] = df[timestamp_column].dt.hour + df[timestamp_column].dt.minute / 60
df['sine'] = np.sin(df['time_in_hours'] * 2 * np.pi / 24)
df['cosine'] = np.cos(df['time_in_hours'] * 2 * np.pi / 24)
print(df)


# In[4]:


df.columns


# In[5]:


df.columns.tolist()


# In[6]:


df.columns = df.columns.str.strip()
columns_to_drop = ['time', 'time_in_hours']
df = df.drop(columns=columns_to_drop, errors='ignore')
df


# In[7]:


columns = ['sine', 'cosine'] + [col for col in df.columns if col not in ['sine', 'cosine']]
df = df[columns]
df


# In[8]:


df=df.rename(columns={'sine':'hour_sin', 'cosine':'hour_cos'})
df


# In[9]:


df1=pd.read_csv("/Users/priyamdeka/phd/data/data2/code_data/x_variables1.csv")
df1


# In[10]:


df2=pd.concat([df,df1], axis=1, ignore_index=True)
df2


# In[11]:


df3=pd.concat([df,df1], axis=1)
df3


# In[12]:


df3.columns


# In[13]:


rename_columns={'air_temperature[degree celcius]':'air_temperature',
                'air_pressure[mmHg]':'air_pressure',
                'relative_humidity[%]':'relative_humidity'
               }
df3.rename(columns=rename_columns, inplace=True)
df3


# In[14]:


df3.dtypes


# In[15]:


df3=df3.astype('float64')
df3


# In[16]:


df3.dtypes


# In[ ]:





# In[17]:


df3


# In[18]:


df4=pd.read_csv('/Users/priyamdeka/phd/data/data2/y_variable/y_features.csv')
df4


# In[19]:


rename1={'heat_demand_values[kw]':'heating_loads'}
df4.rename(columns=rename1, inplace=True)
df4


# In[20]:


df4.dtypes


# In[23]:


df3.drop(4368)
df3


# In[25]:


index_to_remove = 4368
df3 = df3.drop(index_to_remove)


# In[26]:


df3


# In[27]:


df3.to_excel('/Users/priyamdeka/phd/data/data2/final_data/x_data2.xlsx', index=False)
df3.to_csv('/Users/priyamdeka/phd/data/data2/final_data/x_data2.csv', index=False)


# In[28]:


df3.dtypes


# In[29]:


df4.dtypes


# In[30]:


df4.to_excel('/Users/priyamdeka/phd/data/data2/final_data/y_data2.xlsx', index=False)
df4.to_csv('/Users/priyamdeka/phd/data/data2/final_data/y_data2.csv', index=False)


# In[31]:


columns_to_remove = [9, 10]
df5= df3.drop(df3.columns[columns_to_remove], axis=1)
df5


# In[33]:


df6=df3.drop(df3.columns[[8, 9]], axis=1)
df6


# In[34]:


df3


# In[35]:


df3


# In[ ]:




