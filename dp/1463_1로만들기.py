import sys

target = int(sys.stdin.readline().rstrip())

cnt = [0] * (target + 1)
for i in range(2, target + 1):
    cnt[i] = cnt[i - 1] + 1
    if i % 2 == 0:
        cnt[i] = min(cnt[i], cnt[i // 2] + 1)
    if i % 3 == 0:
        cnt[i] = min(cnt[i], cnt[i // 3] + 1)
print(cnt[target])
