# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 12:56:49 2020

@author: ayush
"""

def countingValleys(n, s):
    v=l=0
    d={'U':1,'D':-1}
    for step in s:
        l+=d[step]
        if l==0 and step=='U':
            v+=1
    return v
