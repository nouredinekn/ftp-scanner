# 🚀 FTP Scanner & Checker by nouredinekn

![Python](https://img.shields.io/badge/Python-3.7%2B-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Security](https://img.shields.io/badge/Security-Research%20Only-red.svg)

## 📌 Description
This repository contains two powerful Python scripts for scanning FTP servers and checking login credentials.

- **🔍 ftpscan.py**: Scans a list of IPs or domains to check if FTP (port 21) is open.
- **🔑 checker-ftp.py**: Attempts to log in to FTP servers using a list of username/password pairs and retrieves accessible folders.

## ⚙️ Installation
To install and use this tool, follow these steps:

```bash
# Clone the repository
git clone https://github.com/nouredinekn/ftp-scanner.git

# Navigate to the directory
cd ftp-scanner

# Run the script
python ftpscan.py
```

## 📦 Requirements
- Python 3
- `ftplib` (built-in module)
- `socket` (built-in module)
- `concurrent.futures` (built-in module)

## ⚡ Usage
### **🖥️ ftpscan.py** (FTP Port Scanner)
This script scans a list of IPs or domains to check if FTP is open.

#### **How to Use:**
1. Create a file containing IPs or domains (one per line).
2. Run the script and enter the file name when prompted.
3. Results will be saved in `open_ftp_ips.txt`.

```bash
python ftpscan.py
```

### **🔓 checker-ftp.py** (FTP Brute-force & Folder Checker)
This script attempts to log in to FTP servers using a list of credentials and retrieves accessible folders.

#### **How to Use:**
1. Create a file (`FTP_LIST_FILE.txt`) containing FTP server IPs or domains.
2. Create a file (`userpass-ftp.txt`) with login credentials in the format `username:password`.
3. Run the script and enter the file name when prompted.
4. Valid credentials and accessible folders will be saved in `valid_ftp_credentials.txt`.

```bash
python checker-ftp.py
```

## ⚠️ Legal Disclaimer
**This tool is for educational and security research purposes only.** Unauthorized use on systems you do not own or have explicit permission to test is illegal. The author is not responsible for any misuse or damages caused by the use of this tool.

## 👤 Author
- **🛠️ Nouredine KN**
- 📬 Telegram: [nouredine_kn](https://t.me/nouredine_kn)
- 🏆 GitHub: [nouredinekn](https://github.com/nouredinekn)
