# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#0503作業1
#101_AI班林建名

from colorama import Back, Style, init
import time
import os

count = 0
init()

while True:   
    if count >=1 and count<= 5:
        print(Back.RED + "  " + Style.RESET_ALL)
        print(f"{count}")
    elif count == 6:
        print("  "  +Back.YELLOW + "  " + Style.RESET_ALL)
        print(f"{count}")
    elif count >= 7 and count <10:
        print("    "  +Back.GREEN + "  " + Style.RESET_ALL)
        print(f"{count}")
    elif count == 10:
        count = 0
        print("    "  +Back.GREEN + "  " + Style.RESET_ALL)
        print(f"{count}")
    time.sleep(1)
    count += 1
    os.system('cls' if os.name == 'nt' else 'clear')