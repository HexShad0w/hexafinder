# инструмент Hexafinder 

import subprocess
import os
class Color:
    BLUE = '\033[94m'
    GREEN = '\033[1;92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    MAGENTA = "\033[95m"
    WHITE = "\033[97m"
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

def run_subprocess(cmd, description):
    print(Color.YELLOW + f"Starting {description} ..." + Color.RESET)
    try:
        subprocess.run(cmd, shell=True)
        print(Color.CYAN + f"{description} completed." + Color.RESET)
    except KeyboardInterrupt:
        print(Color.RED + f"\n{description} interrupted by user. Skipping to the next step..." + Color.RESET)

def hex_tool(domain):
    file_to_use = "output.txt"

    with open("final.txt", "w") as final_file:
        pass

    subfinder_start = input(Color.GREEN + "Do you want to start Subfinder? y/n: " + Color.RESET)
    if subfinder_start.lower() == "y":
        subfinder_cmd = f"subfinder -d {domain} > output.txt"
        run_subprocess(subfinder_cmd, "Subfinder")
        subprocess.run("cat output.txt >> final.txt", shell=True)

    httpx_start = input(Color.GREEN + "Do you want to start Httpx? y/n: " + Color.RESET)
    if httpx_start.lower() == "y":
        httpx_cmd = "cat output.txt | httpx -ports 80,443,8080,8000,8888 -threads 200 > sort.txt"
        run_subprocess(httpx_cmd, "Httpx")
        file_to_use = "sort.txt"

        subprocess.run("cat sort.txt >> final.txt", shell=True)

    katana_start = input(Color.GREEN + "Do you want to start Katana? y/n: " + Color.RESET)
    if katana_start.lower() == "y":
        katana_cmd = f"cat {file_to_use} | katana -jc >> final.txt"
        run_subprocess(katana_cmd, "Katana")

    print(Color.CYAN + "All selected scans have been completed." + Color.RESET)

    sort_url = input(Color.BLUE + "Would you like to sort URLs from final.txt? y/n: " + Color.RESET)
    if sort_url.lower() == "y":
        sort_urls()

def sort_urls():
    while True:
        start = input(Color.GREEN + "\nWould you like to start/continue sorting? y/n: " + Color.RESET).lower()
        if start == "n":
            print(Color.RED + "Exiting sorting session..." + Color.RESET)
            break
        
        sort = input(Color.PURPLE + "Enter the URL pattern you would like to filter (e.g., '.php', 'api', 'login'): " + Color.RESET)
        file = input(Color.CYAN + "Enter the name of the output file to save results: " + Color.RESET)
        
        sort_cmd = f"grep -E '{sort}' final.txt > {file}"
        subprocess.run(sort_cmd, shell=True)
        
        print(Color.GREEN + f"Sorted results saved to {file}" + Color.RESET)

def main():
    os.system('clear')
    print(Color.BLUE + r"""
    __                    _____           __         
   / /_  ___  _  ______ _/ __(_)___  ____/ /__  _____
  / __ \/ _ \| |/_/ __ `/ /_/ / __ \/ __  / _ \/ ___/
 / / / /  __/>  </ /_/ / __/ / / / / /_/ /  __/ /    
/_/ /_/\___/_/|_|\__,_/_/ /_/_/ /_/\__,_/\___/_/     
                                                     
made by hexsh1dow                
    """ + Color.RESET)

    domain = input(Color.YELLOW + "Enter the domain to scan: " + Color.RESET)
    start = input(Color.GREEN + "Would you like to start the scan? y/n: " + Color.RESET)

    if start.lower() == "y":
        hex_tool(domain)
    else:
        print(Color.RED + "Session terminated." + Color.RESET)

if __name__ == "__main__":
    main()
