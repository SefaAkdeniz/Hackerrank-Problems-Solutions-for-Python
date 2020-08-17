# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:14:25 2020

@author: sefa
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    positiveCount=0
    negativeCount=0
    zeroCount=0
    totalCount=0

    for each in arr:
        totalCount+=1
        if each<0:
            negativeCount+=1
        elif each>0:
            positiveCount+=1
        else:
            zeroCount+=1

    print(positiveCount/totalCount)
    print(negativeCount/totalCount)
    print(zeroCount/totalCount)


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
