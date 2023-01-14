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
#    DEBUG_OUT = True


def q_B_top():
    if DEBUG_OUT:
        q_B("0BB1")
        q_B("01B0")
    else:
        q_B()


def q_B(s=None):
    if not DEBUG_OUT:
        s = list(input())

    ans = ""
    for ss in s:
        if ss == "B":
            ans = ans[:-1]
        else:
            ans += ss
    
    print(ans)


def q_C_top():
    if DEBUG_OUT:
        q_C(2, [4, 8], 8)
        q_C(3, [1, 1, 3], 3)
        q_C(3, [4, 2, 5], 5)
        q_C(4, [-100, -100, -100], 0)
    else:
        q_C()


def q_C(n=None, a_list=None, exp=None):
    if not DEBUG_OUT:
        n = input()
        a_list = list(map(int, input().split()))
    min_cost = 100**2 * 100
    min_a, max_a = min(a_list), max(a_list)
    for rep_v in range(min_a, max_a + 1):
        cost = 0
        for i, a in enumerate(a_list):
            cost += (a - rep_v)**2
            # たまにチェックして途中終了する
            if i % 10000 == 0 and min_cost < cost:
                break

        if min_cost > cost:
            min_cost = cost

    print(min_cost)
    if DEBUG_OUT:
        assert(min_cost == exp)


def q_D_top():
    if DEBUG_OUT:
        q_D("needed")
        q_D("atcoder")
        q_D("aaa")
    else:
        q_D()


def q_D(s=None):
    if not DEBUG_OUT:
        s = input()
    if DEBUG_OUT:
        print(s)

    s_list = list(s)

    for sp in range(0, len(s_list)):
        for ep in range(sp+2, len(s_list)):  # len(s_part) >= 2
            s_part = s_list[sp:ep]

            s_cc = collections.Counter(s_part)
            char_most = s_cc.most_common()[0][0]
            if len(s_cc) == 1:  # include only one kind of char.
                char_most_2nd = 0  # RE
            else:
                char_most_2nd = s_cc.most_common()[1][0]

            if s_cc[char_most] > s_cc[char_most_2nd]:
                print(sp+1, ep)
                if DEBUG_OUT:
                    print("".join(s_part))
                return

    # balanced str
    print(-1, -1)
    return

"""
def q_D_1(s=None):
    if not DEBUG_OUT:
        s = input()

    if DEBUG_OUT:
        print(s)

    s_list = list(s)
    s_cc = collections.Counter(s_list)
    char_most = s_cc.most_common()[0][0]
    if len(s_cc) == 1:
        char_most_2nd = 0  # RE
    else:
        char_most_2nd = s_cc.most_common()[1][0]

    if s_cc[char_most] > s_cc[char_most_2nd]:
        is_unbalance = True
    else:
        is_unbalance = False
    print(-1, -1)

    #if is_unbalance:
    #    sp = s_list.index(char_most)
    #    sr_list = list(reversed(s_list))
    #    ep = len(s_list) - sr_list.index(char_most) - 1
    #    print(sp + 1, ep + 1)
    #else:
    #    print(-1, -1)
"""



if __name__ == "__main__":
    #q_A_top()
    #q_B_top()
    #q_C_top()
    q_D_top()
