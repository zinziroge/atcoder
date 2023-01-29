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


def q_007_top():
    if DEBUG_OUT:
        q_007(
            4,
            [4000, 4400, 5000, 3200],
            3,
            [3312, 2992, 4229],
        )
        q_007(
            1,
            [4000],
            10,
            [3582, 3538, 3320, 3312, 3296, 3257, 3111, 3040, 3013, 2994,],
        )
        q_007(
            10,
            [869120000, 998244353, 777777777, 123456789, 100100100, 464646464, 987654321, 252525252, 869120001, 1000000000],
            10,
            [4229, 20210406, 1, 268435456, 3582, 536870912, 1000000000, 869120, 99999999, 869120001,]
        )
        q_007(
            100,
            [298750376, 229032640, 602876667, 944779015, 909539868, 533609371, 231368330, 445484152,
             408704870, 850216874, 349286798,  30417810, 807260002, 554049450,  40706045, 380488344,
             749325840, 801881841, 459457853,  66691229,   5235900,   8100458,  46697277, 997429858,
             827651689, 790051948, 981897272, 271364774, 536232393, 997361572, 449659237, 602191750,
             294800444, 346669663, 792837293, 277667068, 997282249, 468293808, 444906878, 702693341,
             894286137, 845317003,  27053625, 926547765, 739689211, 447395911, 902031510, 326127348,
             582956343, 842918193, 235655766, 844300842, 438389323, 406413067, 862896425, 464876303,
              68833418,  76340212, 911399808, 745744264, 551223563, 854507876, 196296968,  52144186,
             431165823, 275217640, 424495332, 847375861, 337078801,  83054466, 648322745, 694789156,
             301518763, 319851750, 432518459, 772897937, 630628124, 581390864, 313132255, 350770227,
             642944345, 677742851, 448945480, 688009163, 160941957, 290297295,   5532462, 823543277,
              19634445,  15791361, 193309093,  66202596,  72364149, 743270896, 297240520, 264035189,
             898589962,  59916738, 307942952, 403411309],
            30,
            [930579110, 22697034, 44652533, 280533771, 753567118, 684927419, 923477579, 557613803, 
             779616458, 389130756, 323671659, 3117850, 408004003, 224808850, 18421958, 359047808, 
             364572866, 334631363, 854759331, 647435074, 826055423, 668443532, 620408208, 32237184, 
             67299071, 251185742, 217292659, 16181227, 850865411, 218577687,],
        )
        q_007(
            5,
            [10,10,10,10,10],
            5,
            [10,11,9,12]
        )
        q_007(
            5,
            [10,10,11,11,11],
            5,
            [10,11,9,12]
        )

    else:
        q_007()


def q_007(n=None, a_list=None, q=None, b_list=None):
    if not DEBUG_OUT:
        n = list(map(int, input().split()))[0]
        a_list = list(map(int, input().split()))
        q = list(map(int, input().split()))[0]
        b_list = []
        for _ in range(q):
            b = list(map(int, input().split()))[0]
            b_list.append(b)
    else:
        print()

    a_list = sorted(a_list)
    for b in b_list:
        i = bisect.bisect_left(a_list, b)
        if DEBUG_OUT:
            print(i, "",  end="")
        if i==0:
            print(abs(a_list[0] - b))
        elif i == len(a_list):
            print(abs(a_list[-1] - b))
        else:
            print(
                min(abs(a_list[i-1] - b), abs(a_list[i] - b), )
            )

    # global g_a_list
    # global g_b
    # g_a_list = sorted(a_list)
    # g_a_list = [g_a_list[0] - 1] + g_a_list + [g_a_list[-1] + 1]
    # for b in b_list:
    #     g_b = b
    #     i = meguru_bisect(ok=0, ng=len(g_a_list) - 1)
    #     if i==0:
    #         print(abs(g_a_list[1] - b))
    #     elif i==len(g_a_list) - 1:
    #         print(abs(g_a_list[-2] - b))
    #     else:
    #         print(
    #             min(
    #                 abs(g_a_list[i] - b), 
    #                 abs(g_a_list[i+1] - b), 
    #             )
    #         )

    #b_list = sorted(b_list)
    #a_ary = np.array(a_list)
    #min_diff_list = []
    #for b in b_list:
    #    diff_abs_ary = np.abs(a_ary - np.array([b] * n))
    #    min_diff = np.min(diff_abs_ary)
    #    min_diff_list.append(min_diff)
    #
    #print("\n".join([str(i) for i in min_diff_list]))


if __name__ == "__main__":
    q_007_top()
