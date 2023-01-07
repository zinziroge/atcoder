
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

    sabc_list = [list(sa), list(sb), list(sc)]

    a2n = {"a": 0, "b": 1, "c": 2}
    n2a = ["A", "B", "C"]
    i_turn = 0
    while True:
        if len(sabc_list[i_turn]) == 0:
            break
        next_c = sabc_list[i_turn].pop(0)
        i_turn = a2n[next_c]
    
    print(n2a[i_turn])


if __name__ == "__main__":
    # q_A_top()
    q_B_top()
    # q_C_top()
    # q_D_top()
