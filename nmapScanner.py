#nmapScanner is created to be familiar to the use of nmap by Binjie Li
#it is better than TCP scanner and can find some filter.
#2017/12/18
import nmap
import optparse

def nmapScan(tgtHost, tgtPort):
    nmScan = nmap.PortScanner()
    nmScan.scan(tgtHost, tgtPort)
    state = nmScan[tgtHost]['tcp'][int(tgtPort)]['state']
    print " [*] " + tgtHost + " tcp/ " + tgtPort + " " + state

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
    for tgtPort in tgtPorts:
        nmapScan(tgtHost, tgtPort)

if __name__ == '__main__':
    main()