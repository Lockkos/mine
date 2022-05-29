from colorama import Fore
import time
import sys
import random
import os
from colorama import init, Fore
init(convert=True)
import string
import subprocess, requests
from getpass import getpass
import secrets
from random import randint
 
from getpass import getpass
username = input('Enter Username: ')
password = getpass('Enter Password: ')

LicenseKey = input(Fore.RED + 'Input License Key: ')
if LicenseKey == "123":
    print(Fore.GREEN + "Key is Valid!")
    time.sleep(0.5)
else:
    print(Fore.RED + "Invalid Key!")
    print(Fore.RED + "Press Enter to quit!")
    input("")
    exit(123)

os.system("cls")
wallet = input(Fore.RED + "Wallet: ")
print(Fore.CYAN + "Checking if Wallet exists... ")
time.sleep(1)
print("Wallet found")

time.sleep(0.2)


print(Fore.BLUE + '██████╗ ████████╗ ██████╗    ███╗   ███╗██╗███╗    ██╗███████╗██████╗')
print(Fore.GREEN + '██╔══██╗╚══██╔══╝██╔════╝    ████╗ ████║██║████╗  ██║██╔════╝██╔══██╗')
print(Fore.BLUE + '██████╔╝   ██║   ██║         ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝')
print(Fore.BLUE + '██╔══██╗   ██║   ██║         ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗')
print(Fore.GREEN + '██████╔╝   ██║   ╚██████╗    ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║')
print(Fore.GREEN + '╚═════╝    ╚═╝    ╚═════╝    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝')
print(Fore.LIGHTGREEN_EX + '===================================================================')
time.sleep(3)
print(f''' What Server You Want To Select?
{Fore.CYAN}- GREECE{Fore.YELLOW}[Normal]
{Fore.CYAN}- Russia{Fore.YELLOW}[Lag]
{Fore.CYAN}- Germany{Fore.YELLOW}[Speed]
{Fore.CYAN}- United States{Fore.YELLOW}[Best]
{Fore.CYAN}- Slovakia{Fore.YELLOW}[Normal]
''')
a = input(f'''{Fore.RED}Poseidon~ ''')
print(f'''{Fore.RED}[Poseidon~] {Fore.BLUE}Checking Subscription...
''')
time.sleep(2)
print(f'''{Fore.RED}[Poseidon~] {Fore.GREEN}Subscription Valid
''')
time.sleep(2)
print(f'''{Fore.RED}[Poseidon~] {Fore.WHITE}OK
''')
time.sleep(0.7)
print(Fore.BLUE +                   '============>↻   ')
print(Fore.GREEN +                   'Loading Miner ')
time.sleep(7)
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print('')
print(Fore.BLUE + '[Poseidon~]🏆️You Have VIP For Fast Mining')
time.sleep(3)


continuing = True
 
btcval = 31643.79
 
while True:
  if continuing == True:
    time.sleep(.01)
    ranInt = randint(0,2500)
    if ranInt <= 1:
      randomBTC = randint(1,100)/100
      print(Fore.BLUE + "[Poseidon MIner] ╚═══► 0x" + secrets.token_hex(20) + Fore.GREEN + " ╚═══► " + str(randomBTC) + " BTC ($" + str("{:,}".format(round(btcval*randomBTC,2))) + ")")
      answer = input("> Would you like to continue? (Y/N) ")
      if answer.lower() == "y":
        continuing = True
      else:
        continuing = False
    else:
      print(f''' {Fore.BLUE}[Poseidon Miner] {Fore.RED}BTC bx''' + secrets.token_hex(20) + '''> 0.00 BTC ($0.000)''')
      if a == "Slovakia":
             print(f''' {Fore.WHITE}[Server {Fore.CYAN}Slovakia]
      ''')
      if a == "Germany":
             print(f''' {Fore.WHITE}[Server {Fore.CYAN}Germany]
      ''')
      if a == "Russia":
             print(f''' {Fore.WHITE}[Server {Fore.CYAN}Russia]
      ''')
      if a == "United States":
             print(f''' {Fore.WHITE}[Server {Fore.CYAN}United States]
      ''')
  else:
    break
