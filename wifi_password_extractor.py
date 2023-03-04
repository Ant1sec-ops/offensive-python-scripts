# This script will extract all saved wifi passwords in plain texed from the system


import subprocess
print("[*] Welcome to wifi password extactor! [*]")
print("[*] Usage: python3 wifi_password_extractor.py[*]")
def print_profiles():
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
            try:
                print('')
                print ("{:<30}|  {:<}".format(i, results[0]))
                print("-"*50)
            except IndexError:
                print ("{:<30}|  {:<}".format(i, ""))
        except subprocess.CalledProcessError:
            print ("{:<30}|  {:<}".format(i, "ENCODING ERROR"))

if __name__ == "__main__":
    print_profiles()
