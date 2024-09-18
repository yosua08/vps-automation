#! /usr/bin/python3

import os

print("Starting job to run nessus")

file_name = 'run_nessus.py'

# Add permision to execute file
print("[1] Success add permission ")
exec_permision = f'chmod +x {file_name}'
os.system(exec_permision)

# Setting firewall to allow port 8834
print("[2] Success allow port 8834")
allow_fw = f'ufw allow 8834'
os.system(allow_fw)

# Check status firewall
print("[3] Success check status firewall")
fw_status = f'ufw status'
os.system(allow_fw)

# Run nessus
print("[4] Success run nessusd on port 8834")
run_nessus = f'systemctl start nessusd'
os.system(run_nessus)

# Check nessus status
print("[5] Success check nessus status")
nessus_status = f'systemctl status nessusd'
os.system(nessus_status)