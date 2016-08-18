#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
prev_filename = None
current_count = 0
word = None
N=0
df={}
l1=[]


for line in sys.stdin:
    line = line.strip()
    l1.append(line)
    filename,wordcount = line.split('\t', 1)
    word,count = wordcount.split(' ', 1)
    count=int(count)
    if prev_filename == filename:
        N=N+count
    else:
       if prev_filename != None:
            df[prev_filename]=N
       N=0
       prev_filename = filename
df[prev_filename]=N


for h in l1:
    filename,wordcount = h.split('\t', 1)
    word,count = wordcount.split(' ', 1) 
    for k in df:
        if filename == k:
           wf=word+' '+filename
           nN=count+' '+str(df[k])
           print '%s\t%s' % (wf,nN)
    
