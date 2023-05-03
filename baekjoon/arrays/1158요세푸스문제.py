from collections import deque
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
p = [1] * (n + 1)
t = 0
i = 1
answer = []
deq = deque([i for i in range(1, n+1)])
k = -(m-1)
while len(deq) !=0:
    deq.rotate(k)
    answer.append(deq.popleft())

print(str(answer).replace("[", "<").replace("]", ">"), end= "")
