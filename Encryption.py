import math
import os
import random
import re
import sys
from math import *
# Complete the encryption function below.
def encryption(s):
    n=len(s)
    l= floor(sqrt(n))
    c=ceil(sqrt(n))
    r=[]
    for i in range(c):
        t=[]
        j=0
        while i+j<n:
            t.append(s[i+j])
            j+=c
        r.append("".join(t))
    return " ".join(r)


if __name__ == '__main__':

    s = input()

    result = encryption(s)

    print(result)