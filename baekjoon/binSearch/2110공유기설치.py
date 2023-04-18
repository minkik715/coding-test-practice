def main():
    n, c = map(int, input().split())
    house_locate: list[int] = []
    for i in range(n):
        house_locate.append(int(input()))
    house_locate.sort()

    print(binSearch(c, house_locate))


def binSearch(c, house_locate):
    pl = 1
    pr = house_locate[-1] - house_locate[0]
    while pl <= pr:
        middle = (pl + pr) // 2
        install_c = install(house_locate, middle)
        if install_c >= c:
            pl = middle + 1
        else:
            pr = middle - 1
    return middle

def install(house_locate: list[int], segment: int):
    current = house_locate[0]
    cnt = 0
    for next_c in house_locate[1:]:
        if current+segment <= next_c:
           cnt += 1
           current = next_c
    return cnt
if __name__ == '__main__':
    main()