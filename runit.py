#!/usr/bin/env python

import requests
import json
import pprint
# crontab
# */5 0 0 0 0 /some/path/runit.py > runit.log 2>&1

#hold alerts received
alert = {}

#{
#  "mem-used-pct" : 83.6,
#  "disc-space-avail" : [
#                         { "discname" : "/dev/SDA1", "availbytes" : "12345000"},
#                         { "discname" : "/dev/SDA2", "availbytes" : "12345000"}
#                       ],
#  "cpu-used-pct" : 55.0
#}


r = requests.get('https://someurl/status')

pprint.pprint(r.json())

for k, v in r.json().items():
     if 'mem-used-pct' in k:
         #Memory Usage is >95.0%
         if v > 95:
           alert[mem-used-pct]='greater than 95'
     if 'disc-space-avail' in k:
         #Disc Space Available on either disc < 1k
         for diskname in v:
             for key,value in diskname.items(): 
                 if 'diskname' in key:
                    disk_path = value
                 if 'availbytes' < 1000:
                    alert[disk_path]=availbytes
     if 'cpu-used-pct' in k:
         #CPU usage is >97.0%
         if v > 97:
           alert[cpu-used-pct]='greater than 97'

#I have only done this in python
SUBDOMAIN='monitoring'
API_ACCESS_KEY='abcdefg'


def trigger_incident(key,value):
    headers = {
        'Authorization': 'Token token={0}'.format(API_ACCESS_KEY),
        'Content-type': 'application/json',
    }
    payload = json.dumps({
      "service_key": "",
      "event_type": "trigger",
      "description": "FAILURE key value",
      "client": "Sample Monitoring Service",
      "client_url": "https://monitoring.service.com",
      "details": {
        "ping time": "1500ms",
        "load avg": 0.75
      }
    })
    r = requests.post(
                    'https://events.pagerduty.com/generic/2010-04-15/create_event.json',
                    headers=headers,
                    data=payload,
    )
    print r.status_code
    print r.text

for k, v in alerts.items():
    trigger_incident(k,v)
