
from itertools import product
import random
import sys
import collections
from pathlib import Path

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    DEBUG_OUT = True


def q_B_top():
    if DEBUG_OUT:
        q_B(3)
        q_B(10)
        q_B(100000)
    else:
        q_B()


def q_B(n=None):
    if not DEBUG_OUT:
        n = int(input())
        print()
    
    a = 10**9  + 7  # is prime number
    power = 1
    for i in range(1, n + 1):
        power = (power * i) % a
        #power = power * i
    print(power)
    #print(power % a)


def q_C_top():
    if DEBUG_OUT:
        q_C("aca", "accc", "ca")
        q_C("abcb", "aacb", "bccc")
    else:
        q_C()


def q_C(sa=None, sb=None, sc=None):
    if not DEBUG_OUT:
        n = input()
        a_list = list(map(int, input().split()))


if __name__ == "__main__":
    # q_A_top()
    q_B_top()
    # q_C_top()
    # q_D_top()
