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


def q_069_top():
    if DEBUG_OUT:
        q_069("""
2 3
"""[1:-1].split('\n'))

        q_069("""
10 2
"""[1:-1].split('\n'))

        q_069("""
2021 617
"""[1:-1].split('\n'))

    else:
        q_069()


def q_069(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        n, k = list(map(int, input().split()))
    else:
        print()
        n, k = list(map(int, user_input.pop(0).split()))
    
    # check
    if k < 3:
        if n >= 2 and k < 2:  # k=1
            print(0)
            return
        elif n >= 3 and k < 3:  # k=1 or 2
            print(0)
            return

    # calc
    ans = k
    if n > 1:
        ans = ans * (k - 1)
        ans %= large_prime_num
    if n > 2:
        # too slow
        # for _ in range(n - 2):
        #     ans *= k - 2
        #     ans %= large_prime_num
        k2_mod = (k - 2) % large_prime_num
        

    print(ans)


if __name__ == "__main__":
    q_069_top()
