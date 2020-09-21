from collections import Counter
def sockMerchant(n, ar):
    c=0
    for i in Counter(ar).values():
        c+=i//2
    return c