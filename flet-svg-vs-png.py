# Flet SVG vs PNG Demo - Hololeo Labs
# requires flet 0.1.60
# demonstrates using SVG vs PNG scaling pixelation
import flet
from flet import Image, Page, Slider, Column, Row, ElevatedButton, Text

def main(page: Page):

    svg_logo = "https://raw.githubusercontent.com/dnfield/flutter_svg/master/example/assets/wikimedia/Firefox_Logo_2017.svg"
    png_logo = "https://i.imgur.com/Dj0DBD1.png"

    def slider_on_change (e):
        amount = e.control.value/100 +0.20
        amount = amount * 5
        page.image.scale = amount
        page.update()

    def on_svg_btn (e):
        page.header.value = "logo.svg (vector)"
        page.image.src = svg_logo
        page.update()

    def on_png_btn (e):
        page.header.value = "logo.png (pixel)"
        page.image.src = png_logo     
        page.update()   

    page.title = "Flet svg vectors! Hololeo Labs"
    page.header = Text ("logo.png (pixel)", size=24)
    page.image = Image (src=svg_logo,width=200,height=200, expand=True)
    svg_btn = ElevatedButton("svg", on_click = on_svg_btn)
    png_btn = ElevatedButton("png", on_click = on_png_btn)
    slider = Slider(min=0, max=100, label="{value}%", expand=True)
    slider.on_change = slider_on_change    
    r1 = Row ([page.image], expand = True, alignment="center")
    r2 = Row ([svg_btn, png_btn,slider])
    page.image.src = png_logo
    col = Column ([r1,page.header,r2],expand=True)
    page.add (col)
    
flet.app(target=main, assets_dir="assets")
