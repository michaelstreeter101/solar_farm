# Original author: MWS
# Creation Date: 2020-11-04
# Purpose: 
# v1 - read in a JSON file
import json
import datetime

class pyrometer:
    def __init__( self ):
        # There are 12 Dailydata JSON format files, one for each month. 
        # Open the Dailydata file for this month and read in the daily_profile dict.
        now = datetime.datetime.now()
        month = now.strftime("%m") # Month 00-12

        with open('Dailydata_51.640_-0.510_SA_' + month + '_35deg_0deg.json') as json_file:
            self.data = json.load(json_file)

        self.dp = self.data['outputs']['daily_profile']

    def dp_now( self ):
        # the dp dict contains the Daildata for the current month. 
        # Return the daily_profile element for the current hour.
        now = datetime.datetime.now()
        hour = now.strftime("%H") # Hour 00-23

        # NB: Gcs(i) = Global clear-sky irradiance on a fixed plane in W/m2
        # NB: T2m = 2-m air temperature in ºC
        print( self.dp[ int( hour ) ] ) # e.g. {'month': 11, 'time': '12:00', 'Gcs(i)': 616.91, 'T2m': 9.93}

        return self.dp[ int( hour ) ]

    def __str__(self):
        return str( self.dp_now() )

# Test code
# p = pyrometer()
# print( p )