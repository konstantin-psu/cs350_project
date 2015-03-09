#!/usr/bin/python3

import json
import os
import sys
import argparse
import re
from pprint import  pprint
import numpy

parser = argparse.ArgumentParser(description='To get test folder path')
parser.add_argument('-t', dest = 'testPath', type=str, help= 'Test folder path', required=True)

args = parser.parse_args()
if args.testPath is None:
   sys.exit(1)

files=os.listdir(args.testPath)
info={} #TODO deicde on info structure for fast search
        # building a tree
        # name -> partition_type
        # partition type -> sizes
        # size -> experiments
"""

"""
s = '{'
e = '}'
bools = [
    'correctness',
    'is integer',
    'stability'
]
ints = [
      'basic operations',
      'ceiling',
      'cutoff',
      'number of duplicates',
      'partition operations',
      'size',
      'total partition',
      'total space used',
      'total split time',
      'total time'
]
for i in files:
    print(args.testPath+i)
    with open(args.testPath+i, 'r') as input:
        flag = False
        sub = {}
        content = input.readlines()
        for i in content:
            if i.strip() == s:
                flag = True
                continue
            elif i.strip() == e:
                # Dump
                flag = False
                for i in sub:
                    if i in ints:
                        if re.match(r'null', sub[i], re.IGNORECASE):
                            sub[i]=None
                            continue
                        sub[i]=numpy.float_(sub[i])
                    elif i in bools:
                        sub[i]=bool(sub[i])
                try:
                    info[sub['name']]
                except KeyError:
                    info[sub['name']] = {}

                try:
                    info[sub['name']][sub['partition type']]
                except KeyError:
                    info[sub['name']][sub['partition type']] = {}

                try:
                    info[sub['name']][sub['partition type']][int(sub['size'])]
                except KeyError:
                    info[sub['name']][sub['partition type']][int(sub['size'])] = {}

                l = len(info[sub['name']][sub['partition type']][int(sub['size'])])
                info[sub['name']][sub['partition type']][int(sub['size'])][l] = sub
                sub = {}
                continue
            if flag:
                m=re.sub(r',','',i.strip(),re.IGNORECASE)
                m=re.sub(r'"','',m,re.IGNORECASE)
                a=m.split(':')
                sub[a[0]]=a[1]
        pprint(info)
#Expect only json files to be in test dir



