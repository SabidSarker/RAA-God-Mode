import requests
import time
import os
import random
from bs4 import BeautifulSoup

# কালার কোড
G = '\033[32m'; R = '\033[31m'; Y = '\033[33m'; C = '\033[36m'; W = '\033[0m'

def banner():
    os.system('clear')
    print(f"""
{C}================================================
    {G}ULTIMATE FB DISCOVERY TOOL {Y}[v2.0]
{C}================================================
    {W}1. অটো নম্বর চেকার + নাম (Number Series)
    2. ইমেইল লিস্ট চেকার + নাম (Email List)
    3. ফ্রি প্রক্সি স্ক্যাপার (Get Fresh Proxies)
    0. এক্সিট
{C}================================================{W}
    """)

# ১. প্রক্সি স্ক্যাপার ফাংশন
def scrape_proxies():
    print(f"{Y}[*] ইন্টারনেট থেকে প্রক্সি সংগ্রহ করা হচ্ছে...{W}")
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
    try:
        res = requests.get(url)
        proxies = res.text.split('\r\n')
        with open("proxies.txt", "w") as f:
            for p in proxies:
                if p: f.write(p + "\n")
        print(f"{G}[✔] {len(proxies)}টি প্রক্সি সেভ করা হয়েছে (proxies.txt){W}")
    except:
        print(f"{R}[!] প্রক্সি সংগ্রহ করা যায়নি।{W}")

# ২. নাম বের করার ফাংশন
def get_name(target, proxy=None):
    url = f"https://m.facebook.com/login/identify/?ctx=recover&email={target}"
    headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 10)"}
    try:
        p_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"} if proxy else None
        res = requests.get(url, headers=headers, proxies=p_dict, timeout=5)
        soup = BeautifulSoup(res.text, 'html.parser')
        name = soup.find("strong")
        return name.text if name else "Unknown Name"
    except:
        return "Name Hidden/Error"

# ৩. মেইন চেকার ফাংশন
def checker(target, proxy_list):
    proxy = random.choice(proxy_list) if proxy_list else None
    url = f"https://www.facebook.com/login/identify/?ctx=recover&email={target}"
    try:
        p_dict = {"http": f"http://{proxy}", "https": f"http://{proxy}"} if proxy else None
        res = requests.get(url, proxies=p_dict, timeout=5)
        if "did_submit=1" not in res.url:
            name = get_name(target, proxy)
            return True, name
        return False, None
    except:
        return None, None

def main():
    while True:
        banner()
        choice = input(f"{Y}[?] অপশন সিলেক্ট করুন: {W}")
        
        proxies = []
        if os.path.exists("proxies.txt"):
            with open("proxies.txt", "r") as f:
                proxies = [line.strip() for line in f if line.strip()]

        if choice == '1':
            prefix = input(f"{C}[+] সিরিজ (যেমন 01711): {W}")
            start = int(input(f"{C}[+] শুরু (৬ ডিজিট): {W}"))
            end = int(input(f"{C}[+] শেষ (৬ ডিজিট): {W}"))
            for i in range(start, end + 1):
                num = f"{prefix}{str(i).zfill(6)}"
                status, name = checker(num, proxies)
                if status:
                    print(f"{G}[✔] আইডি আছে! নম্বর: {num} | নাম: {name}{W}")
                else:
                    print(f"{R}[X] আইডি নেই: {num}{W}")
                time.sleep(1)

        elif choice == '2':
            file = input(f"{C}[+] ফাইল নাম: {W}")
            try:
                with open(file, "r") as f:
                    for line in f:
                        mail = line.strip()
                        status, name = checker(mail, proxies)
                        if status: print(f"{G}[✔] সচল: {mail} | নাম: {name}{W}")
                        else: print(f"{R}[X] নেই: {mail}{W}")
                        time.sleep(1)
            except: print(f"{R}ফাইল পাওয়া যায়নি!{W}")

        elif choice == '3':
            scrape_proxies()
            time.sleep(2)

        elif choice == '0':
            break

if __name__ == "__main__":
    main()
