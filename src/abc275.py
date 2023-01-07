def q_1():
    n = int(input())
    h_list = list(map(int, input().split()))

    i_h_max = 0
    h_max = h_list[0]
    for i_h, h in enumerate(h_list):
        if h > h_max:
            h_max = h
            i_h_max = i_h

    print(i_h_max+1)


def q_2():
    a, b, c, d, e, f = list(map(int, input().split()))
    s = (a * b * c) - (d * e * f)
    print(s % 998244353)


def q_3():
    import itertools
    import numpy as np

    s_list = []
    for _ in range(9):
        s_list.append(input())
    v_list = []
    for r, s in enumerate(s_list):
        for c, ch in enumerate(list(s)):
            if ch == "#":
                v_list.append([r, c])

    cnt = 0
    for v_set in itertools.combinations(v_list, 4):
        v1, v2, v3, v4 = v_set
        # (v1,v2,v3,v4)
        # (v1,v2,v4,v3)
        # (v1,v3,v2,v4)
        # (v1,v3,v4,v2)
        # (v1,v4,v2,v3)
        # (v1,v4,v3,v2)
        # 対角線が直交、2辺が直交
        """
        v1 = np.array(v1)
        v2 = np.array(v2)
        v3 = np.array(v3)
        v4 = np.array(v4)
        if np.dot(v1 - v3, v2 - v4)==0 and np.dot(v1 - v2, v1 - v4)==0:
            print(cnt, 1, v1,v2,v3,v4)
            cnt += 1
        elif np.dot(v1 - v4, v2 - v3)==0 and np.dot(v1 - v2, v1 - v3)==0:
            print(cnt, 2, v1,v2,v3,v4)
            cnt += 1
        elif np.dot(v1 - v2, v3 - v4)==0 and np.dot(v1 - v3, v1 - v4)==0:
            print(cnt, 3, v1,v2,v3,v4)
            cnt += 1
        elif np.dot(v1 - v4, v3 - v2)==0 and np.dot(v1 - v3, v1 - v2)==0:
            print(cnt, 4, v1,v2,v3,v4)
            cnt += 1
        elif np.dot(v1 - v2, v4 - v3)==0 and np.dot(v1 - v4, v1 - v3)==0:
            print(cnt, 5, v1,v2,v3,v4)
            cnt += 1
        elif np.dot(v1 - v3, v4 - v2)==0 and np.dot(v1 - v4, v1 - v2)==0:
            print(cnt, 6, v1,v2,v3,v4)
            cnt += 1
        """
        v1 = np.array(v1)
        v2 = np.array(v2)
        v3 = np.array(v3)
        v4 = np.array(v4)
        # 対角線が直交、2辺が直交
        if (v1 + v2 == v3 + v4).all():
            d1, d2 = v1 - v2, v3 - v4
            if not(d1[0]==d2[1] and d1[1]==d2[0]):
                continue
            d1, d2 = v1 - v3, v1 - v4
            if not(d1[0]==d2[1] and d1[1]==d2[0]):
                continue
            cnt += 1
        elif (v1 + v3 == v2 + v4).all():
            d1 = np.dot(v1 - v3, v2 - v4)
            d2 = np.dot(v1 - v2, v1 - v4)
            if d1 == 0 and d2 == 0:
                cnt += 1
        elif (v1 + v4 == v2 + v3).all():
            d1 = np.dot(v1 - v4, v2 - v3)
            d2 = np.dot(v1 - v2, v1 - v3)
            if d1 == 0 and d2 == 0:
                cnt += 1
    print(cnt)

if __name__ == "__main__":
    #q_1()
    #q_2()
    q_3()