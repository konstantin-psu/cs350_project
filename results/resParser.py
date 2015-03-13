#!/usr/bin/python3

import json
import os
import sys
import argparse
import re
from pprint import  pprint
from  numpy import sort
import numpy
import matplotlib.pyplot as plt
from numpy import std

parser = argparse.ArgumentParser(description='To get test folder path')
parser.add_argument('-t', dest = 'testPath', type=str, help= 'Test folder path', required=True)

def p(a):
    print("x 0fx")
    for i in a:
        print(str(i)+" "+str(a[i]))
    print("")
args = parser.parse_args()
if args.testPath is None:
   sys.exit(1)

from numpy import log2

logf = {}
size = 1
olist = []
m = size*log2(size)
logf[size] = m
# print(str(size)+" & "+ str(m))
olist.append(size)
while size < 19000000:
    if size < 1000000:
        size *= 10
    else:
        size += 1000000
    m = size*log2(size)
    olist.append(size)
    logf[size] = m
    # print(str(size)+" & "+ str(m))

# files=os.listdir(args.testPath)
files = args.testPath
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
    with open(args.testPath, 'r') as input:
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
                name = i.split('.')[0]
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
                info[sub['name']][sub['partition type']][int(sub['size'])] = sub
                sub = {}
                continue
            if flag:
                subsub += i.strip()
                # m=re.sub(r',','',i.strip(),re.IGNORECASE)
                # m=re.sub(r'"','',m,re.IGNORECASE)
                # a=m.split(':')
                # sub[a[0]]=a[1]
        # pprint(info)

def dump(info, name, type):
    with open(name+type+files.split(".")[0]+".dat", 'a') as out:
    # with open(name+type+"BottomUpheapSort.dat", 'a') as out:
        out.write("x 0fx\n")
        out.write(json.dumps(info, sort_keys = True, indent=0, separators=(' ', ' ')))
        out.write("\n")

txaxys = []
tyaxis = []
sxaxys = []
syaxis = []
ax = {}
axs = {}
superRes = {}
for i in info:
    # if i == "mergesort":
        ssort = info[i]
        for j in ssort:
            # if j == 'gauss':
                distr=ssort[j]
                # print("=====================================================")
                # print(j)
                for k in distr:
                    ax[k]=distr[k]['total time']
                    axs[k]=distr[k]['basic operations']
#                     txaxys.append(k)
#                     tyaxis.append(distr[k]['total time'])
#                     sxaxys.append(k)
#                     syaxis.append(distr[k]['basic operations'])
#                 print("time")
#                 pprint(ax)
#                 print("steps")
#                 pprint(axs)
#                 dump(ax, j, "time")
#                 dump(axs, j, "steps")
#                 print(j+ ' steps ')

                superRes[j] = []
                for i in olist:
                    try:
                        a = [axs[i], logf[i]]
                    except KeyError:
                        continue
                    if (i != 1):
                        b = (axs[i] / logf[i])
                    else:
                        b = 0
                    superRes[j].append(b)

                    # print(str(i)+" "+str(std(a))+ "   "+str(b))
                ax.clear()
                axs.clear()

# print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(files.split(".")[0])
for i in superRes:
    # print("Standard deviation "+i + " "+str(std(superRes[i])))
    print(i + " "+str(numpy.average(superRes[i])))
#
# txaxys=sort(txaxys)
# tyaxis=sort(syaxis)
# plt.plot(txaxys, tyaxis, 'r--', txaxys, sort(syaxis), 'bs')
# plt.show()
# pprint(ax)
# pprint(axs)

#Expect only json files to be in test dir



