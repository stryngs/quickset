from .lib.arps import Arps
from .lib.beacons import Beacons
from .lib.deauths import Deauths
from .lib.probes import Probes
from .lib.supplicants import Supplicants

class Shared(object):
    """Create a shared class for all modules

    algo    == Algorithm to use for 802.11
    bus     == wireless or wired interface type
    esrates == ...
    essid   == 802.11 network name
    ipDst   == Destination IP Address
    ipGtw   == Gateway IP Address
    ipSrc   == Source IP Address
    macGw   == Gateway MAC address
    macRx   == Receiving MAC address
    macTx   == Transmitting MAC address
    nicChan == 802.11 channel to transmit on
    nicChr  == nicChan to ordinal
    rates   == ...
    reason  == ...
    seqNum  == Sequence number
    """
    __slots__ = ['algo',
                 'bus',
                 'esrates',
                 'essid',
                 'ipDst',
                 'ipGtw',
                 'ipSrc',
                 'macGw',
                 'macRx',
                 'macTx',
                 'nicChan',
                 'rates',
                 'reason',
                 'seqNum']

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
                 nicChan = 1,
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
        self.nicChan = nicChan
        self.rates = rates
        self.reason = reason
        self.seqNum = seqNum

## Instatiations
sh = Shared()
arps = Arps(sh)
beacons = Beacons(sh)
deauths = Deauths(sh)
probes = Probes(sh)
supplicants = Supplicants(sh)
