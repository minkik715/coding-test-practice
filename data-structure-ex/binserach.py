def bin_search_basic(arr: list[int], target):
    min = 0
    max = len(arr) - 1
    arr.sort()
    if max <= 0:
        return None
    while min <= max:
        middle = (min + max) // 2
        expect_target = arr[middle]
        if expect_target == target:
            return middle
        elif expect_target > target:
            max = middle + 1
        else:
            min = middle - 1
    return None


def upper_bound(arr: list[int], target):
    start = arr[0]
    last = arr[-1]
    answer = 0
    while start <= last:
        middle = (start+ last) //2
        if middle <= target:
            answer = middle
            start = middle + 1
        else:
            last = middle -1
    return answer +1


def lower_bound(arr: list[int], target):
    return  0
def main():
    print(upper_bound([1,1,1,1,1,1,1,1,1,1,1, 3], 2))

if __name__ == "__main__":
    main()
