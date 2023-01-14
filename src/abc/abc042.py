from itertools import product
import random
import sys

random.seed(42)

DEBUG_OUT = False
DEBUG_OUT = True


def q_A_top():
    q_A()


def q_A():
    bunsetsu_list = list(map(int, input().split()))
    bs = sorted(bunsetsu_list)
    if bs[0]==5 and bs[1]==5 and bs[2]==7:
        print("YES")
    else:
        print("NO")


def q_B_top():
    if DEBUG_OUT:
        for _ in range(1000):
            n = random.randint(1, 1000)
            ll = random.randint(1, 1000)

            print(n, ll)
            words = []
            alphabet = list("abcdefghijklmnopqrstuvwxyz")
            for _ in range(n):
                #word = ""
                #for _ in range(ll):
                #    word += alphabet[random.randint(0, len(alphabet) - 1)]
                word = "".join([alphabet[random.randint(0, len(alphabet) - 1)] for _ in range(ll)])
                words.append(word)
            print(words)
            q_B(n, ll, words)
    else:
        q_B()


def q_B(n=None, l=None, words=None):
    if not DEBUG_OUT:
        n, _ = list(map(int, input().split()))
        # print(n)
        words = []
        for _ in range(n):
            words.append(input())

    words = sorted(words)

    ans = ""
    for word in words:
        ans += word
        if DEBUG_OUT:
            ans += "-"
    print(ans)


def q_C_top():
    if DEBUG_OUT:
        for _ in range(1000):
            #n = 1000 #random.randint(1, 100)
            #k = 8 #random.randint(1, 10)
            #ds = [1,3,4,5,6,7,8,9]

            #n = 9999
            #k = 1
            #ds = [0]

            #n = 9999
            #k = 1
            #ds = [9]

            #n = 6171
            #k = 9
            #ds = [0,3,8,4,7,5,1,9,2]

            #n = 4942
            #k = 2
            #ds = [0, 9]

            #n = 1730
            #k = 3
            #ds = [5,7,2,3,1,4,8]

            n = random.randint(1, 10000 - 1)
            k = random.randint(1, 10 - 1)
            ds = random.sample(range(0, 9 + 1), k)
            # print("dislike:", ds)
            if set(ds) == set(range(1, 9 + 1)):
                continue
            q_C(n, k, set(ds))
            print("")
    else:
        q_C()


def q_C(n=None, k=None, ds=None):
    # input
    if not DEBUG_OUT:
        n, k = list(map(int, input().split()))
        ds = set(map(int, input().split()))

    #
    like_nums = set(range(0, 10)) - ds
    same_keta_max_val = 0
    for v in [sorted(like_nums)[-1]] * len(str(n)):
        same_keta_max_val = same_keta_max_val * 10 + v

    if DEBUG_OUT:
        print("n:", n, "like:", like_nums)
        print("max:", same_keta_max_val)

    ans = 0
    if n <= same_keta_max_val:
        # 同じ桁数で解があるとき
        for c in list(map(int, list(str(n)))):
            for v in sorted(like_nums):
                if c <= v:  # equal or lager
                    ans = ans * 10 + v
                    break
        
        if ans < n:
            v_list = []
            # 最上位桁
            for v in like_nums:
                if list(map(int, list(str(n))))[0] < v:  # larger
                    v_list.append(v)
                    break
            # 最上位桁以外
            v_list += [sorted(like_nums)[0]] * (len(str(n)) - 1)
            #
            ans = 0
            for v in v_list:
                ans = ans * 10 + v
    else:
        # 同じ桁数で払えないなら1桁増やしたときの最小値を選択する
        # 最上位は0以外の最小値、それ以下は最小値を並べる
        v_list = []
        # 最上位桁
        like_nums_exclude_zero = like_nums - set([0])
        # 最上位桁以外
        v_list.append(sorted(like_nums_exclude_zero)[0])
        v_list += [sorted(like_nums)[0]] * len(str(n))

        for v in v_list:
            ans = ans * 10 + v

    print(ans)
    if (ans - n) / n > n*0.5:
        print(ans, n, ans - n)
        sys.exit(1)


if __name__ == "__main__":
    # q_A_top()
    # q_B_top()
    q_C_top()
