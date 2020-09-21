# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 13:00:59 2020

@author: ayush
"""

import math
import os
import random
import re
import sys

# Complete the permutationEquation function below.
def permutationEquation(p):
    r=[]
    n=len(p)
    for i in range(1,n+1):
        r.append(p.index(p.index(i)+1)+1)
    return r
