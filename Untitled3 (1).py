#!/usr/bin/env python
# coding: utf-8

# In[5]:


import pyautogui as posicaoabrearquivo

posicaoabrearquivo.hotkey('win','r')

posicaoabrearquivo.sleep(2)

posicaoabrearquivo.typewrite('notepad')

posicaoabrearquivo.sleep(2)

posicaoabrearquivo.press('enter')

posicaoabrearquivo.sleep(3)

posicaoabrearquivo.typewrite('abrimos o notepad com um script')

posicaoabrearquivo.sleep(3)

fecharjanelaNP = posicaoabrearquivo.getActiveWindow()

posicaoabrearquivo.sleep(3)

fecharjanelaNP.close()

posicaoabrearquivo.sleep(2)

posicaoabrearquivo.press('tab')

posicaoabrearquivo.sleep(2)

posicaoabrearquivo.press('enter')


# In[ ]:




