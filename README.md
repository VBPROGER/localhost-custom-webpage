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
pip install flask
curl https://raw.githubusercontent.com/VBPROGER/localhost-custom-webpage/main/src/lhost_custom.py > lhost_custom.py
chmod +x lhost_custom.py
}
clear || cls || :; _d || _f
```
### Mac OS
Same as Linux.
### Windows
```bash
cls && pip install flask || echo "PIP seems is not installed. Install it."; exit
```
