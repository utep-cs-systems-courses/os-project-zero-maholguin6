#!/usr/bin/env python3

import sys
import re

def tofile(output, result):
    """
    Writes  result to file
    """

    with open(output, "w") as file:
        for k,v in result.items():
            file.write("{} {}\n".format(k,v))


def arrange(a):
    """
    Arrange Dictionary alphabetically
    """

    tmp = {}
    for i in sorted(a):
        tmp[i] = a[i]
    return tmp


def cleanify(filename):
    """
    Clean textfile and save it in a Dictionary
    """

    result = {}
    unwanted = '[^a-zA-Z]'

    with open(filename, "r") as text:
        for line in text:
            line = line.lower()
            line = re.sub(unwanted, ' ', line)
            for word in line.split():
                if word not in result:
                    result[word] = 1
                else:
                    result[word] += 1
    
    return result

#I/O filenames extracted from sys argv

fromFile = sys.argv[1]
toFile = sys.argv[2]

t = cleanify(fromFile)
result = arrange(t)
tofile(toFile, result)

