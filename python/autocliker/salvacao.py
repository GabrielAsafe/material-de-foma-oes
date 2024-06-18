import pyautogui

import os
import time

pyautogui.press("win")
pyautogui.typewrite('notepad')
pyautogui.press('enter')

time.sleep(1)

notepad_window = pyautogui.getWindowsWithTitle('notepad')[0]

pyautogui.hotkey('ctrl', 'n')

while(True):

    pyautogui.typewrite("\nHello There\n")
    time.sleep(30)


