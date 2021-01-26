#!/usr/bin/env/ python3

import sys

file= sys.argv[1]

with open (file, 'r') as f:
	for a in f:
	print(a)
	for b in file[a]:
		print(b, ':', file[a][b])
