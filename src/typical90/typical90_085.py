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
    #DEBUG_OUT = True


def q_085_top():
    if DEBUG_OUT:
        q_085("""
42
"""[1:-1].split('\n'))

        q_085("""
7
"""[1:-1].split('\n'))

        q_085("""
192
"""[1:-1].split('\n'))

    else:
        q_085()


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


def divisor_list_s(num):
    """
    約数
    """
    divisors = []
    for i in range(1, int(num**0.5)+1):
        if num % i == 0:
            divisors.append(i)
            if i**2 == num:
                continue
            divisors.append(int(num/i))
#     return divisors # 昇順にしなくてよいならソートは不要
    return sorted(divisors)  # 昇順にしたいときはソートする
    #return divisors


def q_085(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        n = list(map(int, input().split()))[0]
    else:
        print()
        n = list(map(int, user_input.pop(0).split()))[0]
    
    divisors = divisor_list_s(n)
    if DEBUG_OUT:
         print(divisors)

    cnt = 0
    # テストが1つだけTLEで通らない
    for i_a, a in enumerate(divisors):
        if a > math.sqrt(n):
            continue
        for i_b, b in enumerate(divisors[i_a:]):
            # 有効なパターンのa, bが決まったらcは決まる

            #    for c in divisors[i_a + i_b:]:
            #        if n == a*b*c:
            #            cnt += 1
            #if n < a*b:
            if n < a*b:
                break
            if math.sqrt(n) < a*b:
                #continue
                # divisors は昇順に並んでいるので以降は必ず n < a * b
                #break
                ...
            if n % (a*b) != 0:
                continue
            c = n // (a*b)
            if c < b:
                continue
            cnt += 1
    #for a, b, c in combinations_with_replacement(divisors, 3):
    #    if n == a*b*c:
    #        cnt += 1
    #        #print(a,b,c)
    print(cnt)
    #pf_list = prime_factorize(n)
    #pf_cnt = collections.Counter(pf_list)
    #yakusu_list = []
    ##combinations_with_replacement(pf, 3)

    
if __name__ == "__main__":
    q_085_top()
