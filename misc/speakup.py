from scapy.all import *
import quickset as qs

""" Intended to make a given MAC speak up when spoken to """

def pHandler(sh):
    def snarf(packet):
        if packet.haslayer(Dot11ProbeReq):
            print('go')
            qs.gs(sh.injSocket, sh.spare, verbose = True)
    return snarf


def bssidSpew(stop_event, sh, beacons):
    skt = conf.L2socket(iface = sh.nic)
    while True:
        if stop_event.is_set():
            print("Thread has been interrupted by an event.")
            return
        qs.gs(skt, beacons.open(), verbose = False)
        time.sleep(.1)


## prep
qs.sh.injSocket = conf.L2socket(iface = 'wlan1mon')
qs.sh.essid = '<ESSID>'
qs.sh.nic = '<MON MODE NIC'
qs.sh.macRx = '<Rx MAC>'
qs.sh.macTx = '<Tx MAC>'
qs.sh.channel = 6
qs.sh.spare = qs.probes.response()

bssidStop = qs.threading.Event()
bssidThread = qs.threading.Thread(target = bssidSpew, args = (bssidStop, qs.sh, qs.beacons))
bssidThread.start()
# bssidStop.set()

## All the things
pHandler = pHandler(qs.sh)
f = sniff(iface = 'wlan1mon', prn = pHandler, filter = 'ether host b8:27:eb:04:47:7b')
