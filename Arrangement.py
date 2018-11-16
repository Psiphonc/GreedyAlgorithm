def perm(list, k, m):
    if k == m:
        print(ls)
    else:
        for i in range(k, m + 1):
            list[k], list[i] = list[i], list[k]
            perm(list, k + 1, m)
            list[k], list[i] = list[i], list[k]


ls = input("list:")
ls = list(ls)
print(perm(ls, 0, len(ls) - 1))
