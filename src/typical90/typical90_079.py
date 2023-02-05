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


def q_079_top():
    if DEBUG_OUT:
        q_079("""
3 3
0 0 0
0 0 0
0 0 0
1 1 0
1 1 0
0 0 0
"""[1:-1].split('\n'))

        q_079("""
3 3
0 0 0
0 0 0
0 0 0
0 0 0
0 1 0
0 0 0
"""[1:-1].split('\n'))

        q_079("""
5 5
6 17 18 29 22
39 50 25 39 25
34 34 8 25 17
28 48 25 47 42
27 47 24 32 28
4 6 3 29 28
48 50 21 48 29
44 44 19 47 28
4 49 46 29 28
4 49 45 1 1
"""[1:-1].split('\n'))
    else:
        q_079()


def q_079(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        h, w = list(map(int, input().split()))
        a_list = []
        b_list = []
        for _ in range(h):
            _a = list(map(int, input().split()))
            a_list.append(_a)
        for _ in range(h):
            _b = list(map(int, input().split()))
            b_list.append(_b)
    else:
        print()
        h, w = list(map(int, user_input.pop(0).split()))
        a_list = []
        b_list = []
        for _ in range(h):
            _a = list(map(int, user_input.pop(0).split()))
            a_list.append(_a)
        for _ in range(h):
            _b = list(map(int, user_input.pop(0).split()))
            b_list.append(_b)

    a_ary = np.array(a_list)
    b_ary = np.array(b_list)

    diff_ary = b_ary - a_ary
    diff_sum = np.sum(diff_ary)

    if diff_sum % 4 == 0:
        print("Yes")
    else:
        print("No")
        return

    # Yes case:
    # +操作するとdiff_sumが-4され、-操作するとdiff_sumbが+4される

    
if __name__ == "__main__":
    q_079_top()
