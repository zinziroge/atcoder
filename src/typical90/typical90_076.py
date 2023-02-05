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

large_prime_num = 10**9 + 7


def combinations_count(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))


def q_076_top():
    if DEBUG_OUT:
        q_076("""
10
1 1 1 1 1 1 1 1 1 1
"""[1:-1].split('\n'))

        q_076("""
3
1 1 1
"""[1:-1].split('\n'))

        q_076("""
3
1 18 1
"""[1:-1].split('\n'))

        q_076("""
4
1 9 1 9
"""[1:-1].split('\n'))

    else:
        q_076()


def q_076(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        n = list(map(int, input().split()))[0]
        a_list = list(map(int, input().split()))
    else:
        print()
        n = list(map(int, user_input.pop(0).split()))[0]
        a_list = list(map(int, user_input.pop(0).split()))
    
    sum_a = sum(a_list)
    if sum_a % 10 != 0:
        print("No")
        return
    sum_a_div10 = sum_a // 10

    # 周をまたいでもいいように2周分確保しておく
    a_list.extend(a_list)  # 0...2n-1

    sp = 0
    ep = 0
    sum_a_part = 0
    while True:
        # ↓これだと遅い
        # sum_a_part = sum(a_list[sp:ep])

        if sum_a_part == sum_a_div10:
            print("Yes")
            return
        elif sum_a_part < sum_a_div10:
            ep += 1
            # ↓こうする
            sum_a_part += a_list[ep]
        else:  # sum_a_part > sum_a_div10
            sp += 1
            # ↓こうする
            sum_a_part -= a_list[sp]

        # 1周した?
        if sp >= n:
            print("No")
            return


if __name__ == "__main__":
    q_076_top()
