
from itertools import product
import random
import sys
import collections
from pathlib import Path

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    #DEBUG_OUT = True


def q_B_top():
    if DEBUG_OUT:
        q_B(
            *[2, 2],
            [
                [2, 0],
                [0, 0],
            ],
            [
                [-1, 0],
                [1, 0]
            ],
        )
        q_B(
            *[3, 4],
            [
                [10, 10],
                [-10, -10],
                [3, 3],
            ],
            [
                [1, 2],
                [2, 3],
                [3, 5],
                [3, 5]
            ]
        )
        q_B(
            *[5, 5],
            [
                [-100000000, -100000000],
                [-100000000, 100000000],
                [100000000, -100000000],
                [100000000, 100000000],
                [0, 0],
            ],
            [
                [0, 0],
                [100000000, 100000000],
                [100000000, -100000000],
                [-100000000, 100000000],
                [-100000000, -100000000],
            ],
        )
    else:
        q_B()


def q_B(n=None, m=None, sp_list=None, cp_list=None):
    if not DEBUG_OUT:
        n, m = list(map(int, input().split()))
        sp_list = []
        for _ in range(n):
            # student positions
            sp_list.append(list(map(int, input().split())))
        cp_list = []
        for _ in range(m):
            # check poits
            cp_list.append(list(map(int, input().split())))
    if False: #DEBUG_OUT:
        print(n, m)
        print(sp_list)
        print(cp_list)
        print()
    
    nearest_cp_list = []
    for sp in sp_list:
        j_min_cp = 0
        min_dist = 10**9
        for j, cp in enumerate(cp_list):
            dist = abs(sp[0] - cp[0]) + abs(sp[1] - cp[1])
            if dist < min_dist:  # <= はだめ
                min_dist = dist
                j_min_cp = j
        nearest_cp_list.append(j_min_cp)
    for i in nearest_cp_list:
        print(i + 1)





def q_C_top():
    if DEBUG_OUT:
        q_C("aca", "accc", "ca")
        q_C("abcb", "aacb", "bccc")
    else:
        q_C()


def q_C(sa=None, sb=None, sc=None):
    if not DEBUG_OUT:
        n = input()
        a_list = list(map(int, input().split()))


if __name__ == "__main__":
    # q_A_top()
    q_B_top()
    # q_C_top()
    # q_D_top()
