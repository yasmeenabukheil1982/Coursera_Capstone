#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install html5lib


# In[2]:


pip install bs4


# In[12]:


pip install lxml


# ## Beginning of Part 1
# ## import required library

# In[1]:


import pandas as pd 


# ## Define the Wiki URL

# In[2]:


URL = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"


# ## Read the wiki 

# In[3]:


df = pd.read_html(URL)[0]


# ## Only process the cells that have an assigned borough. Ignore cells with a borough that is Not assigned

# In[4]:


df = df[df.Borough != 'Not assigned']


# ## for each similar postcode, combine corresponding neighbourhood in one row with the neighborhoods separated with a comma

# In[5]:


df = df.groupby(['Postcode', 'Borough'])['Neighbourhood']
df = df.apply(list).apply(lambda x:', '.join(x))
df = df.to_frame().reset_index()
df.head()


# ## f a cell has a borough but a Not assigned neighborhood, then the neighborhood will be the same as the borough

# In[6]:


for index, row in df.iterrows():
    if row['Neighbourhood'] == 'Not assigned':
        row['Neighbourhood'] = row['Borough']


# ## use the .shape method to print the number of rows of your dataframe

# In[7]:


df.shape


# ## Beginning of Part 2
# ## Read a csv file that has the geographical coordinates of each postal code

# In[8]:


file=pd.read_csv("https://cocl.us/Geospatial_data")


# ## Rename Postal Code to Postcode and combine the excel file data with dataframe based on Postcode

# In[9]:


file.columns = ['Postcode', 'Latitude', 'Longitude']
df = pd.merge(file, df, on='Postcode')
df


# ## Reorder columms to match the required format of the dataframe 

# In[10]:


df = df[['Postcode', 'Borough', 'Neighbourhood', 'Latitude', 'Longitude']]
df


# In[ ]:





# In[ ]:




