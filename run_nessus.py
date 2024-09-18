#! /usr/bin/python3

import os
import argparse

print("Starting job to run nessus")

def start():
    print("Starting the process...")

    # Setting firewall to allow port 8834
    print("[1] Success allow port 8834")
    allow_fw = f'sudo ufw allow 8834'
    os.system(allow_fw)

    # Check status firewall
    print("[2] Success check firewall status")
    fw_status = f'sudo ufw status'
    os.system(fw_status)

    # Run nessus
    print("[3] Success run nessusd on port 8834")
    run_nessus = f'sudo systemctl start nessusd'
    os.system(run_nessus)

    # Check nessus status
    print("[4] Success check nessus status")
    nessus_status = f'sudo systemctl status nessusd'
    os.system(nessus_status)

def stop():
    print("Stopping the process...")

    # Setting firewall to allow port 8834
    print("[1] Success deny port 8834")
    allow_fw = f'sudo ufw deny 8834'
    os.system(allow_fw)

    # Check status firewall
    print("[2] Success check firewall status")
    fw_status = f'sudo ufw status'
    os.system(fw_status)

    # Run nessus
    print("[3] Success run nessusd on port 8834")
    run_nessus = f'sudo systemctl stop nessusd'
    os.system(run_nessus)

    # Check nessus status
    print("[4] Success check nessus status")
    nessus_status = f'sudo systemctl status nessusd'
    os.system(nessus_status)

def main():
    # Create the parser and add arguments
    parser = argparse.ArgumentParser(description="Control the process with start and stop options.")
    
    # Adding a positional argument with specific choices
    parser.add_argument(
        'command',  # Positional argument
        choices=['start', 'stop'],  # Valid choices
        help="Choose what action to perform: start, stop."
    )
    
    # Parse the arguments
    args = parser.parse_args()

    # Call the corresponding function based on the choice
    if args.command == 'start':
        start()
    elif args.command == 'stop':
        stop()

if __name__ == "__main__":
    main()