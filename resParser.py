#!/usr/bin/python3

import json
import os
import sys
import argparse
import re
from pprint import  pprint
import numpy
import matplotlib.pyplot as plt

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
    # print(args.testPath+i)
    with open(args.testPath+i, 'r') as input:
        flag = False
        sub = {}
        subsub = ""
        content = input.readlines()
        for i in content:
            if i.strip() == s:
                subsub += i.strip()
                flag = True
                continue
            elif i.strip() == e:
                # Dump
                subsub += i.strip()
                flag = False
                jj = json.loads(subsub)
                subsub = ""
                # for i in sub:
                #     if i in ints:
                #         if re.match(r'null', sub[i], re.IGNORECASE):
                #             sub[i]=None
                #             continue
                #         sub[i]=numpy.float_(sub[i])
                #     elif i in bools:
                #         sub[i]=bool(sub[i])
                sub = jj
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
                subsub += i.strip()
                # m=re.sub(r',','',i.strip(),re.IGNORECASE)
                # m=re.sub(r'"','',m,re.IGNORECASE)
                # a=m.split(':')
                # sub[a[0]]=a[1]
        # pprint(info)

xaxys = []
yaxis = []
for i in info:
    # if i == "mergesort":
        sort = info[i]
        for j in sort:
            # distr=sort[j]
            print(j)
            # pprint(distr)
            # for k in distr:
            #     print(str(k)+ " : "+str(len(distr[k])))
            # break
        # break


#Expect only json files to be in test dir



