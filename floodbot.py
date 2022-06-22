import pyautogui
import time
time.sleep(5)
for c in range(0, 101):
    f = open("flood.txt", "r")
    for word in f:
        pyautogui.typewrite(word)
        time.sleep(0.5)
        for d in range(0, 2):
            pyautogui.press("enter")
