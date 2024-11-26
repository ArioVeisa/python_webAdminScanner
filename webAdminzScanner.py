import requests

# Input URL target
base_url = input("Masukkan URL Target (contoh: https://example.com): ").strip()

# File untuk wordlist path
wordlist_file = "./admin-directory.txt"  # File yang berisi daftar path

# Baca wordlist dari file
try:
    with open(wordlist_file, "r", encoding="utf-8") as file:
        paths = [line.strip() for line in file if line.strip()]
        if not paths:
            print(f"[!] File '{wordlist_file}' kosong.")
            exit()
except FileNotFoundError:
    print(f"[!] File '{wordlist_file}' tidak ditemukan.")
    exit()

print(f"\nScanning admin paths for target: {base_url}\n")

# Scan paths dari wordlist
for path in paths:
    url = f"{base_url.rstrip('/')}/{path}"  # Hilangkan trailing slash di base URL
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"[+] Found: {url} (Status: {response.status_code})")
        elif response.status_code == 403:
            print(f"[!] Forbidden: {url} (Status: {response.status_code})")
        else:
            print(f"[-] Not Found: {url} (Status: {response.status_code})")
    except requests.exceptions.RequestException as e:
        print(f"[!] Error accessing {url}: {e}")

print("\nScan complete!")
