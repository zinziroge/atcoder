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


def q_020_top():
    if DEBUG_OUT:
        q_020(4,3,2)
        q_020(16,3,2)
        q_020(8,3,2)
    else:
        q_020()


def q_020(a=None, b=None, c=None):
    if not DEBUG_OUT:
        a, b, c = list(map(int, input().split()))
    else:
        print()

    if a < c**b:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    q_020_top()
