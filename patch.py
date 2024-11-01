import os
import time
import psutil
from datetime import datetime
from colorama import init, Fore, Style

# Initialize colorama for Windows support
init()

# Branding Information
VISTA_GROUP_NAME = "Vista Group"
DISCORD_LINK = "https://discord.gg/yvTj9NEcyt"
WEBSITE = "https://cdn.oldrec.net"

def display_banner():
    print(Fore.CYAN + Style.BRIGHT)
    print("=========================================")
    print(f"     {VISTA_GROUP_NAME} - ULTRAKILL PATCHER")
    print("       Halloween 2024 Edition")
    print("=========================================")
    print(Fore.YELLOW + f" Discord: {DISCORD_LINK}")
    print(f" Website: {WEBSITE}")
    print(Fore.CYAN + "=========================================" + Style.RESET_ALL)

# Function to set the system time (requires admin rights)
def set_system_time(new_time):
    os.system(f"date {new_time.strftime('%m-%d-%Y')}")
    os.system(f"time {new_time.strftime('%H:%M:%S')}")

# Save the current system time
original_time = datetime.now()

# Display the banner
display_banner()

# Set the system time to Halloween 2024
halloween_time = datetime(2024, 10, 31, 0, 0, 0)
print(Fore.GREEN + "Setting system date to Halloween 2024..." + Style.RESET_ALL)
set_system_time(halloween_time)
print(Fore.GREEN + "System date set to Halloween 2024" + Style.RESET_ALL)

# Check if ULTRAKILL.exe is running
def is_ultrakill_running():
    for process in psutil.process_iter(['name']):
        if process.info['name'] == 'ULTRAKILL.exe':
            return True
    return False

# Wait until ULTRAKILL.exe is detected
while not is_ultrakill_running():
    print(Fore.YELLOW + "Waiting for ULTRAKILL.exe to start..." + Style.RESET_ALL)
    time.sleep(5)

# ULTRAKILL.exe detected, wait 30 seconds
print(Fore.GREEN + "ULTRAKILL.exe detected, waiting 30 seconds..." + Style.RESET_ALL)
time.sleep(30)

# Restore original date and time
print(Fore.GREEN + "Restoring original system date and time..." + Style.RESET_ALL)
set_system_time(original_time)
print(Fore.GREEN + "System date and time restored to original values." + Style.RESET_ALL)

# Final message
print(Fore.CYAN + "\nThank you for using the ULTRAKILL Patcher!")
print(f"Join {VISTA_GROUP_NAME} on Discord for updates and support." + Style.RESET_ALL)
