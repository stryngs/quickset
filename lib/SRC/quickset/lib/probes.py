from scapy.all import *
import binascii

class Probes(object):
    """Handles Probe scenarios

    Expects a class passed as shared with a minimum of:
        esrates == ...
        essid   == 802.11 network name
        macRx   == Receiving MAC address
        macTx   == Transmitting MAC address
        channel == 802.11 channel to transmit on
        rates   == ...
    """
    __slots__ = ['esrates',
                 'essid',
                 'macRx',
                 'macTx',
                 'channel',
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
               /Dot11Elt(ID = 'DSset', info = chr(self.sh.channel))


    def response(self):
        """[1.0(B) Mbps, 2.0(B) Mbps, 5.5(B) Mbps, 11.0(B) Mbps]"""

        ## Both Dot11EltVendorSpecific just in case
        ## DD 09 00 10 18 02 01 F0 2C 00 00 DD 18 00 50 F2 02 01 01 80 00 03 A4 00 00 27 A4 00 00 42 43 BC 00 62 32 66 00

        return RadioTap()\
               /Dot11FCS(addr1 = self.sh.macRx,
                         addr2 = self.sh.macTx,
                         addr3 = self.sh.macTx,
                         FCfield = 8,
                         ID = 14849,
                         proto = 0,
                         SC = 51920,
                         subtype = 5,
                         type = 0)\
               /Dot11ProbeResp(cap = 'ESS')\
               /Dot11Elt(info = self.sh.essid)\
               /Dot11EltRates(rates = [130, 132, 139, 150])\
               /Dot11EltDSSSet(channel = self.sh.channel)\
               /Dot11EltVendorSpecific(binascii.unhexlify('DD 09 00 10 18 02 01 F0 2C 00 00'.replace(' ', '')))
