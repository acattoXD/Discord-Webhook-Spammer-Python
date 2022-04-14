import time, sys, time, os
from time import sleep
import requests
from colorama import Fore, init

os.system('title Webhook Tool by acattoXD')

from colorama import Fore, init
init(convert=True)
print(f"""{Fore.LIGHTBLUE_EX}

                                 /$$     /$$               /$$   /$$ /$$$$$$$                                /$$       /$$                           /$$               /$$                         /$$
                                | $$    | $$              | $$  / $$| $$__  $$                              | $$      | $$                          | $$              | $$                        | $$
  /$$$$$$   /$$$$$$$  /$$$$$$  /$$$$$$ /$$$$$$    /$$$$$$ |  $$/ $$/| $$  \ $$       /$$  /$$  /$$  /$$$$$$ | $$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ | $$   /$$       /$$$$$$    /$$$$$$   /$$$$$$ | $$
 |____  $$ /$$_____/ |____  $$|_  $$_/|_  $$_/   /$$__  $$ \  $$$$/ | $$  | $$      | $$ | $$ | $$ /$$__  $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$  /$$/      |_  $$_/   /$$__  $$ /$$__  $$| $$
  /$$$$$$$| $$        /$$$$$$$  | $$    | $$    | $$  \ $$  >$$  $$ | $$  | $$      | $$ | $$ | $$| $$$$$$$$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$/         | $$    | $$  \ $$| $$  \ $$| $$
 /$$__  $$| $$       /$$__  $$  | $$ /$$| $$ /$$| $$  | $$ /$$/\  $$| $$  | $$      | $$ | $$ | $$| $$_____/| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$_  $$         | $$ /$$| $$  | $$| $$  | $$| $$
|  $$$$$$$|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$/|  $$$$$$/| $$  \ $$| $$$$$$$/      |  $$$$$/$$$$/|  $$$$$$$| $$$$$$$/| $$  | $$|  $$$$$$/|  $$$$$$/| $$ \  $$        |  $$$$/|  $$$$$$/|  $$$$$$/| $$
 \_______/ \_______/ \_______/   \___/   \___/   \______/ |__/  |__/|_______/        \_____/\___/  \_______/|_______/ |__/  |__/ \______/  \______/ |__/  \__/         \___/   \______/  \______/ |__/
                                                                                                                                                                                                      
                                                                                                                                                                                                      
                                                                                                                                                                                                      

""")
print(f'{Fore.CYAN}Webhook Tools:{Fore.RESET}\n\n1. {Fore.GREEN}Spam Webhook {Fore.RESET}(1)\n2. {Fore.RED}Delete Webhook {Fore.RESET}(2)\n')
print(f'\n{Fore.WHITE}Mode --> {Fore.RESET}', end='')

mode = int(input(''))

if mode not in [1, 2]:
    print(f'---\n{Fore.BLUE}Webhook{Fore.RESET} -> {Fore.RED}ERROR{Fore.RESET} : Incorrect Mode, please try again with the correct mode.')
    time.sleep(1)

try:
    if mode == 2:
        print(f"{Fore.RED}Webhook URL{Fore.RESET}")
        webhook = str(input(" > "))
        _data = requests.get(webhook)
        print(f'{Fore.GREEN}Deleted Webhook!')
        requests.delete(webhook)
        sleep(4)
except requests.exceptions.MissingSchema:
    print(f'{Fore.RED}ERROR{Fore.RESET}: Invalid Webhook!')
    sleep(2)
    exit()


try:
    if mode == 1:
        print(f"===========\n{Fore.RED}Webhook URL{Fore.RESET}")
        webhook = str(input(" > "))
        print(f"{Fore.BLUE}Message{Fore.RESET}")
        message = str(input(" > "))
        while True:
            _data = requests.post(webhook, json={'content': message}, headers={'Content-Type': 'application/json'})
            if _data.status_code == 204:
                print(f"{Fore.GREEN} Sent that message to the webhook!")
except requests.exceptions.MissingSchema:
    print(f'{Fore.RED}ERROR{Fore.RESET}: Invalid Webhook!')
    sleep(2)
    exit()