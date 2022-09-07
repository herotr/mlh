import os
import requests, json
from concurrent.futures import ThreadPoolExecutor
import time
import platform
try:
        import requests
        from colorama import Fore,Style
except:
        os.system('pip install requests')
        os.system('pip install colorama')



if platform=='win32':
   system('color')

if os.name == 'nt':
   os.system('cls')
else:
   os.system('clear')


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

os.system('clear || cls')
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
    time.sleep(0.0065)

authorInformation = f"""
-----------------------------------------------------------------------------------
                Channel--> t.me/srf_cc                                             Group   --> t me/checker_ccs
                Owner  --> t.me/srfxdz                             
----------------------------------------------------------------------------------- """


for col in authorInformation:
    print(ColorsClass.CBLUE2 + col, end="")
    sys.stdout.flush()
    time.sleep(0.0060)


lineBreck = "\n"
for col in lineBreck:
    print(ColorsClass.ENDC + col, end="")
    sys.stdout.flush()
    time.sleep(0.4)


banners = f"""
"""
print(banners)
choiceusers = input(f"{Fore.GREEN}[{Fore.GREEN}!{Fore.GREEN}]{Fore.RED} ENTER YOUR PASSWORD {Fore.WHITE}  = {Fore.WHITE}   {Style.RESET_ALL}")
if choiceusers == "ILOVESHARIF":

  banners = f"""
Login Successful
\033[35m
âââââââââââââââââââââââââââââââââââââââââââ
âââââââââââââââââââââââââââââââââââââââââââ
âââââââââââââââââââââââââââââââââââââââââââ
âââââââââââââââââââââââââââââââââââââââââââ
âââââââââââââââââââââââââââââââââââââââââââ
âââââââââââââââââââââââââââââââââââââââââââ

  Tool By  \033 @Srfxdz  \n
\033[31m This Tool Is Totally Free If You Bought This You Got Scammed
           \033[33m     Channel--> t.me/srf_cc                     
                Group   --> t me/checker_ccs
                Owner  --> t.me/srfxdz

{Fore.GREEN}[{Fore.WHITE}1{Fore.GREEN}] LARAVEL IP GRABBING BY LEAKIX
{Fore.GREEN}[{Fore.WHITE}2{Fore.GREEN}] LARAVEL IP GRABBING BY NETLAS
{Fore.GREEN}[{Fore.WHITE}3{Fore.GREEN}] IP RANGER (MASS IP VAILIDATOR)


"""
os.system('clear || cls')
os.system('clear')
print(banners)
choiceusers = input(f"{Fore.GREEN}-SELECT AN OPTION {Fore.RED}>  {Style.RESET_ALL}")

if choiceusers == "1":
   def grab(keywords):
       for pages in range(5000):
           print(f"\n{Fore.GREEN}Pages : {pages}{Style.RESET_ALL}")           vars = 'https://leakix.net/search?page='+str(pages)+'&q='+keywords+'&scope=leak'
           headers = {'api-key': 's', 'Accept': 'application/json'}           response = requests.get(vars, headers=headers).text
           tojson = json.loads(response)
           for results in tojson:
               lovs = results['ip']
               print(lovs)
               saves = open('ip_list.txt','a')
               saves.write(lovs+"\n")
               saves.close()

   keywords = input('\r\rEnter_Your_Dork_Here â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢>>').split()
   threads = input('\r\rEnter_Speed_Here â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢>> ')
   if keywords:
     try:
        with ThreadPoolExecutor(int(threads)) as l:
            l.map(grab,keywords)
     except Exception as w:
        print(w)



elif choiceusers == "2":
   def grab(keywords):
       for pages in range(1,500):
           print(f"\n{Fore.GREEN}Pages : {pages}{Style.RESET_ALL}")           vars = f"https://natlas.io/search?query={keywords}&page={str(pages)}&format=hostlist"
           headers = {
             'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language' : 'en-GB,en-US;q=0.9,en;q=0.8'
            }
           response = requests.get(vars, headers=headers)
           print(response.text)
           with open("ip_list2.txt","a") as file:
             file.write(f"{response.text}\n")


   keywords = input('\r\rEnter_Your_Dork_Here â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢>>').split()
   threads = input('\r\rEnter_Speed_Here â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢â¢>>')
   if keywords:
     try:
        with ThreadPoolExecutor(int(threads)) as l:
            l.map(grab,keywords)
     except Exception as w:
        print(w)
elif choiceusers == "3":
     def ranges(xinputip):
         try:
            xstrip = "."
            xspl = xinputip.split(".")
            for xresult in range(0, 999 + 1):
                xres = xspl[0] + xstrip + xspl[1] + xstrip + xspl[2] + xstrip + str(xresult)
                print(f"[{Fore.RED}+{Style.RESET_ALL}]{Fore.GREEN} {xres}{Style.RESET_ALL}")
                open('unfiltered.txt','a').write(xres+"\n")
            for xresult in range(0, 999 + 1):
                xres2 = xspl[0] + xstrip + xspl[1] + xstrip + str(xresult) + xstrip + xspl[2]
                print(f"[{Fore.RED}+{Style.RESET_ALL}]{Fore.GREEN} {xres2}{Style.RESET_ALL}")
                open('unfiltered.txt','a').write(xres2+"\n")
         except:
            pass

     xinputip = open(input(f"{Fore.GREEN}[{Fore.RED}!{Fore.GREEN}] {Fore.WHITE}IP List{Fore.GREEN} --{Fore.RED}>  {Style.RESET_ALL}"), 'r').read().split("\n")
     thread = input(f"{Fore.GREEN}[{Fore.RED}!{Fore.GREEN}{Fore.WHITE} Threads {Fore.GREEN}--{Fore.RED}>  {Style.RESET_ALL}")
     if xinputip:
       try:
          with ThreadPoolExecutor(int(thread)) as pq:
              pq.map(ranges,xinputip)
       except:
          pass
