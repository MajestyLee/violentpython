#the program is used to be familiar to the use of python in network, the aim is to create a port scanner
#created by Binjie Li, 2017/12/18
#version 1.0
#!/bin/bash
import os
import optparse
from socket import *

#try to connect target host and port
def connScan(tgtHost, tgtPort): 
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        print '[+] %d/tcp open'% tgtPort
        connSkt.close()
    except:
        print '[+] %d/tcp closed'% tgtPort

#scan the port by using name 
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost) # by using name search the host
    except:
        print "[-] cannot resolve '%s': Unknown host"%tgtHost
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print '\n[+] Scab Results for: ' + tgtName[0]
    except:
        print '\n[+] Scab Results for: ' + tgtIP
    setdefaulttimeout(1) #timeout
    for tgtPort in tgtPorts:
        print 'Scanning port ' + tgtPort
        connScan(tgtHost, int(tgtPort))

parser = optparse.OptionParser('usage %prog -H'+ '<target host> -p <target port>')
parser.add_option('-H', dest = 'tgtHost', type = 'string', help = 'specify target host')
parser.add_option('-p', dest = 'tgtPort', type = 'int', help = 'specify target port')
(options, args) = parser.parse_args()
tgtHost = options.tgtHost
tgtPort = options.tgtPort
if (tgtHost == None) | (tgtPort == None):
    print parser.usage
else:
    print "scan ok"
    exit(0)
