import pyautogui, time
from random import seed
import random

time.sleep(1)
pyautogui.FAILSAFE = True
seed(1)
for i in range(1000):
    if i % 6 == 0 or i % 3 == 0 or i % 9 ==0:
        value = random.randint(155,389)/ 10000
        print('click every fifth' + str(value))
        pyautogui.click(500,600, clicks=1,interval=value,button='left')
    else:
        value = random.randint(155,389)/ 100000000000
        print('click ' + str(value))
        pyautogui.click(500,600, clicks=1,interval=value,button='left')
    # pyautogui.click(500,600, clicks=12,interval=.00000000000001,button='left')
