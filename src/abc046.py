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
    #DEBUG_OUT = True


def q_B_top():
    if DEBUG_OUT:
        q_B(2, 2)
        q_B(1, 10)
        q_B(10, 8)
    else:
        q_B()


def q_B(n=None, k=None):
    if not DEBUG_OUT:
        n, k = list(map(int, input().split()))
    if DEBUG_OUT:
        print()
    # e.g.: n=2, k=2, ans=[[k0,k1], [k1,k0]]=2
    # e.g.: n=1, k=10, ans=[[k0],[k1],...[k9]]=10
    ans = k*(k - 1)**(n - 1)  # 最初はk色、以降はk-1色から選択するので
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

