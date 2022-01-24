#!/usr/bin/env python
# coding: utf-8

# Abrindo o navegador Chrome e pesquisando o valor do dólar hoje

# In[2]:


import pyautogui as ag

ag.sleep(3)

#print(ag.position())

ag.moveTo(x=35, y=531)

ag.sleep(2)

ag.doubleClick(x=35, y=531)

ag.sleep(2)

ag.press('enter')

ag.sleep(2)

ag.typewrite("dolar")

ag.sleep(2)

ag.press('enter')


# In[ ]:




