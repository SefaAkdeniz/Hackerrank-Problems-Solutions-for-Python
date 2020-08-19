# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 15:00:41 2020

@author: sefa
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    maxHeight=max(ar)
    response=0

    for each in ar:
        if each == maxHeight:
            response+=1

    return response

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
