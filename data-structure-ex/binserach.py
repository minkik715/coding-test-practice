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


def bin_search_min_max(arr: list[int], target, type : str):

    # 내가 헷갈렸던 부분이 무엇인가 [1, 3, 5, 6, 10, 13, 34, 50, 90, 100]
    # 예를들어 나는 위 리스트에서 50을 기준으로 최대를 찾는다고 생각하면 100이 나와야 한다 생각했고 최소를 찾는다 하면 1이 나와야한다는 이상한 생각을 하고 있었음
    # 생각해보니 최소는 50을 기준으로 50보다 큰 것중 최소인 것이고 최대는 50을 기준으로 50보다 작은 것중 최대인 것이다.
    # 내 이전 생각은 그냥 리스트의 최대값 최솟값을 찾는 것과 다른게 없었음 ... 멍청하다
    min = 0
    max = len(arr) - 1
    arr.sort()
    if max <= 0:
        return None
    while min <= max:
        middle = (min + max) // 2
        expect_target = arr[middle]
        if target == expect_target:
            return target
        elif expect_target < target:
            min = middle + 1
        else:
            max = middle -1
    if type == "min":
        return max
    if type == "max":
        return min

    return middle


def main():
    target = 43
    result = bin_search_basic([1, 3, 5, 6, 10, 13, 34, 50, 90, 100], target)
    if result is not None:
        print(f"success to find {target}, that is on {result}")
    else:
        print(f"fail to find {target}")


if __name__ == "__main__":
    main()
