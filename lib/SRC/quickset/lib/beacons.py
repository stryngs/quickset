from scapy.all import *

class Beacons(object):
    """Handles Beacon scenarios

    Expects a class passed as shared with a minimum of:
        essid == 802.11 network name
        macTx == Receiving MAC address
    """

    __slots__ = ['essid',
                 'macTx',
                 'sh']

    def __init__(self, shared):
        self.sh = shared


    def open(self):
        """Send open beacon"""
        return RadioTap()\
               /Dot11(type = 0,
                      subtype = 8,
                      addr1 = 'ff:ff:ff:ff:ff:ff',
                      addr2 = self.sh.macTx,
                      addr3 = self.sh.macTx)\
               /Dot11Beacon()\
               /Dot11Elt(ID = 'SSID',
                         info = self.sh.essid,
                         len = len(self.sh.essid))


    def halfway(self):
        """Send protected beacon, kind of..."""
        return RadioTap()\
               /Dot11(type = 0,
                      subtype = 8,
                      addr1 = 'ff:ff:ff:ff:ff:ff',
                      addr2 = self.sh.macTx,
                      addr3 = self.sh.macTx)\
               /Dot11Beacon(cap = 'ESS+privacy')\
               /Dot11Elt(ID = 'SSID', info = self.sh.essid, len = len(self.sh.essid))



    def protected(self):
        """Send protected beacon"""
        return RadioTap()\
               /Dot11(type = 0,
                      subtype = 8,
                      addr1 = 'ff:ff:ff:ff:ff:ff',
                      addr2 = self.sh.macTx,
                      addr3 = self.sh.macTx)\
               /Dot11Beacon(cap = 'ESS+privacy')\
               /Dot11Elt(ID = 'SSID', info = self.sh.essid, len = len(self.sh.essid))\
               /Dot11Elt(ID = 'RSNinfo', info = (b'\x01\x00'                     #RSN Version 1
                                                 b'\x00\x0f\xac\x02'             #Group Cipher Suite : 00-0f-ac TKIP
                                                 b'\x02\x00'                     #2 Pairwise Cipher Suites (next two lines)
                                                 b'\x00\x0f\xac\x04'             #AES Cipher
                                                 b'\x00\x0f\xac\x02'             #TKIP Cipher
                                                 b'\x01\x00'                     #1 Authentication Key Managment Suite (line below)
                                                 b'\x00\x0f\xac\x02'             #Pre-Shared Key
                                                 b'\x00\x00'))                   #RSN Capabilities (no extra capabilities)
