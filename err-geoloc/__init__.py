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
## Updated: Time-stamp: <2017-10-09 08:20:00>
##-------------------------------------------------------------------
from errbot import BotPlugin, botcmd
from geopy.geocoders import Nominatim
import sys, json, geopy, os

class Geoloc(BotPlugin):

    def get_configuration_template(self):
        return {'unique_id':'', #Should be set to either person, id or nick depending on the backend. Use !plugin config geoloc to set.
                'json_path': '', #Set the full path to the json file. Ex "/var/www/html/user_db.json"
                'url': ''
                }  
    @botcmd()
    def geoloc_set(self, msg, args):
        """Define your location
        usage: !geoloc set New York
        """
        
        geolocator = Nominatim()
        location = geolocator.geocode(args) #Create a location array using the data provided by the user
        if os.path.exists(self.config['json_path']): #Check if the database exists
            with open(self.config['json_path'], 'r') as f: #Load the json database file
                user_db = json.load(f)
        else:
            user_db = {} #Create the database if it doesnt
        user_db[str(getattr(msg.frm, self.config['unique_id']))] = { #Insert the user data into an object
                "user": str(msg.frm),
                "place": location[0],
                "latitude":location[1][0],
                "longitude":location[1][1],
        }
        with open(self.config['json_path'], 'w') as f: #Write the user data to the json file
            json.dump(user_db, f)
        yield("Your location is set as %s" % user_db[str(getattr(msg.frm, self.config['unique_id']))]['place']) #Prompt the location back to the user to make sure he chose the right one
        yield("Here is the current updated map : %s" % self.config['url'])

    @botcmd()
    def geoloc_get(self, msg, args):
        """Get your current location
        usage: !geoloc get
        """
        with open(self.config['json_path'], 'r') as f:
            user_db = json.load(f)
        if user_db[str(getattr(msg.frm, self.config['unique_id']))] is None:
            yield("Please set a location with !loc set")
            raise SystemExit(0)
        else:
            yield("Your location is set as %s" % user_db[str(getattr(msg.frm, self.config['unique_id']))]['place'])

## File : __init__.py ends
