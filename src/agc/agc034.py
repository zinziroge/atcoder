
from itertools import product
import random
import sys
import collections
from pathlib import Path
import copy

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    #DEBUG_OUT = True


def q_B_top():
    if DEBUG_OUT:
        q_B("ABCABC")
        q_B("C")
        q_B("ABCACCBABCBCAABCB")
    else:
        q_B()


def q_B(s=None):
    if not DEBUG_OUT:
        s = input()
    s_list = list(s)

    i = 0
    n_ope = 0
    """
        AAA..AABC の並びはAの数だけ変換できる
        BCA..AAAA

        AAA..AABCBCBC... と並んでいるのが変換回数が多い。Aの繰り返し回数 + BCの繰り返し回数
    """
    while True:
        if s_list[i:i+3] == ["A", "B", "C"]:

    
    """
    i = 0
    n_ope = 0
    while True:
        if s_list[i:i+3] == ["A", "B", "C"]:
            s_list[i:i+3] = ["B", "C", "A"]
            # あらたにABC
            i = max(i - 1, 0)
            n_ope += 1
        else:
            i += 1
        if len(s_list) <= i:
            break
    """

    if DEBUG_OUT:
        print("".join(s_list))
    print(n_ope)


if __name__ == "__main__":
    # q_A_top()
    q_B_top()
    # q_C_top()
    # q_D_top()
