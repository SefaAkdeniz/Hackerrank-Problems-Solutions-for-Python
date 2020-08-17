# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 10:35:00 2020

@author: sefa
"""

#!/bin/python3

import os

def simpleArraySum(ar):
    total=0
    for each in ar:
        total=total+each

    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = simpleArraySum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
