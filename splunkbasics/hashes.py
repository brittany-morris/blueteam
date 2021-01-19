#!/usr/bin/env python3

# find a way to traverse a directory and subdirectory
# get a list sorted of all files within all directories
# hash all files individually
	#print those hashes to a list
# take hashes and hash that list

import os
import sys

input_dir = sys.argv[1]
title_list = []
path_list = []

#Title List
for root, dirs, files in os.walk(input_dir):
	for file in files:
		if file.endswith('.txt'):
		#	print(os.path.join(root,file))
			title_list.append(file)

for elem in sorted(title_list, key = str.casefold):
	print(elem)

# path list
for root, dirs, files in os.walk(input_dir):
        for file in files:
                if file.endswith('.txt'):
                #       print(os.path.join(root,file))
                        path_list.append(os.path.join(root,file))

for elem in sorted(path_list, key = str.casefold):
        print(elem)

#comparing list and printing full path if title is present in order of the title list

for line in title_list:
	if line == path_list:
		print(line)
