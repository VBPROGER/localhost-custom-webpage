#!/usr/bin/python3
import os
#os.system('clear || cls || :')
try:
    from flask import Flask
except BaseException:
    print('Flask seems is not to be installed... Install it.')
    exit(0)

global html
html = ''
app = Flask(__name__)
try:
    with open('index.html', 'r') as file:
        html = file.read()
except FileNotFoundError:
    print('The "index.html" file doesn\'t exist!')
except IsADirectoryError:
    print('That\'s a directory, not file!')
except BaseException:
    print('Error :(')
    exit(0)

@app.route('/')
def home():
    global html
    return str(html)

app.run(port = 8080, debug = False)