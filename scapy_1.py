#the code is used to be familiar to scapy
from scapy.all import *
import pcap
dnsRecords = {}

def handlePkt(pkt):
    if pkt.haslayer(DNSRR):
        rrname = pkt.getlayer(DNSRR).rrname
        rdata = pkt.getlayer(DNSRR).rdata
        if dnsRecords.has_key(rrname):
            if rdata not in dnsRecords[rrname]:
                dnsRecords[rrname].append(rdata)
        else:
            dnsRecords[rrname] = []
            dnsRecords[rrname].append(rdata)

def main():
    sniff(prn = handlePkt)
    # for pkt in sniffer:
    #     handlePkt(pkt)
    for item in dnsRecords:
        print '[+] ' + item + ' has ' + str(len(dnsRecords[item])) + ' unique IPs. '

if __name__ == '__main__':
    main()