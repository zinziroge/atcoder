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


g_b = 0
g_a_list = []


def is_ok(arg):
    # 条件を満たすかどうか？問題ごとに定義
    global g_a_list, g_b
    return g_b >= g_a_list[arg]


def meguru_bisect(ng, ok):
    '''
    初期値のng,okを受け取り,is_okを満たす最小(最大)のokを返す
    まずis_okを定義すべし
    ng ok は  とり得る最小の値-1 とり得る最大の値+1
    最大最小が逆の場合はよしなにひっくり返す
    '''
    while (abs(ok - ng) > 1):
        mid = (ok + ng) // 2
        if is_ok(mid):
            ok = mid
        else:
            ng = mid
    return ok


def q_024_top():
    if DEBUG_OUT:
        q_024(
            2, 5,
            [1, 3],
            [2, 1],
        )
        q_024(
            3, 1,
            [7, 8, 9],
            [7, 8, 9],
        )
        q_024(
            7, 999999999,
            [3, 1, 4, 1, 5, 9, 2],
            [1, 2, 3, 4, 5, 6, 7],
        )
    else:
        q_024()


def q_024(n=None, k=None, a_list=None, b_list=None):
    if not DEBUG_OUT:
        n, k = list(map(int, input().split()))
        a_list = list(map(int, input().split()))
        b_list = list(map(int, input().split()))
    else:
        print()

    diff_list = []
    for a, b in zip(a_list, b_list):
        diff_list.append(abs(b - a))
    diff_sum = sum(diff_list)

    if k - diff_sum >= 0 and (k - diff_sum) % 2==0:
        # diff_sum 回操作して、残りk - diff_sum回は+,-を繰り返す
        print("Yes")
    else:
        print("No")
    
if __name__ == "__main__":
    q_024_top()
