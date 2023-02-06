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


def q_034_top():
    if DEBUG_OUT:
        q_034("""
5 1
1 2 3 4 5
"""[1:-1].split('\n'))

        q_034("""
5 4
1 1 2 4 2
"""[1:-1].split('\n'))

        q_034("""
10 2
1 2 3 4 4 3 2 1 2 3
"""[1:-1].split('\n'))
    else:
        q_034()


def q_034(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        n, k = list(map(int, input().split()))
        a_list = list(map(int, input().split()))
    else:
        print()
        n, k = list(map(int, user_input.pop(0).split()))
        a_list = list(map(int, user_input.pop(0).split()))

    # 尺取り法
    sp = 0
    ep = 1
    len_longest = 0
    ccnt = {}
    ccnt[a_list[sp]] = 1
    # a_part = a_list[sp:ep]

    while True:
        len_ccnt = len(ccnt.keys())

        if len_ccnt <= k:
            if len_longest < (ep - sp):
                len_longest = (ep - sp)

            if ccnt.get(a_list[ep]):
                ccnt[a_list[ep]] += 1
            else:
                ccnt[a_list[ep]] = 1

            # 終端を伸ばす
            ep += 1

            # 終端がa_listを越えたら終了
            if ep == len(a_list):
                # ここが汚い
                len_ccnt = len(ccnt.keys())
                if len_ccnt <= k:
                    if len_longest < (ep - sp):
                        len_longest = (ep - sp)

                break
        elif len_ccnt > k:
            # 要素の種類が多すぎるので減らす
            ccnt[a_list[sp]] -= 1
            if ccnt[a_list[sp]] == 0:
                del(ccnt[a_list[sp]])
            sp += 1

    print(len_longest)

    
if __name__ == "__main__":
    q_034_top()
