#!/usr/bin/env python
# coding: utf-8

# <h1>hotkey permite combinar duas teclas<h1>

# In[ ]:


import pyautogui as ag

ag.sleep(2)
ag.hotkey('win', 'r')

ag.sleep(2)
ag.typewrite('n
             otepad')
ag.sleep(2)
ag.press('enter')
ag.sleep(2)
ag.typewrite('Abrimos o notepad usando um Script')
closenotepad = ag.getActiveWindow()
closenotepad.close()
ag.press('tab')
ag.sleep(2)
ag.press('enter')
ag.sleep(2)


# In[ ]:




