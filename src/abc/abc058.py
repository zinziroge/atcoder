
from itertools import product
import random
import sys
from collections import Counter
from pathlib import Path

import numpy as np

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    DEBUG_OUT = True


def q_B_top():
    if DEBUG_OUT:
        q_B("xyz", "abc", "xaybzc")
        q_B(
            "atcoderbeginnercontest", "atcoderregularcontest",
            "aattccooddeerrbreeggiunlnaerrccoonntteesstt")
        for _ in range(10):
            orig_str = "".join(
                    [
                        chr(ord("a") + random.randint(0, 26-1))
                        for i in range(1, random.randint(1, 100+1))
                    ]
                )
            q_B(
                orig_str[0::2], orig_str[1::2],
                orig_str
            )
    else:
        q_B()


def q_B(odd_str=None, even_str=None, orig_str=None):
    if not DEBUG_OUT:
        odd_str = input()
        even_str = input()
    if DEBUG_OUT:
        print()
        for c in list(odd_str):
            print(c, "", end="")
        print()
        for c in list(even_str):
            print("", c, end="")
        print()
    ans = ""
    for o, e in zip(list(odd_str), list(even_str)[:len(odd_str)]):
        ans += o + e
    if len(odd_str) > len(even_str):
        ans += odd_str[-1]
    print(ans)
    if DEBUG_OUT:
        print(orig_str)
        if ans != orig_str:
            print("ERROR")


def q_C_top():
    if DEBUG_OUT:
        q_C(
            3,
            [
                "cbaa",
                "daacc",
                "acacac"
            ]
        )
        q_C(
            3,
            [
                "a",
                "aa",
                "b",
            ]
        )
    else:
        q_C()


def q_C(n=None, s_list=None):
    if not DEBUG_OUT:
        n = int(input())
        s_list = []
        for _ in range(n):
            s_list.append(input())
    if DEBUG_OUT:
        print()
        print(n)
        print(s_list)

    # s_list毎の要素の共通文字を抽出する
    # s_listを文字列の長さの昇順で並べ替える。候補を少なくできるので。
    s_list = sorted(s_list, key=len)
    # 共通文字のリスト
    common_cnt_c = Counter(s_list[0])
    if DEBUG_OUT:
        print(common_cnt_c)
    for s in s_list[1:]:
        _tmp_cnt_c = {}
        s_cnt_c = Counter(s)
        for k, v in common_cnt_c.items():
            if s_cnt_c.get(k) is not None:
                n = s_cnt_c.get(k)
            else:
                n = 0

            _tmp_cnt_c[k] = min(v, n)
        common_cnt_c = Counter(**_tmp_cnt_c)
        if DEBUG_OUT:
            print(common_cnt_c)

    ans = ""
    for k, v in sorted(common_cnt_c.items(), key=lambda x: x[0]):
        ans += k * v
    print(ans)


def q_D_top():
    if DEBUG_OUT:
        q_D(
            3, 3,
            [1, 3, 4],
            [1, 3, 6],
        )
        q_D(
            6, 5,
            [-790013317, -19231079, 95834122, 418379342, 586260100, 802780784],
            [-253230108, 193944314, 363756450, 712662868, 735867677],
        )


    else:
        q_D()


def q_D(n=None, m=None, x_list=None, y_list=None):
    if not DEBUG_OUT:
        n, m  = list(map(int, input().split()))
        x_list = list(map(int, input().split()))
        y_list = list(map(int, input().split()))
    if DEBUG_OUT:
        print()
        print(n, m)
        print(x_list)
        print(y_list)

    #xw = x_list[-1] - x_list[0]
    #yw = y_list[-1] - y_list[0]
    xn = len(x_list) - 1
    yn = len(y_list) - 1
    #n_blk = (len(x_list) - 1) * (len(y_list) - 1)
    #a = 10**9 + 7
    #ans = (xw * yw * n_blk) % a
    #print(ans)

    x_ary = []
    for x in range(xn):
        x_ary.append((xn - x) * (x + 1))
    y_ary = []
    for y in range(yn):
        y_ary.append((yn - y) * (y + 1))
    cnt_ary = np.array(y_ary).reshape(yn, -1) * np.array(x_ary).reshape(1, -1)
    #print(cnt_ary.shape)
    print(cnt_ary[::-1, :])

    a = 10**9 + 7
    area_size_ary = np.empty((yn, xn), dtype=np.int64)
    for i_y in range(yn):
        for i_x in range(xn):
            area_size_ary[i_y, i_x] = \
                (x_list[i_x + 1] - x_list[i_x]) * \
                (y_list[i_y + 1] - y_list[i_y])
    print(area_size_ary[::-1, :])
    
    sum = 0
    for i_y in range(yn):
        for i_x in range(xn):
            sum += (sum + (cnt_ary[i_y, i_x] * area_size_ary[i_y, i_x])) % a
    print(sum)


if __name__ == "__main__":
    # q_A_top()
    # q_B_top()
    # q_C_top()
    q_D_top()
