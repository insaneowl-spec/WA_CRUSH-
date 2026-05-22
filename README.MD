# WA CRUSH - WhatsApp Account Termination Tool

> **Developer: INSANE OWL**
> **Version: 1.0 | Termux Edition**
> **For Authorized Security Testing Only**

## LEGAL NOTICE

This tool is for **authorized penetration testing only**. You must have explicit permission to test the target phone number. Unauthorized use is illegal. The developer is not responsible for misuse.

## Features

- Telegram controlled - attack from anywhere
- 7 attack vectors simultaneously
- 60-150 threads for maximum damage
- IRREVERSIBLE - permanently bans the number
- First-run setup wizard
- Auto-fetches your Chat ID
- Config saved for future use

## Installation (Step by Step for Termux)

Copy and paste each command one at a time:

```bash
pkg update -y && pkg upgrade -y
pkg install python git -y
pip install requests
git clone https://github.com/insaneowl-spec/WA_CRUSH-.git
cd WA_CRUSH-
bash install.sh
crush
