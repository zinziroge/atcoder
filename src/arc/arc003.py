
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
    # DEBUG_OUT = True


def q_A_top():
    if DEBUG_OUT:
        q_A(34, "ABABAAABACDDDABADFFABABDABFAAABFAA")
        q_A(5, "FFFFF")
    else:
        q_A()


def q_A(n=None, ranks=None):
    if not DEBUG_OUT:
        n = input()
        ranks = input()
    else:
        ...

    score_sum = 0
    score = {
        "A": 4,
        "B": 3,
        "C": 2,
        "D": 1,
        "F": 0,
    }
    for r in list(ranks):
        score_sum += score[r]
    
    ans = score_sum / len(ranks)
    print(ans)


def q_B_top():
    if DEBUG_OUT:
        q_B("aca", "accc", "ca")
        q_B("abcb", "aacb", "bccc")
    else:
        q_B()


def q_B(sa=None, sb=None, sc=None):
    if not DEBUG_OUT:
        sa = input()
        sb = input()
        sc = input()
        print()


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
    q_A_top()
    # q_B_top()
    # q_C_top()
    # q_D_top()
