import time
import os

os.system("clear")
print("""
=========================================================================
|                            CODED BY JROKEN                            |
|                                                                       |
|                               DOWNPLOAD                               |
|                                                                       |
|           Telegram          t.me/hakoo29                              |
|                                                                       |
|           İnstagram       instagram.com/hakoo28_                      |
|                                                                       |
|           Github           github.com/jroken                          |
|                                                                       |
|                         FOR ANDROİD/TERMUX & LİNUX                    |
=========================================================================
""")
time.sleep(1)

print("""
    [0]  İnstall Nmap
    [1]  İnstall Sqlmap
    [2]  İnstall MetaSploit
    [3]  İnstall Fatrat
    [4]  İnstall SearchSploit
    [5]  İnstall Osif 
    [6]  İnstall RedHawk
    [7]  İnstall Nikto
    [8]  İnstall Nethunter
    [9]  İnstall Hammer
    [10] İnstall Xadmin
    [11] İnstall Sms Bomber
    [12] İnstall WebSploit
    [13] İnstall İnstagram Brute Force
    [14] İnstall Lazymux
    [15] İnstall Phishing Tools
    [16] İnstall Ngrok
    [17] İnstall WindowRAt
    [18] İnstall Hydra
    [19] İnstall Cupp
    [20] İnstall AdbSploit
    [21] İnstall Fsociety
    [22] İnstall Vulnx
    [23] İnstall Social-Engineer ToolKit
    [24] İnstall Sherlock Tool
    [25] İnstall Unicorn

    [99] Exit

      """)
secim = input("    Dwnp >  ")
if (secim=="0"):
    os.system("pkg install nmap -y")
elif (secim=="1"):
    os.system("git clone https://github.com/sqlmapproject/sqlmap")

elif (secim=="2"):
    os.system("pkg install metasploit")

elif (secim=="3"):
    os.system("git clone https://github.com/screetsec/TheFatRat")

elif (secim=="4"):
    os.system("git clone https://github.com/offensive-security/exploitdb")

elif (secim=="5"):
    os.system("git clone https://github.com/CiKu370/OSIF")

elif (secim=="6"):
    os.system("git clone https://github.com/Tuhinshubhra/RED_HAWK")

elif (secim=="7"):
    os.system("git clone https://github.com/Neo-Oli/termux-ubuntu.git")

elif (secim=="8"):
    os.system("git clone https://github.com/sullo/nikto")

elif (secim=="9"):
    os.system("git clone https://github.com/cyweb/hammer")

elif (secim=="10"):
    os.system("git clone https://github.com/sshwsfc/xadmin")

elif (secim=="11"):
    os.system("git clone https://github.com/TheSpeedX/TBomb")

elif (secim=="12"):
    os.system("git clone https://github.com/websploit/websploit.git")

elif (secim=="13"):
    os.system("git clone https://github.com/Ap4the/apathe-bruteforce")

elif (secim=="14"):
    os.system("git clone https://github.com/Gameye98/Lazymux")

elif (secim=="15"):
    os.system("git clone https://github.com/Cesar-Hack-Gray/scam")

elif (secim=="16"):
    os.system("pkg install zip wget -y")
    os.system("wget https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-arm.zip")
    os.system("unzip ngrok-stable-linux-arm.zip")

elif (secim=="17"):
    os.system("git clone https://github.com/machine1337/window-rat")

elif (secim=="18"):
    os.system("apt install hydra")

elif (secim=="19"):
    os.system("git clone https://github.com/Mebus/cupp")

elif (secim=="20"):
    os.system("git clone https://github.com/mesquidar/adbsploit")

elif (secim=="21"):
    os.system("git clone https://github.com/Manisso/fsociety")

elif (secim=="22"):
    os.system("git clone https://github.com/anouarbensaad/vulnx")

elif (secim=="23"):
    os.system("git clone https://github.com/trustedsec/social-engineer-toolkit")

elif (secim=="24"):
    os.system("git clone https://github.com/sherlock-project/sherlock")

elif (secim=="25"):
    os.system("git clone https://github.com/trustedsec/unicorn")

elif (secim=="99"):
    print("THANKS")
    time.sleep(0.5)
    print("""EXIT... """)
    time.sleep(1)

else :
    print("""
    
 WRONG CHOICE GOOD DAY 
    
    """)
    time.sleep(1)
