import sys
n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))

t1 = B[:]
t2 = B[:]
t3 = A[:]
t3.sort()
t1.sort()
order = []
for i in t1:
    idx = t2.index(i)
    t2[idx] = -1
    order.append(idx)
for o in order:
    A[o] = t3.pop()

answer = 0
for i in range(n):
    answer += A[i]*B[i]
print(answer, end="")
