from itertools import product
import random
import sys
import collections
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
        q_D(3, [2023, 63, 1059872604593911])
    else:
        q_D()


def q_D(t=None, num_list=None):
    if not DEBUG_OUT:
        num_list = []
        t = int(input())
        for _ in range(t):
            num_list.append(int(input()))

    for num in num_list:
        num_sq = int(math.sqrt(num))
        print("num_sq", num_sq)
        prime_list = get_primes(num_sq)
        for prime in prime_list[::-1]:
            another_prime = num / (prime * prime)
            if another_prime == int(another_prime) and \
               (another_prime in prime_list):
                print(prime, int(another_prime))
                break


if __name__ == "__main__":
    # q_A_top()
    # q_B_top()
    # q_C_top()
    q_D_top()
