from itertools import product, combinations
import math
import random
import sys
import collections
from pathlib import Path
import bisect

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


def q_010_top():
    if DEBUG_OUT:
        q_010(
            7,
            [
            [1, 72],
            [2, 78],
            [2, 94],
            [1, 23],
            [2, 89],
            [1, 40],
            [1, 75],
            ],
            1,
            [[2, 6]]
        )
        q_010(
            20,
            [
                [2, 90],
                [1, 67],
                [2, 9],
                [2, 17],
                [2, 85],
                [2, 43],
                [2, 11],
                [1, 32],
                [2, 16],
                [1, 19],
                [2, 65],
                [1, 14],
                [1, 51],
                [2, 94],
                [1, 4],
                [1, 55],
                [2, 90],
                [1, 89],
                [1, 35],
                [2, 81],
            ],
            20,
            [
                [3 ,17],
                [5 ,5],
                [11, 11],
                [8 ,10],
                [3 ,13],
                [2 ,6],
                [3 ,7],
                [3 ,5],
                [12, 18],
                [4 ,8],
                [3 ,16],
                [6 ,8],
                [3 ,20],
                [1 ,12],
                [1 ,6],
                [5 ,16],
                [3 ,10],
                [17, 19],
                [4 ,4],
                [7 ,15],
            ]
        )

    else:
        q_010()


def q_010(n=None, cp_list=None, q=None, lr_list=None):
    if not DEBUG_OUT:
        n = list(map(int, input().split()))[0]
        c_list = []
        p_list = []
        for _ in range(n):
            c, p = list(map(int, input().split()))
            c_list.append(c)
            p_list.append(p)
        
        q = list(map(int, input().split()))[0]
        l_list = []
        r_list = []
        for _ in range(q):
            l, r =list(map(int, input().split()))
            l_list.append(l)
            r_list.append(r)
    else:
        c_list = []
        p_list = []
        for c, p in cp_list:
            c_list.append(c)
            p_list.append(p)

        l_list = []
        r_list = []
        for l, r in lr_list:
            l_list.append(l)
            r_list.append(r)
        del lr_list, cp_list 
        print()

    c1_ruisekiwa = [0]
    c2_ruisekiwa = [0]
    for c, p in zip(c_list, p_list):
        if c==1:
            c1_ruisekiwa.append(c1_ruisekiwa[-1] + p)
            c2_ruisekiwa.append(c2_ruisekiwa[-1])
        else:
            c1_ruisekiwa.append(c1_ruisekiwa[-1])
            c2_ruisekiwa.append(c2_ruisekiwa[-1] + p)

    for l, r in zip(l_list, r_list):
        c1_sum = c1_ruisekiwa[r] - c1_ruisekiwa[l-1]
        c2_sum = c2_ruisekiwa[r] - c2_ruisekiwa[l-1]
        print(c1_sum, c2_sum)

        """
        c_sub_list = c_list[l - 1: r - 1 + 1]
        p_sub_list = p_list[l - 1: r - 1 + 1]
        c_sum = sum(p_sub_list)

        if 1 in c_sub_list and 2 in c_sub_list:
            i_c1_min, i_c1_max = c_sub_list.index(1), len(c_sub_list) - c_sub_list[::-1].index(1) + 1
            i_c2_min, i_c2_max = c_sub_list.index(2), len(c_sub_list) - c_sub_list[::-1].index(2) + 1

            if i_c1_max - i_c1_min < i_c2_max - i_c2_min:
                c1_sum = 0
                for c, p in zip(c_sub_list[i_c1_min:i_c1_max+1], p_sub_list[i_c1_min: i_c1_max+1]):
                    if c==1:
                        c1_sum += p
                print(c1_sum, c_sum - c1_sum)
            else:
                c2_sum = 0
                for c, p in zip(c_sub_list[i_c2_min:i_c2_max+1], p_sub_list[i_c2_min: i_c2_max+1]):
                    if c==2:
                        c2_sum += p
                print(c_sum - c2_sum, c2_sum)
        elif 1 in c_sub_list and not (2 in c_sub_list):
            print(c_sum, 0)
        else:
            print(0, c_sum)
        """

        ## sum of c1
        #for c, p in zip(c_list[l - 1: r - 1 + 1], p_list[l-1: r - 1 + 1]):
        #    if c==1:
        #        c1_sum += p
        #c2_sum = c_sum - c1_sum
        #print(c1_sum, c2_sum)


if __name__ == "__main__":
    q_010_top()
