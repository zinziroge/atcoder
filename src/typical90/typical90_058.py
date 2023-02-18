from itertools import product, combinations, combinations_with_replacement
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


def q_058_top():
    if DEBUG_OUT:
        q_058("""
5 3
"""[1:-1].split('\n'))

        q_058("""
0 100
"""[1:-1].split('\n'))

        q_058("""
99999 1000000000000000000
"""[1:-1].split('\n'))

        q_058("""
0 1
"""[1:-1].split('\n'))

        q_058("""
0 2
"""[1:-1].split('\n'))

        q_058("""
0 1000000000000000000
"""[1:-1].split('\n'))

        q_058("""
0 999999999999999999
"""[1:-1].split('\n'))

        q_058("""
99999 1
"""[1:-1].split('\n'))

        q_058("""
99999 999999999999999999
"""[1:-1].split('\n'))

    else:
        q_058()


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


def q_058(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        n, k = list(map(int, input().split()))
    else:
        print()
        n, k = list(map(int, user_input.pop(0).split()))
    
    vis = [False] * 99999
    x = n
    loop_values = []
    true_cnt = 0
    start_value = None
    for i_k in range(k):
        y = sum([int(i) for i in list(str(x))])
        z = (x + y) % 10**5

        if vis[z] and true_cnt == 0:
            # 1週目開始, loop_cycle数計測開始
            true_cnt = 1
            loop_values.append(z)
            start_value = z
        elif start_value is not None and z == start_value:
            # 2週目開始
            break
        elif true_cnt == 1:
            # 1週目の計測中
            #loop_cycle += 1
            loop_values.append(z)

        #print(true_cnt, vis[z], x, y, z)
        vis[z] = True
        x = z

    nokori = k - i_k - 1
    loop_cycle = len(loop_values)
    if DEBUG_OUT:
        print(k, i_k, len(loop_values))
        print(loop_values[:20])
        print(loop_values[-20:])
        #print(loop_values[-619:-619+20])
        #print(loop_values[4734-619+1:4734-619+1+20])

    if loop_cycle == 0:
        print(x)
    else:
        if DEBUG_OUT:
            print(nokori, nokori % loop_cycle)
        print(loop_values[nokori % loop_cycle])

    """
    # naive
    x = n
    for _ in range(k):
        y = sum([int(i) for i in list(str(x))])
        z = (x + y) % 10**5
        print(z, z - x)
        x = z
    """


    
if __name__ == "__main__":
    q_058_top()
