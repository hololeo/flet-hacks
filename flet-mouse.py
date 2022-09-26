# Flet Mouse Position - Hololeo Labs
# this is a hack! Do not use it on nuclear submarines or missions to mars!
import flet
from flet import Page, Text
from flet import threading
import time
import pyautogui as pg

def main (page:Page):
    def on_thread (e):
        while e.th.running is True:
            x,y = pg.position()
            s = f"Desktop Mouse:x:{x},y:{y}"
            page.txt.value = s
            page.update()
            time.sleep (0.1)   

    page.title = "Flet Mouse Position - Hololeo Labs"
    page.window_always_on_top = True
    page.header  = Text ("Using pyautogui to get desktop mouse position", size = 30, color="blue")
    page.txt = Text ("",size=50)
    page.add (page.header, page.txt)

    # start thread to not lock up main thread
    page.th = threading.Thread (target=on_thread, args=[page], daemon= True)
    page.th.running = True
    page.th.start()    
    page.update() 

flet.app (target=main)
