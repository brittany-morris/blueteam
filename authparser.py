#!/usr/bin/env python3

# Take a file via command line
# pull out IP addresses and add them to a dictionary
# count the number of times that IP address is seen
# make a list of ip addresses with how many times they are seen
# take the total seen of all numbers and break it up into percentage seen

import sys
import re

inputfile = sys.argv[1]

with open(inputfile, 'r') as f:
	for line in f:
		ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', line.strip())
		print(ip)
