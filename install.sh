#!/bin/bash

#========================================================
# WA CRUSH - WhatsApp Account Termination Tool
# Version: 1.0 | Termux Edition
# Developer: INSANE OWL
# Repository: https://github.com/insaneowl-spec/WA_CRUSH-
#========================================================

# Colors
R='\033[1;91m'
G='\033[1;92m'
Y='\033[1;93m'
B='\033[1;94m'
P='\033[1;95m'
C='\033[1;96m'
W='\033[1;97m'
N='\033[0m'
BLD='\033[1m'

clear

echo -e "${R}"
echo "╔═══════════════════════════════════════════════════════════════╗"
echo "║                                                               ║"
echo "║   ${C}██╗    ██╗ █████╗      ██████╗██████╗ ██╗   ██╗███████╗██╗  ██╗${R}   ║"
echo "║   ${C}██║    ██║██╔══██╗    ██╔════╝██╔══██╗██║   ██║██╔════╝██║  ██║${R}   ║"
echo "║   ${C}██║ █╗ ██║███████║    ██║     ██████╔╝██║   ██║███████╗███████║${R}   ║"
echo "║   ${C}██║███╗██║██╔══██║    ██║     ██╔══██╗██║   ██║╚════██║██╔══██║${R}   ║"
echo "║   ${C}╚███╔███╔╝██║  ██║    ╚██████╗██║  ██║╚██████╔╝███████║██║  ██║${R}   ║"
echo "║   ${C} ╚══╝╚══╝ ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝${R}   ║"
echo "║                                                               ║"
echo "╚═══════════════════════════════════════════════════════════════╝${N}"
echo ""
echo -e "${P}${BLD}              WA CRUSH INSTALLER v1.0${N}"
echo -e "${Y}              WhatsApp Account Termination Tool${N}"
echo -e "${C}              Developer: INSANE OWL${N}"
echo -e "${G}              https://github.com/insaneowl-spec/WA_CRUSH-${N}"
echo ""
echo -e "${G}========================================${N}"
echo -e "${G}  For Authorized Penetration Testing Only ${N}"
echo -e "${G}========================================${N}"
echo ""

sleep 2

# Check if running in Termux
if [ ! -d "/data/data/com.termux" ]; then
    echo -e "${R}[!] This tool is designed for Termux on Android${N}"
    echo -e "${Y}[!] For other platforms, install Python and requests manually${N}"
fi

echo -e "${C}[*] Starting WA CRUSH installation...${N}"
echo ""

# Update packages
echo -e "${Y}[*] Updating Termux packages...${N}"
pkg update -y && pkg upgrade -y
echo -e "${G}[+] Packages updated successfully${N}"
echo ""

# Install Python
echo -e "${Y}[*] Installing Python 3...${N}"
pkg install python -y
echo -e "${G}[+] Python 3 installed successfully${N}"
echo ""

# Install pip packages
echo -e "${Y}[*] Installing required Python libraries...${N}"
pip install --upgrade pip
pip install requests colorama
echo -e "${G}[+] Python libraries installed successfully${N}"
echo ""

# Create config directory
echo -e "${Y}[*] Creating configuration directory...${N}"
mkdir -p $PREFIX/etc/wa-crush
mkdir -p $HOME/.wa-crush
echo -e "${G}[+] Configuration directory created${N}"
echo ""

# Copy main script to bin
echo -e "${Y}[*] Installing main script...${N}"
cp wa-crush.py $PREFIX/bin/wa-crush
chmod +x $PREFIX/bin/wa-crush
echo -e "${G}[+] Script installed to $PREFIX/bin/wa-crush${N}"
echo ""

# Create shortcut command
echo -e "${Y}[*] Creating shortcut commands...${N}"

# wa-crush command
echo '#!/bin/bash' > $PREFIX/bin/wa-crush
echo "python $PREFIX/bin/wa-crush.py \$@" >> $PREFIX/bin/wa-crush
chmod +x $PREFIX/bin/wa-crush

# crush shortcut
echo '#!/bin/bash' > $PREFIX/bin/crush
echo "python $PREFIX/bin/wa-crush.py \$@" >> $PREFIX/bin/crush
chmod +x $PREFIX/bin/crush

echo -e "${G}[+] Shortcut commands created: wa-crush, crush${N}"
echo ""

# Verify installation
echo -e "${Y}[*] Verifying installation...${N}"
echo ""
if command -v python &> /dev/null; then
    echo -e "${G}[✓] Python: OK${N}"
else
    echo -e "${R}[✗] Python: FAILED${N}"
fi

if python -c "import requests" &> /dev/null; then
    echo -e "${G}[✓] Requests library: OK${N}"
else
    echo -e "${R}[✗] Requests library: FAILED${N}"
fi

if [ -f "$PREFIX/bin/wa-crush.py" ]; then
    echo -e "${G}[✓] Main script: OK${N}"
else
    echo -e "${R}[✗] Main script: FAILED${N}"
fi

echo ""
echo -e "${G}========================================${N}"
echo -e "${G}     INSTALLATION COMPLETE!${N}"
echo -e "${G}========================================${N}"
echo ""
echo -e "${C}${BLD}To run WA CRUSH, use:${N}"
echo -e "${W}  $ wa-crush${N}"
echo -e "${W}  $ crush${N}"
echo ""
echo -e "${Y}${BLD}Next Steps:${N}"
echo -e "${W}  1. Type: ${C}crush${W} or ${C}wa-crush${N}"
echo -e "${W}  2. You will be prompted to enter your Bot Token and Chat ID${N}"
echo -e "${W}  3. Configuration will be saved for future use${N}"
echo -e "${W}  4. The Telegram bot will start${N}"
echo -e "${W}  5. Open Telegram and send commands to your bot${N}"
echo ""
echo -e "${P}${BLD}Telegram Commands:${N}"
echo -e "${W}  ${C}/nuke +[number]${W}   - Destroy WhatsApp number${N}"
echo -e "${W}  ${C}/stress +[number]${W} - Maximum intensity attack${N}"
echo -e "${W}  ${C}/status${W}           - Check attack progress${N}"
echo -e "${W}  ${C}/stop${W}             - Stop attack${N}"
echo -e "${W}  ${C}/help${W}             - Show help${N}"
echo ""
echo -e "${Y}Example:${N}"
echo -e "${W}  /nuke +14155551234${N}"
echo ""
echo -e "${R}${BLD}WARNING: This tool permanently destroys WhatsApp accounts${N}"
echo -e "${R}Use only on numbers you own or have explicit permission to test${N}"
echo ""
echo -e "${G}${BLD}[+] WA CRUSH is ready to use!${N}"
echo ""
