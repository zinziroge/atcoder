
from itertools import product
import random
import sys
import collections
from pathlib import Path
import numpy as np

random.seed(42)

if Path(__file__).stem == "Main":
    DEBUG_OUT = False
else:
    DEBUG_OUT = False
    DEBUG_OUT = True


def q_C_top():
    if DEBUG_OUT:
        q_C("erasedream")
        q_C("dreameraser")
        q_C("dreamerer")
        q_C("dreamerdream")

        print("-- expected 'YES'")
        words = ["dream", "dreamer", "erase", "eraser"]
        for _ in range(10):
            s = ""
            for _ in range(10):
                s += words[random.randint(0, len(words) - 1)]
            print("".join(list(reversed(s))))
            q_C(s)

        print("-- expected 'YES or NO'")
        words = ["dream", "dreamer", "erase", "eraser", "er"]#, "e", "r"]
        for _ in range(10):
            s = ""
            for _ in range(4):
                s += words[random.randint(0, len(words) - 1)]
            print("".join(list(reversed(s))))
            q_C(s)
    else:
        q_C()


def q_C(s=None):
    # erase が特殊
    # dreameraser : dream + eraser はYESだが, dreamer + aserはNO
    # dreamerdream : dream + dream + er はNOだが, dreamer + dreamはYES
    words = ["dream", "dreamer", "erase", "eraser"]
    if not DEBUG_OUT:
        s = input()

    s = "".join(list(reversed(s)))
    words = ["".join(list(reversed(word))) for word in words]

    i = 0
    t = ""
    while True:
        is_yes = False
        for word in words:
            if s[i: i + len(word)] == word:
                i += len(word)
                t += word
                is_yes = True
                if DEBUG_OUT:
                    print(f"{word} ", end="")
                break

        if not is_yes:
            if DEBUG_OUT:
                print()
            print("NO")
            return

        if i >= len(s):
            if DEBUG_OUT:
                print()
            print("Yes")
            return


if __name__ == "__main__":
    # q_A_top()
    # q_B_top()
    q_C_top()
    # q_D_top()
