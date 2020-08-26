# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 15:46:21 2020

@author: sefa
"""


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    final_grade=[]
    for grade in grades:
        if grade<38:
            print(grade)
            final_grade.append(grade)
        elif grade%5<3:
            print(grade)
            final_grade.append(grade)
        else:
            rounded=grade
            while(1):
                rounded+=1
                if rounded%5==0:
                    break
            final_grade.append(rounded)
            print(rounded)

    return final_grade
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
