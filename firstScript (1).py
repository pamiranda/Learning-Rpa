#!/usr/bin/env python
# coding: utf-8
Abrindo a calculadora no menu Iniciar
# In[13]:


import pyautogui as ag

ag.sleep(4)
#print(ag.position())


ag.moveTo(x=24, y=749)
ag.click(x=24, y=749)

ag.sleep(2)

ag.moveTo(x=468, y=362)
ag.click(x=468, y=362)


