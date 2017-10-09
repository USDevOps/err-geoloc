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
## Updated: Time-stamp: <2017-10-08 10:01:49>
##-------------------------------------------------------------------
from errbot import BotPlugin, botcmd
from geopy.geocoders import Nominatim
import sys, json, geopy

class Geoloc(BotPlugin):

    @botcmd()
    def geoloc_set(self, msg, args):
        geolocator = Nominatim()
        location = geolocator.geocode(args)
        with open('user_db.json', 'r') as f:
            user_db = json.load(f)
        user_db[str(msg.frm.person)] = {
                "user": msg.frm.person,
                "place": location[0],
                "latitude":location[1][0],
                "longitude":location[1][1],
        }
        with open('user_db.json', 'w') as f:
            json.dump(user_db, f)
        yield("Your location is set as %s" % user_db[str(msg.frm.person)]['place'])

    @botcmd()
    def geoloc_get(self, msg, args):
        with open('user_db.json', 'r') as f:
            user_db = json.load(f)
        if user_db[str(msg.frm.person)] is None:
            yield("Please set a location with !loc set")
            raise SystemExit(0)
        else:
            yield("Your location is set as %s" % user_db[str(msg.frm.person)]['place'])

    @botcmd()
    def geoloc_debug(self, msg, args):
        name = "@%s" % str(msg.frm.nick)
        if name in self.bot_config.BOT_ADMINS:
            yield(user_db)
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
