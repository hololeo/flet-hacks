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

    def update_lorem ():
        #s = lorem.createText (dd.value,int(tf.value))
        s = "asdf"
        t2.value = s
        page.update()

    def dropdown_changed(e):
        update_lorem()

    def tf_on_changed (e):
        try: 
            val = int(e.control.value)
            if val > 99:
                val = 99
            tf.value = val
            update_lorem()
        except:
            print ("num textfield not number")
            tf.value = 3

    tf = TextField (
        label="",
        keyboard_type = "number",
        value = 3,
        max_lines=1,
        min_lines=1,
        width=50,
        on_submit = tf_on_changed,
        on_blur = tf_on_changed       
    )

    dd = Dropdown(
        on_change=dropdown_changed,
        value = "Paragraph",
        options=[
            dropdown.Option("Word"),
            dropdown.Option("Sentence"),
            dropdown.Option("Paragraph"),
        ],
        width=200,
    )

    page.header = Text (
        value = "Flet Lorem Ipsum Generator",
        size = 25
    )
    page.ui_row = Row ([tf,dd])
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
    page.add (Column ([page.header, page.ui_row, page.output], expand= True))
    page.update()

flet.app(target=main, port=7777)
#flet.app(target=main, port=7777, view=flet.WEB_BROWSER)





