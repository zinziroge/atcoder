import sys

n = int(input())
trv_list = []
#trv = list(map(int, input().split()))
#while trv:
#    trv_list.append(trv)
#    trv = list(map(int, input().split()))
for _ in range(n):
    trv_list.append(list(map(int, input().split())))

c_txy = [0, 0, 0]
can_do = True
for g_txy in trv_list:
    t_dist = g_txy[0] - c_txy[0]
    x_dist = abs(g_txy[1] - c_txy[1])
    y_dist = abs(g_txy[2] - c_txy[2])
    if t_dist < x_dist + y_dist:
        can_do = False
        break
    # else:  # elif t_dist >= x_dist + y_dist
    elif (x_dist + y_dist - t_dist) % 2 != 0:
        can_do = False
        break
    c_txy = g_txy

if can_do:
    print("Yes")
else:
    print("No")