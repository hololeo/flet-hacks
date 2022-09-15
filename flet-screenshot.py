# by hololeo
from flet import flet, Page, Image, Container, Text, TextField, Row, Column, ElevatedButton, alignment
import time
import pyscreenshot as ImageGrab

# pip3 install pyscreenshot

def take_screenshot (e):
    page = e.control.page
    y = page.window_top
    x = page.window_left
    w = page.window_width
    h = page.window_height

    # note: in two monitor setup, this only works if flet window in first monitor (0,0)
    screen = ImageGrab.grab(
        bbox=( x, y, w+x,h+y )
    )

    # Flet caches local images, so ugly cache buster needed
    # this code needs improvement!

    t = str(time.time())
    loadImageCacheBuster = f"assets/{t.split('.')[0]}.png"
    screen.save(loadImageCacheBuster)
    loadImage = Image(src=loadImageCacheBuster, fit="contain")

    # load /replace saved screenshot image
    if len(page.imageContainer.controls) >= 1:
        page.imageContainer.clean()
    page.imageContainer.controls.append (loadImage)
    page.update()

def main (page: Page):
    page.title = "Flet Screenshot Hack - @Hololeo"
    page.window_always_on_top =  True
    btn = ElevatedButton ("Take screenshot", on_click = take_screenshot) 
    input_tf = TextField ()
    page.imageContainer = Column ()
    page.add ( Row ([input_tf,btn]))    
    page.add (page.imageContainer )
    page.scroll = "auto"
    page.update ()

flet.app(target=main, assets_dir="assets")
