# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:23:31 2020

@author: ayush
"""

def migratoryBirds(arr):
    l = [0] * len(arr)
    for i in range(len(arr)):
        l[arr[i]] += 1
    return l.index(max(l))