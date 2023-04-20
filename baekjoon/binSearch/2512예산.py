def bin_serach(moneys: list, limit: int):
    money_sum = sum(moneys)
    if money_sum <= limit:
        return max(moneys)

    start = 0
    last = limit
    answer = (start + last) // 2
    while start <= last:
        middle = (start + last) // 2
        check_limit = check(moneys, middle)
        if check_limit <= limit:
            answer = middle
            start = middle + 1
        else:
            last = middle - 1

    return answer


def check(moneys: list, national_money):
    national_money_sum = 0
    for money in moneys:
        if money <= national_money:
            national_money_sum += money
        else:
            national_money_sum += national_money
    return national_money_sum

def main():
    n = int(input())
    moneys = list(map(int, input().split()))
    limit = int(input())
    print(bin_serach(moneys,limit))

if __name__ == "__main__":
    main()