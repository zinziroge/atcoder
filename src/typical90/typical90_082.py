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


def q_082_top():
    if DEBUG_OUT:
        q_082("""
3 5
"""[1:-1].split('\n'))

        q_082("""
98 100
"""[1:-1].split('\n'))

        q_082("""
1001 869120
"""[1:-1].split('\n'))

        q_082("""
381453331666495446 746254773042091083
"""[1:-1].split('\n'))

    else:
        q_082()


def q_082(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        l, r = list(map(int, input().split()))
    else:
        print()
        l, r = list(map(int, user_input.pop(0).split()))

    l_keta = 1
    ll = l
    while True:
        ll = ll // 10
        if ll == 0:
            break
        l_keta += 1

    r_keta = 1
    rr = r
    while True:
        rr = rr // 10
        if rr == 0:
            break
        r_keta += 1
    
    if DEBUG_OUT:
        print(l_keta, r_keta)

    # lの桁数のlの直前までの合計値
    l_keta_start = 10 ** (l_keta - 1)
    before_l_cnt = (l_keta_start + (l - 1)) * ((l - 1) - l_keta_start + 1) * l_keta // 2
    # rの桁数のrの直後からrの桁の最後まで合計値
    r_keta_end = 10**r_keta - 1
    after_r_cnt = (r_keta_end + (r + 1)) * (r_keta_end - (r+1) + 1) * r_keta // 2
        
    cnt = 0
    for i in range(l_keta, r_keta+1):
        #cnt += i * (10**(i+1) - 1 - 10**i + 1))
        cnt += ((10**(i-1) + (10**i - 1)) * (9 * 10**(i - 1)) * i // 2) % large_prime_num
    
    cnt = (cnt + large_prime_num - before_l_cnt - after_r_cnt) % large_prime_num
    print(cnt)
        

if __name__ == "__main__":
    q_082_top()
