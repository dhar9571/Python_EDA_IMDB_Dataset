#!/usr/bin/env python
# coding: utf-8

# # Importing Libraries:

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# # Loading te Dataset:

# In[6]:


data = pd.read_csv("C:\\Users\\dk957\\Downloads\\imdb_data.csv")


# In[9]:


data.nunique()


# In[12]:


list(data.columns)


# In[13]:


# removing columns which are not required:

data = data[['id',
 'belongs_to_collection',
 'budget',
 'genres',
 'original_language',
 'original_title',
 'popularity',
 'production_companies',
 'production_countries',
 'release_date',
 'runtime',
 'status',
 'title',
 'Keywords',
 'cast',
 'crew',
 'revenue']]


# In[15]:


pd.set_option("display.max_columns",None)


# In[17]:


data.isna().sum()


# In[32]:


data = data[['id',
 'budget',
 'genres',
 'original_language',
 'original_title',
 'popularity',
 'production_companies',
 'production_countries',
 'release_date',
 'runtime',
 'status',
 'title',
 'cast',
 'crew',
 'revenue']]


# In[33]:


data.info()


# In[34]:


data.isna().sum()


# In[35]:


sns.heatmap(data)


# In[44]:


sns.heatmap(data.isna(), cmap='YlGnBu')


# In[45]:


corr = data.corr()


# In[49]:


sns.heatmap(corr,annot=True,cmap="coolwarm")


# In[50]:


import seaborn as sns
import pandas as pd

# create a sample dataframe
df = pd.DataFrame({
    'A': [1, 2, 3, 4, 5],
    'B': [5, 4, 3, 2, 1],
    'C': [1, 3, 5, 7, 9],
    'D': [9, 7, 5, 3, 1]
})

# create a correlation matrix
corr_matrix = df.corr()

# create a correlation heatmap using Seaborn
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')


# In[ ]:




