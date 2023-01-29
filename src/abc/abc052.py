
from itertools import product, combinations
import math
import random
import sys
import collections
from pathlib import Path
import numpy as np

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    DEBUG_OUT = True


def factorization(n):
    """
    https://qiita.com/snow67675476/items/e87ddb9285e27ea555f8
    nを素因数分解
    2以上の整数n => [[素因数, 指数], ...]の2次元リスト

    factorization(24) 
    ## [[2, 3], [3, 1]] 
    ##  24 = 2^3 * 3^1
    """

    d = {}
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp % i ==0:
            cnt=0
            while temp % i ==0:
                cnt += 1
                temp //= i
            d[i] = cnt

    if temp != 1:
        d[temp] = 1

    if d is {}:
        d[n] = 1

    return d


def q_C_top():
    if DEBUG_OUT:
        q_C(3)
        q_C(6)
        #q_C(1000)
    else:
        q_C()


def q_C(n=None):
    if not DEBUG_OUT:
        n = int(input())
    m = 10**9 + 7
    d = {}
    for i in range(2, n+1):
        _d_tmp = factorization(i)
        for k, v in _d_tmp.items():
            if k in d.keys():
                d[k] += v
            else:
                d[k] = v
    if DEBUG_OUT:
        print(d)
    
    n_yakusuu = 1
    for k, v in d.items():
        n_yakusuu = (n_yakusuu * (v + 1)) % m
    #fact_result = factorization(math.factorial(n))
    #print(fact_result)
    #return
    #for prime, shisu in fact_result:
    #    n_yakusu *= (shisu + 1)
    print(n_yakusuu)


def q_D_top():
    if DEBUG_OUT:
        q_D(
            4, 2, 5,
            [1, 2, 5, 7])
        q_D(
            7, 1, 100,
            [40, 43, 45, 105, 108, 115, 124]
            )
        q_D(
            7, 1, 2,
            [24, 35, 40, 68, 72, 99, 103],
        )
    else:
        q_D()


def q_D(n=None, a=None, b=None, x_list=None):
    if not DEBUG_OUT:
        n, a, b = list(map(int, input().split()))
        x_list = list(map(int, input().split()))

    hirou = 0
    cur_x = 0
    for i, x in enumerate(x_list[:-1]):
        d = x_list[i+1] - x
        if d*a > b:
            # warp
            hirou += b
        else:
            #walk
            hirou += d*a
    print(hirou)

if __name__ == "__main__":
    # q_A_top()
    # q_B_top()
    # q_C_top()
    q_D_top()
