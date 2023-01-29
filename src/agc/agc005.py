
from itertools import product
import random
import sys
import collections
from pathlib import Path
import copy

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    #DEBUG_OUT = True


def q_A_top():
    if DEBUG_OUT:
        q_A("TSTTSS")
        q_A("SSTTST")
        q_A("TSSTTTSS")
    else:
        q_A()


def q_A(x=None):
    if not DEBUG_OUT:
        x = input()

    st_list = list(x)
    
    # 連続するSの個数、連続するTの個数 の繰り返しにする。
    stn_list = []
    prev_c = st_list[0]
    n = 1
    for c in st_list[1:]:
        if c == prev_c:
            n += 1
        else:
            stn_list.append(n)
            n = 1
        prev_c = c
    stn_list.append(n)

    # 先頭がSでないときはSがゼロ個であることを追加
    if st_list[0] == 'T':
        stn_list = [0] + stn_list
    # 終端がTでないときはTがゼロ個であることを追加
    if st_list[-1] == 'S':
        stn_list = stn_list + [0]
    if DEBUG_OUT:
        print(stn_list)

    while True:
        new_stn_list = []
        for stn in zip(*[iter(stn_list)]*2):
            m = min(stn)
            s, t = stn[0] - m, stn[1] - m
            if s==0 and t==0:
                ...
            elif len(new_stn_list) >= 2:
                if s==0 and new_stn_list[-1]==0:
                    # tがないので飛ばして、sをつめる
                    new_stn_list[-2] += s
                    new_stn_list[-1] = t
                elif s==0 and new_stn_list[-1]!=0:
                    # sがないので飛ばして、tをつめる
                    new_stn_list[-1] += t
                else:
                    new_stn_list.extend([s, t])
            else:
                new_stn_list.extend([s, t])

        if stn_list == new_stn_list:
            break
        stn_list = copy.copy(new_stn_list)

    if DEBUG_OUT:
        print(new_stn_list)
    #n = len(new_stn_list)
    #if len(new_stn_list) > 0:
    #    if new_stn_list[0] == 0:
    #        n -= 1
    #    if new_stn_list[-1] == 0:
    #        n -= 1
    print(sum(new_stn_list))


if __name__ == "__main__":
    q_A_top()
    # q_B_top()
    # q_C_top()
    # q_D_top()
