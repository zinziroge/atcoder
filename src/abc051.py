
from itertools import product, permutations, combinations
import random
import sys
import collections
from pathlib import Path

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    #DEBUG_OUT = True


def q_B_top():
    if DEBUG_OUT:
        q_B(2, 2)
        q_B(5, 15)
    else:
        q_B()


def q_B(k=None, s=None):
    if not DEBUG_OUT:
        k, s = list(map(int, input().split()))
    if DEBUG_OUT:
        print()

    xyz_list = []
    # x <= y <= z

    """ too slow
    for x in range(0, k+1):
        for y in range(x, k+1):
            for z in range(y, k+1):
                #print(x, y, z)
                if x+y+z == s:
                    xyz_list.append([x, y, z])
    """

    ans = 0
    for xyz in xyz_list:
        # (0,0,2) => (2,0,0), (0,2,0), (0,0,2) => 3
        ans += len(set(permutations("".join(map(str, xyz)), 3)))
    print(ans)


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
