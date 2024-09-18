#! /usr/bin/python3

import os
import argparse

print("Starting job to run xmrig")

def start():
    # Create tmux session
    print("[1] Success create tmux session")
    create_session = f'sudo tmux new-session -d -s mining'
    os.system(create_session)

    # Start xmrig
    print("[2] Success run xmrig")
    run_xmrig = f" sudo tmux send -t mining 'xmrig -o rx.unmineable.com:3333 -a rx -k -u DOGE:D7MrSwFABXmGze7oVLVTaASZNSdLDh4J1t.HiitsMe -p x' ENTER"
    os.system(run_xmrig)

def stop():
    # Stop process and exit from tmux session
    print("[1] Success kill tmux session")
    stop_process = f"sudo tmux kill-session -t mining"
    os.system(stop_process)

def main():
    parser = argparse.ArgumentParser(description="Control the process with start and stop options.")

    parser.add_argument(
        'command',
        choices=['start', 'stop'],
        help="Choose what action to perform: start, stop."
    )

    args = parser.parse_args()

    if args.command == 'start':
        start()
    elif args.command == 'stop':
        stop

if __name__ == '__main__':
    main()