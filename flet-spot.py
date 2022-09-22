# Flet Metals Spot Kitco Prices by Hololeo

import flet
from flet import Page, Tab, Tabs, Image
import time
import threading

isRunning = False

def update_App():
    global isRunning
    update_tabs()
    time.sleep (60)
    update_App()

def getSilver():
    return Image(src=f"https://www.kitco.com/images/live/silver.gif?ts={time.time()}")

def getGold():
    return Image(src=f"https://www.kitco.com/images/live/gold.gif?ts={time.time()}")

def getPlatinum():
    return Image(src=f"https://www.kitco.com/images/live/plati.gif?ts={time.time()}")

def tab_on_change (e):
    update_tabs ()

def update_tabs ():
    t = gPage.tabs
    t.tabs[0].content = getGold()
    t.tabs[1].content = getSilver()
    t.tabs[2].content = getPlatinum()
    t.update()  

def buildTabs(page):
    t = Tabs(
        selected_index=1,
        animation_duration=300,
        tabs=[
            Tab (text="Gold",content=getGold(),),
            Tab (text="Silver",content=getSilver(),),
            Tab (text="Platinum",content=getPlatinum(),),
        ],
        expand=1,
        on_change = tab_on_change
    )
    return t

def main(page: Page):
    global gPage
    gPage = page
    page.title = "Flet Spot - Hololeo Labs"
    page.tabs = buildTabs(page)
    page.add(page.tabs)
    page.update()
    isRunning = True
    th = threading.Thread (target=update_App, args={}, daemon=True)
    th.start()
    
flet.app(target=main)

