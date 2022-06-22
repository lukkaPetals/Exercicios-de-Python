import pyautogui
import time
for c in range(0, 9):
    time.sleep(5)
    f = open("flood.txt", "r")
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")
