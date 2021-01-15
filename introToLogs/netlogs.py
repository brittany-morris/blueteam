#!/usr/bin/env python3

import sys
import re

file= sys.argv[1]
iplist= {} # create an empty dictionary

with open(file, 'r') as f:
	for line in f:
		ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line.strip())
		print(ip)





#outfile = open("out.txt","w") #open output file

#for key in iplist.keys():
 #   line = "%-15s = %s" % (key, iplist[key])
  #  print line   # print uf desired.
   # outfile.write(line + "\n")
