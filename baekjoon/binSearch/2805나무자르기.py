def bin_search(need_tree_size, tree_sizes: list[int]):
    pl = 1
    pr = max(tree_sizes)
    while pl <= pr:
        middle = (pl + pr) // 2
        tree_bucket = cut_tree_size(tree_sizes, middle)
        if tree_bucket == need_tree_size:
            return middle
            break
        elif tree_bucket > need_tree_size:
            pl = middle + 1
        else:
            pr = middle - 1
    return pr


def cut_tree_size(tree_sizes, cut_size) -> int:
    result = 0
    for tree_size in tree_sizes:
        size = tree_size - cut_size
        if size > 0:
            result += size
    return result


def main():
    n, need_tree_size = list(map(int, input().split()))
    tree_sizes = list(map(int, input().split()))
    print(bin_search(need_tree_size, tree_sizes))


if __name__ == '__main__':
    main()
