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


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


def q_075_top():
    if DEBUG_OUT:
        q_075("""
42
"""[1:-1].split('\n'))

        q_075("""
48
"""[1:-1].split('\n'))

        q_075("""
54
"""[1:-1].split('\n'))

        q_075("""
53
"""[1:-1].split('\n'))
    else:
        q_075()


def q_075(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        n = list(map(int, input().split()))[0]
    else:
        print()
        n = list(map(int, user_input.pop(0).split()))[0]

    a = prime_factorize(n)
    c = collections.Counter(a)

    beki_list = c.values()
    sum_beki = sum(beki_list)
    if DEBUG_OUT:
         print(c, sum_beki)
    magic_cnt = math.ceil(math.log2(sum_beki))
    print(magic_cnt)


if __name__ == "__main__":
    q_075_top()
