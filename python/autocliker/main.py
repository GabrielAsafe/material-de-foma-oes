import pyautogui as p
import time
import threading

p.moveTo(5,5)
x,y = p.locateAllOnScreen('teams.png', confidence=0.9)

print(x.left + x.height, x.top)

p.click(x.left + x.height, x.top+y.width)

time.sleep(1)


p.click(228,324)

p.click(780,966)


while(True):
    p.write('ola, caro colega')
    p.press('enter')


