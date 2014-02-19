# IAmWatchingYou.py
import urllib
from xml.etree.ElementTree import parse
import time

default_route = '0'
default_latitude = 34

def distance(lat1, lat2):
    'Return distance in miles between two lats'
    return 69*abs(lat1-lat2)

def monitor(latitude=default_latitude,route_number=default_route):
    print '-'*30
    print 'ID          Distance in miles'
    print '-'*30
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route='+route_number)
    doc = parse(u)
    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if True:
            lat = float(bus.findtext('lat'))
            dis = distance(lat, latitude)
            print busid,'  |  ', dis, 'miles'
    print '-'*30


route = raw_input('Route Number: ')
latitude = float(raw_input('Latitude (has to be a float) :'))
it = 0
while True:
    monitor(latitude,route)
    time.sleep(5)
    if it == 3:
        q = raw_input("quit? (y/n) ")
        if q == 'y':
            break
        it = 0
    it+=1
