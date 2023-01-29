
from itertools import product
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


def q_C_top():
    if DEBUG_OUT:
        q_C(5, [2, 4, 4, 0, 2])
        q_C(7, [6, 4, 0, 2, 4, 0, 2])
        q_C(8, [7, 5, 1, 1, 7, 3, 5, 3])
    else:
        q_C()


def q_C(n=None, a_list=None):
    if not DEBUG_OUT:
        n = int(input())
        a_list = list(map(int, input().split()))
    a_cnt = collections.Counter(a_list)
    #print(a_cnt)

    if n%2==0:
        for a in a_cnt.keys():
            if a%2 == 0:
                # 偶数人でaが偶数
                print(0)
                return
    else:
        for a in a_cnt.keys():
            if a % 2 == 1:
                # 奇数人でaが奇数
                print(0)
                return

    for k, v in a_cnt.items():
        if k == 0 and v != 1:
            print(0)
            return
        elif k != 0 and v != 2:
            print(0)
            return

    m = 10**9 + 7
    nn = n//2
    ans = 2**nn % m
    print(ans)


if __name__ == "__main__":
    # q_A_top()
    # q_B_top()
    q_C_top()
    # q_D_top()
