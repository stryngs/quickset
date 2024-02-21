from scapy.all import *

"""
0: 'reserved',
1: 'unspec',
2: 'auth-expired',
3: 'deauth-ST-leaving',
4: 'inactivity',
5: 'AP-full',
6: 'class2-from-nonauth',
7: 'class3-from-nonass',
8: 'disas-ST-leaving',
9: 'ST-not-auth',
"""

class Disassocs(object):
    """Handles Disassociation scenarios

    Expects a class passed as shared with a minimum of:
        macRx  == Receiving MAC address
        macTx  == Transmitting MAC address
        macGw  == Gateway MAC address
        reason == ...
    """
    __slots__ = ['sh']

    def __init__(self, shared):
        self.sh = shared


    def disassoc(self):
        return RadioTap()\
               /Dot11FCS(type = 0,
                         subtype = 10,
                         addr1 = self.sh.macRx,
                         addr2 = self.sh.macTx,
                         addr3 = self.sh.macGw)\
               /Dot11Disas(reason = self.sh.reason)
