#!/bin/bash
R='\033[1;91m'; G='\033[1;92m'; Y='\033[1;93m'; C='\033[1;96m'; P='\033[1;95m'; W='\033[1;97m'; N='\033[0m'; BLD='\033[1m'
clear
echo -e "${R}╔═══════════════════════════════════════════════════════════════╗"
echo -e "║${C}██╗    ██╗ █████╗      ██████╗██████╗ ██╗   ██╗███████╗██╗  ██╗${R}║"
echo -e "║${C}██║    ██║██╔══██╗    ██╔════╝██╔══██╗██║   ██║██╔════╝██║  ██║${R}║"
echo -e "║${C}██║ █╗ ██║███████║    ██║     ██████╔╝██║   ██║███████╗███████║${R}║"
echo -e "║${C}██║███╗██║██╔══██║    ██║     ██╔══██╗██║   ██║╚════██║██╔══██║${R}║"
echo -e "║${C}╚███╔███╔╝██║  ██║    ╚██████╗██║  ██║╚██████╔╝███████║██║  ██║${R}║"
echo -e "║${C} ╚══╝╚══╝ ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝${R}║"
echo -e "╚═══════════════════════════════════════════════════════════════╝${N}"
echo -e "${P}${BLD}              WA CRUSH INSTALLER v1.0${N}"
echo -e "${Y}              WhatsApp Account Termination Tool${N}"
echo -e "${C}              Developer: INSANE OWL${N}"
echo -e "${G}              github.com/insaneowl-spec/WA_CRUSH-${N}\n"
sleep 2
echo -e "${C}[*] Starting installation...\n${N}"
echo -e "${Y}[*] Installing dependencies...${N}"
pip install requests colorama 2>/dev/null
mkdir -p $PREFIX/etc/wa-crush
cp wa-crush.py $PREFIX/bin/wa-crush.py 2>/dev/null
chmod +x $PREFIX/bin/wa-crush.py 2>/dev/null
echo '#!/bin/bash' > $PREFIX/bin/wa-crush
echo "python3 $PREFIX/bin/wa-crush.py \"\$@\"" >> $PREFIX/bin/wa-crush
chmod +x $PREFIX/bin/wa-crush
echo '#!/bin/bash' > $PREFIX/bin/crush
echo "python3 $PREFIX/bin/wa-crush.py \"\$@\"" >> $PREFIX/bin/crush
chmod +x $PREFIX/bin/crush
echo -e "${G}[+] Installation complete!${N}"
echo -e "${Y}Run: ${C}crush${N}"
