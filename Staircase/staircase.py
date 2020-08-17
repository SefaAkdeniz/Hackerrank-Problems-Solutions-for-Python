# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 11:27:41 2020

@author: sefa
"""


#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    
    for i in range(n):
        string= " "
        for j in range(n):
            if j>i:
                string+=' '
            else:
                string+= '#'
                
        print(string[::-1])
            

if __name__ == '__main__':
    n = int(input())

    staircase(n)
