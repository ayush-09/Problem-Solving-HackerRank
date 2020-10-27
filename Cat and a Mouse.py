import math
import os
import random
import re
import sys


def catAndMouse(x, y, z):
    catA = abs(x - z)
    catB = abs(y - z)
    if catA == catB:
        return "Mouse C"
    elif catA < catB:
        return "Cat A"
    else:
        return "Cat B"

if __name__ == '__main__':
    
    q = int(input())

    for q_itr in range(q):
        xyz = input().split()

        x = int(xyz[0])

        y = int(xyz[1])

        z = int(xyz[2])

        result = catAndMouse(x, y, z)

        print(result + '\n')
