#!/usr/bin/python3
# Configuration import: use yaml
import yaml, os
from flask import Flask, render_template

DEF_CONF_NAME = 'web_conf.yaml'
DEF_IP =        'localhost'
DEF_PORT =      5000
DEF_INDEX_F =   'index.html'
try:
    F =             open(DEF_CONF_NAME, 'r+')
except (BaseException, Exception, IOError, OSError):
    print('Please configure your server in file `web_conf.yaml`.')
    os._exit(1)

# Start
config = yaml.safe_load(F.read())
app = Flask(__name__)
F.close() # Close file to avoid some problems..

@app.route('/')
def index():
    # Index (main) page
    return render_template(config.get('index') or DEF_INDEX_F)

# Start server
app.run(host = config.get('ip') or DEF_IP, port = config.get('port') or DEF_PORT)
