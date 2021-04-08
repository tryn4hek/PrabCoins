import server
import colorama
import os, sys, random

import time
from time import sleep as slp
from server.pCoinData import *
from server import KeyGenerator as makeKey

from colorama import Fore
colorama.init(autoreset=True)

LBColor = Fore.LIGHTBLUE_EX
LYColor = Fore.LIGHTYELLOW_EX
LRColor = Fore.LIGHTRED_EX
LGColor = Fore.LIGHTGREEN_EX
WColor = Fore.WHITE

coins1 = coins1
coins2 = coins2
haveacc = haveacc
keypcoins = keypcoins
usrnam = usrnam
minerrank = minerrank
yaexp = 0

mineDelay1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mineDelay2 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

realDelay1 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
realDelay2 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]

PingPC = [116, 77, 352, 406, 270, 298, 142, 150, 259, 120, 246, 49, 14, 6, 127]

os.system("clear")
StartLayer = f"""
                           PrabCoins v0.5 Beta
               ========================================
               
                                 Mine
                                 Exit
                              
Welcome Back, {usrnam}
Balance: {coins2}.{coins1}
Rank: {minerrank}
"""

logsLayer = f"""

{LRColor}=====================[ {LGColor}LOGS{LRColor} ]=====================>
{LRColor}===============================================>

"""

print(StartLayer)
while True:
    choosingOpt = input(f"{LBColor} >{WColor} ")

    if choosingOpt == "Mine" or choosingOpt == "mine":
        print(logsLayer)
        print(f"{LBColor} [•]{WColor} Choosed{LYColor} Mine{WColor}.")
        slp(1)
        print()
        print(f"{LGColor} [+]{WColor} Checking Account...")
        slp(3)
        
        if haveacc == 0:
            wantMkAcc = input(f"{LRColor} [!]{WColor} No Account Detected, Do you want to make account [y/N]? ")
        
            if wantMkAcc == "n" or wantMkAcc == "N":
                print(f"{LRColor} [!]{WColor} Failed to mining PrabCoins, No account Detected.")
                
            elif wantMkAcc == "y" or wantMkAcc == "Y":
                print(f"{LGColor} [+]{WColor} Creating Account...")
                slp(4)
                print(f"{LGColor} [+]{WColor} Generating Key...")
                slp(4)
                makeKey.GenerateKey()
                slp(1)
                print(f"{LGColor} [+]{WColor} Restarting...")
                slp(5)
                break
                os.system("python /sdcard/PrabCoins/main.py")
                
            else:
                print(f"{LRColor}[!] No Option called {wantMkAcc}")
            
        elif haveacc == 1:
            inpusrnam = input(f"{LBColor} [•] Username >{WColor} ")
        
            with open("/sdcard/PrabCoins/server/pCoinData.py", "w") as savingAcc:
                    savingAcc.write(f'coins1 = {coins1}' + '\n')
                    savingAcc.write(f'coins2 = {coins2}' + '\n')
                    savingAcc.write(f'haveacc = 2' + '\n')
                    savingAcc.write(f'keypcoins = "{keypcoins}"' + '\n')
                    savingAcc.write(f'usrnam = "{inpusrnam}"' + '\n')
                    savingAcc.write('minerrank = "Beginner"' + '\n')
                    savingAcc.write('yaexp = 0' + '\n')
                
            print(f"{LGColor} [+]{WColor} Successfully Created Account!")
            slp(1)
            break
            os.system("python main.py")
            
        elif haveacc == 2:
        
            print()
            print(f"{LGColor} [+]{WColor} Starting Mining...")
            slp(3)
            try:
                blockMined = 0
                while True:
                    currenTime = time.strftime('%H:%M:%S')
                    truePing = random.choice(PingPC)
                    trueEarn1 = random.choice(mineDelay2)
                    trueEarn2 = random.choice(mineDelay1)
                    
                    trueDelay1 = random.choice(realDelay1)
                    trueDelay2 = random.choice(realDelay2)
                    print()
                    
                    if minerrank == "Beginner":
                        if yaexp >= 1250:
                            yaexp -= 1250
                            minerrank = "Experienced"
                            
                        else:
                            pass
                        
                    elif minerrank == "Experienced":
                        if yaexp >= 2500:
                            yaexp -= 2500
                            minerrank = "Master"
                            
                        else:
                            pass
                        
                    
                    print(f"> {LBColor}[{currenTime}]{LGColor} Requesting to Block Server...")
                    
                    if truePing <= 100:
                        
                        slp(trueDelay1)
                        coins1 += trueEarn1
                        blockMined += 1
                        yaexp += 25
                        print(f">{LYColor} Mined Block {blockMined} {LGColor}|{LYColor} Earned: {trueEarn1} {LGColor}|{LYColor} Ping: {LGColor}{truePing}ms {LGColor}|{LYColor} Balance: {coins2}.{coins1}")
                        
                        with open("/sdcard/PrabCoins/server/pCoinData.py", "w") as savingCoins1:
                            savingCoins1.write(f'coins1 = {coins1}' + '\n')
                            savingCoins1.write(f'coins2 = {coins2}' + '\n')
                            savingCoins1.write(f'haveacc = {haveacc}' + '\n')
                            savingCoins1.write(f'keypcoins = "{keypcoins}"' + '\n')
                            savingCoins1.write(f'usrnam = "{usrnam}"' + '\n')
                            savingCoins1.write(f'minerrank = "{minerrank}"' + '\n')
                            savingCoins1.write(f'yaexp = {yaexp}' + '\n')
                        
                    elif truePing >= 100:
                        
                        slp(trueDelay2)
                        coins1 += trueEarn2
                        blockMined += 1
                        yaexp += 25
                        print(f">{LYColor} Mined Block {blockMined} {LGColor}|{LYColor} Earned: {trueEarn2} {LGColor}|{LYColor} Ping: {LRColor}{truePing}ms {LGColor}|{LYColor} Balance: {coins2}.{coins1}")
                        
                        with open("/sdcard/PrabCoins/server/pCoinData.py", "w") as savingCoins2:
                            savingCoins2.write(f'coins1 = {coins1}' + '\n')
                            savingCoins2.write(f'coins2 = {coins2}' + '\n')
                            savingCoins2.write(f'haveacc = {haveacc}' + '\n')
                            savingCoins2.write(f'keypcoins = "{keypcoins}"' + '\n')
                            savingCoins2.write(f'usrnam = "{usrnam}"' + '\n')
                            savingCoins2.write(f'minerrank = "{minerrank}"' + '\n')
                            savingCoins2.write(f'yaexp = {yaexp}')
                            
                    if coins1 >= 10000:
                        coins1 -= 10000
                        coins2 += 1
                    
            except KeyboardInterrupt:
                print("\nKeyboardInterrupt!")
                print("Auto Saved Data.")
                
    elif choosingOpt == "exit" or choosingOpt == "Exit":
        print("Goodbye, Miner!")
        break
    