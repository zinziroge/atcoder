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


def q_033_top():
    if DEBUG_OUT:
        q_033(2, 3)
        q_033(3, 4)
        q_033(3, 6)  # 6
        q_033(4, 4)  # 4
        q_033(4, 5)  # 6
        q_033(5, 4)  # 6
        q_033(5, 5)  # 9
        q_033(1, 4)  # 4
        q_033(1, 5)  # 5
        q_033(4, 1)  # 4
        q_033(5, 1)  # 5
    else:
        q_033()


def q_033(h=None, w=None):
    if not DEBUG_OUT:
        h, w = list(map(int, input().split()))
    else:
        print()
    
    h2 = h//2
    w2 = w//2
    h_mod = h % 2
    w_mod = w % 2
    
    """
    #.     #. #
    .. --- .. .
    
    --

    #.     #. #
    ..     .. .

    #. --- #. #
    """
    if h==1:
        print(w)
    elif w==1:
        print(h)
    else:
        n = h2 * w2 + (h_mod * w2) + (w_mod * h2) + h_mod * w_mod
        print(n)


if __name__ == "__main__":
    q_033_top()
