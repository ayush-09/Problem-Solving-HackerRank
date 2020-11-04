import math
import os
import random
import re
import sys
from collections import Counter
def pickingNumbers(a):
    arr= Counter(a)
    m=0
    for i in range(100):
        m = max(m,arr[i]+arr[i+1])
    return m
            
    # Write your code here

if __name__ == '__main__':
    
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    print(str(result) + '\n')

