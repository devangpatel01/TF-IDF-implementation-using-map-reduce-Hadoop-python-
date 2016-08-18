#!/usr/bin/env python

import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    wordfilename,count=line.split('\t',1)
    word,filename=wordfilename.split(' ',1)
    z=word+' '+count;
    print '%s\t%s' % (filename, z)
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        
