# Flet threads cpu stress test by Hololeo
import flet
from flet import Page, Text
from flet import threading
import time

def main (page:Page):
    def on_thread (e):
        while e.th.running is True:
            # print ("thread tick")
            page.txt.value = time.time()
            page.update()
            time.sleep (0.1)
    page.window_always_on_top = True
    page.txt = Text ("",size=50)
    page.add (page.txt)
    page.th = threading.Thread (target=on_thread, args=[page], daemon= True)
    page.th.running = True
    page.th.start()
    page.update()    
flet.app (target=main)
#flet.app(target=main, view=flet.WEB_BROWSER)
