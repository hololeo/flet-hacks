# Flet Lorem Ipsum Generator - Hololeo Labs
import flet
from flet import Page, Row, Text, TextField, Slider, Dropdown, dropdown, padding

def main(page: Page):
    page.title = "Flet Lorem Ipsum Generator - Hololeo Labs"
    page.window_always_on_top = True
    page.update()

flet.app(target=main, port=7777)
#flet.app(target=main, port=7777, view=flet.WEB_BROWSER)


