from itertools import product
import random
from pathlib import Path

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    #DEBUG_OUT = True


def q_C_top():
    if DEBUG_OUT:
        q_C(2, 2, [1000, 1500])
        q_C(2, 1, [1000, 1500])
        q_C(10, 5, [2604, 2281, 3204, 2264, 2200, 2650, 2229, 2461, 2439, 2211])
    else:
        q_C()


def q_C(n=None, k=None, r_list=None):
    if not DEBUG_OUT:
        n, k = list(map(int, input().split()))
        r_list = list(map(int, input().split()))
    
    r_list = sorted(r_list)
    c = 0
    # 全部見れるならレートの小さいのから見る
    # 全部見れないなら、レートの高いK個をレートの小さい順にみる
    for r in r_list[len(r_list) - k:]:
        if c < r:
            c = (c + r) / 2
        else:
            break
    print(c)

if __name__ == "__main__":
    q_C_top()
