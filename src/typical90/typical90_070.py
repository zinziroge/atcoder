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


def q_070_top():
    if DEBUG_OUT:
        q_070("""
2
-1 2
1 1
"""[1:-1].split('\n'))

        q_070("""
2
1 0
0 1
"""[1:-1].split('\n'))

        q_070("""
5
2 5
2 5
-3 4
-4 -8
6 -2
"""[1:-1].split('\n'))

        q_070("""
4
1000000000 1000000000
-1000000000 1000000000
-1000000000 -1000000000
1000000000 -1000000000
"""[1:-1].split('\n'))
    else:
        q_070()


def calc_fuben(factory_ary, psup_x):
    d_ary = factory_ary - psup_x
    fuben = np.sum(np.abs(d_ary))
    return fuben


def q_070(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        n = list(map(int, input().split()))[0]
        x_list = []
        y_list = []
        for _ in range(n):
            x, y = list(map(int, input().split()))
            x_list.append(x)
            y_list.append(y)
    else:
        print()
        n = list(map(int, user_input.pop(0).split()))[0]
        x_list = []
        y_list = []
        for _ in range(n):
            x, y = list(map(int, user_input.pop(0).split()))
            x_list.append(x)
            y_list.append(y)
    
    x_list = sorted(x_list)
    y_list = sorted(y_list)

    factory_ary = np.array([x_list, y_list], dtype=np.int64).T

    fuben_xy = 0
    # 左に1動くと、左にある点の数m だけ近くなり、右にある点の数n-mだけ遠くなる
    # 移動することで左右の点の数が変化するのでどこかで最小値がある
    # 二分探索で移動して、不便度が増えたら逆方向に戻る
    for i_xy in range(2):  # x,y
        factory_ary_x = factory_ary[:, i_xy]
        ballance_x = factory_ary_x.shape[0] // 2
        if factory_ary_x.shape[0] % 2 == 0:
            psup_x = (factory_ary_x[ballance_x - 1] + factory_ary_x[ballance_x]) / 2
        else:
            psup_x = factory_ary_x[ballance_x]
        
        dist_x = np.abs(factory_ary_x - psup_x)
        fuben_xy += np.sum(dist_x)

        if DEBUG_OUT:
            print(dist_x, psup_x, ballance_x)
    print(int(fuben_xy))

    """
    for i_xy in range(2):  # x,y
        # optimize x or y
        min_fuben = 10**16  #10**9 * 2 * 10**5
        factory_ary_x = factory_ary[:, i_xy]
        min_x, max_x = np.min(factory_ary_x), np.max(factory_ary_x)
        psup_x = (min_x + max_x) // 2
        sft_x = int((max_x - psup_x) / 2 + 0.5)

        if DEBUG_OUT:
            print(sft_x, psup_x, min_fuben, )
            print(f"{'xy'[i_xy]}")
        while True:
            fuben_p = calc_fuben(factory_ary_x, psup_x + sft_x)
            fuben_m = calc_fuben(factory_ary_x, psup_x - sft_x)
            next_fuben = min([fuben_p, fuben_m])

            # update min of fuben
            if min_fuben > next_fuben:
                min_fuben = next_fuben

            # update factory xy
            if next_fuben == fuben_p:
                psup_x += sft_x
            elif next_fuben == fuben_m:
                psup_x += -sft_x

            if sft_x == 1:
                break
            #sft_x = sft_x // 2
            sft_x = int(sft_x / 2 + 0.5)


            if DEBUG_OUT:
                print(sft_x, psup_x, min_fuben, )

        if DEBUG_OUT:
            print(sft_x, psup_x, min_fuben, )
        fuben_xy += min_fuben
    """

    
if __name__ == "__main__":
    q_070_top()
