#! /usr/bin/python3

import os

print("Starting job to run xmrig")

# Go to xmrig directory
print("[1] Success change directory")
ch_dir = f'/root/xmrig/xmrig-6.21.0'
os.chdir(ch_dir)

# Create screen session & start xmrig
print("[2] Success create screen session")
run_xmrig = f'screen -S mining\
                   ./xmrig -o rx.unmineable.com:3333 -a rx -k -u DOGE:D7MrSwFABXmGze7oVLVTaASZNSdLDh4J1t.HiitsMe -p x pause'
os.system(run_xmrig)