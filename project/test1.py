import pyautogui as pag
import time

screen_width, screen_height = pag.size()

pag.moveTo(screen_width/2, screen_height/2, duration=2)
time.sleep(0.3)
pag.click()
time.sleep(0.3)
pag.write("hello world!", interval=0.1)
