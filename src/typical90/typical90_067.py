from itertools import product, combinations
import math
import random
import sys
import collections
from pathlib import Path
import bisect
import math

import numpy as np

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    DEBUG_OUT = True


def q_067_top():
    if DEBUG_OUT:
        #q_067(21, 1)
        #q_067(1330, 1)
        q_067(2311640221315, 15)
        q_067(0, 1)
        q_067(6, 1)
        q_067(7, 1)
        q_067(10, 1)
    else:
        q_067()


def q_067(n=None, k=None):
    if not DEBUG_OUT:
        n, k = list(input().split())
        n = f"{n}"
        k = int(k)
    else:
        print()
        n = f"{n}"
    
    n10 = 0
    for i in list(n):
        n10 = n10*8 + int(i)
    
    if n10==0:
        print("0")
        return

    for _ in range(k):
        n8 = 0
        s = ""
        while n10 >= 9:
            i = n10 % 9
            i = 5 if i==8 else i
            n10 = n10 // 9 
            s = f"{i}{s}"

        if not(n10==0):
            i = n10 % 9
            i = 5 if i==8 else i
            s = f"{i}{s}"
        
        n10 = 0
        for i in list(s):
            n10 = n10*8 + int(i)

    print(s)

if __name__ == "__main__":
    q_067_top()
