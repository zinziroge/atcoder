
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
    DEBUG_OUT = True


def q_E_top():
    if DEBUG_OUT:
        """
        q_E(
            9, 3,
            [
                [8, 3],
                [4, 2],
                [2, 1],
            ]
        )
        q_E(
            100, 6,
            [
                [1, 1],
                [2, 3],
                [3, 9],
                [4, 27],
                [5, 81],
                [6, 243],
            ]
        )
        """
        q_E(
            9999, 10,
            [
                [540, 7550],
                [691, 9680],
                [700, 9790],
                [510, 7150],
                [415, 5818],
                [551, 7712],
                [587, 8227],
                [619, 8671],
                [588, 8228],
                [176, 2461],
            ]
        )
    else:
        q_E()


def q_E(h=None, n=None, ab_list=None):
    if not DEBUG_OUT:
        h, n = list(map(int, input().split()))
        a_list = []
        b_list = []
        for _ in range(n):
            a, b = list(map(int, input().split()))
            a_list.append(a)
            b_list.append(b)
    else:
        a_list = []
        b_list = []
        for a, b in ab_list:
            a_list.append(a)
            b_list.append(b)

    cp = []  # cost performance
    for a, b in zip(a_list, b_list):
        cp.append(a / b)

    b_used = 0
    while True:
        i_most_cp_magic = cp.index(max(cp))

        # 最高のcost performanceの魔法1回でh<=0になるなら終わり
        if h - a_list[i_most_cp_magic] <= 0:
            b_used += b_list[i_most_cp_magic]
            break

        # そうでないなら、最高のcost performanceの魔法でとにかく減らす
        b_used += b_list[i_most_cp_magic] * (h // a_list[i_most_cp_magic])
        h = h % a_list[i_most_cp_magic]
        if h==0:
            break

        # update cp table
        for i in range(n):
            if h < a_list[i]:
                # cost performanceが下がる
                cp[i] = h / b_list[i]

    print(b_used)




if __name__ == "__main__":
    # q_A_top()
    # q_B_top()
    # q_C_top()
    # q_D_top()
    q_E_top()
