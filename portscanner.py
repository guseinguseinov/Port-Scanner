#!/usr/bin/env python

import socket
import subprocess
import sys
from datetime import datetime

# Clear the screen
subprocess.call('clear', shell=True)

# Ask for input
remote_server = input("[+] Enter a remote host to scan:")
remote_server_ip = socket.gethostbyname(remote_server)

# Print a nice banner with information on which host we are about to scan
print('-'*60)
print(f"[+] Please wait, scanning remote host {remote_server_ip}")
print('-'*60)

# Checks what time scan start
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024
# there can also be some errors
try:
    for port in range(1, 1024):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remote_server_ip, port))

        if result == 0:
            print(f"{port}: open.")
        sock.close()

except KeyboardInterrupt:
    print("[+] You printed CTRL+C")
    sys.exit()

except socket.gaierror:
    print("[-] Host name could not be resolved, exiting")
    sys.exit()

except socket.error:
    print("[-] Could not connect to server.")
    sys.exit()

# Checking the time again
t2 = datetime.now()

total_time = t2-t1
print(f"[+] Scanning completed in {total_time}")
