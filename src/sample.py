def calc(a_list):
  b_list = []
  for a in a_list:
    if a%2==0:
      b_list.append(a//2)
    else:
      return []
  return b_list


n = int(input())
a_list = list(map(int, input().split()))
cnt = 0
while True:
  a_list = calc(a_list)
  if len(a_list) > 0:
    cnt += 1
  else:
    break
print(cnt)