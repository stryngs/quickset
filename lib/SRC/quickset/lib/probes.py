from scapy.all import *

class Probes(object):
    """Handles Probe scenarios

    Expects a class passed as shared with a minimum of:
        esrates == ...
        essid   == 802.11 network name
        macRx   == Receiving MAC address
        macTx   == Transmitting MAC address
        nicChan == 802.11 channel to transmit on
        nicChr  == nicChan to ordinal
        rates   == ...
    """
    __slots__ = ['esrates',
                 'essid',
                 'macRx',
                 'macTx',
                 'nicChan',
                 'nicChr',
                 'rates',
                 'sh']

    def __init__(self, shared):
        self.sh = shared


    def request(self):
        return RadioTap()\
               /Dot11(type = 0,
                      subtype = 4,
                      addr1 = self.sh.macRx,
                      addr2 = self.sh.macTx,
                      addr3 = self.sh.macRx)\
               /Dot11ProbeReq()\
               /Dot11Elt(ID = 'SSID', info = self.sh.essid)\
               /Dot11Elt(ID = 'Rates', info = self.sh.rates)\
               /Dot11Elt(ID = 'ESRates', info = self.sh.esrates)\
               /Dot11Elt(ID = 'DSset', info = self.sh.nicChr)
