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


def q_061_top():
    if DEBUG_OUT:
        q_061(
            6,
            [[1, 2],
             [1, 1],
             [2, 3],
             [3, 1],
             [3, 2],
             [3, 3],]
        )
        q_061(
            6,
            [[2, 1],
             [3, 1],
             [2, 2],
             [3, 1],
             [2, 3],
             [3, 1],]
        )
        q_061(
            6,
            [[1, 1000000000],
             [2, 200000000],
             [1, 30000000],
             [2, 4000000],
             [1, 500000],
             [3, 3], ]
        )
    else:
        q_061()


def q_061(q=None, tx_list=None):
    if not DEBUG_OUT:
        q = list(map(int, input().split()))[0]
        t_list = []
        x_list = []
        for _ in range(q):
            t, x = list(map(int, input().split()))
            t_list.append(t)
            x_list.append(x)
    else:
        print()
        t_list = []
        x_list = []
        for t, x in tx_list:
            t_list.append(t)
            x_list.append(x)

    yama = np.empty((q*2,), dtype=int)   # indexが若い方が上(index=0が一番上)
    si = q - 1
    ei = q
    for t, x in zip(t_list, x_list):
        if t==1:
            yama[si] = x
            si -= 1
        elif t==2:
            yama[ei] = x
            ei += 1
        elif t==3:
            print(yama[si + x, ])
    
    #yama = []
    #for t, x in zip(t_list, x_list):
    #    if t==1:
    #        yama = [x] + yama
    #    elif t==2:
    #        yama.append(x)
    #    elif t==3:
    #        print(yama[x - 1])


if __name__ == "__main__":
    q_061_top()
