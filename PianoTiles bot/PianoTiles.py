import pyautogui
import time
import keyboard
import PIL.ImageGrab

time.sleep(2)
A = PIL.ImageGrab.grab().load()[729,635] #collected RGB value of pixel
S = PIL.ImageGrab.grab().load()[851,637]
D = PIL.ImageGrab.grab().load()[1027,603]
F = PIL.ImageGrab.grab().load()[1235,667]
start = (73, 138, 236) #RGB value of Starting tile, the first tile
if A == start:
       pyautogui.click(729,635)
elif S == start:
       pyautogui.click(851,637)
elif D == start:
       pyautogui.click(1027,603)
elif F == start:
       pyautogui.click(1235,667)
       
while not keyboard.is_pressed("q"):
    A1 = list(PIL.ImageGrab.grab().load()[729,635])
    a, b, c = A1
    if a>200 and b<160  and c>230:  # tile color is pink, RGB value (236, 33, 255), 
        pyautogui.click(729,635)  # hence compare it to find some near to this
    S1 = list(PIL.ImageGrab.grab().load()[851,637])
    a, b, c = S1
    if a>200 and b<160 and c>230:
        pyautogui.click(851,637)
    D1 = list(PIL.ImageGrab.grab().load()[1027,603])
    a, b, c = D1
    if a>200 and b<160 and c>230:
        pyautogui.click(1027,603)
    F1 = list(PIL.ImageGrab.grab().load()[1235,667])
    a, b, c = F1
    if a>200 and b<160 and c>230:
        pyautogui.click(1235,667)






# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:34:06 2021

@author: AATMAN
"""
