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


def q_078_top():
    if DEBUG_OUT:
        q_078(
            5, 5,
            [[1, 2],
            [1, 3],
            [3, 2],
            [5, 2],
            [4, 2],])
        q_078(
            2, 1,
            [[1, 2]])
        q_078(
            7, 18,
            [
            [7, 2],
            [1, 6],
            [5, 2],
            [1, 3],
            [7, 6],
            [5, 3],
            [5, 6],
            [5, 4],
            [1, 7],
            [2, 6],
            [3, 4],
            [5, 1],
            [4, 7],
            [4, 6],
            [5, 7],
            [3, 2],
            [4, 2],
            [1, 4],
            ])
    else:
        q_078()


def q_078(n=None, m=None, ab_list=None):
    if not DEBUG_OUT:
        n, m = list(map(int, input().split()))
        a_list, b_list = [], []
        for _ in range(m):
            a, b = list(map(int, input().split()))
            a_list.append(a)
            b_list.append(b)
    else:
        print()
        a_list, b_list = [], []
        for a, b in ab_list:
            a_list.append(a)
            b_list.append(b)

    """
    数字が小さいノードは探索範囲が狭い
    数字が大きい方から小さい方にリストを作る
    d = {3: [1, 2]}
    """

    edge_cnt = {}
    for a, b in zip(a_list, b_list):
        a, b = (b, a) if a > b else (a, b)  # a < b
        if edge_cnt.get(b):
            if edge_cnt.get(b).get(a):
                edge_cnt[b][a] = True
            else:
                edge_cnt[b][a] = True
        else:
            edge_cnt[b] = {}
            edge_cnt[b][a] = True
    
    if DEBUG_OUT:
        print(edge_cnt)

    n_cnt = 0
    for k, v in edge_cnt.items():
        if len(v) == 1:
            n_cnt += 1
    print(n_cnt)

if __name__ == "__main__":
    q_078_top()
