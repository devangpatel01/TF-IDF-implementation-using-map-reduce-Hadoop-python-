#!/usr/bin/env python

import sys
import os


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    wf,nN=line.split('\t',1)
    w,f=wf.split(' ',1)
    z=f+' '+nN+' '+str(1)
    print '%s\t%s' % (w,z)

        
