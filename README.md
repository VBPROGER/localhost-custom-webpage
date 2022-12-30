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
