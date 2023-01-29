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
    #DEBUG_OUT = True


def q_002_top():
    if DEBUG_OUT:
        q_002(2)
        q_002(3)
        q_002(10)
    else:
        q_002()


def q_002(n=None):
    if not DEBUG_OUT:
        n = int(input())
    else:
        print()

    if n % 2 == 1:
        print()
        return

    n_valid_k = 0
    for i in range(2**n):
        bits = bin(i)[2:]
        bits = "0" * (n - len(bits)) + bits
        k_open = 0
        k_close = 0
        is_valid_k = True
        k_s = ""
        for b in bits:
            if b == '0':
                k_open += 1
                k_s += "("
            if b == '1':
                k_close += 1
                k_s += ")"

            if k_open < k_close:
                is_valid_k = False
                break

        if k_open != k_close:
            is_valid_k = False

        if is_valid_k:
            n_valid_k += 1
            print(k_s)

    if DEBUG_OUT:
        print(n_valid_k)


if __name__ == "__main__":
    q_002_top()
