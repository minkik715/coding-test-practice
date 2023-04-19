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
    answer = 0
    while pl <= pr:
        middle = (pl + pr) // 2
        install_c = install(house_locate, middle)
        if install_c >= c:
            answer = middle
            pl = middle + 1
        else:
            pr = middle - 1
    return answer

def install(house_locate: list[int], segment: int) -> int:
    current = house_locate[0]
    c = 1
    for i in house_locate[1:]:
        if current + segment <= i:
            c += 1
            current = i
    return c

if __name__ == '__main__':
    main()