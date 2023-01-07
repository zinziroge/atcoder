
import itertools
import numpy as np
import math

def q_1():
    s = list(input())
    #print(s)
    s.reverse()
    t = True
    for i, c in enumerate(s):
      if c == "a":
        cnt = i
        print(len(s) - cnt)
        t = False
        break

    if t:
        print(-1)


def q_2():
    n, m = list(map(int, input().split()))
    city_list = [[] for _ in range(n)]
    #print(city_list)
    for _ in range(m):
        _a, _b = list(map(int, input().split()))
        city_list[_a-1].append(_b-1)
        city_list[_b-1].append(_a-1)
        #print(_a,_b,city_list)
    city_list = [sorted(c) for c in city_list]
    #print(city_list)
    for city in city_list:
        #print(city)
        print(len(city), " ".join([str(c+1) for c in city]))


def q_3():
    n = int(input())
    p_list = list(map(int, input().split()))
    num_list = list(range(1, n + 1))
    prev_v = []
    cnt = 0
    #print(n, p_list, num_list)
    for v in itertools.permutations(num_list, n):
        #print(v, type(v))
        if list(v) == p_list:
            #print(list(prev_v))
            print(" ".join([str(c) for c in list(prev_v)]))
            print(cnt)
            break
        prev_v = v
        cnt += 1
    """
    i_ans = 0
    #print(n, p_list)
    ans_list = list(itertools.permutations(num_list, n))
    for i, p in enumerate(p_list):
        num_list.remove(p)
        if len(num_list) > 0:
            i_ans += (p - 1) * len(list(itertools.permutations(num_list, len(num_list)))) 
        print(i,p,i_ans,num_list,len(list(itertools.permutations(num_list, len(num_list)))) )
    print(i_ans)
    #print(len(ans))
    ans = ans_list[i_ans - 1]
    print(" ".join([str(c) for c in list(ans)]))
    """

if __name__ == "__main__":
    #q_1()
    #q_2()
    q_3()