# localhost-custom-webpage
This tool allows you host webpage with **CUSTOM** html code using Python and Flask.
# Requirements
- Python
- - Python library "Flask"
# How to..?
## Install
### Linux
Run this command in terminal:
```bash
_f(){
clear || cls || :; echo "PIP seems is not installed. Install it."; exit
}
_d(){
sudo apt install curl; sudo apt install wget;
pip3 install flask
wget https://raw.githubusercontent.com/VBPROGER/localhost-custom-webpage/main/src/localhost_hoster.py
chmod +x localhost_hoster.py
}
clear || cls || :; _d || _f
```
### Mac OS
Same as Linux.
### Windows
```bash
echo "Not aviable for Windows yet, but soon will be. Download ZIP from GitHub."
# cls && pip install flask || echo "PIP seems is not installed. Install it."; exit
```
## Run
You need to setup your server.
First, create folder `templates` and file `templates/index.html`.
You can add anything there. Now, add file called `web_conf.yaml` with the following contents:
```yaml
# * web_conf.yaml *
# These contents can be changed!
index: index.html # Do not use `templates/*.html`, use just `*.html`.
ip: 127.0.0.1 # You can also set as `localhost`, or any other IP.
port: 1234 # Port to host on
```
This will be config for your web server. Now, start the server:
### Start in Linux
```sh
env python3 localhost_hoster.py
```
### Start in Mac OS
```sh
python3 localhost_hoster.py
```
### Start in Windows
```powershell
python3.exe localhost_hoster.py
```
The server is now running. Congratulations!
## Stop
### Stopping server in Linux
To stop your server, press Ctrl+D.
### Stopping server in Mac OS
Same as Linux.
### Stopping server in Windows
To stop your server, press Ctrl+Z.
