import socket
import concurrent.futures


print('''
 _______  _______  _______                                      
|       ||       ||       |                                     
|    ___||_     _||    _  |                                     
|   |___   |   |  |   |_| |                                     
|    ___|  |   |  |    ___|                                     
|   |      |   |  |   |                                         
|___|      |___|  |___|                                         
 _______  _______  _______  __    _  __    _  _______  ______   
|       ||       ||   _   ||  |  | ||  |  | ||       ||    _ |  
|  _____||       ||  |_|  ||   |_| ||   |_| ||    ___||   | ||  
| |_____ |       ||       ||       ||       ||   |___ |   |_||_ 
|_____  ||      _||       ||  _    ||  _    ||    ___||    __  |
 _____| ||     |_ |   _   || | |   || | |   ||   |___ |   |  | |
|_______||_______||__| |__||_|  |__||_|  |__||_______||___|  |_|
                                                                                                                                    
   by: nouredine kn
   telegram: nouredine_kn
   github: https://github.com/nouredinekn                                                                   
''')
# Configuration
FTP_PORT = 21
TIMEOUT = 2  # Timeout for each connection attempt
THREADS = 10000  # Number of concurrent threads
INPUT_FILE = input('[+] ENTRE IP||DOMAIN LIST.txt:' )
OUTPUT_FILE = "open_ftp_ips.txt"

# Read IPs from file
def read_ips(file_path):
    try:
        with open(file_path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"[!] Error: File '{file_path}' not found.")
        return []

# Check if FTP (port 21) is open on an IP
def check_ftp(ip):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(TIMEOUT)
            if sock.connect_ex((ip, FTP_PORT)) == 0:  # Port is open
                result = f"[+] {ip}:21 is open (Possible FTP service)"
                print(result)
                return ip
    except Exception as e:
        print(f"[!] Error scanning {ip}: {e}")
    return None

# Save results to file
def save_results(open_ips):
    if open_ips:
        with open(OUTPUT_FILE, "w") as f:
            for ip in open_ips:
                f.write(f"{ip}\n")
        print(f"\n[+] Results saved to {OUTPUT_FILE}")
    else:
        print("\n[-] No open FTP servers found.")

# Main function using multithreading
def main():
    ips = read_ips(INPUT_FILE)
    if not ips:
        return
    
    print(f"[*] Checking {len(ips)} IPs for FTP (Port {FTP_PORT}) using {THREADS} threads...\n")

    open_ips = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=THREADS) as executor:
        results = executor.map(check_ftp, ips)

    # Collect open IPs
    open_ips = [ip for ip in results if ip]

    # Save results
    save_results(open_ips)

if __name__ == "__main__":
    main()
