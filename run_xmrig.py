#! /usr/bin/python3

import os

print("Starting job to run xmrig")

# Create screen session
print("[1] Success create tmux session")
create_session = f'sudo tmux new-session -d -s mining'
os.system(create_session)

# Start xmrig
print("[2] Success run xmrig")
run_xmrig = f" sudo tmux send -t mining 'xmrig -o rx.unmineable.com:3333 -a rx -k -u DOGE:D7MrSwFABXmGze7oVLVTaASZNSdLDh4J1t.HiitsMe -p x' ENTER"
os.system(run_xmrig)