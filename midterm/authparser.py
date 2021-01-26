#!/usr/bin/env python3

import re
import sys

def extract_IPs(line):
    # do something with the line to get IP addresses
    # REGEX to match full IP address
    ip_regex = re.compile(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}')
    ip_addresses = re.findall(ip_regex, line)
    return ip_addresses

def count_ip_addresses(ip_list):
    # make an empty dictionary of the counts
    ip_counts = {}
    # loop through the ip_list
    for ip in ip_list:
        ip_counts[ip] = ip_counts.get(ip, 0) + 1
    return ip_counts

def main():
    #1. take args from cmdline
    filename = sys.argv[1] # assume this is a plaintext file

    # 1.1 - create empty list for the total IP addresses
    ip_list = []

    # 2. read the file and
    # for each line :
    with open(filename, 'r') as f:
        for line in f:

    #   3. Extract IP address from line and place in a list
            ip_addresses = extract_IPs(line)

    #   4. add IP address list to the total IP address list
            ip_list.extend(ip_addresses)

    #   5. go through total list - map list to a dictionary of counts
        ip_dictionary = count_ip_addresses(ip_list)

    # print the dictionary
    print(ip_dictionary)

if __name__ == '__main__':
    main()
