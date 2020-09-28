# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:40:21 2020

@author: ayush
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
    left=right=0
    for i in range(n):
        left+=arr[i][i]
        right+=arr[i][n-1-i]
    return abs(left - right)
    # Write your code here

if __name__ == '__main__':

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    print(result)

