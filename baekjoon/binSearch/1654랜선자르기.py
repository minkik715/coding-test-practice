def bin_search(max_n: int, lines: list[int], k: int):
    min_n = 1
    middle = int((max_n+min_n)/2)
    while min_n <= max_n:
        bucket = 0
        for line in lines:
            bucket += cut_line_cnt(line, middle)
        if bucket >= k:
            min_n = middle +1
            middle = int((max_n + min_n) / 2)
        else:
            max_n = middle -1
            middle = int((max_n + min_n) / 2)
    return middle


def main():
    n, k = map(int, input().split())
    lines = []
    for i in range(n):
        lines.append(int(input()))
    each_length = max(lines)
    print(bin_search(each_length, lines, k))


# 1. 최대 랜선 길이를 구해야 하니 때문에 랜선 길이중 가장 긴것을 기준

def cut_line_cnt(line_length, each_length):
    return int(line_length // each_length)


if __name__ == '__main__':
    main()