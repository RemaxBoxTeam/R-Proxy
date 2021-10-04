import colorama
import requests
import time
import sys , os
rd = colorama.Fore.RED
bl = colorama.Fore.BLUE
gn = colorama.Fore.LIGHTGREEN_EX
yl = colorama.Fore.MAGENTA
cl = colorama.Fore.WHITE
mag = colorama.Fore.LIGHTRED_EX
fs = colorama.Fore.YELLOW
op = sys.platform
if "win" in op:
    os.system("pip install colorama requests")
    os.system("cls")
else:
    os.system("pip3 install colorama requests")
    os.system("clear")
def banner():
    print (rd + """
    
  ___                    ___            _____               
 | _ \___ _ __  __ ___ _| _ ) _____ __ |_   _|__ __ _ _ __  
 |   / -_) '  \/ _` \ \ / _ \/ _ \ \ /   | |/ -_) _` | '  \ 
 |_|_\___|_|_|_\__,_/_\_\___/\___/_\_\   |_|\___\__,_|_|_|_|
                                                            
    """)
    print (yl + "Created By Maximum Radikali :)")
    print (gn + "Channel : https://t.me/RemaxBoxTeam" )
    print (bl + "Proxy Grabber Socks5 , Socks4 , https -- v1.0")

banner() 
site = "http://pubproxy.com/api/proxy?limit=1&format=txt&type=socks4"

def socks4():
    f = requests.get("http://pubproxy.com/api/proxy?limit=1&format=txt&type=socks4").text
    return f

def socks5():
    f = requests.get("http://pubproxy.com/api/proxy?limit=1&format=txt&type=socks5").text
    return f
def http():
    f =  requests.get("http://pubproxy.com/api/proxy?limit=1&format=txt&type=http").text
    return f 
test  = int(input(fs + "\n1-socks4\n2-socks5\n3-http" + gn + "\nPlease Choose an option that you want -> " + cl))

if test == 1:
    print (yl + "You chose First option ..")
    print (rd + "Please wait ...")
    time.sleep(2)
    print(gn + "\n\n The operation has been successfully \n \n" +  bl + "Proxy : "+str(socks4()) + cl)
    
elif test == 2:
    print (yl + "You chose First option ..")
    print (rd + "Please wait ...")
    time.sleep(2)
    print(gn + "\n\n The operation has been successfully \n \n" +  bl + "Proxy : "+str(socks5()) + cl)
    
elif test == 3:
    print (yl + "You chose First option ..")
    print (rd + "Please wait ...")
    time.sleep(2)
    print(gn + "\n\nThe operation has been successfully \n \n" +  bl + "Proxy : "+str(http()) + cl)
    
