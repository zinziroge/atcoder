
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
        q_B("QWERTYASDFZXCV")
        q_B("ZABCZ")
        q_B("HASFJGHOGAKZZFEGA")
    else:
        q_B()


def q_B(s=None):
    if not DEBUG_OUT:
        s = input()
        print()

    s_list = list(s)
    sp = s.index("A")
    ep = len(s_list) - 1 - list(reversed(s_list)).index("Z") 
    print(ep - sp + 1)


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
