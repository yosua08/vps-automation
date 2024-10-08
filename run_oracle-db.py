#! /usr/bin/python3

import os
import argparse

print("Starting job to run oracle db")

def start():
    # Allow port 1521
    print("[1] Success allow port 1521")
    allow_fw = f'sudo ufw allow 1521'
    os.system(allow_fw)

    # Start oracle db
    print("[2] Success run oracle db on port 1521")
    start_command = f'sudo docker run -d --name oracle-xe \
                    -p 1521:1521 -p 5500:5500 \
                    -e ORACLE_PWD=G@ring123 \
                    container-registry.oracle.com/database/express:latest'
    os.system(start_command)

def stop():
    # Stop oracle db
    print("[1] Success kill oracle db process")
    stop_command = f'sudo docker kill oracle-xe'
    os.system(stop_command)

    # Close port 1521
    print("[2] Success close port 1521")
    deny_fw = f'sudo ufw deny 1521'
    os.system(deny_fw)

def main():
    parser = argparse.ArgumentParser(description="Control the process with start and stop options.")

    parser.add_argument(
        'command',
        choices=['start', 'stop', 'check-sessions'],
        help="Choose what action to perform: start, stop and check-session."
    )

    args = parser.parse_args()

    if args.command == 'start':
        start()
    elif args.command == 'stop':
        stop()

if __name__ == '__main__':
    main()