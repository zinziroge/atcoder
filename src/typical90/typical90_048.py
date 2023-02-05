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


def q_048_top():
    if DEBUG_OUT:
        q_048("""
4 3
4 3
9 5
15 8
8 6
"""[1:-1].split('\n'))

        q_048("""
2 2
7 6
3 2
"""[1:-1].split('\n'))

        q_048("""
10 12
987753612 748826789
36950727 36005047
961239509 808587458
905633062 623962559
940964276 685396947
959540552 928301562
60487784 37828572
953685176 482123245
87983282 66762644
912605260 709048491
"""[1:-1].split('\n'))
    else:
        q_048()


def q_048(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        n, k = list(map(int, input().split()))
        a_list = []
        b_list = []
        for _ in range(n):
            a, b = list(map(int, input().split()))
            a_list.append(a)
            b_list.append(b)
    else:
        print()
        n, k = list(map(int, user_input.pop(0).split()))
        a_list = []
        b_list = []
        for _ in range(n):
            a, b = list(map(int, user_input.pop(0).split()))
            a_list.append(a)
            b_list.append(b)
        
    # a_ary = np.array(a_list) # 満点
    # b_ary = np.array(b_list) # 部分点
    # c_ary = a_ary - b_ary # 部分点から満点で加点される点
    c_list = []
    for a, b in zip(a_list, b_list):
        c_list.append(a - b)
    
    ac_list = []
    ac_list.extend(b_list)
    ac_list.extend(c_list)
    ac_list = sorted(ac_list)
    ans = sum(ac_list[-k:])
    print(ans)


if __name__ == "__main__":
    q_048_top()
