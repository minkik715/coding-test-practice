import copy
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
targets = list(map(int, sys.stdin.readline().rstrip().split()))

deq = deque()
[deq.append(i + 1) for i in range(n)]


def move_first_to_last_price(dq: deque, target: int) -> int:
    cnt = 0
    while dq[0] != target:
        dq.append(dq.popleft())
        cnt += 1
    return cnt


def move_last_to_first_price(dq: deque, target: int) -> int:
    cnt = 0
    while dq[0] != target:
        dq.appendleft(dq.pop())
        cnt += 1
    return cnt
price = 0
for target in targets:
    fl = move_first_to_last_price(copy.deepcopy(deq), target)
    lf = move_last_to_first_price(copy.deepcopy(deq), target)
    if fl <= lf:
        while deq[0] != target:
            deq.appendleft(deq.pop())
        price += fl
    else:
        while deq[0] != target:
            deq.append(deq.popleft())
        price += lf
    deq.popleft()
print(price, end="")
