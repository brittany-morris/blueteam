#!/usr/bin/env python3

import sys
import re

file= sys.argv[1]
iplist= {} # create an empty dictionary

with open(file, 'r') as f:
	for line in f:
		ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line.strip())
		print(ip)
	#	ip.append(iplist)
	#	print(iplist)



