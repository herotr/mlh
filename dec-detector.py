import os, requests, time
from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing import Pool
import threading
import sys
from colorama import Fore, Style
try:
        import requests
        import colorama

except:
        os.system('pip install requests')
        os.system('pip install colorama')


def screen_clear():
    _ = os.system('')

# Import Modules
import sys
import os
import time



# Colors
class ColorsClass:
    CRED2 = "\33[91m"
    CBLUE2 = "\33[94m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"

os.system('clear')
os.system('clear')
# banner
banner = f"""
âââââââââââââââââââââââââââââââââââââââââââ
âââââââââââââââââââââââââââââââââââââââââââ
âââââââââââââââââââââââââââââââââââââââââââ
âââââââââââââââââââââââââââââââââââââââââââ
âââââââââââââââââââââââââââââââââââââââââââ
âââââââââââââââââââââââââââââââââââââââââââ

  Tool By  \033 @Srfxdz  \n
This Tool Is Totally Free If You Bought This You Got Scammed  """


for col in banner:
    print(ColorsClass.CRED2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0025)

authorInformation = f"""
-----------------------------------------------------------------------------------
                Channel--> t.me/srf_cc                                             Group   --> t me/checker_ccs
                Owner  --> t.me/srfxdz                             
----------------------------------------------------------------------------------- """


for col in authorInformation:
    print(ColorsClass.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0040)


lineBreck = "\n"
for col in lineBreck:
    print(ColorsClass.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)

os.system('clear')
bl = Fore.BLUE
wh = Fore.WHITE
gr = Fore.GREEN
red = Fore.RED
res = Style.RESET_ALL
yl = Fore.YELLOW

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0'}

def laravelcheck (star):
    if "://" in star:
      star = star
    else:
      star = "http://" + star
    star = star.replace('\n', '').replace('\r', '')
    url = star + "/.env"
    check = requests.get(url, headers=headers, timeout=1)
    resp = check.text
    try:
        if "DB_HOST" in resp:
            print(f"Laravel {gr}OK{res} => {star}\n")
            mrigel = open("Laravel.txt", "a")
            mrigel.write(f'{star}\n')
        else:
            print(f"{red}Not{res} Laravel => {star}\n")
    except:
        pass
def wpcheck (star):
    if "://" in star:
      star = star
    else:
      star = "http://" + star
    star = star.replace('\n', '').replace('\r', '')
    url = star + "/xmlrpc.php"
    check = requests.get(url, headers=headers, timeout=3)
    rexp = check.text
    try:
        if "XML-RPC" in rexp:
            print(f"Wordpress {gr}OK{res} => {star}\n")
            mrigel = open("Wordpress.txt", "a")
            mrigel.write(f'{star}\n')
        else:
            print(f"{red}Not{res} Wordpress => {star}\n")
    except:
        pass


def filter(star):
    try:
       laravelcheck(star)
       wpcheck(star)
    except:
       pass


def main():
    print(f'''   {gr}

âââââââââââââââââââââââââââââââââââââââââââ
âââââââââââââââââââââââââââââââââââââââââââ
âââââââââââââââââââââââââââââââââââââââââââ
âââââââââââââââââââââââââââââââââââââââââââ
âââââââââââââââââââââââââââââââââââââââââââ
âââââââââââââââââââââââââââââââââââââââââââ

  Tool By  \033 @Srfxdz  \n for Detecting Vlurnerable links :)
{yl}   This Tool only Work with .env not with debug
   To get the Debug detection tool contact @srfxdz (Telegram)


{red}This Tool Is Totally Free If You Bought This You Got Scammed
   ''')
    list = input(f"{gr}FILE PATH OF unfiltered.txt/{red}srfxdz> {gr}${res} ")
    star = open(list, 'r').readlines()
    try:
       ThreadPool = Pool(50)
       ThreadPool.map(filter, star)
       ThreadPool.close()
       ThreadPool.join()
    except:
       pass

if __name__ == '__main__':
    screen_clear()
    main()