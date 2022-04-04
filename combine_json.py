import os
import json
import glob
import re


def search(s):
    working_directoy = os.getcwd()
    for _,_,filename in os.walk(working_directoy):
        for f in filename:
            if f.find(s) != -1:
                yield os.path.join(working_directoy,f)

result = []
for f in search('following'):
    with open(f, "rb") as infile:
        result.append(json.load(infile))

with open("merged_following.json",  "w", encoding="utf8") as outfile:
     json.dump(result, outfile)
