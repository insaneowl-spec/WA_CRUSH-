#!/bin/bash

# Quick setup for WA CRUSH
echo "[*] Installing WA CRUSH dependencies..."
pkg install python -y
pip install requests
echo "[+] Dependencies installed!"
echo "[*] Run 'python wa-crush.py' to start"
