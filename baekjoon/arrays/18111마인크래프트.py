import sys

N, M, B = map(int, input().split())
grounds = []
for _ in range(N):
    [grounds.append(i) for i in map(int, sys.stdin.readline().rstrip().split())]

cnt = sys.maxsize
height = 0

for i in range(257):
    plus =0
    minus =0
    for g in grounds:
        if g > i:
            minus += g-i
        else :
            plus += i-g
    if plus > minus +B:
        continue
    t = (minus *2) + plus

    if t <= cnt:
        cnt = t
        height = i

print(cnt, height)
