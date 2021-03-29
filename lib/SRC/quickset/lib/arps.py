from scapy.all import *

class Arps(object):
    """Handles ARP scenarios

    Expects a class passed as shared with a minimum of:
        bus   == wireless or wired interface type
        ipDst == Destination IP Address
        ipGtw == Gateway IP Address
        ipSrc == Source IP Address
        macGw == Gateway MAC address
        macRx == Receiving MAC address
        macTx == Transmitting MAC address
        mode  == wireless or wired; based on shared.bus
    """
    slots = ['bus',
             'ipDst',
             'ipGtw',
             'ipSrc',
             'macGw',
             'macRx',
             'macTx',
             'sh']

    def __init__(self, shared):
        self.sh = shared


    def broadCast(self):
        """Broadcasted ARP"""
        print(self.sh.bus)
        if self.sh.bus == 'wireless':
            return RadioTap()\
                   /Dot11FCS(addr1 = 'ff:ff:ff:ff:ff:ff',
                             addr2 = self.sh.macTx,
                             addr3 = self.sh.macRx,
                             subtype = 8,
                             type = 2,
                             FCfield = 1,
                             ID = 54000,
                             SC = 23000)\
                   /Dot11QoS()\
                   /LLC(dsap = 170, ssap = 170, ctrl = 3)\
                   /SNAP(code = 2054)\
                   /ARP(op = 2,
                        hwdst = 'ff:ff:ff:ff:ff:ff',
                        hwsrc = self.sh.macTx,
                        psrc = self.sh.ipSrc)
        else:
            return Ether(dst = 'ff:ff:ff:ff:ff:ff', src = self.sh.macTx, type = 2054)\
                   /ARP(op = 2,
                        hwdst = 'ff:ff:ff:ff:ff:ff',
                        hwsrc = self.sh.macTx,
                        psrc = self.sh.ipSrc)


    def oneWay(self):
        """one-way ARP"""
        if self.sh.bus == 'wireless':
            return RadioTap()\
                   /Dot11FCS(addr1 = self.sh.macGw,
                             addr2 = self.sh.macTx,
                             addr3 = self.sh.macGw,
                             subtype = 8,
                             type = 2,
                             FCfield = 1,
                             ID = 54000,
                             SC = 23000)\
                   /Dot11QoS()\
                   /LLC(dsap = 170, ssap = 170, ctrl = 3)\
                   /SNAP(code = 2054)\
                   /ARP(op = 2,
                        hwdst = self.sh.macGw,
                        hwsrc = self.sh.macTx,
                        pdst = self.sh.ipGtw,
                        psrc = self.sh.ipSrc)
        else:
            return Ether(dst = self.sh.macRx, src = self.sh.maxTx, type = 2054)\
                   /ARP(op = 2,
                        hwdst = self.sh.macGw,
                        hwsrc = self.sh.macTx,
                        pdst = self.sh.ipGtw,
                        psrc = self.sh.ipSrc)


    def twoWay(self):
        """two-way ARP
        Returns rtrArp followed by tgtArp"""
        if self.sh.bus == 'wireless':
            p2 = RadioTap()\
                 /Dot11FCS(addr1 = self.sh.macGw,
                           addr2 = self.sh.macTx,
                           addr3 = self.sh.macRx,
                           subtype = 8,
                           type = 2,
                           FCfield = 1,
                           ID = 54000,
                           SC = 23000)\
                 /Dot11QoS()\
                 /LLC(dsap = 170, ssap = 170, ctrl = 3)\
                 /SNAP(code = 2054)\
                 /ARP(op = 2,
                      hwdst = self.sh.macRx,
                      hwsrc = self.sh.macTx,
                      pdst = self.sh.ipDst,
                      psrc = self.sh.ipGtw)
        else:
            p2 = Ether(dst = self.sh.macGw, src = self.sh.maxTx, type = 2054)\
                 /ARP(op = 2,
                      hwdst = self.sh.macRx,
                      hwsrc = self.sh.macTx,
                      pdst = self.sh.ipDst,
                      psrc = self.sh.ipGtw)
        return [p2, self.oneWay]
