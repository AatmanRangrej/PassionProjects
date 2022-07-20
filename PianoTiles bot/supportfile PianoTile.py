import pyautogui
import time
import keyboard
import PIL.ImageGrab
time.sleep(2)
A = PIL.ImageGrab.grab().load()[729,635] #collected RGB value of pixel
S = PIL.ImageGrab.grab().load()[851,637]
D = PIL.ImageGrab.grab().load()[1027,603]
F = PIL.ImageGrab.grab().load()[1235,667]


print("A ", A)
print("S ", S)
print("D ", D)
print("F ", F)


#print(pyautogui.position())