from itertools import product
import random

random.seed(42)

DEBUG_OUT = False
DEBUG_OUT = True


def q_3_top():
    if DEBUG_OUT:
        for _ in range(1000):
            n_cmd = random.randint(1, 1)
            cmd_str = ""
            for _ in range(n_cmd):
                cmd_str += list("ABXY")[random.randint(0, 4-1)]
            q_3(n_cmd, cmd_str)
    else:
        q_3()


def q_3(n_cmd=None, cmd_str=None):
    if n_cmd is None or cmd_str is None:
        n_cmd = int(input())
        cmd_str = input()
    if DEBUG_OUT:
        print()
        print(n_cmd)
        print(cmd_str)

    """
    cmd_str = cmd_str.replace("AB", "L")
    cmd_str = cmd_str.replace("XY", "R")
    print(cmd_str)
    print(len(cmd_str))
    """

    n_cmd_min = n_cmd
    cmd_min_str = cmd_str
    cmd_pair = {"L": "", "R": ""}

    for cmd_pair_L in product('ABXY', repeat=2):
        # print(cmd_pair_L, type(cmd_pair_L), "".join(list(cmd_pair_L)))
        cmd_str_1 = cmd_str.replace("".join(list(cmd_pair_L)), "L")
        for cmd_pair_R in product('ABXY', repeat=2):
            cmd_str_2 = cmd_str_1.replace("".join(list(cmd_pair_R)), "R")
            if len(cmd_str_2) < n_cmd_min:
                n_cmd_min = len(cmd_str_2)
                cmd_min_str = cmd_str_2
                cmd_pair = {"L": cmd_pair_L, "R": cmd_pair_R}

    if DEBUG_OUT:
        print(cmd_min_str)
        print(cmd_pair)
    print(len(cmd_min_str))


def q_4_top():
    q_4()


def q_4():
    goban = []
    h, w = list(map(int, input().split()))
    for _ in range(h):
        goban.append(list(input()))
    print(goban)



if __name__ == "__main__":
    #q_3_top()
    q_4_top()
