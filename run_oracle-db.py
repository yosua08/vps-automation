#! /usr/bin/python3

import os
import argparse

print("Starting job to run oracle db")

def run():
    # Allow port 1521
    print("[1] Success allow port 1521")
    allow_fw = f'sudo ufw allow 1521'
    os.system(allow_fw)

    # Start oracle db
    print("[2] Success run oracle db on port 1521")
    run_command = f'sudo docker run -d --name oracle-xe \
                    -p 1521:1521 -p 5500:5500 \
                    -e ORACLE_PWD=G@ring123 \
                    container-registry.oracle.com/database/express:latest'
    os.system(run_command)

def start():
    # Allow port 1521
    print("[1] Success allow port 1521")
    allow_fw = f'sudo ufw allow 1521'
    os.system(allow_fw)

    # Start oracle db
    print("[2] Success start oracle db on port 1521")
    start_command = f'sudo docker start oracle-xe'
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

def remove():
    # Remove existing container 
    print("[1] Success remove existing oracle db process")
    stop_command = f'sudo docker rm oracle-xe'
    os.system(stop_command)

    # Close port 1521
    print("[2] Success close port 1521")
    deny_fw = f'sudo ufw deny 1521'
    os.system(deny_fw)

def main():
    parser = argparse.ArgumentParser(description="Control the process with start and stop options.")

    parser.add_argument(
        'command',
        choices=['start', 'stop', 'run', 'remove'],
        help="Choose what action to perform: start, stop, run and remove."
    )

    args = parser.parse_args()

    if args.command == 'start':
        start()
    elif args.command == 'stop':
        stop()
    elif args.command == 'run':
        run()
    elif args.command == 'remove':
        remove()

if __name__ == '__main__':
    main()