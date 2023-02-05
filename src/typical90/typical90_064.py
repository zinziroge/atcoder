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
    #DEBUG_OUT = True

large_prime_num = 10**9 + 7


def q_064_top():
    if DEBUG_OUT:
        q_064("""
3 3
1 2 3
2 3 1
1 2 -1
1 3 2
"""[1:-1].split('\n'))

        q_064("""
20 10
61 51 92 -100 -89 -65 -89 -64 -74 7 87 -2 51 -39 -50 63 -23 36 74 37
2 2 -45
6 19 82
2 9 36
7 13 71
16 20 90
18 20 -24
14 17 -78
10 11 -55
7 19 -26
20 20 -7
"""[1:-1].split('\n'))

    else:
        q_064()


def q_064(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        n, q = list(map(int, input().split()))
        a_list = list(map(int, input().split()))
        lrv_list = []
        for _ in range(q):
            lrv = list(map(int, input().split()))
            lrv_list.append(lrv)
    else:
        print()
        n, q = list(map(int, user_input.pop(0).split()))
        a_list = list(map(int, user_input.pop(0).split()))
        lrv_list = []
        for _ in range(q):
            lrv = list(map(int, user_input.pop(0).split()))
            lrv_list.append(lrv)
    
    diff_list = [0]  # indexは1から使う
    # diff_list[1] は 1と2の差分
    for i, v in enumerate(a_list[:-1]):
        diff_list.append(a_list[i + 1] - v)
    fuben = sum(map(abs, diff_list))
    
    for lrv in lrv_list:
        l, r, v = lrv
        if l - 1 > 0:
            fuben = fuben - abs(diff_list[l - 1])
            diff_list[l - 1] += v
            fuben = fuben + abs(diff_list[l - 1])
        if r < len(diff_list):
            fuben = fuben - abs(diff_list[r])
            diff_list[r] -= v
            fuben = fuben + abs(diff_list[r])
        print(fuben)


if __name__ == "__main__":
    q_064_top()
