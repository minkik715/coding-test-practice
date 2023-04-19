def main():
    n = int(input())
    owns = list(map(int, input().split()))
    t = int(input())
    targets = list(map(int, input().split()))
    owns.sort()
    print(*bin_search(owns, targets))


def bin_search(owns: list, targets: list) -> list:
    answer = []
    for target in targets:
        start = 0
        last = len(owns) - 1
        check = True
        while start <= last:
            middle = (start + last) // 2

            if owns[middle] == target:
                answer.append(1)
                #owns.remove(target) remove 연산 O(N)으로 시간 복잡도 엄청나게 증가함.
                check = False
                break
            elif owns[middle] > target:
                last = middle - 1
            else:
                start = middle + 1
        if check:
            answer.append(0)
    return answer


if __name__ == "__main__":
    main()
