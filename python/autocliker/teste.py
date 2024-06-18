import pyautogui as p
import time

print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = p.position()
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)


#         #pyautogui.moveTo(100,,5)
#         #pyautogui.moveTo(0,200,5)
#         #pyautogui.dragTo(100, 200, button='left')
            
#         #pyautogui.dragTo(100, 200, button='left')     # drag mouse to X of 100, Y of 200 while holding down left mouse button
#         #pyautogui.dragTo(300, 400, 2, button='left')  # drag mouse to X of 300, Y of 400 over 2 seconds while holding down left mouse button
        
                
        
except KeyboardInterrupt:
    print('\n')

time.sleep(5)

# p.mouseDown(button='left')
# p.moveTo(1000, 1000)

# p.mouseUp(button='left')

# p.keyDown('win')
# p.press('r')  
# p.keyUp('win')
# p.hotkey('win', 'r')
# p.write('cmd')
# p.press('enter')

# time.sleep(1)

# p.write('ipconfig')
# p.press('enter')

# texto = p.prompt(text='', title='' , default='')
# print(texto)
