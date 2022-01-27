#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pyautogui as pg

opçao = pg.confirm('Clique na opção desejada', buttons = ['Excel', 'Word', 'Notepad'])

if opçao == "Excel":
    pg.hotkey ("win", "r")
    pg.sleep(2)
    pg.typewrite("Excel")
    pg.sleep(2)
    pg.press("enter")
    pg.sleep(2)
    pg.moveTo(x=267, y=193)    
elif opçao == "Word":
    pg.hotkey("win", "r")
    pg.sleep(2)
    pg.typewrite("word")
    pg.press("enter")
    
elif opçao == "Notepad":
    pg.hotkey("win", "r")
    pg.sleep(2)
    pg.typewrite("Notepad")
    pg.press("enter")


# In[ ]:





# In[ ]:




