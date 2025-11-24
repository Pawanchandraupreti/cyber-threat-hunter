import random
import time
import os
from scapy.all import *

class BeaconSimulator:
    def __init__(self, c2_servers):
        self.c2 = c2_servers
        self.jitter = lambda: random.randint(30, 300)
        
    def beacon(self):
        while True:
            server = random.choice(self.c2)
            payload = f"session={random.getrandbits(128)}&data={os.urandom(64).hex()}"
            send(IP(dst=server)/TCP(dport=443)/Raw(load=payload))  # Fixed TCP instead of ICP
            time.sleep(self.jitter())

              

              