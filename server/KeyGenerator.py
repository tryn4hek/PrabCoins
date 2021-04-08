# Code Generator by Perwira Prabu Tamam.

def GenerateKey():
    import random
    import colorama
    from colorama import Fore
    
    KeyB1 = ["qq", "qw", "qe", "qr", "qt", "qy", "wq", "ww", "we", "wr", "wt", "wy", "eq", "ew", "ee", "er", "et", "ey", "rq", "rw", "re", "rr", "rt", "ry", "tq", "tw", "te", "tr", "tt", "ty", "yq", "yw", "ye", "yr", "yt", "yy", "Qq", "Qw", "Qe", "Qr", "Qt", "Qy", "Wq", "Ww", "We", "Wr", "Wt", "Wy", "Eq", "Ew", "Ee", "Er", "Et", "Ey", "Rq", "Rw", "Re", "Rr", "Rt", "Ry", "Tq", "Tw", "Te"]
    
    ip1 = random.choice(KeyB1)
    ip2 = random.choice(KeyB1)
    ip3 = random.choice(KeyB1)
    ip4 = random.choice(KeyB1)
    
    mixedKey = ip1 + ip2 + ip3 + ip4
    
    print(f"{Fore.LIGHTGREEN_EX} [+]{Fore.WHITE} Generated Key.")
    with open("server/pCoinData.py", "w") as savingKey:
        savingKey.write('coins1 = 0' + '\n')
        savingKey.write('coins2 = 0' + '\n')
        savingKey.write('haveacc = 1' + '\n')
        savingKey.write(f'keypcoins = "{mixedKey}"' + '\n')
        savingKey.write(f'usrnam = "Guest"' + '\n')
        savingKey.write('minerrank = "Beginner"' + '\n')
        savingKey.write('yaexp = 0' + '\n')
        
def HashCode():
    import random
    import colorama
    from colorama import Fore
    
    Code = ["T7gN", "rVh5", "cE4V", "irN4", "3kRv", "3PCh", "Lg2F", "M38y", "tNP8", "M7Js", "a5Mn", "xPF6", "7Rbo", "X9vL", "e7Bg", "ZN3u", "un2N", "k6Vi", "jMp2", "dxM2"]
    
    code1 = random.choice(Code)
    code2 = random.choice(Code)
    code3 = random.choice(Code)
    code4 = random.choice(Code)
    code5 = random.choice(Code)
    code6 = random.choice(Code)
    
    mixedCode = code1 + code2 + code3 + code4 + code5 + code6
    print(f"> Hashing Code {mixedCode}...")
