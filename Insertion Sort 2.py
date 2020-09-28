# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 10:44:12 2020

@author: ayush
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the insertionSort2 function below.
def insertionSort2(n, arr):
    n=len(arr)
    for i in range(1,n):
        key = arr[i] 
  
        # Move elements of arr[0..i-1], that are 
        # greater than key, to one position ahead 
        # of their current position 
        j = i-1
        while j >=0 and key < arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key
        for i in range(n): 
            print ("%d" %arr[i],end=" ")
        print()

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    insertionSort2(n, arr)
