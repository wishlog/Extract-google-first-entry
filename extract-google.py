import json
import os
import re
import sys
import csv


from natsort import natsorted, ns
from decimal import Decimal
from pprint import pprint

ios_versions = [
"ASA5506",
"ASA5515",
"CISCO2821",
"NetScreen%205XT",
"WS-C3850",
]

Input google custom search key:
key = "thekey"
cx = "cx"

with open('output.csv', 'w') as csvfile:
       	writer = csv.writer(csvfile)
       	for ios_version in ios_versions:
       		try:
       			ios = os.popen('curl https://www.googleapis.com/customsearch/v1\?q\=' + ios_version + '+eos\&key\=' + key + '\&cx\=' + cx 2> /dev/null').read()
       			first_entry = json.loads(ios)["items"][0]

       			cvss = {'low':0, 'medium':0, 'high':0, 'critical':0}
       			vuln_desc = ""
       			fixed = []
       			#pprint(data)
       			print(ios_version+ "\t" + first_entry["link"])


       		except:
       			#print to output
       			print(ios_version.replace('\\', '') + '\t' + 'error')

       			#Print to file in csv format:
       			writer.writerow([ios_version.replace('\\', ''), 'error'])
