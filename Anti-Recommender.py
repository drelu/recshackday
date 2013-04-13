# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# # Getting users from Relify

# <codecell>

import sys
import os
import json
import urllib2, urllib
import pandas
import ast
from string import Template
from random import choice

SAMPLE_SIZE=1024
BASE_PATH=".."
base_url=Template("https://api.relify.com/1/recommenders/49acbd0d-5aa9-431d-b87d-20f6fb2ba2a5/$user/recommended?count=20&access_token=7777b492e3beeb93b99d1f33ccbfb2b5")

output_file=open("user_dump.json", "w")
users_retail=open(os.path.join(BASE_PATH, "users_retail"), "r").readlines()
results= {}

for i in range(0, SAMPLE_SIZE):    
    user_id = choice(users_retail).split("\t")[0]
    user_url=base_url.substitute(user=user_id)
    request = urllib2.Request(user_url)
    handler = urllib2.urlopen(request)
    recommendation = ast.literal_eval(handler.read())
    if len(recommendation)>0:
        #print "User ID: " + user_id + " Recommendation: " + str(recommendation)
        results[user_id]=recommendation
    
#    if i%200:
#        print "Read %d entries"%(i)
#        json.dump(results, output_file)
        
json.dump(results, output_file)    
output_file.close()
print results.values()

# <codecell>

import json
jfile = open("test.json").read()
results = json.loads(jfile)
print results.values()

# <markdowncell>

# # Do some evaluation

# <codecell>

import pandas
data = [item for sublist in results.values() for item in sublist]
data_df = pandas.DataFrame(data)
counts = data_df["place_id"].value_counts()

# <codecell>

final_venues=[]
found={}
for i in data:
    print "Place: %s Count: %s"%(str(i), str(counts[i["place_id"]]))
    placeid = i["place_id"]
    i["score"] = counts[placeid]
    
    if found.has_key(placeid)==False:
        found[i["place_id"]]=True
        final_venues.append(i)

score_file = open("score.json","w")        
json.dump(final_venues, score_file)    
score_file.close()

# <codecell>

for i in counts:
    print i

# <codecell>


