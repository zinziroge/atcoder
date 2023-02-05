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
    # DEBUG_OUT = True


def q_044_top():
    if DEBUG_OUT:
        q_044("""
8 5
6 17 2 4 17 19 1 7
2 0 0
1 7 2
1 2 6
1 4 5
3 4 0
"""[1:-1].split('\n'))

        q_044("""
9 6
16 7 10 2 9 18 15 20 5
2 0 0
1 1 4
2 0 0
1 8 5
2 0 0
3 6 0
"""[1:-1].split('\n'))

        q_044("""
11 18
23 92 85 34 21 63 12 9 81 44 96
3 10 0
3 5 0
1 3 4
2 0 0
1 4 11
3 11 0
1 3 5
2 0 0
2 0 0
3 9 0
2 0 0
3 6 0
3 10 0
1 6 11
2 0 0
3 10 0
3 4 0
3 5 0
"""[1:-1].split('\n'))
    else:
        q_044()


def q_044(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        n, q = list(map(int, input().split()))
        a_list = list(map(int, input().split()))
        txy_list = []
        for _ in range(q):
            txy = list(map(int, input().split()))
            txy_list.append(txy)
    else:
        print()
        n, q = list(map(int, user_input.pop(0).split()))
        txy_list = []
        a_list = list(map(int, user_input.pop(0).split()))
        for _ in range(q):
            txy = list(map(int, user_input.pop(0).split()))
            txy_list.append(txy)
        
    # listだと遅いので配列にする
    a_ary = np.array(a_list, dtype=int)
    a_len = a_ary.shape[0]
    offset = 0  # 配列自体はシフトせず、ポインタだけずらす
    # x, y は1オリジンだが、配列は0オリジン
    for t, x, y in txy_list:
        if t == 1:
            a_ary[(x + offset - 1) % a_len], a_ary[(y + offset - 1) % a_len] = \
                a_ary[(y + offset - 1) % a_len], a_ary[(x + offset - 1) % a_len]
        elif t == 2:
            offset = offset - 1
        else:
            print(a_ary[x + offset - 1])
        if DEBUG_OUT:
            print(offset, a_ary)


if __name__ == "__main__":
    q_044_top()
