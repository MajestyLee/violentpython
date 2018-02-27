#the program is used to grasp the Banner in the application
#created by Binjie Li, 2017/12/18
#version 1.0
#!/bin/bash
import optparse
import socket
from socket import *
from threading import *
screenLock = Semaphore(value = 1)

#try to connect target host and port
def connScan(tgtHost, tgtPort): 
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send('ViolentPython\r\n')
        results = connSkt.recv(100)
        screenLock.acquire()
        print '[+] %d/tcp open'% tgtPort
        print '[+] ' + str(results)
        connSkt.close()
    except:
        screenLock.acquire()
        print '[+] %d/tcp closed'% tgtPort
    finally:
        screenLock.acquire()
        connSkt.close()

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

def main():
    parser = optparse.OptionParser('usage %prog -H'+ '<target host> -p <target port>')
    parser.add_option('-H', dest = 'tgtHost', type = 'string', help = 'specify target host')
    parser.add_option('-H', dest = 'tgtPort', type = 'string', help = 'spcify target port[s] separated by comma')
    (options, args) = parser.parse_args()
    tgtHost = options.tgtHost
    tgtPorts = str(options.tgtPort).split(', ')
    if (tgtHost == None) | (tgtPorts[0] == None):
        print '[-] You must specify a target host and port[s].'
        exit(0)
    portScan(tgtHost, tgtPorts)
    if __name__ == '__main__':
        main()