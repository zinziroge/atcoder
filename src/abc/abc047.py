
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


def q_B_top():
    if DEBUG_OUT:
        q_B(
            *[5, 4, 2],
            [[2, 1, 1],
             [3, 3, 4], ],
        )
        q_B(
            *[5, 4, 3],
            [
                [2, 1, 1],
                [3, 3, 4],
                [1, 4, 2],
            ]
        )
        q_B(
            *[10, 10, 5],
            [
                [1, 6, 1],
                [4, 1, 3],
                [6, 9, 4],
                [9, 4, 2],
                [3, 1, 3],
            ]
        )
    else:
        q_B()


def q_B(w=None, h=None, n=None, xya_list=None):
    if not DEBUG_OUT:
        w, h, n = list(map(int, input().split()))
        xya_list = []
        for _ in range(n):
            xya_list.append(list(map(int, input().split())))
    if DEBUG_OUT:
        print()

    block = np.ones((h, w), dtype=int)
    for xya in xya_list:
        x, y, a = xya
        if a == 1:
            block[:, :x] = 0
        elif a == 2:
            block[:, x:] = 0
        elif a == 3:
            block[:y, :] = 0
        else:
            block[y:, :] = 0

    if DEBUG_OUT:
        print(block[::-1, :])
    print(np.sum(block))



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
