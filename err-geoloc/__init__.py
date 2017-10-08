#!/usr/bin/env python
##-------------------------------------------------------------------
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File : __init__.py
## Author : Romain Brucker <brucker.romain@gmail.com>, Denny Zhang <contact@dennyzhang.com>
## Description :
## --
## Created : <2017-10-04>
## Updated: Time-stamp: <2017-10-06 19:34:49>
##-------------------------------------------------------------------
from errbot import BotPlugin, botcmd
from geopy.geocoders import Nominatim
import sys, json, geopy
import gmplot
from gmplot import GoogleMapPlotter as gmp

class Geoloc(BotPlugin):

    def activate(self):
        super(Geoloc, self).activate()
        if 'location_db' not in self:     
            self['location_db'] = {}


    @botcmd()
    def geoloc_set(self, msg, args):
        geolocator = Nominatim()
        location = geolocator.geocode(args)
        location_db = self['location_db']
        location_db[str(msg.frm.person)] = {
                "user": msg.frm.person,
                "place": location[0],
                "latitude":location[1][0],
                "longitude":location[1][1],
        }
        yield("Your location is set as %s" % self['location_db'][str(msg.frm.person)]['place'])
        self['location_db'] = location_db
        gmap = gmp.from_geocode("Washington DC", 5)
        for i in location_db:
            gmap.marker(location_db[i]['latitude'], location_db[i]['longitude'], "red", None, location_db[i]['user'])
            gmap.text(location_db[i]['latitude']-0.5, location_db[i]['longitude'], color="#000000", text=location_db[i]['user'])
        gmap.draw('/tmp/map.html', api_key=self['api_key'])

    @botcmd()
    def geoloc_get(self, msg, args):
        if self['location_db'][str(msg.frm.person)] is None:
            yield("Please set a location with !loc set")
            raise SystemExit(0)
        else:
            yield("Your location is set as %s" % self['location_db'][str(msg.frm.person)]['place'])

    @botcmd()
    def geoloc_debug(self, msg, args):
        name = "@%s" % str(msg.frm.nick)
        if name in self.bot_config.BOT_ADMINS:
            yield(self['location_db'])
        else:
            yield("you need to be an admin to use this command")

    @botcmd()
    def geoloc_wipe(self, msg, args):
        name = "@%s" % str(msg.frm.nick)
        if name in self.bot_config.BOT_ADMINS:
            self['location_db'] = {}
            yield("Database reset")
        else:
            yield("you need to be an admin to use this command")

    @botcmd()
    def geoloc_set_api(self, msg, args):
        name = "@%s" % str(msg.frm.nick)
        if name in self.bot_config.BOT_ADMINS:
            api_key = args
            self['api_key'] = api_key
            yield("api_key set to %s" % api_key)
        else:
            yield("you need to be an admin to use this command")

## File : __init__.py ends
