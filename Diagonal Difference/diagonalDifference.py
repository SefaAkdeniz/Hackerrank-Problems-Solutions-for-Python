# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 10:56:53 2020

@author: sefa
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    primaryDiagonal=0
    secondaryDiagonal=0
    for i in range(len(arr)):
        primaryDiagonal+=arr[i][i]
        secondaryDiagonal+=arr[i][len(arr)-i-1]
    
    return abs(primaryDiagonal-secondaryDiagonal)
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
