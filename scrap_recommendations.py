#/usr/bin/python

import sys
import os
import json
import urllib2, urllib
import pandas
from string import Template
from random import choice

BASE_PATH=".."
SAMPLE_SIZE=10

base_url=Template("https://api.relify.com/1/recommenders/49acbd0d-5aa9-431d-b87d-20f6fb2ba2a5/$user/recommended?count=20&access_token=7777b492e3beeb93b99d1f33ccbfb2b5")

users_retail=open(os.path.join(BASE_PATH, "users_retail"), "r")

output="user_dump.json"
output_file=open(output, "w")

results= {}

#for index, i in enumerate(users_retail):

if len(users_retail)<SAMPLE_SIZE:
    SAMPLE_SIZE=users_retail

for i in range(0, SAMPLE_SIZE):    
    user_id = choice(users_retail).split("\t")[0]
    user_url=base_url.substitute(user=user_id)
    request = urllib2.Request(user_url)
    handler = urllib2.urlopen(request)
    recommendation = handler.read()
    print "User ID: " + user_id + " Recommendation: " + recommendation
    results[user_id]=recommendation 
    
    if index%200:
        print "Read %d entries"%(index)
        json.dump(results, output_file)
        
json.dump(results, output_file)    
output_file.close()
users_retail.close()



