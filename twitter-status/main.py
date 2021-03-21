import json
import os
import sys
import time

import concurrent.futures

from scapy.all import sniff, IP

arg_parted = sys.argv[1].split('@')
interface, user = arg_parted[0], arg_parted[1]
inactivity_threshold = 120 # seconds of inactivity to consider user offine
last_connected = 1000 # dummy value for holding time we last connected to twitter
last_status = 'offline'
twitter_ip_range = '104.244.42.0/24' # IP range that twitter.com uses, as of now

def online():
    global last_status
    while True:
        time.sleep(3)
        if abs(int(time.time()) - last_connected) > inactivity_threshold:
            if last_status != 'offline':
                last_status = 'offline'
                print('user status changed, now offline')
                os.system(f'sudo -u {user} python3 {sys.path[0]}/change.py offline')
        elif last_status != 'online':
            last_status = 'online'
            print('user status changed, now online')
            os.system(f'sudo -u {user} python3 {sys.path[0]}/change.py online')

def trigger(packet):
    global last_status, last_connected
    if packet.getlayer(IP).len > 3000:
        last_connected = int(time.time())

def start_sniffing():
    sniff(iface=interface, filter=f'tcp and net {twitter_ip_range}', prn=trigger)

threadpool = concurrent.futures.ThreadPoolExecutor(max_workers=2)
futures = (threadpool.submit(func) for func in (start_sniffing, online))
for i in concurrent.futures.as_completed(futures):
    print(i.result())
