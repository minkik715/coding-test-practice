def main():
    n, m = map(int, input().split())
    arr = [[0] * m for _ in range(n)]
    for i in range(n):
        l = list(map(int, input().split()))
        for t in range(m):
            arr[i][t] = arr[i][t] + l[t]
    for i in range(n):
        l = list(map(int, input().split()))
        for t in range(m):
            arr[i][t] = arr[i][t] + l[t]
    for i in range(n-1):
        print(*arr[i])
    print(*arr[n-1], end="")

if __name__ == "__main__":
    main()
