# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:05:32 2020

@author: sefa
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    pointArray=[0,0]
    for i in range(len(a)):
        if a[i]<b[i]:
            pointArray[1]=pointArray[1]+1
        elif a[i]>b[i]:
            pointArray[0]=pointArray[0]+1
    return pointArray

    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
