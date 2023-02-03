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


def q_022_top():
    if DEBUG_OUT:
        q_022(2, 2, 3)
        q_022(2, 2, 4)
        q_022(1000000000000000000, 999999999999999999, 999999999999999998)

    else:
        q_022()


def q_022(a=None, b=None, c=None):
    if not DEBUG_OUT:
        a, b, c = list(map(int, input().split()))
    else:
        print()
    
    # 立方体の一辺の長さをxとする
    # min(a,b,c) >= x
    # a = x*na, b = x*nb, c = x*nc
    # xはa,b,cの最大公約数
    # n = na + nb + nc = a/x + b/x + c/x
    gcd_abc = math.gcd(math.gcd(a, b), c)
    if DEBUG_OUT:
        print(gcd_abc)
    n = (a // gcd_abc) + (b // gcd_abc) + (c // gcd_abc) - 3
    print(int(n))

    # 2999999999999999994
    # 3000000000000000000

if __name__ == "__main__":
    q_022_top()
