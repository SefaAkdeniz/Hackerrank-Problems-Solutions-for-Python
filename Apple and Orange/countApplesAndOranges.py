# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 15:47:56 2020

@author: sefa
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    appleCount=0
    for apple in apples:
        if s<= apple+a <= t:
            appleCount+=1
    orangeCount=0
    for orange in oranges:
        if s<= orange+b <= t:
            orangeCount+=1
    print(appleCount)
    print(orangeCount)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)