from scapy.all import *

"""
auth           >
auth success   <
assoc request  >
assoc response <
authenticated  <
associated     >
"""

class Supplicants(object):
    """Handles Supplicant scenarios

    Authenticates with open wifi by default
    Expects a class passed as shared with a minimum of:
        algo    == Algorithm to use for 802.11
        esrates == ...
        essid   == 802.11 network name
        macRx   == Receiving MAC address
        macTx   == Transmitting MAC address
        rates   == ...
        seqNum  == Sequence number
"""
    __slots__ = ['algo',
                 'esrates',
                 'essid',
                 'macRx',
                 'macTx',
                 'rates',
                 'seqNum',
                 'sh']

    def __init__(self, shared):
        self.sh = shared

    def authenticate(self):
        return RadioTap()\
               /Dot11(type = 0,
                      subtype = 11,
                      addr1 = macRx,
                      addr2 = macTx,
                      addr3 = macRx)\
               /Dot11Auth(algo = self.sh.algo,
                          seqnum = self.sh.seqNum)


    def associate(self):
        return RadioTap()\
               /Dot11(type = 0,
                      subtype = 0,
                      addr1 = self.sh.macRx,
                      addr2=self.sh.macTx,
                      addr3=self.sh.macRx)\
               /Dot11AssoReq()\
               /Dot11Elt(ID = 'SSID', info = self.sh.essid)\
               /Dot11Elt(ID = 'Rates', info = self.sh.rates)\
               /Dot11Elt(ID = 'ESRates', info = self.sh.esrates)
