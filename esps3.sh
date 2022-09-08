#!/bin/bash
python -m ensurepip --upgrade
#install sfo
/home/deck/.local/bin/pip3 install ps3iso
#install the script
python es-ps3-hd-link.py
