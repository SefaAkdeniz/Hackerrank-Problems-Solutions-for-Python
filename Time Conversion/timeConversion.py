#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    last_2_character = s[-2:]
    hour, minute, second = s[:-2].split(":")

    if last_2_character == 'AM' and hour=='12':
        hour='00'
    if last_2_character == 'PM' and hour!='12':
        hour=str(int(hour)+12)

    time= hour+':'+minute+':'+second
    return time

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
