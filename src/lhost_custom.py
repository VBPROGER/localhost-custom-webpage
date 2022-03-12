#!/usr/bin/python3
import os
#os.system('clear || cls || :')
try:
    from flask import Flask
except BaseException:
    print('Flask seems is not to be installed... Install it.')
    exit(0)

def html(codeHtml = None, *args):
    global FINAL_HTML_CODE
    FINAL_HTML_CODE = ''
    for code in codeHtml:
        FINAL_HTML_CODE += str(code).replace('\n', '')
    return str(FINAL_HTML_CODE)
def Flask_Init():
    app = Flask(__name__)
    if __name__ == "__main__":
        debug = True
        @app.route('/')
        def home():
            FINAL_HTML_CODE = GLOBAL_HTML_CODE
            return str(FINAL_HTML_CODE)
        app.run(port = 8080, debug = debug)
def Main_Init():

    DoneCode = 'finish16';
    Input_Content = '';
    HTML = []

    print('Welcome!\nThis tool allows you to host website on localhost with custom HTML content.\nPaste your HTML code below (type "'+str(DoneCode)+'"):')
    while not Input_Content == DoneCode:
        Input_Content = input()
        if not Input_Content == DoneCode:
            HTML.append(Input_Content)
    if str(len(HTML)) != '0' and str(len(HTML)) != '1' and HTML != None and HTML != '':
        print('Initialiazing Flask...')
        global GLOBAL_HTML_CODE
        GLOBAL_HTML_CODE = html(codeHtml = HTML)
        print('Starting flask on "http://127.0.0.1:8080"')
        Flask_Init()
        exit(0)
    else:
        print('Sorry, empty HTML code is not allowed.')

if __name__ ==  '__main__':
    Main_Init()
# HTML code example:
"""
<h1>hello!</h1>
<p>what's up?</p>
finish16
"""
