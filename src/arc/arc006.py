
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


def q_A_top():
    if DEBUG_OUT:
        q_A(34, "ABABAAABACDDDABADFFABABDABFAAABFAA")
        q_A(5, "FFFFF")
    else:
        q_A()


def q_A(n=None, ranks=None):
    if not DEBUG_OUT:
        n = input()
        ranks = input()
    else:
        ...

    score_sum = 0
    score = {
        "A": 4,
        "B": 3,
        "C": 2,
        "D": 1,
        "F": 0,
    }
    for r in list(ranks):
        score_sum += score[r]
    
    ans = score_sum / len(ranks)
    print(ans)


def q_B_top():
    if DEBUG_OUT:
        q_B(
            3, 2,
            ["| |-|",
             "|-| |"],
            "o"
        )
        q_B(
            10, 2,
            ["| |-| |-| |-| |-| |",
             "|-| |-| |-| |-| |-|",],
             "            o      "
        )
        q_B(
            1, 5,
            ["|",
             "|",
             "|",
             "|",
             "|",],
             "o"
        )
        q_B(
            4, 2,
            ["| | | |",
             "| | | |"],
             "      o",
        )
        q_B(
            9, 8,
            ["| | | | | | | | |",
             "|-| | |-| | |-| |",
             "| | |-| | |-| | |",
             "| |-| | | | | |-|",
             "| | | |-| | | |-|",
             "| | |-| |-| | | |",
             "|-| | |-| | |-| |",
             "| | | | | |-| | |"],
             "            o    "
        )
    else:
        q_B()


def q_B(n=None, ll=None, amida=None, goal=None):
    if not DEBUG_OUT:
        n, ll = list(map(int, input().split()))
        amida = []
        for i in range(ll):
            amida.append(input())
        goal = input()
    else:
        ...

    cur_pos = list(goal).index("o")
    for l in range(ll-1, 0-1, -1):
        a = list(amida[l])
        if 0 <= cur_pos - 2 < len(a) and a[cur_pos - 1] == "-":
            cur_pos -= 2
        elif 0 <= cur_pos + 2 < len(a) and a[cur_pos + 1] == "-":
            cur_pos += 2
    print(cur_pos // 2 + 1)


def q_C_top():
    if DEBUG_OUT:
        q_C(
            5,
            [4, 3, 1, 2, 1, ],
        )
        q_C(
            7,
            [93, 249, 150, 958, 442, 391, 25, ],
        )
        q_C(
            4,
            [100, 100, 100, 100],
        )
        q_C(
            6,
            [5, 10, 15, 20, 25, 30, ],
        )
        q_C(
            15,
            [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, ],
        )
    else:
        q_C()


def q_C(n=None, w_list=None, sc=None):
    if not DEBUG_OUT:
        n = int(input())
        w_list = []
        #w_list = list(map(int, input().split()))
        for _ in range(n):
            w_list.append(int(input()))
    else:
        print()

    w_list = w_list[::-1]
    yama_list = []
    for w in w_list:
        yama_top_list = [d_list[-1] for d_list in yama_list]
        tgt_yama = None
        min_diff_w = 100000
        for i, yama_top in enumerate(yama_top_list):
            diff_w = w - yama_top
            if 0 <= diff_w <= min_diff_w:
                min_diff_w = diff_w
                tgt_yama = i

        if tgt_yama is None:
            # yama追加
            yama_list.append([w])
        else:
            yama_list[tgt_yama].append(w)
    if DEBUG_OUT:
        print(yama_list)
    print(len(yama_list))


if __name__ == "__main__":
    # q_A_top()
    # q_B_top()
    q_C_top()
    # q_D_top()
