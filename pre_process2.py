#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
import numpy as np
df= pd.read_csv("/Users/priyamdeka/Downloads/Load_data_new.csv")
print (df)


# In[41]:


indices_to_remove=list(range(0,59904))+list(range(64272,70080))
df=df.drop(indices_to_remove)
df


# In[42]:


df.columns


# In[43]:


columns_to_remove=['solar_irridiation[W/m²]','total_cloud_cover[from ten]','electricity_demand_values[kw]']
df=df.drop(columns_to_remove,axis=1)
df


# In[48]:


df=df.rename(columns={"Time":"Timestamps"})
df


# In[71]:


df.to_csv("/Users/priyamdeka/phd/data/data2/1.csv")


# In[77]:


df


# In[81]:


df1


# In[84]:


columns_to_drop=["air_temperature[degree celcius]","relative_humidity[%]","wind_speed[M/S]","heat_demand_values[kw]"]
df1=df1.drop(columns=columns_to_drop)
df1


# In[85]:


df1.columns


# In[86]:


df1.to_csv("/Users/priyamdeka/phd/data/data2/timestamp.csv")


# In[69]:


print("df1.shape(1)")


# In[88]:


df2=pd.read_csv("/Users/priyamdeka/phd/data/data2/timestamp.csv")


# df2

# In[89]:


df2


# In[90]:


df2=df2.drop(columns="Unnamed: 0", axis=1)
df2


# In[94]:


df2["Timestamps"]=pd.to_datetime(df2["Timestamps"], format= '%Y-%m-%d %H:%M:%S')
df2


# In[95]:


df2["Hour_radians"]=(df2["Timestamps"].dt.hour * 2 * np.pi)/24


# In[96]:


df2


# In[97]:


df2["hour_sine"]= np.sin(df2["Hour_radians"])


# In[98]:


df2


# In[99]:


df2["hour_cos"]=np.cos(df2["Hour_radians"])


# In[100]:


df2


# In[101]:


df2=df2.drop(columns=["Timestamps","Hour_radians"],axis=1)


# In[102]:


df2


# In[113]:


df2.to_csv("/Users/priyamdeka/phd/data/data2/timestamp_sin_cos.csv")


# In[114]:


df


# In[116]:


df3=pd.read_csv("/Users/priyamdeka/phd/data/data2/1.csv")
df3


# In[117]:


df3=df3.drop(columns=["Unnamed: 0"])
df3


# In[118]:


df3=df3.drop(columns=["air_temperature[degree celcius]","relative_humidity[%]","wind_speed[M/S]","heat_demand_values[kw]"], axis=1)


# In[119]:


df3


# In[120]:


df3["air_pressure[mmHg]"]=df3["air_pressure[mmHg]"].interpolate()


# In[121]:


df3


# In[122]:


df3.to_csv("/Users/priyamdeka/phd/data/data2/air_pressure.csv")


# In[124]:


df4=pd.read_csv("/Users/priyamdeka/phd/data/data2/1.csv")
df4


# In[125]:


df5=df4.drop(columns=["Unnamed: 0","air_pressure[mmHg]","relative_humidity[%]","wind_speed[M/S]","heat_demand_values[kw]"], axis=1)
df5


# In[126]:


df5["air_temperature[degree celcius]"]=df5["air_temperature[degree celcius]"].interpolate
df5


# In[127]:


df5.to_csv("/Users/priyamdeka/phd/data/data2/air_temperature_interpolated.csv")


# In[131]:


df6 = df4.drop(columns=["Unnamed: 0", "air_pressure[mmHg]", "air_temperature[degree celcius]", "wind_speed[M/S]", "heat_demand_values[kw]"], axis=1)
df6


# In[132]:


df6["relative_humidity[%]"] = df6["relative_humidity[%]"].interpolate()
df6


# In[133]:


df6.to_csv("/Users/priyamdeka/phd/data/data2/relative_humidity_interpolated.csv")


# In[134]:


df7=df4.drop(columns=["Unnamed: 0","air_pressure[mmHg]","air_temperature[degree celcius]","relative_humidity[%]","heat_demand_values[kw]"],axis=1)


# In[135]:


df7


# In[136]:


df7["wind_speed[M/S]"]= df7["wind_speed[M/S]"].interpolate()


# In[137]:


df7


# In[138]:


df7.to_csv("/Users/priyamdeka/phd/data/data2/wind_speed_interpolated.csv")


# In[139]:


df4


# In[140]:


df8=df4.drop(columns=["Unnamed: 0","air_pressure[mmHg]","air_temperature[degree celcius]","relative_humidity[%]","wind_speed[M/S]"], axis=1)


# In[141]:


df8


# In[142]:


df8.to_csv("/Users/priyamdeka/phd/data/data2/TS.csv")


# In[145]:


df8.to_excel("/Users/priyamdeka/phd/data/data2/TS.xlsx", index=False)


# In[146]:


df9= df8["heat_demand_values[kw]"].interpolate()
df9


# In[147]:


df9.to_csv("/Users/priyamdeka/phd/data/data2/y_variable/heating_loads_interpolated.csv")


# In[148]:


df10=pd.read_csv("/Users/priyamdeka/phd/data/data2/y_variable/HL_zero_missingvalues.csv")
df10


# In[149]:


df10["heat_demand_values[kw]"]=df10["heat_demand_values[kw]"].interpolate()
df10


# In[150]:


df10["heat_demand_values[kw]"]=df10["heat_demand_values[kw]"].fillna(method="ffill")
df10


# In[152]:


df10


# In[153]:


df10['Timestamps'] = pd.to_datetime(df10['Timestamps'])
df10 = df10.set_index('Timestamps')
df10['heat_demand_values[kw]'] = df10['heat_demand_values[kw]'].interpolate(method='time')
df10


# In[155]:


df10.index = pd.to_datetime(df10.index)
df10_interpolated = df10.interpolate(method='time')
df10


# In[157]:


df10.to_csv("/Users/priyamdeka/phd/data/data2/hl1.csv")


# In[ ]:




