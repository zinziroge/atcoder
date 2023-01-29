
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
        q_B(3, 2,
            [[1, 2],
             [2, 3]],
            )
        q_B(3, 3,
            [[1, 2],
             [2, 3],
             [2, 3], ]
            )
        q_B(4, 4,
            [[1, 2],
             [2, 3],
             [4, 1],
             [3, 4],]
            )
    else:
        q_B()


def q_B(n=None, m=None, opes=None):
    if not DEBUG_OUT:
        n, m = list(map(int, input().split()))
        opes = []
        for _ in range(m):
            opes.append(list(map(int, input().split())))
    # 箱はN個
    # M回操作
    # 赤いボールが入っていることがある箱から移動すると赤いボールが入っている可能性のある箱が広がる
    #
    # 赤玉フラグの立っている箱からボールが移動してきた箱は赤玉フラグを建てる
    # ボールがゼロ個になったら赤玉フラグを下げる
    # 上記以外はフラグは変化なし
    box_list = [1] * n
    box_has_red = [False] * n
    box_has_red[0] = True

    for ope in opes:
        from_box, to_box = ope
        from_box -= 1  # 1 origin -> 0 origin
        to_box -= 1

        box_list[from_box] -= 1
        box_list[to_box] += 1

        box_has_red[to_box] = box_has_red[to_box] or box_has_red[from_box]
        if box_list[from_box] == 0:
            box_has_red[from_box] = False

    print(sum(box_has_red))


if __name__ == "__main__":
    # q_A_top()
    q_B_top()
    # q_C_top()
    # q_D_top()
