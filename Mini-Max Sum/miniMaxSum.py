# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:46:25 2020

@author: sefa
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    print(str(sum(arr[:4])),str(sum(arr[-4:])))

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
