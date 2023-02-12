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

large_prime_num = 10**9 + 7


def combinations_count(n, k):
    return math.factorial(n) // (math.factorial(n - k) * math.factorial(k))


def q_018_top():
    if DEBUG_OUT:
        q_018("""
4
2 1 1
4
0
1
2
3
"""[1:-1].split('\n'))

        q_018("""
5121
312000000 4123 3314
6
123
12
445
4114
42
1233
"""[1:-1].split('\n'))

    else:
        q_018()


def q_018(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        t = list(map(int, input().split()))[0]
        l, x, y = list(map(int, input().split()))
        q = list(map(int, input().split()))[0]
        e_list = []
        for _ in range(q):
            e = list(map(int, input().split()))[0]
            e_list.append(e)
    else:
        print()
        t = list(map(int, user_input.pop(0).split()))[0]
        l, x, y = list(map(int, user_input.pop(0).split()))
        q = list(map(int, user_input.pop(0).split()))[0]
        e_list = []
        for _ in range(q):
            e = list(map(int, user_input.pop(0).split()))[0]
            e_list.append(e)

    for e in e_list:
        theta = 2 * math.pi * e / t # 観覧車の位置
        ky = -l/2 * math.sin(theta)
        kz = l/2 - l/2 * math.cos(theta)
        
        phi = math.atan2(kz, math.sqrt(x** 2 + (y - ky)**2))
        print(phi / math.pi * 180)

        

if __name__ == "__main__":
    q_018_top()
