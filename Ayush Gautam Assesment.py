#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# In[2]:


weather = pd.read_csv("data/weather.csv.txt")


# In[3]:


weather


# In[4]:


data = {'City': ['London', 'London', 'London', 'London', 'Paris', 'Paris', 'Paris', 'Paris'],
        'Season': ['Fall', 'Winter', 'Spring', 'Summer','Fall', 'Winter', 'Spring', 'Summer'],
            'Temperature': [68,94,103,21,46,86,26,70]}


# In[5]:


df=pd.DataFrame(data)


# In[6]:


df.set_index('City', inplace=True)


# In[7]:


df


# In[8]:


from datetime import datetime, timedelta

start_date = datetime(1947, 8, 15)
end_date = datetime.now()


date_range = pd.date_range(start=start_date, end=end_date, freq='D')


df = pd.DataFrame({
    'day': date_range.day,
    'month': date_range.month,
    'year': date_range.year
})
print (df)


# In[9]:


df.head(20)


# In[10]:


df.to_csv('C:/Users/admin/Documents/example.csv', index=False)


# In[11]:


df


# In[12]:


from collections import Counter

def top_k_frequent(nums, k): 
    counts = Counter(nums)
    
    top_k = counts.most_common(k)
    
    return [item[0] for item in top_k]


# In[13]:


nums = [1, 2, 3, 4, 5, 1, 2, 3, 1, 2, 1]
k = 2
print(top_k_frequent(nums, k))


# In[ ]:


SELECT Id, Full_Name, Marks
FROM students_data
ORDER BY marks DESC
LIMIT 3;


# In[ ]:


WITH Quartile_Marks AS (
  SELECT
    student_id,
    marks,
    NTILE(4) OVER (ORDER BY marks) AS quartile
  FROM
    students_data )
SELECT
  student_id,
  marks,
  CASE
    WHEN quartile = 1 THEN '1st Division'
    WHEN quartile = 2 THEN '2nd Division'
    WHEN quartile = 3 THEN '3rd Division'
    WHEN quartile = 4 THEN '4th Division'
  END AS quartile_group
FROM
  Quartile_Marks;


# In[ ]:




