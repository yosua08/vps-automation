#! /usr/bin/python3

import os
import argparse

print("Starting job to run xmrig")

def start():
    # Create tmux session
    print("[1] Success create tmux session")
    create_session = f'sudo tmux new-session -d -s mining'
    active_sessions = f"sudo tmux list-sessions"
    os.system(create_session)
    os.system(active_sessions)

    # Start xmrig
    print("[2] Success run xmrig")
    run_xmrig = f" sudo tmux send -t mining 'xmrig -o rx.unmineable.com:3333 -a rx -k -u DOGE:D7MrSwFABXmGze7oVLVTaASZNSdLDh4J1t.HiitsMe -p x' ENTER"
    os.system(run_xmrig)

def stop():
    # Stop process and exit from tmux session
    print("[1] Success kill tmux session")
    stop_process = f"sudo tmux kill-session -t mining"
    active_sessions = f"sudo tmux list-sessions"
    os.system(stop_process)
    os.system(active_sessions)

def sessions():
    # Check active sessions
    print("Success check active sessions")
    active_sessions = f"sudo tmux list-sessions"
    os.system(active_sessions)

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
    elif args.command == 'check-sessions':
        sessions()

if __name__ == '__main__':
    main()