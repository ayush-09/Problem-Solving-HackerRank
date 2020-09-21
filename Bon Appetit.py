# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 10:34:03 2020

@author: ayush
"""

def bonAppetit(bill, k, b):
    s = sum(bill)
    charges = (s - bill[k])//2
    if charges == b:
        print("Bon Appetit")
    else:
        print(b-charges)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)