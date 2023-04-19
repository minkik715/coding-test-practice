def upper_bound(trees: list, k: int):
    first, last = 0, trees[-1]
    answer = (first + last) // 2
    while first <= last:
        middle = (first + last) // 2
        get_tree = cut_trees(trees, middle)
        if get_tree >= k:
            answer = middle
            first = middle + 1
        else:
            last = middle - 1
    return answer


def cut_trees(trees: list, cut_height):
    cut_tree_height = 0
    for tree in trees:
        t = tree - cut_height
        if t > 0:
            cut_tree_height += t
    return cut_tree_height


def main():
    n, k = map(int, input().split())
    trees = list(map(int, input().split()))
    trees.sort()
    print(upper_bound(trees, k))


if __name__ == "__main__":
    main()