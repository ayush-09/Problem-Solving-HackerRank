# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:40:48 2020

@author: ayush
"""

def pageCount(n, p):
    front = p//2
    if n%2==1:
        back = (n-p)//2
    else:
        back = (n-p+1)//2
    return min(front,back)
    # Write your code here.
    