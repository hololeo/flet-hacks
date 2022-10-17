# Flet Shell - Hololeo labs
# passes a command line to shell, and captures and displays output
# WARNING EXPERIMENTAL - running this gives direct access to your shell!
# needs optimizations, etc - 'its a hack!'

import flet
from flet import Page,Text, TextField, Column,alignment
import os, subprocess, sys

env = os.environ.copy()

def run_process(cmd_str, cwd=None, realtime=True, page=None, close_at_end=False, on_output=None):
    # shoutout @Skquark for original sub process code, since modified
    cmd_list = cmd_str if type(cmd_str) is list else cmd_str.split()
    if realtime:
        if cwd is None:
            process = subprocess.Popen(cmd_str, shell = True, env=env, bufsize = 1, stdout=subprocess.PIPE, stderr = subprocess.STDOUT, encoding='utf-8', errors = 'replace' ) 
        else:
            process = subprocess.Popen(cmd_str, shell = True, cwd=cwd, env=env, bufsize = 1, stdout=subprocess.PIPE, stderr = subprocess.STDOUT, encoding='utf-8', errors = 'replace' ) 
        while True:
            realtime_output = process.stdout.readline()
            if realtime_output == '' and process.poll() is not None:
                break
            if realtime_output:
                print (realtime_output.strip(), flush=False)
                s = realtime_output.strip()
                on_output(s)
                sys.stdout.flush()
        if close_at_end:
            pass
    else:
        if cwd is None:
            return subprocess.run(cmd_list, stdout=subprocess.PIPE, env=env).stdout.decode('utf-8')
        else:
            return subprocess.run(cmd_list, stdout=subprocess.PIPE, env=env, cwd=cwd).stdout.decode('utf-8')

def on_output (s):
    global gPage
    newText = Text (value = s, size = 16, color = "yellow", selectable = True)
    gPage.output.controls.append (newText)
    gPage.output.update()    

def makeCommandLineInput ():
    global on_output, gPage
    def onSubmit (e):
        rawinput = e.control.value
        gPage.output.clean()  
        run_process (f"{rawinput}", page=e.page, on_output=on_output, realtime=True)
        print (rawinput)
    t = TextField (label="Dangerous Command Line", on_submit=onSubmit)
    return t

def makeOutput():
    global gPage
    control = Text (
        value = "Flet Shell - Hololeo Labs",
        color = "Green",
        size =24,
        selectable = True,
        width = gPage.width,
    )
    col = Column (
        controls = [control],
        scroll="auto", 
        auto_scroll = True,
        alignment = "start",
        expand = True
    ) 
    col.root = col
    col.textfield = control  
    return col

gPage = None
def main(page: Page):
    global gPage
    gPage = page
    page.title = "Flet Shell - Hololeo Labs"
    page.commandline = makeCommandLineInput()
    page.output = makeOutput()
    col = Column ([page.output,page.commandline])
    col.expand = True
    col.alignment = "start"
    page.add (col)
    page.update()

flet.app(target=main, assets_dir="assets")
# flet.app(target=main, view=flet.WEB_BROWSER)
