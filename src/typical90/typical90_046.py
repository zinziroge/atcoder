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


def q_046_top():
    if DEBUG_OUT:
        q_046("""
3
10 13 93
5 27 35
55 28 52
"""[1:-1].split('\n'))

        q_046("""
3
10 56 102
16 62 108
20 66 112
"""[1:-1].split('\n'))

        q_046("""
20
238 395 46 238 264 114 354 52 324 14 472 64 307 280 209 24 165 194 179 248
270 83 377 332 173 21 362 75 66 342 229 117 124 481 48 235 376 13 420 74
175 427 76 278 486 169 311 47 348 225 41 482 355 356 263 95 170 156 340 289
"""[1:-1].split('\n'))
    else:
        q_046()


def q_046(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        n = list(map(int, input().split()))[0]
        a_list = list(map(int, input().split()))
        b_list = list(map(int, input().split()))
        c_list = list(map(int, input().split()))
    else:
        print()
        n = list(map(int, user_input.pop(0).split()))[0]
        a_list = list(map(int, user_input.pop(0).split()))
        b_list = list(map(int, user_input.pop(0).split()))
        c_list = list(map(int, user_input.pop(0).split()))

    a_list = [x % 46 for x in a_list]
    cnt_a_list = [0] * 46
    for k, v in collections.Counter(a_list).items():
        cnt_a_list[k] = v

    b_list = [x % 46 for x in b_list]
    cnt_b_list = [0] * 46
    for k, v in collections.Counter(b_list).items():
        cnt_b_list[k] = v

    c_list = [x % 46 for x in c_list]
    cnt_c_list = [0] * 46
    for k, v in collections.Counter(c_list).items():
        cnt_c_list[k] = v

    if DEBUG_OUT:
        print(cnt_a_list)

    cnt_ab_list = [0] * 46
    for i in range(46):
        for j in range(46):
            cnt_ab_list[(i+j) % 46] += cnt_a_list[i] * cnt_b_list[j]

    cnt_abc_list = [0] * 46
    for i in range(46):
        for j in range(46):
            cnt_abc_list[(i+j) % 46] += cnt_ab_list[i] * cnt_c_list[j]

    if DEBUG_OUT:
        print(cnt_abc_list)

    print(cnt_abc_list[0])

if __name__ == "__main__":
    q_046_top()
