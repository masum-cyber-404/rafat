import os, re, requests, json, bs4
import sys,time,random
from bs4 import BeautifulSoup as parser
ses=requests.Session()
os.system('clear')
def runtxt(z):
    for e in z + "\n":
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
print("""  
  __  __    _    ____  _   _ __  __      _    _   _ __  __ _____ ____  
 |  \/  |  / \  / ___|| | | |  \/  |    / \  | | | |  \/  | ____|  _ \ 
 | |\/| | / _ \ \___ \| | | | |\/| |   / _ \ | |_| | |\/| |  _| | | | |
 | |  | |/ ___ \ ___) | |_| | |  | |  / ___ \|  _  | |  | | |___| |_| |
 |_|  |_/_/   \_\____/ \___/|_|  |_| /_/   \_\_| |_|_|  |_|_____|____/ 
                                                                       

         
   \033[91;1m╔═════════════════════════════════╗
   \033[1;32m║\033[1;33m[\033[91;1m•\033[1;33m]\033[1;33m OWNER        : \033[1;32mMASUM AHMED   \033[1;92m║
   \033[1;32m║\033[1;33m[\033[91;1m•\033[1;33m]\033[1;33m FACEBOK      : \033[1;32mMASUM AHMED   \033[1;92m║
   \033[1;32m║\033[1;33m[\033[91;1m•\033[1;33m]\033[1;33m GITHUB       : \033[1;32mMASUM-XD      \033[1;92m║
   \033[1;32m║\033[1;33m[\033[91;1m•\033[1;33m]\033[1;33m TEAM         : \033[1;32mMCF TEAM.BD   \033[1;92m║
   \033[1;32m║\033[1;33m[\033[91;1m•\033[1;33m]\033[1;33m TOOL VIRSION : \033[1;32m0.1           \033[1;92m║
   \033[1;32m║\033[1;33m[\033[91;1m•\033[1;33m]\033[1;33m TOOL'S       : \033[1;32mFB AUTO SHARE \033[1;92m║
   \033[91;1m╚═════════════════════════════════╝
     
     
        PLEASE ENTER A COOKIE TO RUN

""")
def login():
    cookie = input("  \033[1;92m[✓]Enter Cookie : ")
    try:
        data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 4.3; SM-N750K Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
        find_token = re.search("(EAAG\w+)", data.text)
        open("token.txt", "w").write(find_token.group(1))
        open("cookie.txt", "w").write(cookie)
        menu()
    except:
        os.system("rm token.txt cookie.txt")
        exit(" Login Failed, Cookies or Link Invalid")
def menu():
    try:
        token = open("token.txt","r").read()
        cok = open("cookie.txt","r").read()
        cookie = {"cookie":cok}
        nama = ses.get(f"https://graph.facebook.com/me?fields=name&access_token={token}",cookies=cookie).json()["name"]
    except:
        login()
    runtxt(f"""\x1b[1;92m             LET'S START 
\033[1;32m  ___________________________________
""")
    idt = input("[✓]Enter Post Link :")
    limit = int(input("[✓]Enter Share Limit :"))
    try:
        n = 0
        header = {"authority":"graph.facebook.com","cache-control":"max-age=0","sec-ch-ua-mobile":"?0","user-agent":"Mozilla/5.0 (Linux; Android 4.3; SM-N750K Build/JSS15J) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"}
        for x in range(limit):
            n+=1
            post = ses.post(f"https://graph.facebook.com/v13.0/me/feed?link={idt}&published=0&access_token={token}",headers=header, cookies=cookie).text
            data = json.loads(post)
            if "id" in post:
                runtxt(f" \x1b[1;92m{n}. SHARE √ SENT [ {data['id']} ]")
            else:
                exit(" Failed To Share, Invalid Token")
    except:
        exit(" Failed To Share, Invalid Token")
        
login()