#!/usr/bin/env python3

import sys
import re

def tofile(output):
    with open(output, "w") as to:
        for k,v in result.items():
            to.write("{} {}\n".format(k,v))


def arrange(a):
    tmp = {}
    for i in sorted(a):
        tmp[i] = a[i]
    return tmp

#I/O filenames extracted from sys argv

fileName = sys.argv[1]
output = sys.argv[2]

#Dictionary to append words
result = {}

# regex patter
pattern = '[^a-zA-Z]'


#open read file and remove unwanted chars
with open(fileName, "r") as text:
    for line in text:
        line = line.lower()
        line = re.sub(pattern, ' ', line)
        for word in line.split():
            if word not in result:
                result[word] = 1
            else:
                result[word] += 1


result = arrange(result)

tofile(output)

