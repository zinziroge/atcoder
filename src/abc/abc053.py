
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
        q_B("QWERTYASDFZXCV")
        q_B("ZABCZ")
        q_B("HASFJGHOGAKZZFEGA")
    else:
        q_B()


def q_B(s=None):
    if not DEBUG_OUT:
        s = input()
        print()

    s_list = list(s)
    sp = s.index("A")
    ep = len(s_list) - 1 - list(reversed(s_list)).index("Z") 
    print(ep - sp + 1)


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


def q_D_top():
    if DEBUG_OUT:
        q_D(
            5,
            [1, 1, 1, 1, 1, ],)
        q_D(
            5,
            [1, 2, 1, 3, 7])
        q_D(
            15,
            [1, 3, 5, 2, 1, 3, 2, 8, 8, 6, 2, 6, 11, 1, 1],)
    else:
        q_D()


def q_D(n=None, a_list=None):
    if not DEBUG_OUT:
        n = int(input())
        a_list = list(map(int, input().split()))
    a_list = sorted(a_list)
    a_cnt_dict = collections.Counter(a_list)
    a_keys = sorted(a_cnt_dict.keys())
    #a_cnt_list = sorted(a_cnt_dict.items(), key=lambda x: x[0])
    if DEBUG_OUT:
        print(a_cnt_dict)
    #print(a_cnt_list)
    #print(len(a_cnt.keys()))
    i = 0
    n_eat = 0
    while True:
        a_cnt = a_cnt_dict[a_keys[i]]
        if a_cnt > 1:
            j_min = -1  # i + j_min + 1 で自分自身を食べる
            does_find_double = False
            for j, k in enumerate(a_keys[i+1:]):
                b_cnt = a_cnt_dict[k]
                if j_min is -1 and b_cnt == 1:
                    j_min = j
                if b_cnt > 1:
                    # eat
                    a_cnt_dict[a_keys[i + j + 1]] -= 1
                    a_cnt_dict[a_keys[i]] -= 1
                    n_eat += 1
                    does_find_double = True
                    break
            
            if not does_find_double:
                # ダブりがなかったときは自分より大きい最近傍のカードをたべる
                # eat
                a_cnt_dict[a_keys[i + j_min + 1]] -= 1
                a_cnt_dict[a_keys[i]] -= 1
                n_eat += 1
        else:
            i += 1

        if len(a_cnt_dict) == i:
            break

    if DEBUG_OUT:
        print(a_cnt_dict)
    ans = 0
    for k, v in a_cnt_dict.items():
        if v == 1:
            ans += 1
        elif v < 0 or v > 2:
            print("error")
    print(ans)


if __name__ == "__main__":
    # q_A_top()
    # q_B_top()
    # q_C_top()
    q_D_top()
