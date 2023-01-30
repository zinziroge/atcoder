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


def q_027_top():
    if DEBUG_OUT:
        q_027(
            5,
            ["e869120",
             "atcoder",
             "e869120",
             "square1001",
             "square1001",]
        )
        q_027(
            4,
            ["taro",
             "hanako",
             "yuka",
             "takashi",]
        )
        q_027(
            10,
            ["square869120",
             "square869120",
             "square869120",
             "square869120",
             "square869120",
             "square869120",
             "square869120",
             "square869120",
             "square869120",
             "square869120",]
        )

    else:
        q_027()


def q_027(n=None, s_list=None):
    if not DEBUG_OUT:
        n = list(map(int, input().split()))[0]
        s_list = []
        for _ in range(n):
            s_list.append(input())
    else:
        print()
    
    users = {}
    for i, s in enumerate(s_list):
        if not users.get(s):
            users[s] = True
            print(i + 1)

    # ccnt = collections.Counter(s_list)
    # for k, v in ccnt.items():
    #     print(s_list.index(k) + 1)

    
if __name__ == "__main__":
    q_027_top()
