#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    countBird=[0,0,0,0,0]
    
    for each in arr:
        countBird[each-1]+=1

    tempMaxCount=countBird[0]
    maxIndexBird=0
    for each in range(1,5):
        if countBird[each]>tempMaxCount:
            tempMaxCount=countBird[each]
            maxIndexBird=each

    return maxIndexBird+1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
