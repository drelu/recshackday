import sys
import os
import json
import time
import urllib2, urllib
import pandas
import ast
from string import Template
from random import choice

SAMPLE_SIZE=10000
BASE_PATH=".."
base_url=Template("https://api.relify.com/1/recommenders/49acbd0d-5aa9-431d-b87d-20f6fb2ba2a5/$user/recommended?count=20&access_token=7777b492e3beeb93b99d1f33ccbfb2b5")

output_file=open("user_dump.json", "w")
users_retail=open(os.path.join(BASE_PATH, "users_retail"), "r").readlines()
results= {}

start = time.time()
for i in range(0, SAMPLE_SIZE):    
    user_id = choice(users_retail).split("\t")[0]
    user_url=base_url.substitute(user=user_id)
    request = urllib2.Request(user_url)
    handler = urllib2.urlopen(request)
    recommendation = ast.literal_eval(handler.read())
    if len(recommendation)>0:
        #print "User ID: " + user_id + " Recommendation: " + str(recommendation)
        results[user_id]=recommendation
    
    if i%50==0:
        print "Read %d/%d entries in %s sec"%(i, SAMPLE_SIZE, str(time.time()-start))
        json.dump(results, output_file)
        output_file.flush()
json.dump(results, output_file)    
output_file.close()
