# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 16:38:08 2017

@author: musta
"""

import pyautogui
pyautogui.size()
(1920,1080)
width, height = pyautogui.size()


#pyautogui.click(1733, 11)
#for i in range (2):
#    pyautogui.moveTo(100,100, duration=1)
#    pyautogui.moveTo(200,100, duration=1)
#    pyautogui.moveTo(200,200, duration=1)
#    pyautogui.moveTo(100,200, duration=1)


print pyautogui.position()
pyautogui.click(102, 885)
pyautogui.typewrite(['Enter'])
pyautogui.typewrite(['Enter'])
pyautogui.typewrite(['Enter'])
pyautogui.typewrite(['Enter'])
pyautogui.typewrite('Anything can be automated now')




