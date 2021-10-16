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
def http_1():
    site = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
    fsa = requests.get(site)
    with open("proxy.txt","wb") as test:
        test.write(fsa.content)
def socks4_1():
    site = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all"
    fsa = requests.get(site)
    with open("proxy.txt","wb") as test:
        test.write(fsa.content)
def socks5_1():
    site = "https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all"
    fsa = requests.get(site)
    with open("proxy.txt","wb") as test:
        test.write(fsa.content)
test  = int(input(fs + "\n1-socks4\n2-socks5\n3-http" + gn + "\nPlease Choose an option that you want -> " + cl))

if test == 1:
    print (yl + "You chose First option ..")
    print (rd + "Please wait ...")
    opr = input(gn  + "1) Single Proxy\n2) Proxy list\nSelect an option ->")
    if opr == "1":

        print (yl + "You chose First option ..")
        print (rd + "Please wait ...")
        time.sleep(2)
        print(gn + "\n\n The operation has been successfully \n \n" +  bl + "Proxy : "+str(socks4()) + cl)
    elif opr == "2":
        print (yl + "You chose second option ..")
        print (rd + "Please wait ...")
        socks4_1()
        print (rd + "done , Created Proxy.txt , check the file " + cl)
    else:
        print ("invalid option :)" + cl)

elif test == 2:
    print (yl + "You chose First option ..")
    print (rd + "Please wait ...")
    opr = input(gn  + "1) Single Proxy\n2) Proxy list\nSelect an option ->")
    if opr == "1":

        print (yl + "You chose First option ..")
        print (rd + "Please wait ...")
        time.sleep(2)
        print(gn + "\n\n The operation has been successfully \n \n" +  bl + "Proxy : "+str(socks5()) + cl)
    elif opr == "2":
        print (yl + "You chose second option ..")
        print (rd + "Please wait ...")
        socks5_1()
        print (rd + "done , Created Proxy.txt , check the file " + cl)
    else:
        print ("invalid option :)" + cl)

elif test == 3:
    print (yl + "You chose First option ..")
    print (rd + "Please wait ...")
    opr = input(gn  + "1) Single Proxy\n2) Proxy list\nSelect an option ->")
    if opr == "1":

        print (yl + "You chose First option ..")
        print (rd + "Please wait ...")
        time.sleep(2)
        print(gn + "\n\n The operation has been successfully \n \n" +  bl + "Proxy : "+str(http()) + cl)
    elif opr == "2":
        print (yl + "You chose second option ..")
        print (rd + "Please wait ...")
        http_1()
        print (rd + "done , Created Proxy.txt , check the file " + cl)
    else:
        print ("invalid option :)" + cl)
