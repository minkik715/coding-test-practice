def bin_search(n: int, k: int):
    start = 1
    last = n * n
    answer = 0
    while start <= last:
        middle = (start + last) // 2
        check = get_lower_cnt(n, middle)
        if check >= k:
            answer = middle
            last = middle - 1
        else:
            start = middle + 1
    return answer


def get_lower_cnt(n, target) -> int:
    cnt = 0
    for i in range(1, n + 1):
        cnt += min(n, target // i)
    return cnt


def main():
    n = int(input())
    k = int(input())
    print(bin_search(n, k))


if __name__ == "__main__":
    main()
