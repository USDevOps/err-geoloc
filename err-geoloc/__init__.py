from errbot import BotPlugin, botcmd
from geopy.geocoders import Nominatim
import sys, json, geopy
import gmplot
from gmplot import GoogleMapPlotter as gmp

class Geoloc(BotPlugin):

    def activate(self):
        super(Geoloc, self).activate()
        if 'location' not in self:     
            self['location'] = {}

    @botcmd()
    def geoloc_set(self, msg, args):
        # yield args
        geolocator = Nominatim()
        town = geolocator.geocode(args)
        # yield (msg.frm)
        # yield (location[1][0])


        location = {
                str(msg.frm.person): town,
            }
        self['location'] = location
        yield (location[str(msg.frm.person)][1][1])
        yield (location[str(msg.frm.person)][1][0])
        latitudes = [location[str(msg.frm.person)][1][0]]
        longitudes = [location[str(msg.frm.person)][1][1]] 
        gmap = gmp.from_geocode("San Francisco", 5)
        gmap.marker(location[str(msg.frm.person)][1][0], location[str(msg.frm.person)][1][1], "red", None, "romainrbr")
        gmap.draw('/tmp/map.html')

    @botcmd()
    def geoloc_get(self, msg, args):
        if self['location'][str(msg.frm.person)] is None:
            yield("Please set a location with !loc set")
            raise SystemExit(0)
        else:
            yield("Your location is set as %s" % self['location'][str(msg.frm.person)])
