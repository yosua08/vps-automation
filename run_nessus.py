#! /usr/bin/python3

import os

print("Starting job to run nessus")

# Setting firewall to allow port 8834
print("[1]Success allow port 8834")
allow_fw = f'ufw allow 8834'
os.system(allow_fw)

# Check status firewall
print("[2] Success check status firewall")
fw_status = f'ufw status'
os.system(allow_fw)

# Run nessus
print("[3] Success run nessusd on port 8834")
run_nessus = f'systemctl start nessusd'
os.system(run_nessus)

# Check nessus status
print("[4] Success check nessus status")
nessus_status = f'systemctl status nessusd'
os.system(nessus_status)