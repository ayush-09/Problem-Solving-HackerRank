# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:05:26 2020

@author: ayush
"""

def jumpingOnClouds(c):
    count = 0
    i = 0
    while i < len(c)-1:
        if i + 2 < len(c) and c[i+2] == 0:
            count += 1
            i += 2
        else:
            i += 1
            count += 1
    return count