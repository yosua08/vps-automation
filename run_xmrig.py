#! /usr/bin/python3

import os

print("Starting job to run xmrig")

# Create screen session & start xmrig
print("[1] Success create screen session & run xmrig")
run_xmrig = f'screen -S mining\
                   ./xmrig -o rx.unmineable.com:3333 -a rx -k -u DOGE:D7MrSwFABXmGze7oVLVTaASZNSdLDh4J1t.HiitsMe -p x'
os.system(run_xmrig)