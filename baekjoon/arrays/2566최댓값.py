def main():
    start = -1
    n = 0
    m = 0
    for i in range(9):
        t = (list(map(int, input().split())))
        for j in range(9):
            if start < t[j]:
                start = t[j]
                n = i + 1
                m = j + 1
    print(start)
    print(n, end=" ")
    print(m, end="")


if __name__ == "__main__":
    main()
