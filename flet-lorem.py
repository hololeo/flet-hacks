# Flet Lorem Ipsum Generator - Hololeo Labs
import flet
from flet import Page, Row, Column, Text, TextField, Slider, Dropdown, dropdown, padding

def main(page: Page):
    page.title = "Flet Lorem Ipsum Generator - Hololeo Labs"
    page.window_always_on_top = True
    page.window_opacity = 0.85
    page.bgcolor = "#262d2f"
    page.vertical_alignment = "start"
    page.padding = 10
    page.header = Text (
        value = "Flet Lorem Ipsum Generator",
        size = 25
    )
    page.output = TextField (
        label="",
        keyboard_type = "number",
        value = "Sit et, elit facilisi elit tempus fermentum ipsum ipsum ipsum maecenas nec at enim arcu molestie nibh."*1000,
        content_padding = padding.only (right=20),
        border_width = 2,
        max_lines=100,
        min_lines=10,
        expand = True,
        read_only = True 
    )    
    page.add (Column ([page.header, page.output], expand= True))
    page.update()

flet.app(target=main, port=7777)
#flet.app(target=main, port=7777, view=flet.WEB_BROWSER)





