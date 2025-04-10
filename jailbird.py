import os
import subprocess
import webbrowser
from colorama import Fore, Back, Style, init

# Initialize Colorama
init(autoreset=True)

# Color definitions
RED = Fore.RED
YELLOW = Fore.YELLOW
BLUE = Fore.BLUE
RESET = Style.RESET_ALL

# Define menu and ASCII
ascii_art = f"""
{YELLOW}     ____.      .__.__ __________.__           .___
{YELLOW}    |    |____  |__|  |\\______   \\__|______  __| _/
{YELLOW}    |    \\__  \\ |  |  | |    |  _/  \\_  __ \\/ __ |
{YELLOW}/\\__|    |/ __ \\|  |  |_|    |   \\  ||  | \\/ /_/ |
{YELLOW}\\________(____  /__|____/______  /__||__|  \\____ |
              \\/               \\/               \\/
               {BLUE}Made by thebitcoinbandit
               {BLUE}JAILBIRD VERSION 0.0.0
-----------------------------------------------------{RESET}
"""

menu = f"""
{RED}[01]{RESET} IP Information Gathering
{RED}[02]{RESET} Social Media Information Gathering (COMING SOON)
{RED}[03]{RESET} Phone Number Information Gathering
{RED}[04]{RESET} Email Information Gathering (COMING SOON)
{RED}[05]{RESET} Paste Format (COMING SOON)
{RED}[06]{RESET} Update JailBird
{RED}[07]{RESET} Phishing Tool
{RED}[X]{RESET} EXIT
"""

# Function for IP Information Gathering
def ip_information():
    print("Opening BrowserLeaks for IP Information Gathering...")
    webbrowser.open('https://browserleaks.com/')

# Function for Social Media Information Gathering using Sherlock
def social_media_information():
    print(f"{RED}Enter the username: ", end="")
    user_requested = input()

    print("Downloading and Starting Sherlock for Social Media Information Gathering...")

    # Clone Sherlock if it's not already cloned
    if not os.path.exists('sherlock'):
        subprocess.call(['git', 'clone', 'https://github.com/sherlock-project/sherlock.git'])
    
    os.chdir('sherlock')

    # Run Sherlock with the requested username
    subprocess.call(['python3', 'sherlock.py', user_requested])

    # Return to the original directory after the operation
    os.chdir('..')

# Function for Phone Number Lookup using PhoneInfoga
def phone_number_information():
    phone_number = input("Enter phone number: ")
    print("Downloading and Starting PhoneInfoga for Phone Number Information Gathering...")
    if not os.path.exists('PhoneInfoga'):
        subprocess.call(['git', 'clone', 'https://github.com/sundowndev/phoneinfoga.git'])
    os.chdir('PhoneInfoga')
    subprocess.call(['python3', 'phoneinfoga.py', 'scan', '--number', phone_number])

# Function for Email Information Gathering using theHarvester
def email_information():
    print("Starting theHarvester for Email Information Gathering...")
    subprocess.call(['theHarvester'])

# Function for generating Doxbin paste format (COMING SOON)
def paste_format():
    print("Paste Format feature is coming soon!")

# Function for updating JailBird
def update_jailbird():
    print("Updating JailBird to the latest version...")
    # Change directory to the repository folder where JailBird is cloned
    if os.path.exists(".git"):
        subprocess.call(['git', 'pull'])  # Pull the latest changes from the repository
    else:
        print("The tool is not a git repository. Cloning JailBird from GitHub...")
        subprocess.call(['git', 'clone', 'https://github.com/jailbird-project/JailBird.git'])

# Function for Phishing Tool (Zphisher)
def phishing_tool():
    print("Starting Phishing Tool...")
    subprocess.call(['git', 'clone', 'https://github.com/htr-tech/zphisher.git'])
    os.chdir('zphisher')
    subprocess.call(['bash', 'zphisher.sh'])

# Function for Exit
def exit_tool():
    print("Bye, thanks for using JailBird :3")
    exit()

# Main menu loop
def main():
    while True:
        print(ascii_art)
        print(menu)
        choice = input(f"Enter your choice: {RED}")

        if choice == '01':
            ip_information()
        elif choice == '02':
            social_media_information()
        elif choice == '03':
            phone_number_information()
        elif choice == '04':
            email_information()
        elif choice == '05':
            paste_format()
        elif choice == '06':
            update_jailbird()
        elif choice == '07':
            phishing_tool()
        elif choice.lower() == 'x':  # Handles exit
            exit_tool()
        else:
            print(f"{RED}Invalid option. Please try again.")

if __name__ == '__main__':
    main()
