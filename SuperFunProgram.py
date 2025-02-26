import pyautogui
import random
import time

pyautogui.FAILSAFE = False

for count in range(50):
    pyautogui.moveTo(random.randint(0,1920),random.randint(0,1080))
    pyautogui.click()
    pyautogui.typewrite(["ctrl"])
    pyautogui.typewrite(["alt"])
    
pyautogui.typewrite(["win"])
time.sleep(0.2)
pyautogui.write("notepad")
time.sleep(1)
pyautogui.typewrite(['enter'])
time.sleep(1)
pyautogui.write("LORD FORGIVE FOR I HAVE SINNED, WOE IS ME")
time.sleep(2)

while True:
    pyautogui.write("WOE IS ME\n")
    pyautogui.moveTo(random.randint(0,1920),random.randint(0,1080))