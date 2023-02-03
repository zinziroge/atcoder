from itertools import product, combinations
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
    DEBUG_OUT = True


def q_038_top():
    if DEBUG_OUT:
        q_038(4,6)
        q_038(1000000000000000000, 3)
        q_038(1000000000000000000, 1)
    else:
        q_038()


def my_lcm(a, b):
    return (a * b) // math.gcd(a, b)


def q_038(a=None, b=None, c=None):
    if not DEBUG_OUT:
        a, b = list(map(int, input().split()))
    else:
        print()

    lcm_a_b = my_lcm(a, b)

    if 10**18 < lcm_a_b:
        print("Large")
    else:
        print(lcm_a_b)


if __name__ == "__main__":
    q_038_top()
