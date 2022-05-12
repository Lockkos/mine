from colorama import Fore
import time
import sys
from getpass import getpass
import secrets
from random import randint
 
from getpass import getpass
username = input('Enter Username: ')
password = getpass('Enter Password: ')

print(Fore.BLUE + '██████╗ ████████╗ ██████╗    ███╗   ███╗██╗███╗    ██╗███████╗██████╗')
print(Fore.GREEN + '██╔══██╗╚══██╔══╝██╔════╝    ████╗ ████║██║████╗  ██║██╔════╝██╔══██╗')
print(Fore.BLUE + '██████╔╝   ██║   ██║         ██╔████╔██║██║██╔██╗ ██║█████╗  ██████╔╝')
print(Fore.BLUE + '██╔══██╗   ██║   ██║         ██║╚██╔╝██║██║██║╚██╗██║██╔══╝  ██╔══██╗')
print(Fore.GREEN + '██████╔╝   ██║   ╚██████╗    ██║ ╚═╝ ██║██║██║ ╚████║███████╗██║  ██║')
print(Fore.GREEN + '╚═════╝    ╚═╝    ╚═════╝    ╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝')
time.sleep(3)
print(Fore.BLUE + "Checking Subscription...")
time.sleep(2)
print(Fore.GREEN + "Subscription Valid")
time.sleep(2)
print(Fore.RED + "OK")
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
print(Fore.BLUE + '🏆️You Have VIP For Fast Mining')
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
      print(Fore.BLUE + "[Poseidon Miner] > 0x" + secrets.token_hex(20) + Fore.GREEN + "> 0.00 BTC ($0.000)")
  else:
    break
