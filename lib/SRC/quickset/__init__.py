import binascii
import threading
import time
from .lib.arps import Arps
from .lib.beacons import Beacons
from .lib.deauths import Deauths
from .lib.probes import Probes
from .lib.supplicants import Supplicants
from scapy.all import *
from scapy.sendrecv import __gen_send as gs

class Shared(object):
    """Create a shared class for all modules

    algo      == Algorithm to use for 802.11
    bus       == wireless or wired interface type
    esrates   == ...
    essid     == 802.11 network name
    injSocket == Static socket for speed purposes, use this to inject
    ipDst     == Destination IP Address
    ipGtw     == Gateway IP Address
    ipSrc     == Source IP Address
    macGw     == Gateway MAC address
    macRx     == Receiving MAC address
    macTx     == Transmitting MAC address
    nic       == Network Interface Card
    channel   == 802.11 channel to transmit on
    pHandler  == Shared packet handler
    qsList    == Overview of the shared slots
    rates     == ...
    reason    == ...
    seqNum    == Sequence number
    spare     == spare object slot
    """
    __slots__ = ['algo',
                 'bus',
                 'esrates',
                 'essid',
                 'injSocket',
                 'ipDst',
                 'ipGtw',
                 'ipSrc',
                 'macGw',
                 'macRx',
                 'macTx',
                 'nic',
                 'channel',
                 'qsList',
                 'rates',
                 'reason',
                 'seqNum',
                 'spare']

    def __init__(self,
                 algo = 0,
                 bus = 'wireless',
                 esrates = b'\x30\x48\x60\x6c',
                 essid = None,
                 ipDst = None,
                 ipGtw = None,
                 ipSrc = None,
                 macGw = None,
                 macRx = 'ff:ff:ff:ff:ff:ff',
                 macTx = 'ff:ff:ff:ff:ff:ff',
                 channel = 1,
                 rates = b'\x82\x84\x8b\x96\x0c\x12\x18',
                 reason = 7,
                 seqNum = 1):
        self.algo = algo
        self.bus = bus
        self.esrates = esrates
        self.essid = essid
        self.ipDst = ipDst
        self.ipGtw = ipGtw
        self.ipSrc = ipSrc
        self.macGw = macGw
        self.macRx = macRx
        self.macTx = macTx
        self.channel = channel
        self.rates = rates
        self.reason = reason
        self.seqNum = seqNum


    def qsView(self):
        """Update qsList for easy remembering of the set values"""
        self.qsList = []
        self.qsList.append('algo    - {0}'.format(self.algo))
        self.qsList.append('bus     - {0}'.format(self.bus))
        self.qsList.append('esrates - {0}'.format(self.esrates))
        self.qsList.append('essid   - {0}'.format(self.essid))
        self.qsList.append('ipDst   - {0}'.format(self.ipDst))
        self.qsList.append('ipGtw   - {0}'.format(self.ipGtw))
        self.qsList.append('ipSrc   - {0}'.format(self.ipSrc))
        self.qsList.append('macGw   - {0}'.format(self.macGw))
        self.qsList.append('macRx   - {0}'.format(self.macRx))
        self.qsList.append('macTx   - {0}'.format(self.macTx))
        self.qsList.append('channel - {0}'.format(self.channel))
        self.qsList.append('rates   - {0}'.format(self.rates))
        self.qsList.append('reason  - {0}'.format(self.reason))
        self.qsList.append('seqNum  - {0}'.format(self.seqNum))
        for i in self.qsList:
            print(i)

## Instatiations
sh = Shared()
arps = Arps(sh)
beacons = Beacons(sh)
deauths = Deauths(sh)
probes = Probes(sh)
supplicants = Supplicants(sh)
