import pyfiglet
import time 
from loguru import logger
from termcolor import colored
import sys
import random

def ramdan_celebrate_log():
    logger.warning("🎉 Ramadan is starting ...! 🎉")
    for i in range(28):
        logger.info(f"🎉 Celebrating Ramadan {i+1} 🎉")
        time.sleep(0.15)
    logger.info(f"🎉 Celebrating Ramadan ... 🎉")
        
def wishes_write(string):
    for char in string:
        sys.stdout.write(colored(char, 'yellow'))
        sys.stdout.flush()
        time.sleep(0.01)

ramdan_celebrate_log()
logger.info(colored("🕌 Alhamdulillah! Eid is coming ..... 🌙", "green", attrs=["bold"]))

fn_style = pyfiglet.figlet_format("Eid\nMubarak!\nTo All")
lines = fn_style.split('\n')

max_line_length = max(len(line) for line in lines)
padding = (80 - max_line_length) // 2

for line in lines:
    print(' ' * padding + line)
    time.sleep(0.3)

print("\n")

wishes_write('''
            Wishing you a blessed and joyful Eid!
            May this Eid bring peace and prosperity to all!
            Accept your prayers, fast and good deeds.
            Eid Mubarak! Stay blessed and happy!,
            🌙 Let's EID Celebrate Together! 🌙
''')
print("\n\n")

print(colored("Eid Mubarak! To All", "green", attrs=["bold"]))
