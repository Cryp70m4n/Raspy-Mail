#!/bin/bash
if [ "$EUID" -ne 0 ]; then
  echo "[!] Please Run As Root"
  exit
fi

clear
echo "[+] INSTALLING NOW..."
sudo apt update

sudo apt-get install python3 python3-pip

pip3 install -r requirements.txt



clear
echo "[+] FINISHED INSTALLING!"
