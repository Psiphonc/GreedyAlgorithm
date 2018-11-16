def perm(list, k, m):
    if k == m:
        for i in range(0, m + 1):
            print(list[i], end='')
        print('\n')
    else:
        for i in range(k, m + 1):
            list[k], list[i] = list[i], list[k]
            perm(list, k + 1, m)
            list[k], list[i] = list[i], list[k]


print(perm([1, 2, 3, 4, 5, 6], 0, 5))
