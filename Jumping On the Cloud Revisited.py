# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:11:11 2020

@author: ayush
"""

def jumpingOnClouds(c, k):
    e=100
    i=0
    while True:
        e=e-1-2*c[i]
        i=(i+k)%n
        if(i==0):
            break
    return e

if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))
