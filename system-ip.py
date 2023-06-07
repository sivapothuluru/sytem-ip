from os import system as sys
from urllib.request import urlopen
from urllib.request import Request
from bs4 import BeautifulSoup as BS
import random
black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'
all_col = [red,green,orange,cyan,lightgrey,lightred,lightgreen,yellow,lightcyan]
ran = random.choice(all_col)
sys('clear')


class ip:
    def banner(self):
        print (ran ,'''
             ____               
    _____   /  _/___ 
   / ___/   / // __ \
  (__  )   / // /_/ /    
 /____/   /__/ .___/   
            /_/       
                      
			      
______________________________________________
''')

        print(ran,"\n\n","---"*3," [+] Follow me on github @sivapothuluru ","---"*3,"\n\n")
        print(ran,"\n\n","---"*3," [+] V_1.0 ","---"*3,"\n\n")

    def public_ip(self):
        headers = {'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:51.0) Gecko/20100101 Firefox/51.0"}
        url = Request('https://whatismyipaddress.com/',headers=headers)
        openurl = urlopen(url).read(99999)
        soup = BS(openurl , 'html.parser')
        for z in soup.findAll('span',{'id':'ip'}):
            print (f'{ran} [+] Public Ip is > {z.text}')

    def private_ip(self):
        sys("printf ' [+] My Privet Ip is > ';ifconfig wlan0 | grep 'netmask' | awk -F ' ' '{print $2}'")

    def localhost(self):
        print(ran," [+] default LocalHost > 127.0.0.1\n")

ip = ip()
ip.banner()
ip.public_ip()
ip.private_ip()
ip.localhost()

    
    
