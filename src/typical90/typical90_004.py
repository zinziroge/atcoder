from itertools import product, combinations
import math
import random
import sys
import collections
from pathlib import Path
import numpy as np

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    #DEBUG_OUT = True


def q_004_top():
    if DEBUG_OUT:
        q_004(
            4, 4,
            [[3, 1, 4, 1,],
             [5, 9, 2, 6,],
             [5, 3, 5, 8,],
             [9, 7, 9, 3,],],
        )
    else:
        q_004()


def q_004(h=None, w=None, a_list=None):
    if not DEBUG_OUT:
        h, w = list(map(int, input().split()))
        a_list = []
        for _ in range(h):
            a = list(map(int, input().split()))
            a_list.append(a)
    else:
        print()

    a_ary = np.array(a_list)
    ans_ary = np.empty_like(a_ary)

    w_sum = np.sum(a_ary, axis=0) 
    h_sum = np.sum(a_ary, axis=1) 

    for _h in range(h):
        for _w in range(w):
            ans_ary[_h, _w] = h_sum[_h] + w_sum[_w] - a_ary[_h, _w]
        s = " ".join([str(i) for i in ans_ary[_h, :].tolist()])
        print(s)
    #print(ans_ary)


if __name__ == "__main__":
    q_004_top()
