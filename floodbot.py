import pyautogui
import time
time.sleep(10)
f = open("flood.txt", "r")
for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
