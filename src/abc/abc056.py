
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
        q_B(3, 2, 6)
        q_B(3, 1, 3)
        q_B(5, 10, 1)
    else:
        q_B()


def q_B(w=None, a=None, b=None):
    if not DEBUG_OUT:
        w, a, b = list(map(int, input().split()))
    
    # 移動の向きはないのでa <= b にする
    if a > b:
        a, b = b, a
    
    # [a, a+w] と [b, b+w] が重なるか
    # 重ならない場合は, b - (a+w) だけ動かす
    # ->
    #if (a+w) > b:
    #    print(0)
    #else:
    #    print(b - (a+w))
    print(max(0, b - (a+w)))


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
