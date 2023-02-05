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


def q_014_top():
    if DEBUG_OUT:
        q_014("""
3 3
0 0 0
0 0 0
0 0 0
1 1 0
1 1 0
0 0 0
"""[1:-1].split('\n'))

        q_014("""
6
8 6 9 1 2 0
1 5 7 2 3 9
"""[1:-1].split('\n'))

        q_014("""
10
31 41 59 26 53 58 97 93 23 84
17 32 5 8 7 56 88 77 29 35
"""[1:-1].split('\n'))

        q_014("""
20
804289382 846930886 681692776 714636914 957747792 424238335 719885386 649760491 596516649 189641420 25202361 350490026 783368690 102520058 44897761 967513925 365180539 540383425 304089172 303455735
35005211 521595368 294702567 726956428 336465782 861021530 278722862 233665123 145174065 468703135 101513928 801979801 315634021 635723058 369133068 125898166 59961392 89018454 628175011 656478041
"""[1:-1].split('\n'))

    else:
        q_014()


def q_014(user_input=None):
    if not DEBUG_OUT:
        # replace user_input.pop(0) to input()
        n = list(map(int, input().split()))[0]
        a_list = list(map(int, input().split()))
        b_list = list(map(int, input().split()))
    else:
        print()
        n = list(map(int, user_input.pop(0).split()))[0]
        a_list = list(map(int, user_input.pop(0).split()))
        b_list = list(map(int, user_input.pop(0).split()))

    a_list = sorted(a_list)
    b_list = sorted(b_list)

    fuben = 0
    for a, b in zip(a_list, b_list):
        d = abs(a - b)
        fuben += d

    print(fuben)


if __name__ == "__main__":
    q_014_top()
