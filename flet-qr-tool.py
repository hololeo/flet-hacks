# Flet QR code generator by hololeo

import flet
from flet import Page, Image, TextField, Image
from io import BytesIO
import qrcode   # pip3 install qrcode[pil]
import base64

def qr_str2img (s):
    qr = qrcode.make (s)
    buffered = BytesIO()
    qr.save(buffered, format="JPEG")
    s1 = base64.b64encode(buffered.getvalue())
    b64_string = s1.decode ('utf-8')
    return (b64_string)

def main(page: Page):
    page.title = "QR code generator"
    page.vertical_aligment = "center"
    page.horizontal_alignment = "center"
    page.scroll = "always"

    def textbox_changed(e):
        url = qr_str2img (e.control.value)
        page.controls.pop()
        img = Image (src_base64 = url)
        page.add (img)
        page.update()

    tf1 = TextField(label="Enter URL/Text Data and press ENTER", on_change=textbox_changed) 
    img = Image (src = "https://user-images.githubusercontent.com/11970940/190875540-d45afb9a-9d09-44b0-93c4-8159b28ea6df.png")
    page.add (tf1)
    page.add (img)
    page.update()

flet.app(target=main, assets_dir="./")
#flet.app (target=main, assets_dir="./",port=777, view=flet.WEB_BROWSER)

