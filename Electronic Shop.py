import os
import sys
def getMoneySpent(keyboards, drives, b):
    maxamount = -1
    for keyboard in keyboards:
        for drive in drives:
            if keyboard+drive <= b:
                maxamount = max(maxamount,keyboard+drive)
    return maxamount


if __name__ == '__main__':

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))
    
    moneySpent = getMoneySpent(keyboards, drives, b)

    print(str(moneySpent) + '\n')


