# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:40:02 2020

@author: ayush
"""

def kangaroo(x1, v1, x2, v2):
    if (x1 < x2 and v1 < v2):
        return "No"
    else:
        if (v1!=v2) and (x2-x1)%(v1-v2)==0:
            return "Yes"
        else:
            return "No"

if __name__ == '__main__':

    x1V1X2V2 = input().split()

    x1 = int(x1V1X2V2[0])

    v1 = int(x1V1X2V2[1])

    x2 = int(x1V1X2V2[2])

    v2 = int(x1V1X2V2[3])

    result = kangaroo(x1, v1, x2, v2)
    
    print(result)