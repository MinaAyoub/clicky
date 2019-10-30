import pyautogui
import random

pyautogui.FailSafeException = True

pyautogui.moveTo(875, 0, duration=0)
n =0
while n < 4000:
    r = random.randint(20,570)
    pyautogui.moveTo(r, r, duration=3)
    pyautogui.press("shift")
    
    n += 1


#pyautogui.PAUSE = 2.5
"""
plist = []
print(pyautogui.position())
print (plist)
pyautogui.click()
"""
