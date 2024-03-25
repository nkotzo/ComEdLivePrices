#!/usr/bin/python

import json
import datetime
import requests


ComEd_CurrentAverage_Api_Url = "https://hourlypricing.comed.com/api?type=currenthouraverage&format=json"


# Lets call ComEd and see what the current (or live) price is - returns the current hour average prices
#
response = requests.get(ComEd_CurrentAverage_Api_Url,timeout=10)

#
# Lets see what we got. Needed to figure out what type the pirce verable was.
#
# print('price', price)
#print('type', type(price))
#
#print('raw content: ', response.content)
#print('json content: ', response.json())

#
# Lets pull the current price & time information from the json object. 
#
price = response.json()
#print('Price', price[0]["price"] )
#print('MilliSeconds', price[0]["millisUTC"] )

#
# Convert Millseconds into a data time.
#
date_time = datetime.datetime.fromtimestamp(int(price[0]["millisUTC"])/1000.0)
currentprice = float(price[0]["price"])
#
# Lets see what we've got
#
print('Price: %s at TOD: %s' % (price[0]["price"], date_time))

if (currentprice < 2) :
    print ('its a good time to charge')
else :
    print ('You should hold off, charging car until rate come down')