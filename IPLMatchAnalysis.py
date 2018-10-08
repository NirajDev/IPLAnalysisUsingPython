
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import numpy as np


# In[3]:


import matplotlib.pyplot as plt


# In[4]:


data_1 = pd.read_csv('matches.csv')


# In[5]:


data_1.shape


# In[6]:


data_1.head()


# In[14]:


data_2 = data_1.drop_duplicates(['season'],keep = 'last')


# In[17]:


print (data_2['winner'])


# In[19]:


data_1.head()


# In[24]:


data_2 = data_1[(data_1['toss_decision'] == 'field')]


# In[28]:


pd.value_counts(data_2['toss_decision'])
#chosen field after winning toss


# In[30]:


data_2 = data_1[(data_1['toss_decision'] == 'bat')]


# In[31]:


pd.value_counts(data_2['toss_decision'])
#chosen to bat after winning toss


# In[32]:


data_1 = pd.read_csv('deliveries.csv')


# In[33]:


data_1.head()


# In[45]:


data_2 = data_1.dropna(axis = 0)


# In[46]:


data_2.head()


# In[43]:


data_2 = data_1[data_1['player_dismissed']!=""]


# In[44]:


data_2.head()


# In[50]:


pd.value_counts(data_2['bowler']).head(10)


# In[51]:


data_2 = data_1[data_1['batsman_runs']==4]


# In[52]:


data_2.head()


# In[54]:


print (pd.value_counts(data_2['batsman']).head(10))


# In[55]:


data_2 = data_1[data_1['batsman_runs'] == 6]


# In[56]:


data_2.head()


# In[57]:


print (pd.value_counts(data_2['batsman']).head(10))


# In[58]:


data_2 = data_1[data_1['is_super_over']!=0]


# In[59]:


data_2.head()


# In[60]:


print (pd.value_counts(data_2['batting_team']))


# In[61]:


data_2 = data_1[data_1['wide_runs']!=0]


# In[62]:


data_2 = data_1[data_1['batsman_runs']!=0]


# In[63]:


data_2.head()


# In[65]:


pd.value_counts(data_2['batsman']).head(10)


# In[66]:


vrun = data_2[data_2['batsman'] == 'V Kohli']


# In[67]:


vrun.head()


# In[68]:


print(vrun['batsman_runs'].sum())


# In[75]:


data_1 = pd.read_csv('deliveries.csv')


# In[76]:


data_1.head()


#  data_2 = data_1.groupby(['batsman']).sum()

# In[86]:


data_2 = data_2.sort_values(['batsman_runs'],ascending=False)


# In[92]:


data_2.drop(columns = ['over','inning','match_id','ball','is_super_over','wide_runs','bye_runs','legbye_runs']).head(10)

