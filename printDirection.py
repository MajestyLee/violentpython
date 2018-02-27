#encoding:utf-8
import pcap
import dpkt
import time
import math
import os
import optparse, pygeoip, socket
gi = pygeoip.GeoIP('GeoLiteCity.dat')
def retGeoStr(ip):
    try:
        rec = gi.record_by_name(ip)
        city = rec['city']
        country = rec['country_name']
        if (city != ''):
            geoLoc = city + " " + country
        else:
            geoLoc = country
        return geoLoc
    except:
        return "unregistered"
sniffer=pcap.pcap(name=None, promisc=True, immediate=True)    #注，参数可为网卡名，如eth0
# sniffer.setfilter('tcp port 80')    #设置监听过滤器
for timestamp,raw_buf in sniffer:    #ptime为收到时间，pdata为收到数据
    # print timestamp, raw_buf
    eth = dpkt.ethernet.Ethernet(raw_buf)
    if not isinstance(eth.data, dpkt.ip.IP):
        print 'non ip %s\n' %eth.data
        continue
    # print eth.data
    packet = eth.data
    df = bool(packet.off & dpkt.ip.IP_DF)
    mf = bool(packet.off & dpkt.ip.IP_MF)
    offset = packet.off & dpkt.ip.IP_OFFMASK
    print {'time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))}
    print {'src': '%d.%d.%d.%d'%tuple(map(ord,list(packet.src))), 'dst': '%d.%d.%d.%d'%tuple(map(ord,list(packet.dst)))}
    print {'location of src': retGeoStr(str('%d.%d.%d.%d'%tuple(map(ord,list(packet.src))))), 'location of dst': retGeoStr('%d.%d.%d.%d'%tuple(map(ord,list(packet.dst))))}
    print {'protocol': packet.p, 'len': packet.len, 'ttl': packet.ttl}
    print {'df': df, 'mf': mf, 'offset': offset, 'checksum':packet.sum}
    tcp = packet.data
    print tcp.data
    # print bytes.decode(tcp.data)
    # http = dpkt.http.Request(tcp.data)
    # if http.method == 'GET':
        # uri = http.uri.lower()
        # print uri