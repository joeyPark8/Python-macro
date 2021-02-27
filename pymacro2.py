import pyautogui as pag
import time as t

interval = 40

y = 0

pos = pag.position()

t.sleep(5)

for i in range(5):
    pag.moveTo(1100, 85 + y)
    pag.doubleClick()
    t.sleep(0.5)
    
    pag.hotkey('ctrl', 'c')
    t.sleep(2)

    
    pag.moveTo(221, 85 + y)
    pag.click()
    t.sleep(0.5)

    pag.write('     ')
    t.sleep(0.5)

    pag.hotkey('ctrl', 'v')
    y += interval
    t.sleep(2)
    
