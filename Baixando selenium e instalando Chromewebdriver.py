#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().system('pip install selenium')


# In[3]:


from selenium import webdriver
opennav = webdriver.Chrome()
opennav.get('https://www.google.com.br/')


# In[ ]:




