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


def q_052_top():
    if DEBUG_OUT:
        q_052("""
2
1 2 3 5 7 11
4 6 8 9 10 12
"""[1:-1].split('\n'))

        q_052("""
1
11 13 17 19 23 29
"""[1:-1].split('\n'))

        q_052("""
7
19 23 51 59 91 99
15 45 56 65 69 94
7 11 16 34 59 95
27 30 40 43 83 85
19 23 25 27 45 99
27 48 52 53 60 81
21 36 49 72 82 84
"""[1:-1].split('\n'))
    else:
        q_052()


def q_052(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        n = list(map(int, input().split()))[0]
        a_map = []
        for _ in range(n):
            _a = list(map(int, input().split()))
            a_map.append(_a)
    else:
        print()
        n = list(map(int, user_input.pop(0).split()))[0]
        a_map = []
        for _ in range(n):
            _a = list(map(int, user_input.pop(0).split()))
            a_map.append(_a)
    
    a_ary = np.array(a_map, dtype=int)
    a_sum_dice = np.sum(a_ary, dtype=int, axis=1)

    ans = 1
    for a in a_sum_dice:
        a = int(a % large_prime_num)
        ans = (ans * a) % large_prime_num
    print(ans)



if __name__ == "__main__":
    q_052_top()
