import pygeoip
gi = pygeoip.GeoIP('GeoLiteCity.dat')
def printRecord(tgt):
    rec = gi.record_by_name(tgt)
    city = rec['city']
    # region = rec['repipgion_name']
    country = rec['country_name']
    longi = rec['longitude']
    lat = rec['latitude']
    print '[*] Target: ' + tgt + ' Geo-located. '
    print '[+] ' + str(city) + ', ' + str("region") + ', ' + str(country)
    print '[+] Latitude: ' + str(lat) + ', Longitute: ' + str(longi)
tgt = '112.25.223.108'
printRecord(tgt)
