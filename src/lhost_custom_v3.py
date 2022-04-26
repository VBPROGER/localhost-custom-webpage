#!/usr/bin/python3
# Configuration
FILE_NAME = 'index.html'

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template(FILE_NAME)

# Start server
app.run(host = '0.0.0.0', port = 5000)
