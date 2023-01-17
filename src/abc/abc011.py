from itertools import product
import random
from pathlib import Path

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    DEBUG_OUT = True


def q_B_top():
    if DEBUG_OUT:
        q_B(3, "Mozart plays magic.")
        q_B(3, "Columbus found USA.")
        q_B(7, "I have a scissors for right hand.")
        q_B(4, "abc ab aa aiueo")
        q_B(4, "aaa aa a aa")
    else:
        q_B()


def q_B(n=None, words=None):
    if not DEBUG_OUT:
        n = int(input())
        words = input().split()
    else:
        words = words.split()

    tbl = {
        "b": 1, "c": 1,
        "d": 2, "w": 2,
        "t": 3, "j": 3,
        "f": 4, "q": 4,
        "l": 5, "v": 5,
        "s": 6, "x": 6,
        "p": 7, "m": 7,
        "h": 8, "k": 8,
        "n": 9, "g": 9,
        "z": 0, "r": 0,
    }
    is_1st_word = True
    for i, word in enumerate(words):
        str_num = ""
        for c in list(word):
            c = c.lower()
            str_num += str(tbl[c]) if c in tbl.keys() else ""
        if len(str_num) > 0:
            if not is_1st_word:
                print(" ", end="")
            print(f"{str_num}", end="")
            is_1st_word = False
    print()


if __name__ == "__main__":
    q_B_top()
