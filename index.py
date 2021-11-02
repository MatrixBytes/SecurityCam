import sys
import os
import datetime
import time
import platform
import colorama
from colorama import Fore
import random

def start():
    print(f"{Fore.CYAN}Mint {Fore.GREEN}0.1 {Fore.MAGENTA}[{Fore.GREEN}" + str(datetime.datetime.now().strftime("%d-%m-%y ~ %H:%M:%S")) + (f"{Fore.MAGENTA}]\n"))
    print(f'{Fore.RED}> {Fore.YELLOW}Started on {Fore.MAGENTA}' + platform.system())
    print(f'{Fore.RED}> {Fore.YELLOW}Loading {Fore.MAGENTA}' + str(sys.argv).replace('[', '').replace(']', '') + (f"{Fore.GREEN}\n"))

def stop():
    print(f'\n{Fore.RED}> {Fore.CYAN}Mint end {Fore.MAGENTA}[{Fore.YELLOW}{datetime.datetime.now().strftime("%d-%m-%y ~ %H:%M:%S")}{Fore.MAGENTA}]\n')
    sys.exit()
 
def clear():
    if platform.system() == "Linux":
        os.system('clear')

    if platform.system() == "Windows":
        os.system('cls')

def log(action):
    now = datetime.datetime.now()
    happend = (f'{Fore.RED}[{Fore.CYAN}{now.strftime("%d-%m-%y %H:%M:%S")}{Fore.RED}] {Fore.MAGENTA}{action}')
    return happend

def sleep(val):
    for i in range(1, val + 1):
        print(f'{Fore.RED}Sleeping {Fore.CYAN}> {Fore.GREEN}{i}')
        time.sleep(1)

def userinp(text):
    return input(f'{text}{Fore.RED}> {Fore.GREEN}')

def randomnum(from_num, to_num):
    return random.randint(int(from_num), int(to_num))

def randomstr(list):
    return random.choice(list)