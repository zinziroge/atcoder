from itertools import product, permutations, count
import random
import sys
from collections import Counter
from pathlib import Path
import math

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    DEBUG_OUT = True


def get_primes(limit):
    prime = []
    for i in range(2, limit):
        if i % 10000 == 0:
            print(i)
        for j in range(2, int(limit**0.5)+1):
            if i % j == 0:
                break
        else:
            prime.append(i)
    return prime


def q_D_top():
    if DEBUG_OUT:
        q_D(4, 2, 2, [1, 2, 3, 4])
        q_D(3, 1, 2, [1, 3, 5])
    else:
        q_D()


def q_D(n=None, k=None, d=None, num_list=None):
    if not DEBUG_OUT:
        n, k, d, = list(map(int, input().split()))
        num_list = list(map(int, input().split()))

    num_list = sorted(num_list)
    num_mod_list = [i % d for i in num_list]
    cnt = Counter(num_mod_list)
    print(cnt)
    

    #num_list = sorted(num_list)
    #s_max = sum(num_list[-k:])
    #ans_max = d * (s_max // d)
    #diff_s = s_max - ans_max
    #print(diff_s)
    #comb_list = list(permutations(num_list, k))
    #sum_list = []
    #for comb in comb_list[::-1]:
    #    s = sum(comb)
    #    sum_list.append(s)
    #    if s % d == 0:
    #        print(s)
    #        return
    #sum_list = list(set(sum_list))
    #for s in sum_list[::-1]:
    #    if s % d == 0:
    #        print(s)
    #        return
    
    print(-1)

if __name__ == "__main__":
    # q_A_top()
    # q_B_top()
    # q_C_top()
    q_D_top()
